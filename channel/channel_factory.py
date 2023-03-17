"""
channel factory
"""
from common.log import logger

def create_channel(channel_type):
    """
    create a channel instance
    :param channel_type: channel type code
    :return: channel instance
    """
    logger.info(channel_type)
    if channel_type == 'wx':
        from channel.wechat.wechat_channel import WechatChannel
        return WechatChannel()
    elif channel_type == 'wxy':
        from channel.wechat.wechaty_channel import WechatyChannel
        return WechatyChannel()
    elif channel_type == "telegram":
        from channel.telegrampbot.TelegramChannel import TelegramChannel
        return TelegramChannel()
    raise RuntimeError
