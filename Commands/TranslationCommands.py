from discord.ext import commands

from Functions.TranslatorFunctions import *


class TranslationCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=("t",), help="Translates text to a language (Gt Arabic 'text')")
    async def translate(self, ctx, to_lang, text):
        await ctx.send(embed=microsoft_translator(ctx=ctx, text_to_translate=text, to_language=to_lang))

    @commands.command(aliases=("tu",), help="Translates text from a language to Urdu (Gu English 'text')")
    async def translate_ur(self, ctx, text):
        await ctx.send(embed=microsoft_translator_ur(ctx=ctx, text_to_translate=text))

    @commands.command(aliases=("tq",), help="Translates text to a language (Gt Arabic 'text')")
    async def translated_quote(self, ctx):
        sequence = ["i", "q", "j", "t", "g"]
        await ctx.send(embed=microsoft_translator_quote_ur(ctx=ctx, quote_of=random.choice(sequence)))


def setup(bot):
    bot.add_cog(TranslationCommands(bot))
