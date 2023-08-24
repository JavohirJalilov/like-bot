from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler

TOKEN ='5892121487:AAFJ8hXhSsCFBNMp-hHqFtAfwhO8RtCxdrM'

def start(update: Update, context: CallbackContext):

    chat_id = update.message.chat.id
    bot = context.bot

    like = KeyboardButton(text='👍')
    dislike = KeyboardButton(text='👎')

    keyboard = ReplyKeyboardMarkup([[like, dislike]], resize_keyboard=True)
    
    bot.sendMessage(chat_id, "Welcome to Like bot", reply_markup=keyboard)

def main(update: Update, context: CallbackContext):

    chat_id = update.message.chat.id
    text = update.message.text
    print(text)
    bot = context.bot

    bot.sendMessage(chat_id, text="like: 0\ndislike: 0")

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, main))

updater.start_polling()
updater.idle()