import urllib.parse

import requests
from bs4 import BeautifulSoup


def get_job_data(url, headers):
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        job_titles = soup.find_all("h2", attrs={"class": "title"})
        job_locations = soup.find_all("div", class_="location")
        for title, location in zip(job_titles, job_locations):
            yield title.get_text(strip=True), location.get_text(strip=True)


def main():
    input_keywords = urllib.parse.quote(input("Enter skill/s: "))
    input_location = urllib.parse.quote(input("Enter location: "))

    base_url = "https://ph.indeed.com/jobs?"
    url = f"{base_url}q={input_keywords}&l={input_location}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }

    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        a_elements = soup.find_all("a", id=lambda x: x and x.startswith("job_"))
        job_ids = [element.get("id").split("_")[1] for element in a_elements]

        for job_id in job_ids:
            job_url = f"{url}&vjk={job_id}"
            for title, location in get_job_data(job_url, headers):
                print("Title:", title)
                print("Location:", location)
                print()


if __name__ == "__main__":
    main()
