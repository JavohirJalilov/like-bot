from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler, CallbackQueryHandler
TOKEN ='5892121487:AAFJ8hXhSsCFBNMp-hHqFtAfwhO8RtCxdrM'


def start(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id

    button1 = InlineKeyboardButton(text="button1", callback_data='button__1')
    button2 = InlineKeyboardButton(text="button2", callback_data="2")
    keyboard =InlineKeyboardMarkup([[button1, button2]])

    bot.sendMessage(chat_id,text = "Inline Keyboard", reply_markup=keyboard)

def main(update, context):

    query = update.callback_query
    data = query.data
        
    button1 = InlineKeyboardButton(text="button1", callback_data='button__1')
    button2 = InlineKeyboardButton(text="button2", callback_data="2")
    keyboard =InlineKeyboardMarkup([[button1, button2]])

    query.edit_message_text(text='main', reply_markup = keyboard)

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler((CallbackQueryHandler(main)))
updater.start_polling()
updater.idle()