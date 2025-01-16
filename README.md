# Reddit Memes Telegram Bot

This is a Telegram bot that fetches the top 20 most upvoted memes from the r/memes subreddit over the past 24 hours. The bot generates a beautiful HTML report featuring meme images, titles, authors, scores, and timestamps and sends it to users upon request.

---

## Features
- Fetches the top 20 memes from **r/memes** for the past 24 hours.
- Generates an HTML report with embedded images.
- Sends the report as a downloadable file to users via Telegram.
- Hosted on **Heroku** for 24/7 availability.

---

## How to Use

### Start the Bot
1. Open Telegram and search for the bot by its username (provided by the developer).
2. Click **Start** or type `/start` to begin interacting with the bot.

### Commands
- **/start**: Displays a welcome message and instructions.
- **/help**: Lists all available commands.
- **/memes**: Fetches the top 20 trending memes and sends an HTML report containing:
  - Meme Titles
  - Reddit Authors
  - Meme Images
  - Upvote Scores
  - Creation Timestamps

### Example Interaction
1. **User**: `/memes`
2. **Bot**: `"Preparing your memes...please wait."`
3. The bot sends a downloadable HTML file containing the report.

---

## No Setup Required
Since the bot is hosted on Heroku, there's no need to install or configure anything locally. Just interact with the bot directly on Telegram. However, the free Heroku version has certain limitations that may affect the runtime of the telegram bot.

---

## Built With
- **Python**: Core programming language.
- **Scrapy**: Web scraping framework to fetch Reddit data.
- **PRAW**: Python Reddit API Wrapper.
- **MySQL**: Database to store and track data.
- **Heroku**: Hosting platform for the bot.
- **JawsDB**: Add-on for MySQL database hosting.
- **Python-Telegram-Bot**: For seamless integration with a telegram bot.
