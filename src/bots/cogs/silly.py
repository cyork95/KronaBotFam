from datetime import date
from discord.ext import commands

HALLOWEEN = date(date.today().year, 10, 31)
CHRISTMAS = date(date.today().year, 12, 25)


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


def setup(client):
    client.add_cog(Silly(client))
