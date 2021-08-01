import datetime

import discord
from discord.ext import commands


class InfoCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', help="Displays your ping")
    async def ping(self, ctx):
        print("PINGED")
        embed = discord.Embed(title="Pong!  🕐 ", timestamp=datetime.datetime.utcnow(), color=0xdb0000)
        embed.set_footer(text=f"✔ Request by: {ctx.author.name}")
        embed.add_field(name="  ⌛  **PING** in milliseconds :- "
                        , value=f"  ◾ {round(self.bot.latency * 1000)}ms", inline=False)
        embed.add_field(name="  ⌛  **PING** in seconds:- "
                        , value=f"  ◾ {round(self.bot.latency, ndigits=4)}", inline=False)

        await ctx.reply(embed=embed, mention_author=True)


def setup(bot):
    bot.add_cog(InfoCommands(bot))
