"""Install and setup."""
from distutils.core import setup

setup(
    name="SchoolDigger-Scraper",
    version="1.0.0",
    python_requires=">=3.6",
    packages=[  # this will put these dirs into site-packges/
        "schooldiggerscraper",
    ],
    install_requires=[
        "beautifulsoup4==4.7.1",
        "click==7.0",
        "requests==2.21.0",
    ],
    entry_points={
        "console_scripts": [
            "schooldiggerscraper=schooldiggerscraper.scrape:main",
        ],
    },
    description="Scrape school digger",
    author="Liu,Tianpei",
    author_email="tianpei.liu0@gmail.com",
)
