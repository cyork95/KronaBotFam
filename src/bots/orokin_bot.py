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
orokin.load_extension(f'cogs.warframe_calculators')
orokin.load_extension(f'cogs.warframe_search')


@orokin.command()
@commands.has_permissions(administrator=True)
async def orokin_load(ctx, extension):
    await ctx.message.delete()
    orokin.load_extension(f'cogs.{extension}')
    ctx.send(f'The extension {extension} was loaded!')


@orokin_load.error
async def orokin_load_error(ctx, error):
    embed = discord.Embed(title='Syntax Error',
                          colour=discord.Colour(0x9013fe),
                          description='Did you mistype the extension name?')
    await ctx.send(embed=embed)


@orokin.command()
@commands.has_permissions(administrator=True)
async def orokin_unload(ctx, extension):
    await ctx.message.delete()
    orokin.unload_extension(f'cogs.{extension}')
    await ctx.send(f'The extension {extension} was unloaded!')


@orokin_unload.error
async def orokin_unload_error(ctx, error):
    embed = discord.Embed(title='Syntax Error',
                          colour=discord.Colour(0x9013fe),
                          description='Did you mistype the extension name?')
    await ctx.send(embed=embed)


@orokin.command()
@commands.has_permissions(administrator=True)
async def orokin_reload(ctx, extension):
    await ctx.message.delete()
    orokin.unload_extension(f'cogs.{extension}')
    orokin.load_extension(f'cogs.{extension}')
    await ctx.send(f'The extension {extension} was reloaded!')


@orokin_reload.error
async def orokin_reload_error(ctx, error):
    embed = discord.Embed(title='Syntax Error',
                          colour=discord.Colour(0x9013fe),
                          description='Did you mistype the extension name?')
    await ctx.send(embed=embed)


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
async def orokin_ping(ctx):
    await ctx.message.delete()
    await ctx.send(f'Pong! My latency is: {round(orokin.latency * 1000)}ms')


orokin.run(TOKEN)
