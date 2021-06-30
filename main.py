import telebot
TELEGRAM_BOT_TOKEN = 'Your TOKEN'
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Assalomu alaykum , bot guruhingizdagi kirdi-chiqdilarni tozalaydi.")
@bot.message_handler(content_types=['new_chat_members'])
def delete_msg(message):
	bot.delete_message(message.chat.id, message.id)
bot.polling()
