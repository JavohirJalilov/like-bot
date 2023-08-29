from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler, CallbackQueryHandler
from likedb import LikeDB
import json

db = LikeDB("data.json")

TOKEN ='5892121487:AAFJ8hXhSsCFBNMp-hHqFtAfwhO8RtCxdrM'

def start(update: Update, context: CallbackContext):

    chat_id = update.message.chat.id
    bot = context.bot

    db.add_user(str(chat_id)) # add user

    like = InlineKeyboardButton(text='👍', callback_data="like")
    dislike = InlineKeyboardButton(text='👎', callback_data="dislike")

    keyboard = InlineKeyboardMarkup([[like, dislike]])
    
    bot.sendMessage(chat_id, "Welcome to Like bot", reply_markup=keyboard)

def main(update: Update, context: CallbackContext):

    query = update.callback_query
    callback_data = query.data
    chat_id = query.message.chat.id

    if  callback_data == 'like':
        data = db.add_like(str(chat_id))
    elif callback_data == 'dislike':
        data = db.add_dislike(str(chat_id))

    count_like = data[str(chat_id)]['like']
    count_dislike = data[str(chat_id)]['dislike']

    like = InlineKeyboardButton(text=f'👍 {count_like}', callback_data="like")
    dislike = InlineKeyboardButton(text=f'👎 {count_dislike}', callback_data="dislike")

    keyboard = InlineKeyboardMarkup([[like, dislike]])
    query.edit_message_reply_markup(reply_markup=keyboard)

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(CallbackQueryHandler(main))

updater.start_polling()
updater.idle()