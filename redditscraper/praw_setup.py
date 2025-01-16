import praw
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("PRAW_CLIENT_ID")
client_secret = os.getenv("PRAW_CLIENT_SECRET")
user_agent = os.getenv("PRAW_USER_AGENT")

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)