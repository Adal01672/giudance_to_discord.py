import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
     print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hi")



client.run("NzcwNjg5NTkzMDY2MjU4NDgz.X5hOnQ.8sehhTS-0Xune23vLVO_gkKN7V0")
