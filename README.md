# SchoolDigger-Scraper

A scraper for SchoolDigger

# How to

No need to use pip + virtualenv, I recommend **pipenv**.

## Install pipenv

##### If you have brew:

```shell
brew install pipenv
```

#### If not (use pip)

```shell
pip install pipenv
```

## Pipenv install packages

```shell
pipenv install
```
## Run scraper

#### Start a subshell

```bash
pipenv shell
cd SchoolDigger-Scraper
python main.py --state=MA --level=1 --max-page=1 --sleep=1
```

#### Or run

```bash
cd SchoolDigger-Scraper
pipenv run python main.py --state=MA --level=1 --max-page=1 --sleep=1
```


