import asyncio
import datetime

from BotRunner import bot


def create_channel(name_of_channel, id_of_category, position, overwrites):
    bot.Guild.create_text_channel(name=name_of_channel, category=bot.Guild.CategoryChannel.id(id_of_category),
                                  position=position, overwrites=overwrites)


def create_category(name_of_category, position):
    bot.Guild.create_category(name=name_of_category, position=position)


def edit_voice_channel(name_to_change, channel_id):
    channel = bot.Guild.get_channel(channel_id)
    channel.edit(name=name_to_change)


def time_on_channel():
    time_for_automation = datetime.datetime.now().strftime("%H:%M")
    edit_voice_channel(name_to_change=time_for_automation, channel_id=869789725752455280)
    asyncio.sleep(60)


def date_on_channel():
    time_check = datetime.datetime.now().strftime("%H%M")
    date_for_automation = datetime.datetime.now().strftime("%A, %d-%b-%Y")
    if time_check == "00:00":
        edit_voice_channel(name_to_change=date_for_automation, channel_id=869790026408538113)
        asyncio.sleep(86400)
    else:
        asyncio.sleep(60)
