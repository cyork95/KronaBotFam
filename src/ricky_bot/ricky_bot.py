import os
import sys
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
from src.resources import quotes

load_dotenv()
TOKEN = os.getenv('RICKY_DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='#', description='')


@client.event
async def on_ready():
    print('Username -> ' + client.user.name)
    print('ID -> ' + str(client.user.id))
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.content == '#tpb':
        response = random.choice(quotes.trailer_park_boys_quotes)
        await message.channel.send(response)

    elif message.content == "#ricky_stop":
        sys.exit()


client.run(TOKEN)
