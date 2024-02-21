import discord
from discord.ext import commands

def start(token: str, dev: bool):
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    bot.run(token)
