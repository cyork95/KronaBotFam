import datetime
import os
from discord.ext import commands
from dotenv import load_dotenv
import random
from src.resources import quotes, joke

"""Loads .env file"""
load_dotenv()
TOKEN = os.getenv('WIZARD_DISCORD_TOKEN')

"""Setting up bot"""
wizard = commands.Bot(command_prefix='>')

@wizard.event
async def on_ready():
    """When the bot Connects to discord"""
    print('Username:  ' + wizard.user.name)
    print('ID:  ' + str(wizard.user.id))
    print(f'{wizard.user} has connected to Discord!')


@wizard.command()
async def ping(ctx):
    await ctx.send(f'Pong! My latency is: {round(wizard.latency * 1000)}ms')


@wizard.command(aliases=['8ball'])
async def eight_ball(ctx, *, question):
    await ctx.send(f'Question:    {question}\nAnswer:    {random.choice(quotes.ball_response)}')


wizard.run(TOKEN)
