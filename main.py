import telebot
import os

TOKEN = os.getenv("8517560824:AAH5h4SYZRX_N8HYcloETjNhtnXcTWqRvYQ")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 مرحبًا! أنا بوت تجريبي. أرسل لي أي رسالة وسأردّ عليك!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"📩 قلت: {message.text}")

print("✅ Bot is running...")
bot.polling()
