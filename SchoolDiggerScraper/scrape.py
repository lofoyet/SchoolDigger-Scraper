# -*- coding: utf-8 -*-
"""A requests-based scraper for SchoolDigger.com in Python3.

How-to:

$ python main.py --state=MA --level=1 --max-page=1 --sleep=1


Attributes:
    SchoolDiggerScraper (class): Object to scrape.

Todo:
    * Support middle and high
    * Better error handling

"""
import os
import json
import time
import urllib
import logging

import bs4
import click
import requests

import schooldiggerscraper.utils  # noqa

logging.basicConfig(level=logging.INFO)


class SchoolDiggerScraper(object):
    """Class of scraper, can download and save."""

    def __init__(self, state, level, out, sleep, max_page):
        """Init needed."""
        for k, v in locals().items():
            if not k.startswith("self"):
                setattr(self, k, v)
        self.out_path = os.path.join(
            out,
            "{}_{}_data.json".format(state, schooldiggerscraper.utils.school_level[level])
        )
        self.beautifulsoup = bs4.BeautifulSoup
        for k, v in schooldiggerscraper.utils.__dict__.items():
            if not k.startswith("__"):
                setattr(self, k, v)
        self.main_url = self.main_url.format(**locals())
        self.headers_page["referer"] = \
            self.headers_page["referer"].format(**locals())
        self.headers_init["referer"] = \
            self.headers_init["referer"].format(**locals())
        self.form = self.forms[self.level]
        self.form["values[FIPS]"] = self.state_to_fips[self.state]
        self.logger = logging.getLogger("SchoolDiggerScraper")
        self.data = []

    def download(self):
        session = requests.Session()
        # init run to get cookies
        resp_init = session.get(self.main_url, headers=self.headers_init)
        if resp_init.status_code != 200:
            self.logger.error(
                "Status code {}, job aborted".format(resp_init.status_code)
            )
            exit()
        cookies = requests.utils.cookiejar_from_dict(
            requests.utils.dict_from_cookiejar(session.cookies)
        )
        # get total data size and num pages in first run
        content_dict = self._pull_one_page(
            self.entry_point,
            1,
            0,
            self.form,
            session,
            cookies,
            self.headers_page,
            self.logger,
        )
        self.data.append(content_dict)
        self.pause()
        # get rest
        num_total_records = content_dict["recordsTotal"]
        num_pages = num_total_records // 10 + 1
        for draw in range(2, self.max_page or num_pages + 1):
            start = (draw - 1) * 10
            content_dict = self._pull_one_page(
                self.entry_point,
                draw,
                start,
                self.form,
                session,
                cookies,
                self.headers_page,
                self.logger,
            )
            self.data.append(content_dict)
            self.pause()

    def _pull_one_page(
            self,
            post_url,
            draw,
            start,
            form,
            session,
            cookies,
            headers,
            logger,
    ):
        """Download one page."""
        form["draw"] = draw
        form["start"] = start
        form_urlencoded = urllib.parse.urlencode(form)
        content_len = len(form_urlencoded)
        headers["content-length"] = str(content_len)
        response = session.post(
            post_url,
            headers=headers,
            data=form_urlencoded,
            cookies=cookies,
        )
        scode = response.status_code
        content_dict = {}
        if scode != 200:
            logger.error(
                "Draw {}, Status code {}, skipping".format(draw, scode)
            )
        else:
            logger.info(
                "Draw {} finished".format(draw, scode)
            )
            content_dict = json.loads(response.content)
        return content_dict

    def pause(self, duration=None):
        """Pause."""
        sleep = duration or self.sleep
        time.sleep(sleep)

    def save(self):
        """Save to disc."""
        self.logger.info(
            "Saving to {}".format(os.path.abspath(self.out_path))
        )
        with open(self.out_path, "w") as f:
            for content_dict in self.data:
                f.write("{}\n".format(json.dumps(content_dict)))


@click.command()
@click.option(
    "--state",
    help="State code",
    type=click.Choice(schooldiggerscraper.utils.state_codes),
)
@click.option(
    "--level",
    help="School level, 1 for elementary, 2 for middle, 3 for high",
    type=click.Choice(["1", "2", "3"]),
)
@click.option(
    "--out",
    help="Output directory",
    type=str,
    default="./data",
)
@click.option(
    "--sleep",
    help="Sleep seconds between each page",
    type=int,
    default=5,
)
@click.option(
    "--max-page",
    help="Maximum page number",
    type=int,
    default=None,
)
def main(state, level, out, sleep, max_page):
    scraper = SchoolDiggerScraper(state, int(level), out, sleep, max_page)
    scraper.download()
    scraper.save()


if __name__ == "__main__":
    main()
