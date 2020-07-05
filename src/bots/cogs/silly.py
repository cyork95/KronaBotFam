from datetime import date

import discord
from discord.ext import commands

HALLOWEEN = date(date.today().year, 10, 31)
CHRISTMAS = date(date.today().year, 12, 25)
NEW_YEAR = date(date.today().year + 1, 1, 1)


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

    @is_it_christmas.error
    async def is_it_christmas_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you not have the Christmas Spirit? (Or too many parameters.)')
        await ctx.send(embed=embed)

    @commands.command(aliases=['halloween', 'hween', 'hwn'])
    async def is_it_halloween(self, ctx):
        """Is it Halloween yet?"""
        if date.today() == HALLOWEEN:
            await ctx.send("Yes, it is Halloween today.")
        else:
            msg = f'No, it is not Halloween today. There are {(HALLOWEEN - date.today()).days} days until Halloween.'
            await ctx.send(msg)

    @is_it_halloween.error
    async def is_it_halloween_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='BOO! You have too many parameters maybe.')
        await ctx.send(embed=embed)

    @commands.command(aliases=['newyear', 'ny'])
    async def is_it_new_year(self, ctx):
        """When is the new year?"""
        if date.today() == NEW_YEAR:
            await ctx.send('It\'s New Years today! :tada:')
        else:
            msg = f'No, it is not New Years today. There are {(NEW_YEAR - date.today()).days} days until New Year.'
            await ctx.send(msg)


def setup(client):
    client.add_cog(Silly(client))
