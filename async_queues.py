import argparse
import asyncio
from collections import Counter
import aiohttp
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import sys
from typing import NamedTuple

async def main (args):
    session = aiohttp.ClientSession()
    try:
        links = Counter()
        display (links)
    finally:
        await session.close()

async def fethc_html (session, url):
    async with session.get(url) as response:
        if response.ok and response.context_type == "text/html":
            return await response.text()

def parse_links (url,html):
    soup = BeautifulSoup(html, features = "html.parser")
    for anchor in soup.select("a[href]"):
        href = anchor.get("href").lower()
        if not href.startswith("javascript"):
            yield urljoin(url, href)

def parse_args ():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("d", "--max-depth", type = int, default = 2)
    parser.add_argument("w", "--num-workers", type = int, default = 3)
    return parser.parse_args()

def display (links):
    for url, count in links.most_common():
        print (f"{count :> 3} {url}")

if __name__ == "__main__":
    asyncio.run(main(parse_args()))