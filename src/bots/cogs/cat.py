import urllib
from urllib.request import urlopen

import discord
import json
from discord.ext import commands


class Cats(commands.Cog):
    """This module grabs Random cat pictures and sends a message """

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def random_cat(self, ctx):
        """Gives a random picture of a cat from [random.cat](http://random.cat)."""
        await ctx.message.delete()
        cat_url = 'http://aws.random.cat/meow'
        with urllib.request.urlopen(cat_url) as url:
            cat_data = json.loads(url.read().decode())
        em = discord.Embed(title="Random Cat!", colour=discord.Colour.dark_green())
        em.set_image(url=cat_data["file"])
        em.set_footer(text="Powered by aws.random.cat", icon_url=f"https://cdn.discordapp.com/avatars/"
                                                                 f"{self.client.user.id}/"
                                                                 f"{self.client.user.avatar}.png?size=64")
        await ctx.send(embed=em)

    @random_cat.error
    async def random_cat_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you add parameters you don\'t need?')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Cats(client))
