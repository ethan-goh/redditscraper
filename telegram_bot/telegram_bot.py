from database.db import export_to_csv
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler
import os

load_dotenv()

async def start_command(update, context):
    await update.message.reply_text('''This bot has only one function only, which is to bring you the best memes on reddit. Type /memes to generate the most popular memes from r/memes in the last 24 hours!''')

async def help_command(update, context):
    await update.message.reply_text('''/memes: Generates the top 20 memes from r/memes in the last 24 hours''')

async def memes_command(update, context):
    await update.message.reply_text('''Preparing your memes......please wait.''')
    file_name = export_to_csv('postsdata.csv')
    chat_id = update.message.chat_id
    document = open(file_name, 'rb')
    with open(file_name, 'rb') as document:
        await context.bot.send_document(chat_id, document)



def handle_response(text):
    return "I have no time for conversation. Type /help to learn how to use me."

async def handle_message(update, context):
    await update.message.reply_text(handle_response(update.message.text))

    
if __name__ == '__main__':
    app = Application.builder().token(os.getenv("TELEGRAM_API_KEY")).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('memes', memes_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.run_polling(poll_interval=1)



    
    