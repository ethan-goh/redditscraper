from dotenv import load_dotenv
import os
import mysql.connector
import csv
from redditscraper.spiders.redditspider import RedditSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from threading import Thread


load_dotenv()

def db_connection():
    password = os.getenv("MY_SQL_PASSWORD")
    return mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_DATABASE")
    )

def run_crawler():
    process = CrawlerProcess(get_project_settings())
    process.crawl(RedditSpider)
    process.start()


def export_to_csv(file_name="postsdata.csv"):
    thread = Thread(target=run_crawler)
    thread.start()
    thread.join()
    conn = db_connection()
    cursor = conn.cursor()
    query = "SELECT title, url, score, created_date FROM reddit_posts"
    cursor.execute(query)
    rows = cursor.fetchall()

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "URL", "Score", "Created Date"]) 
        writer.writerows(rows)

    cursor.close()
    conn.close()

    return file_name
