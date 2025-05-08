import requests

API_KEY = "115d4c4c4bff4b12ba3a0271a58e954f"  # Or load from .env

CATEGORIES = ["business", "technology", "science", "health"]
COUNTRY = "us"
PAGE_SIZE = 5  # number of articles per category

def fetch_headlines_by_category(category):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": API_KEY,
        "category": category,
        "country": COUNTRY,
        "pageSize": PAGE_SIZE
    }
    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200 or data.get("status") != "ok":
        print(f"Error fetching news for category '{category}': {data.get('message')}")
        return []

    articles = []
    for article in data["articles"]:
        articles.append({
            "category": category,
            "title": article.get("title"),
            "description": article.get("description"),
            "source": article.get("source", {}).get("name"),
            "url": article.get("url"),
            "published_at": article.get("publishedAt")
        })

    return articles

def fetch_all_news():
    all_articles = []
    for category in CATEGORIES:
        print(f"Fetching news for: {category}")
        category_articles = fetch_headlines_by_category(category)
        all_articles.extend(category_articles)
    return all_articles

def test():
    return "Test Success"