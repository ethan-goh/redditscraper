# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime
from database.db import db_connection



class RedditscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        date_time = adapter.get("created_date")
        created_datetime = datetime.fromtimestamp(date_time)
        readable_date = created_datetime.strftime('%Y-%m-%d %H:%M:%S')
        adapter["created_date"] = readable_date


        return item



class SaveToMySQLPipeline:

    def __init__(self):
        self.conn = db_connection()
        self.cur = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS reddit_posts (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                author VARCHAR(255),
                url TEXT,
                score INT,
                created_date DATETIME
        )""")
        self.cur.execute("""TRUNCATE TABLE reddit_posts""")

    def process_item(self, item, spider):
        myquery = """INSERT INTO reddit_posts
        (title, author, url, score, created_date)
        values(%s, %s, %s, %s, %s)
        """
        val = (
            item.get('title'),
            item.get('author'),
            item.get('url'),
            item.get('score'),
            item.get('created_date')
        )

        self.cur.execute(myquery, val)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()


