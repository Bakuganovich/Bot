from telegram.ext import Updater, MessageHandler
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from Parse import *

d = start(login='', password='')

def Monday(update, context):
    update.message.reply_text(str(' '.join(d['Понедельник'])))
def Tuesday(update, context):
    update.message.reply_text(str(' '.join(d['Вторник'])))
def Wednesday(update, context):
    update.message.reply_text(str(' '.join(d['Среда'])))
def Thursday(update, context):
    update.message.reply_text(str(' '.join(d['Четверг'])))
def  Friday(update, context):
    update.message.reply_text(str(' '.join(d['Пятница'])))
def Saturday(update, context):
    update.message.reply_text(str(' '.join(d['Суббота'])))
def Sunday(update, context):
    update.message.reply_text('Вс')
def start(update, context):
    update.message.reply_text("Какой день недели вас интересует?", reply_markup=markup)
def close_keyboard(update, context):
    update.message.reply_text("ок",reply_markup=ReplyKeyboardRemove())

TOKEN = '5480993749:AAEZ-AK6xIZ5eghhGFyosy1D1glIhWsVH7U'
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
# Зарегистрируем их в диспетчере.

dp.add_handler(CommandHandler("Monday", Monday))
dp.add_handler(CommandHandler("Tuesday", Tuesday))
dp.add_handler(CommandHandler("Wednesday", Wednesday))
dp.add_handler(CommandHandler("Thursday", Thursday))
dp.add_handler(CommandHandler("Friday",  Friday))
dp.add_handler(CommandHandler("Saturday", Saturday))
dp.add_handler(CommandHandler("Sunday", Sunday))

reply_keyboard = [['/Monday', '/Tuesday'],['/Wednesday', '/Thursday'], ['/Friday', '/Saturday'], ['/Sunday']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard = True)



dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("close",close_keyboard))

updater.start_polling()
updater.idle()
