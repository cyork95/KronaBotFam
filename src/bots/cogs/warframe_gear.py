import discord


def display(result):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}")
    if 'buildPrice' in result:
        build_price = result['buildPrice']
        embed_card.add_field(name="Build Price", value=build_price, inline=False)
    if 'buildTime' in result:
        build_time = result['buildTime']
        embed_card.add_field(name="Build Time", value=build_time, inline=False)
    if 'buildQuantity' in result:
        build_quantity = result['buildQuantity']
        embed_card.add_field(name="Build Quantity", value=build_quantity, inline=True)
    return embed_card
