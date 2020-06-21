import discord


def display(result):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}")
    if 'drops' in result:
        for drop_location in result['drops'][:30]:
            drop_location_value = f"**Type:** {drop_location['type']}   \n    " \
                                  f"**Rarity:** {drop_location['rarity']} \n " \
                                  f"**Chance:** {drop_location['chance']}"
            if 'rotation' in drop_location:
                drop_location_value += f"\n **Rotation:** {drop_location['rotation']}"
            embed_card.add_field(name=f"{drop_location['location']}", value=drop_location_value, inline=True)
    else:
        pass
    return embed_card
