import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left the server.")




client.run("NzY2OTExNzE2NTI4NDg4NDY4.X4qQMQ.rVG9vHQsskNeT8JeVqpIZZFFrJI")



