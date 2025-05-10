import requests
from bs4 import BeautifulSoup
import json
import os

def fetch_news():
    url = "https://www.pv-magazine.com/news/"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    articles = soup.select("article.article-box")
    news_list = []

    for article in articles:
        a_tag = article.select_one("h3.article-box__title a")
        if a_tag:
            title = a_tag.get_text(strip=True)
            href = a_tag.get("href", "")
            full_url = href if href.startswith("http") else f"https://www.pv-magazine.com{href}"
            news_list.append({"title": title, "url": full_url})

    os.makedirs("data", exist_ok=True)
    with open("data/news.json", "w", encoding="utf-8") as f:
        json.dump(news_list, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    fetch_news()
