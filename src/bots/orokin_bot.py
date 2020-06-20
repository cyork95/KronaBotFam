import discord
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv
import os

"""Loads .env file"""
load_dotenv()
TOKEN = os.getenv('OROKIN_DISCORD_TOKEN')

"""Setting up bot"""
orokin = commands.Bot(command_prefix='>')
status = cycle(['Warframe', 'Discord Bot', 'Living my bot life'])

"""Loading the Cogs on Startup"""
orokin.load_extension(f'cogs.warframe')

@orokin.command()
@commands.has_permissions(administrator=True)
async def orokin_load(ctx, extension):
    await ctx.message.delete()
    orokin.load_extension(f'cogs.{extension}')
    ctx.send(f'The extension {extension} was loaded!')


@orokin.command()
@commands.has_permissions(administrator=True)
async def orokin_unload(ctx, extension):
    await ctx.message.delete()
    orokin.unload_extension(f'cogs.{extension}')
    await ctx.send(f'The extension {extension} was unloaded!')


@orokin.command()
@commands.has_permissions(administrator=True)
async def orokin_reload(ctx, extension):
    await ctx.message.delete()
    orokin.unload_extension(f'cogs.{extension}')
    orokin.load_extension(f'cogs.{extension}')
    await ctx.send(f'The extension {extension} was reloaded!')


@orokin.event
async def on_ready():
    """When the bot Connects to discord"""
    print('Username:  ' + orokin.user.name)
    print('ID:  ' + str(orokin.user.id))
    change_status.start()
    print(f'{orokin.user} has connected to Discord!')


@tasks.loop(seconds=60)
async def change_status():
    await orokin.change_presence(activity=discord.Game(next(status)))


@orokin.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f'Pong! My latency is: {round(orokin.latency * 1000)}ms')

orokin.run(TOKEN)
