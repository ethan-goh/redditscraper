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


def export_to_csv(file_name="postsdata.html"):
    subprocess.run(['scrapy', 'crawl', 'redditspider'])

    conn = db_connection()
    cursor = conn.cursor()
    query = "SELECT title, author, url, score, created_date FROM reddit_posts"
    cursor.execute(query)
    rows = cursor.fetchall()

    with open(file_name, "w") as file:
        file.write("<html><head><title>Reddit Memes Report</title></head><body>")
        file.write("<h1>Top 20 Memes from Reddit (Past 24 Hours)</h1>")
        file.write("<table border='1' cellpadding='5'>")
        file.write("<tr><th>Title</th><th>Author</th><th>Image</th><th>Score</th><th>Created Date</th></tr>")
        
        for row in rows:
            title, author, url, score, created_date = row
            file.write("<tr>")
            file.write(f"<td>{title}</td>")
            file.write(f"<td>{author}</td>")
            file.write(f"<td><img src='{url}' alt='Meme Image' width='150'></td>")
            file.write(f"<td>{score}</td>")
            file.write(f"<td>{created_date}</td>")
            file.write("</tr>")
        
        file.write("</table></body></html>")

    cursor.close()
    conn.close()

    return file_name
