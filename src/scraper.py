import json
import os
import time
from pathlib import Path

import requests
from dotenv import load_dotenv
from tqdm import tqdm

import src.constants.globals as g

load_dotenv()


def scrape_job_listings(keywords: list[str]):
    """Scrape job listings using the given keywords.

    Args:
        keywords (list[str]): Keywords to be used in query.
    """

    g.DATA_DIR.mkdir(parents=True, exist_ok=True)

    for keyword in tqdm(keywords, desc="Fetching job listings", total=len(keywords)):
        time.sleep(5)  # 2-second delay

        query = {"query": f"{keyword} in Philippines", "page": "1", "num_pages": "20"}

        headers = {
            "X-RapidAPI-Key": os.environ["X_RapidAPI_Key"],
            "X-RapidAPI-Host": "jsearch.p.rapidapi.com",
        }

        response = requests.get(g.SEARCH_URL, headers=headers, params=query)

        if response.status_code == 200:
            _data = response.json()
            _data = _data["data"]

            filename = Path(g.DATA_DIR, f"{keyword}.json")

            with open(filename, "w") as f:
                json.dump(_data, f)

        else:
            print(response.status_code)


def main():
    scrape_job_listings(keywords=g.KEYWORDS)


if __name__ == "__main__":
    main()
