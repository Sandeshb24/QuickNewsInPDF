from fetch_news import fetch_all_news
from Report.database import create_db, insert_articles_into_db

def main():
    # Set up DB and table if not already created
    create_db()

    # Fetch all news
    print("Fetching news...")
    news_data = fetch_all_news()

    # Insert news into database
    if news_data:
        print(f"Inserting {len(news_data)} articles into the database...")
        insert_articles_into_db(news_data)
    else:
        print("No articles fetched.")

if __name__ == "__main__":
    main()
