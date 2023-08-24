from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler
import json

TOKEN ='5892121487:AAFJ8hXhSsCFBNMp-hHqFtAfwhO8RtCxdrM'

def start(update: Update, context: CallbackContext):

    chat_id = update.message.chat.id
    bot = context.bot

    like = KeyboardButton(text='👍')
    dislike = KeyboardButton(text='👎')

    keyboard = ReplyKeyboardMarkup([[like, dislike]], resize_keyboard=True)
    
    bot.sendMessage(chat_id, "Welcome to Like bot", reply_markup=keyboard)

def main(update: Update, context: CallbackContext):
    
    f = open('data.json', 'r')
    data = json.load(f)
    f.close()

    chat_id = update.message.chat.id
    text = update.message.text
    if  text == '👍':
        data['like'] += 1
    elif text == '👎':
        data['dislike'] += 1
    count_like = data.get('like')
    count_dislike = data.get('dislike')
    
    f = open('data.json', 'w')
    f.write(json.dumps(data, indent=4))
    f.close
    bot = context.bot

    bot.sendMessage(chat_id, text=f"like: {count_like}\ndislike: {count_dislike}")

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, main))

updater.start_polling()
updater.idle()