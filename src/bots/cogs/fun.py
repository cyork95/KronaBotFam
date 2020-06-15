import random

import discord
from discord.ext import commands
import re

from src.resources import quotes


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def dice(self, ctx, *, msg="1"):
        """Roll dice. Optionally input # of dice and # of sides. Ex: [p]dice 5 12"""
        await ctx.message.delete()
        invalid = 'Invalid syntax. Ex: `>dice 4` - roll four normal dice. `>dice 4 12` - roll four 12 sided dice.'
        dice_rolls = []
        dice_roll_ints = []
        try:
            dice, sides = re.split("[d\s]", msg)
        except ValueError:
            dice = msg
            sides = "6"
        try:
            for roll in range(int(dice)):
                result = random.randint(1, int(sides))
                dice_rolls.append(str(result))
                dice_roll_ints.append(result)
        except ValueError:
            return await ctx.send(self.client.bot_prefix + invalid)
        embed = discord.Embed(title="Dice rolls:", description=' '.join(dice_rolls))
        embed.add_field(name="Total:", value=sum(dice_roll_ints))
        await ctx.send("", embed=embed)

    @commands.command(aliases=['8ball'])
    async def eight_ball(self, ctx, *, question):
        await ctx.message.delete()
        await ctx.send(f'Question:    {question}\nAnswer:    {random.choice(quotes.ball_response)}')

    @commands.command(pass_context=True, aliases=['pick'])
    async def choose(self, ctx, *, choices: str):
        """Choose randomly from the options you give. [p]choose this | that"""
        await ctx.message.delete()
        await ctx.send('I choose: ``{}``'.format(random.choice(choices.split(","))))


def setup(client):
    client.add_cog(Fun(client))
