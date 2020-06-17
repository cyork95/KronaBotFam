import datetime
import os
from itertools import cycle

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import random
from src.resources import quotes, joke

"""Loads .env file"""
load_dotenv()
TOKEN = os.getenv('WIZARD_DISCORD_TOKEN')

"""Setting up bot"""
wizard = commands.Bot(command_prefix='>')
status = cycle(['Doing Magic', 'Playing Magic', 'Rolling Dice'])

"""Loading the Cogs on Startup"""
wizard.load_extension(f'cogs.fun')

@wizard.command()
@commands.has_permissions(administrator=True)
async def wizard_load(ctx, extension):
    await ctx.message.delete()
    wizard.load_extension(f'cogs.{extension}')
    ctx.send(f'The extension {extension} was loaded!')


@wizard.command()
@commands.has_permissions(administrator=True)
async def wizard_unload(ctx, extension):
    await ctx.message.delete()
    wizard.unload_extension(f'cogs.{extension}')
    await ctx.send(f'The extension {extension} was unloaded!')


@wizard.command()
@commands.has_permissions(administrator=True)
async def wizard_reload(ctx, extension):
    await ctx.message.delete()
    wizard.unload_extension(f'cogs.{extension}')
    wizard.load_extension(f'cogs.{extension}')
    await ctx.send(f'The extension {extension} was reloaded!')


@wizard.event
async def on_ready():
    """When the bot Connects to discord"""
    print('Username:  ' + wizard.user.name)
    print('ID:  ' + str(wizard.user.id))
    change_status.start()
    print(f'{wizard.user} has connected to Discord!')


@wizard.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f'Pong! My latency is: {round(wizard.latency * 1000)}ms')

@tasks.loop(seconds=60)
async def change_status():
    await wizard.change_presence(activity=discord.Game(next(status)))

@wizard.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Command Failed! Please pass in all required arguments.')
    elif isinstance(error, commands.CommandNotFound):
        pass


wizard.run(TOKEN)
