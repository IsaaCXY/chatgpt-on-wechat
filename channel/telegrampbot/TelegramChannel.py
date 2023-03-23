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
    ContextTypes,
    MessageHandler,
    filters,
)


class TelegramChannel(Channel):
    def __init__(self):
        pass

    def startup(self):
        logger.info("创建telegram")
        application = Application.builder().token(conf().get("telegramToken")).build()
        application.add_handler(MessageHandler(filters.ALL, self._echo))
        application.run_polling(allowed_updates=Update.ALL_TYPES)

    async def _echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(update.message.text)

    async def reply_info(self, update: Update, context):
        input_message_text = update.message.text

        if input_message_text.startswith("bot "):
            bot_reply = super(TelegramChannel, self).build_reply_content(input_message_text)
            await update.message.reply_text(bot_reply)
        else:
            await update.message.reply_text(input_message_text)
