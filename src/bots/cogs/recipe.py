from recipe_scrapers import scrape_me
import discord
import random
from discord.ext import commands


class Recipe(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def get_recipe(self, ctx):
        await ctx.message.delete()
        recipe_number = random.randrange(10000, 240752)
        scraper = scrape_me(f'https://www.allrecipes.com/recipe/{recipe_number}/')
        if scraper.title() == 'Johnsonville® Three Cheese Italian Style Chicken Sausage Skillet Pizza':
            await ctx.channel.send("Couldn't get a recipe right now! Try again!")
        else:
            recipe_title = scraper.title()
            total_time = scraper.total_time()
            serving = scraper.yields()
            ingredients = scraper.ingredients()
            instructions = scraper.instructions()
            embed = discord.Embed(
                title='Recipe',
                description='Random Recipe for You!',
                color=discord.Color.blue()
            )

            embed.add_field(name='Recipe:', value=recipe_title)
            embed.add_field(name='Total Time:', value=total_time, inline=False)
            embed.add_field(name='Servings:', value=serving, inline=False)
            embed.add_field(name='Ingredients:', value=ingredients, inline=False)
            embed.add_field(name='Instructions:', value=instructions, inline=False)
            await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(Recipe(client))
