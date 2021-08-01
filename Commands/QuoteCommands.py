from discord.ext import commands

from Functions.TranslatorFunctions import microsoft_translator_quote_ur
from Functions.WebScrapFunctions import *
from config.config import *


class QuoteCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command("quote", aliases=("q",), help="Displays famous quotes")
    async def quote(self, ctx):
        await ctx.channel.send(quote_scraped())

    @commands.command("quoteIslamic", aliases=("qi",), help="Displays Islamic quotes")
    async def quote_islamic(self, ctx):
        await ctx.channel.send(quote_scraped_islamic())

    @commands.command(aliases=("qAg",), hidden=True)
    async def quote_all_ghazaali(self, ctx):
        if ctx.message.author.id == my_discord_profile_id:
            print("ID matches")
            await self.bot.get_channel(daily_quotes_channel_id).send(f'Automated Quote\n@everyone\n'
                                                                     , embed=microsoft_translator_quote_ur(ctx, "g"))

    @commands.command(aliases=("qAj",), hidden=True)
    async def quote_all_jawzi(self, ctx):
        if ctx.message.author.id == my_discord_profile_id:
            print("ID matches")
            await self.bot.get_channel(daily_quotes_channel_id).send(f'Automated Quote\n@everyone\n'
                                                                     , embed=microsoft_translator_quote_ur(ctx, "j"))

    @commands.command(aliases=("qAt",), hidden=True)
    async def quote_all_taymiyah(self, ctx):
        if ctx.message.author.id == my_discord_profile_id:
            print("ID matches")
            await self.bot.get_channel(daily_quotes_channel_id).send(f'Automated Quote\n@everyone\n'
                                                                     , embed=microsoft_translator_quote_ur(ctx, "t"))

    @commands.command(aliases=("qAi",), hidden=True)
    async def quote_all_islamic(self, ctx):
        if ctx.message.author.id == my_discord_profile_id:
            print("ID matches")
            await self.bot.get_channel(daily_quotes_channel_id).send(f'Automated Quote\n@everyone\n'
                                                                     , embed=microsoft_translator_quote_ur(ctx, "i"))

    @commands.command(aliases=("qA",), hidden=True)
    async def quote_all(self, ctx):
        if ctx.message.author.id == my_discord_profile_id:
            print("ID matches")
            await self.bot.get_channel(daily_quotes_channel_id).send(f'Automated Quote\n@everyone\n'
                                                                     , embed=microsoft_translator_quote_ur(ctx, "q"))

    @commands.command("quoteurdu", aliases=("qu",), help="Displays famous urdu quotes")
    async def quote_urdu(self, ctx):
        await ctx.channel.send(urdu_quote_scraped())

    @commands.command("quotetaymiyah", aliases=("qt",), help="Displays famous quotes of Ibn e Taymiyah")
    async def quote_taymiyah(self, ctx):
        await ctx.channel.send(taymiyah_quote_scraped())

    @commands.command("quotejawzi", aliases=("qj",), help="Displays famous quotes of Ibn e Jawzi")
    async def quote_jawzi(self, ctx):
        await ctx.channel.send(al_jawzi_quote_scraped())

    @commands.command("quoteghazali", aliases=("qg",), help="Displays famous quotes of Imam Al-Ghazaali")
    async def quote_ghazali(self, ctx):
        await ctx.channel.send(ghazaali_quote_scraped())


def setup(bot):
    bot.add_cog(QuoteCommands(bot))
