import os
from itertools import cycle

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

"""Loads .env file"""
load_dotenv()
TOKEN = os.getenv('WIZARD_DISCORD_TOKEN')

"""Setting up bot"""
wizard = commands.Bot(command_prefix='>')
status = cycle(['Doing Magic', 'Playing Magic', 'Rolling Dice'])

"""Loading the Cogs on Startup"""
wizard.load_extension(f'cogs.fun')
wizard.load_extension(f'cogs.silly')


@wizard.command()
@commands.has_permissions(administrator=True)
async def wizard_load(ctx, extension):
    await ctx.message.delete()
    wizard.load_extension(f'cogs.{extension}')
    ctx.send(f'The extension {extension} was loaded!')


@wizard_load.error
async def wizard_load_error(self, ctx, error):
    embed = discord.Embed(title='Syntax Error',
                          colour=discord.Colour(0x9013fe),
                          description='Did you mistype the extension name?')
    await ctx.send(embed=embed)


@wizard.command()
@commands.has_permissions(administrator=True)
async def wizard_unload(ctx, extension):
    await ctx.message.delete()
    wizard.unload_extension(f'cogs.{extension}')
    await ctx.send(f'The extension {extension} was unloaded!')


@wizard_unload.error
async def wizard_unload_error(self, ctx, error):
    embed = discord.Embed(title='Syntax Error',
                          colour=discord.Colour(0x9013fe),
                          description='Did you mistype the extension name?')
    await ctx.send(embed=embed)


@wizard.command()
@commands.has_permissions(administrator=True)
async def wizard_reload(ctx, extension):
    await ctx.message.delete()
    wizard.unload_extension(f'cogs.{extension}')
    wizard.load_extension(f'cogs.{extension}')
    await ctx.send(f'The extension {extension} was reloaded!')


@wizard_reload.error
async def krona_reload_error(self, ctx, error):
    embed = discord.Embed(title='Syntax Error',
                          colour=discord.Colour(0x9013fe),
                          description='Did you mistype the extension name?')
    await ctx.send(embed=embed)


@wizard.event
async def on_ready():
    """When the bot Connects to discord"""
    print('Username:  ' + wizard.user.name)
    print('ID:  ' + str(wizard.user.id))
    change_status.start()
    print(f'{wizard.user} has connected to Discord!')


@wizard.command()
async def wizard_ping(ctx):
    await ctx.message.delete()
    await ctx.send(f'Pong! My latency is: {round(wizard.latency * 1000)}ms')


@wizard_ping.error
async def wizard_ping_error(self, ctx, error):
    embed = discord.Embed(title='Syntax Error',
                          colour=discord.Colour(0x9013fe),
                          description='Did you add parameters you don\'t need?')
    await ctx.send(embed=embed)


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
