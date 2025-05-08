# News Summary Report

This project fetches the latest news articles from a free news API, stores them in a local SQLite database, and generates a PDF summary report using Python.

## Features

- API Integration to retrieve live news data
- SQLite database for storing news articles by category
- Modular Python scripts for clean architecture
- Automated PDF report generation using ReportLab

 ## Project Structure
 news-summary-report/
│
├── fetch_news.py # Fetches news data from the API
├── database.py # Sets up SQLite DB and inserts articles
├── generate_report.py # Creates the PDF report
├── main.py # Main script to orchestrate everything


## Requirements

- Python 3.7 or higher
- requests
- reportlab
- python-dotenv

Install dependencies:

```bash
