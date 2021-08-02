import asyncio
import os
from _datetime import datetime
from pytz import timezone
from Commands.QuoteCommands import *
from config.config import *
from config.KeysAndTokens import bot_auth_token

bot = commands.Bot(command_prefix='G')

for cogs in os.listdir("./Commands"):
    if cogs.endswith("Commands.py"):
        bot.load_extension(f"Commands.{cogs[:-3]}")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Gping"))
    print("Logged in!")
    scheduled_time = ["09:00", "22:00", "10:00"]
    channel_for_date = discord.Guild.get_channel(self=bot.get_guild(my_discord_server_id),
                                                 channel_id=date_channel_id)
    while True:
        karachi_pakistan = timezone('Asia/Karachi')
        pakistan_time = datetime.now(karachi_pakistan)
        print(pakistan_time.strftime('%a, %d-%b-%Y'))
        sequence = ["i", "q", "j", "t", "g"]
        time_for_automation = pakistan_time.strftime("%H:%M")
        print(time_for_automation)
        if time_for_automation == scheduled_time[0]:
            await bot.get_channel(daily_quotes_channel_id). \
                send(f'Automated Quote\n@everyone\n',
                     embed=microsoft_translator_quote_ur(bot.get_channel(daily_quotes_channel_id),
                                                         random.choice(sequence)))
        elif time_for_automation == scheduled_time[1]:
            await bot.get_channel(daily_quotes_channel_id). \
                send(f'Automated Quote\n@everyone\n'
                     ,
                     embed=microsoft_translator_quote_ur(bot.get_channel(daily_quotes_channel_id),
                                                         random.choice(sequence)))
        elif time_for_automation == scheduled_time[2]:
            await bot.get_channel(general_knowledge_channel_id). \
                send(f'Automated Quote\n@everyone\n'
                     ,
                     embed=history_today_second(ctx="none"))
        if time_for_automation == "00:00":
            date_for_automation = pakistan_time.strftime("%a, %d-%b-%Y")
            await channel_for_date.edit(name=f"『🗓』: {date_for_automation}")

        await asyncio.sleep(60)


bot.run(bot_auth_token)
