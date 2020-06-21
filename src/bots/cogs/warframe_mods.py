import discord

from src.bots.cogs.warframe_helper_functions import get_drop_locations, get_stats


def display(result):
    description = 'Description Not available'
    if 'description' in result:
        description = result['description']
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{description}")
    if 'drops' in result:
        drop_values = get_drop_locations(result['drops'])
        embed_card.add_field(name="Drop Locations", value=drop_values, inline=False)
    if 'levelStats' in result:
        stats_value = get_stats(result['levelStats'])
        embed_card.add_field(name="Stats", value=stats_value, inline=True)
    return embed_card





