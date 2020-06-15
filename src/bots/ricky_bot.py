import os
from itertools import cycle

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import random
from src.resources import quotes, joke

load_dotenv()
TOKEN = os.getenv('RICKY_DISCORD_TOKEN')

ricky = commands.Bot(command_prefix='>')

status = cycle(['Drinking', 'Smoking Weed'])


@ricky.event
async def on_ready():
    print('Username -> ' + ricky.user.name)
    print('ID -> ' + str(ricky.user.id))
    change_status.start()
    print(f'{ricky.user} has connected to Discord!')


@ricky.command()
async def tpb(ctx):
    await ctx.message.delete()
    await ctx.send(random.choice(quotes.trailer_park_boys_quotes))

@ricky.command(aliases=['joke'])
async def tell_joke(ctx):
    await ctx.message.delete()
    joke_call = joke.get_joke()

    if not joke_call:
        await ctx.send("Sorry I can't think of a joke right now try again sometime!")
    else:
        await ctx.send(joke_call['setup'] + '\n' + joke_call['punchline'])

@tasks.loop(seconds=60)
async def change_status():
    await ricky.change_presence(activity=discord.Game(next(status)))


ricky.run(TOKEN)
