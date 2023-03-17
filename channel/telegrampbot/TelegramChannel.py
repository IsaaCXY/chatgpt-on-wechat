import asyncio

from common.log import logger
from channel.channel import Channel
from telegram import Bot
from telegram.error import Forbidden, NetworkError
from config import conf
from telegram import Chat, ChatMember, ChatMemberUpdated, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    ChatMemberHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)


class TelegramChannel(Channel):
    def __init__(self):
        pass

    def startup(self):
        application = Application.builder().token(conf().get("telegramToken")).build()
        application.add_handler(MessageHandler(filters.ALL, self._echo()))
        application.run_polling(allowed_updates=Update.ALL_TYPES)

    def _echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(update.message.text)

