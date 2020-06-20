import discord

from src.bots.cogs.warframe_helper_functions import get_drop_locations, get_stats


def display(result):
    embed_card = discord.Embed(title=f"{result['name']}")
    if 'rarity' in result:
        embed_card.add_field(name="Rarity", value=result['rarity'], inline=False)
    statsValue = get_stats(result['levelStats'])
    embed_card.add_field(name="Stats", value=statsValue, inline=True)
    if 'drops' in result:
        embed_card.add_field(name=f"Drop Locations", value=get_drop_locations(result['drops']), inline=False)
    return embed_card
