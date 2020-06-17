from random import random

import discord
import json
from enum import Enum
from datetime import date
from discord.ext import commands

HALLOWEEN = date(2017, 10, 31)
CHRISTMAS = date(2017, 12, 25)


class RPSLS(Enum):
    rock = "\N{RAISED FIST} Rock!"
    paper = "\N{RAISED HAND WITH FINGERS SPLAYED} Paper!"
    scissors = "\N{BLACK SCISSORS} Scissors!"
    lizard = "\N{LIZARD} Lizard!"
    spock = "\N{RAISED HAND WITH PART BETWEEN MIDDLE AND RING FINGERS} Spock!"


class RPSLSParser:
    def __init__(self, argument):
        argument = argument.lower()
        if argument == "rock":
            self.choice = RPSLS.rock
        elif argument == "paper":
            self.choice = RPSLS.paper
        elif argument == "scissors":
            self.choice = RPSLS.scissors
        elif argument == "lizard":
            self.choice = RPSLS.lizard
        elif argument == "spock":
            self.choice = RPSLS.spock
        else:
            raise


class Silly(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['christmas', 'xmas'])
    async def is_it_christmas(self, ctx):
        """Is it Christmas yet?"""
        if date.today() == CHRISTMAS:
            await ctx.send("Yes, it is Christmas today.")
        else:
            msg = f'No, it is not Christmas today. There are {(CHRISTMAS - date.today()).days} days until Christmas.'
            await ctx.send(msg)

    @commands.command(aliases=['halloween', 'hween', 'hwn'])
    async def is_it_halloween(self, ctx):
        """Is it Halloween yet?"""
        if date.today() == HALLOWEEN:
            await ctx.send("Yes, it is Halloween today.")
        else:
            msg = f'No, it is not Halloween today. There are {(HALLOWEEN - date.today()).days} days until Halloween.'
            await ctx.send(msg)

    @commands.command(aliases=['rock', 'paper', 'scissors', 'lizard', 'spock', 'rps'])
    async def settle(self, ctx, your_choice: RPSLSParser = None):
        """Play rock paper scissors, lizard spock """
        if your_choice is not None:
            author = ctx.message.author.display_name
            player_choice = your_choice.choice
            available = RPSLS.rock, RPSLS.paper, RPSLS.scissors, RPSLS.lizard, RPSLS.spock
            bot_choice = random.choice(available)
            cond = {
                (RPSLS.rock, RPSLS.paper): False,
                (RPSLS.rock, RPSLS.scissors): True,
                (RPSLS.rock, RPSLS.lizard): True,
                (RPSLS.rock, RPSLS.spock): False,
                (RPSLS.paper, RPSLS.rock): True,
                (RPSLS.paper, RPSLS.scissors): False,
                (RPSLS.paper, RPSLS.lizard): False,
                (RPSLS.paper, RPSLS.spock): True,
                (RPSLS.scissors, RPSLS.rock): False,
                (RPSLS.scissors, RPSLS.paper): True,
                (RPSLS.scissors, RPSLS.lizard): True,
                (RPSLS.scissors, RPSLS.spock): False,
                (RPSLS.lizard, RPSLS.rock): False,
                (RPSLS.lizard, RPSLS.paper): True,
                (RPSLS.lizard, RPSLS.scissors): False,
                (RPSLS.lizard, RPSLS.spock): True,
                (RPSLS.spock, RPSLS.rock): True,
                (RPSLS.spock, RPSLS.paper): False,
                (RPSLS.spock, RPSLS.scissors): True,
                (RPSLS.spock, RPSLS.lizard): False
            }
            em = discord.Embed()
            em.add_field(name=f'{author}', value=f'{player_choice.value}', inline=True)
            em.add_field(name=f'Wizard', value=f'{bot_choice.value}', inline=True)
            if bot_choice == player_choice:
                outcome = None
            else:
                outcome = cond[(player_choice, bot_choice)]
            if outcome is True:
                em.set_footer(text="You win!")
                await ctx.send(embed=em)
            elif outcome is False:
                em.set_footer(text="You lose...")
                await ctx.send(embed=em)
            else:
                em.set_footer(text="We're square")
                await ctx.send(embed=em)
        else:
            msg = 'rock, paper, scissors, lizard, OR spock'
            await ctx.send(f'Enter: `{ctx.prefix}{ctx.invoked_with} {msg}`', delete_after=5)


def setup(client):
    client.add_cog(Silly(client))
