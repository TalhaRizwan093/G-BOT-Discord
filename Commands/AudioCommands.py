from discord.ext import commands
from pytube import YouTube

from Functions.AudioFunctions import *
from config import Strings


class AudioCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="playmylist", aliases=("mp",))
    async def play_my_list(self, ctx):
        for url in Strings.playlist:
            try:
                async with ctx.typing():
                    server = ctx.message.guild
                    voice_channel = server.voice_client
                    filename = await YTDLSource.from_url(url, loop=self.bot.loop)
                    voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
                    filename = str(filename).format()
                    filename = filename.replace("_", " ")
                    filename = filename.split("-")[0:-1]
                    filenameJoined = ""
                    filenameJoined = filenameJoined.join(filename)

                    await ctx.send('Now playing:- \n' + "```" + filenameJoined + "```")

            except ConnectionError:
                await ctx.send("The bot is not connected to a voice channel.")
            print(YouTube(url).length)
            await asyncio.sleep(YouTube(url).length + 5)

    @commands.command(name='join', help='Tells the bot to join the voice channel')
    async def join(self, ctx):
        if not ctx.message.author.voice.channel:
            await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
            return
        else:
            channel = ctx.message.author.voice.channel
            await channel.connect()

    @commands.command(name='leave', help='To make the bot leave the voice channel')
    async def leave(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel.")

    @commands.command(name='play_song', help='To play song')
    async def play(self, ctx, url):
        try:
            async with ctx.typing():
                server = ctx.message.guild
                voice_channel = server.voice_client
                filename = await YTDLSource.from_url(url, loop=self.bot.loop)
                voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
                filename = str(filename).format()
                filename = filename.replace("_", " ")
                filename = filename.split("-")[0:-1]
                filenameJoined = ""
                filenameJoined = filenameJoined.join(filename)

                await ctx.send('Now playing:- \n' + "```" + filenameJoined + "```")
        except:
            await ctx.send("Something is wrong :( ")

    @commands.command(name='pause', help='This command pauses the song')
    async def pause(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.pause()
        else:
            await ctx.send("The bot is not playing anything at the moment.")

    @commands.command(name='resume', help='Resumes the song')
    async def resume(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_paused():
            await voice_client.resume()
        else:
            await ctx.send("The bot was not playing anything before this. Use play_song command")

    @commands.command(name='stop', help='Stops the song')
    async def stop(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.stop()
        else:
            await ctx.send("The bot is not playing anything at the moment.")

    @commands.command(name='disconnect', help='Disconnect the bot from channel')
    async def disconnect(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_connected:
            await voice_client.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel at the moment.")


def setup(bot):
    bot.add_cog(AudioCommands(bot))
