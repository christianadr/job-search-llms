import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

import src.globals as g

load_dotenv()


def scrape_job_listings(keywords: list[str]):
    """Scrape job listings using the given keywords.

    Args:
        keywords (list[str]): Keywords to be used in query.
    """
    for keyword in keywords:
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
