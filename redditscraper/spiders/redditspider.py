import scrapy
from redditscraper.praw_setup import reddit
from redditscraper.items import PostItem

class RedditSpider(scrapy.Spider):
    name = "redditspider"
    allowed_domains = ["reddit.com"]

    def start_requests(self):
        subreddit = reddit.subreddit("memes")
        top_posts = subreddit.top(time_filter="day", limit=20)
        post_item = PostItem()

        for post in top_posts:           
            post_item["title"] = post.title
            post_item["author"] = post.author.name
            post_item["url"] = post.url
            post_item["score"] = post.score
            post_item["created_date"] = post.created_utc
        
            yield post_item