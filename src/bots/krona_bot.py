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


@krona.event
async def on_member_join(member):
    print(f'{member} has joined the server! You guys should give them a human greeting!')


@krona.event
async def on_member_remove(member):
    print(f'{member} has left the server! They will be missed for their contributions (or lack there of)!')


@krona.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f'Pong! My latency is: {round(krona.latency * 1000)}ms')


@krona.command()
async def lazy(ctx):
    await ctx.message.delete()
    await ctx.send("\"The way to get started is to quit talking and begin doing.\" -Walt Disney")


@krona.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    bot_message = channel, '{}: {}'.format(author, content)
    print(bot_message)


@krona.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Command Failed! Please pass in all required arguments.')
    elif isinstance(error, commands.CommandNotFound):
        print(error)


krona.run(TOKEN)
