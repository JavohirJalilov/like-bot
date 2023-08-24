from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler

TOKEN ='5892121487:AAFJ8hXhSsCFBNMp-hHqFtAfwhO8RtCxdrM'

count_like = 0
count_dislike = 0

def start(update: Update, context: CallbackContext):

    chat_id = update.message.chat.id
    bot = context.bot

    like = KeyboardButton(text='👍')
    dislike = KeyboardButton(text='👎')

    keyboard = ReplyKeyboardMarkup([[like, dislike]], resize_keyboard=True)
    
    bot.sendMessage(chat_id, "Welcome to Like bot", reply_markup=keyboard)

def main(update: Update, context: CallbackContext):
    
    global count_like
    global count_dislike
    
    chat_id = update.message.chat.id
    text = update.message.text
    if  text == '👍':
        count_like += 1
    elif text == '👎':
        count_dislike += 1
    bot = context.bot

    bot.sendMessage(chat_id, text=f"like: {count_like}\ndislike: {count_dislike}")

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, main))

updater.start_polling()
updater.idle()