import argparse
import asyncio
from collections import Counter
import aiohttp

async def main (args):
    session = aiohttp.ClientSession()
    try:
        links = Counter()
        display (links)
    finally:
        await session.close()

def parse_args ():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("d", "--max-depth", type = int, default = 2)
    parser.add_argument("w", "--num-workers", type = int, default = 3)
    return parser.parse_args()