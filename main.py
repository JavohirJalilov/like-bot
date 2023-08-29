from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler
from likedb import LikeDB
import json

db = LikeDB("data.json")

TOKEN ='5892121487:AAFJ8hXhSsCFBNMp-hHqFtAfwhO8RtCxdrM'

def start(update: Update, context: CallbackContext):

    chat_id = update.message.chat.id
    bot = context.bot

    db.add_user(str(chat_id)) # add user

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
        data = db.add_like(str(chat_id))
    elif text == '👎':
        data = db.add_dislike(str(chat_id))

    count_like = data[str(chat_id)]['like']
    count_dislike = data[str(chat_id)]['dislike']

    bot = context.bot

    bot.sendMessage(chat_id, text=f"like: {count_like}\ndislike: {count_dislike}")

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, main))

updater.start_polling()
updater.idle()