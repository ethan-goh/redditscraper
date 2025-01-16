from dotenv import load_dotenv
import os
import mysql.connector
import csv
import subprocess


load_dotenv()

def db_connection():
    return mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_DATABASE")
    )


def export_to_csv(file_name="postsdata.csv"):
    subprocess.run(['scrapy', 'crawl', 'redditspider'])

    conn = db_connection()
    cursor = conn.cursor()
    query = "SELECT title, author, url, score, created_date FROM reddit_posts"
    cursor.execute(query)
    rows = cursor.fetchall()

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Author", "URL", "Score", "Created Date"]) 
        writer.writerows(rows)

    cursor.close()
    conn.close()

    return file_name
