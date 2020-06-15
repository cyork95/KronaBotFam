import os
from discord.ext import commands
from dotenv import load_dotenv
import random
from src.resources import quotes

load_dotenv()
TOKEN = os.getenv('RICKY_DISCORD_TOKEN')

ricky = commands.Bot(command_prefix='>')


@ricky.event
async def on_ready():
    print('Username -> ' + ricky.user.name)
    print('ID -> ' + str(ricky.user.id))
    print(f'{ricky.user} has connected to Discord!')


@ricky.command()
async def tpb(ctx):
    await ctx.send(random.choice(quotes.trailer_park_boys_quotes))


ricky.run(TOKEN)
