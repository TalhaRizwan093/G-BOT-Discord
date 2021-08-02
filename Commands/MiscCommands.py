import asyncio

from discord.ext import commands

from Functions.MiscFunctions import *
from config import Strings


class MiscCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="g", help="Displays G™'s attitude!")
    async def g(self, ctx):
        await ctx.channel.send("جی بھائی؟ کوئی مسئلہ؟")

    @commands.command(name="speak", help="G™ will text something")
    async def speak(self, ctx):
        async with ctx.typing():
            await ctx.reply(random.choice(Strings.answer_words))
            await asyncio.sleep(9)
            await ctx.send(f"{str(randart())}")

    @commands.command(name="txtconvertrandom", aliases=("tcr",), help="Converts your text to art! (Gtcr 'text')")
    async def text_converter_random(self, ctx, text):
        await ctx.send(f"```{text_converter_random(text)}```")

    @commands.command(name="txtconvert", aliases=("tc",), help="Converts your text to art into "
                                                               "font you specify! (Gtcr 'text' font)")
    async def text_converter(self, ctx, text, font):
        await ctx.send(f"```{text2art(text=text, font=font)}```")

    @commands.command(name="listfonts", aliases=("lf",), help="Displays list of fonts "
                                                              "available to convert your text")
    async def list_fonts(self, ctx):
        await ctx.send(f"```{list_fonts()}```")


def setup(bot):
    bot.add_cog(MiscCommands(bot))
