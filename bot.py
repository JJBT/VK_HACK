from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, ConversationHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, PhotoSize, File
from pymongo import MongoClient
import logging
import os
from photo import pipeline_image_recognizer


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s' ' - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = "731476129:AAFG8ozmdyP0aiHdEUgtV-fGDunem8WuOpU"


def start(bot, update):
    update.message.reply_text("Хай, зашли фоточку")


def load(bot, update):
    update.message.reply_text("Пошел на хуй, ща я тебе скажу что это за пидор")

    file = bot.get_file(update.message.photo[len(update.message.photo)-1])
    file.download(custom_path='/Users/kov270/PycharmProjects/SocialArt/ph/1.jpg')

    update.message.reply_text(pipeline_image_recognizer('/Users/kov270/PycharmProjects/SocialArt/ph/1.jpg'))


def concert(bot, update):
    pass


if __name__ == "__main__":
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('concert', concert))
    dp.add_handler(MessageHandler(Filters.photo, load))

    updater.start_polling()
