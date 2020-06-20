import discord


def display(result):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}")
    return embed_card
