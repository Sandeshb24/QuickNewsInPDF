import sqlite3

def create_db(db_path="news_data.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news_articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        title TEXT,
        description TEXT,
        source TEXT,
        url TEXT,
        published_at TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert_articles_into_db(articles, db_path="news_data.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for article in articles:
        cursor.execute("""
            INSERT INTO news_articles (category, title, description, source, url, published_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            article['category'],
            article['title'],
            article['description'],
            article['source'],
            article['url'],
            article['published_at']
        ))

    conn.commit()
    conn.close()
    print(f"✅ Inserted {len(articles)} articles into the database.")
