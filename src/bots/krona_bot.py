import discord
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv
import os

"""Loads .env file"""
load_dotenv()
TOKEN = os.getenv('KRONA_DISCORD_TOKEN')

"""Setting up bot"""
krona = commands.Bot(command_prefix='>')
status = cycle(['The Game of Bot', 'Discord Bot', 'Living my bot life'])

"""Loading the Cogs on Startup"""
krona.load_extension(f'cogs.admin')
krona.load_extension(f'cogs.recipe')
krona.load_extension(f'cogs.cat')
krona.load_extension(f'cogs.poll')


@krona.command()
@commands.has_permissions(administrator=True)
async def krona_load(ctx, extension):
    await ctx.message.delete()
    krona.load_extension(f'cogs.{extension}')
    ctx.send(f'The extension {extension} was loaded!')


@krona.command()
@commands.has_permissions(administrator=True)
async def krona_unload(ctx, extension):
    await ctx.message.delete()
    krona.unload_extension(f'cogs.{extension}')
    await ctx.send(f'The extension {extension} was unloaded!')


@krona.command()
@commands.has_permissions(administrator=True)
async def krona_reload(ctx, extension):
    await ctx.message.delete()
    krona.unload_extension(f'cogs.{extension}')
    krona.load_extension(f'cogs.{extension}')
    await ctx.send(f'The extension {extension} was reloaded!')


@krona.event
async def on_ready():
    """When the bot Connects to discord"""
    print('Username:  ' + krona.user.name)
    print('ID:  ' + str(krona.user.id))
    change_status.start()
    print(f'{krona.user} has connected to Discord!')


@tasks.loop(seconds=60)
async def change_status():
    await krona.change_presence(activity=discord.Game(next(status)))


@krona.command()
async def krona_ping(ctx):
    await ctx.message.delete()
    await ctx.send(f'Pong! My latency is: {round(krona.latency * 1000)}ms')


@krona.command()
async def lazy(ctx):
    await ctx.message.delete()
    await ctx.send("\"The way to get started is to quit talking and begin doing.\" -Walt Disney")


@krona.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Command Failed! Please pass in all required arguments.')
    elif isinstance(error, commands.CommandNotFound):
        print(error)


krona.run(TOKEN)
