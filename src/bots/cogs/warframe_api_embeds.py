import discord


def get_alert_api_embed(alert, embed_card):
    embed_card.add_field(name="Alert: ", value=alert['mission']['description'], inline=False)
    embed_card.add_field(name="Expires : ", value=alert['eta'], inline=True)
    embed_card.add_field(name="Affected Node: ", value=alert['mission']['node'], inline=True)
    embed_card.add_field(name="Mission Type: ", value=alert['mission']['type'], inline=True)
    embed_card.add_field(name="Faction: ", value=alert['mission']['faction'], inline=True)
    embed_card.add_field(name="Item Rewards: ", value=alert['mission']['reward']['asString'], inline=True)
    embed_card.add_field(name="Enemies: ", value=f"{alert['mission']['faction']} with levels "
                                                 f"{alert['mission']['minEnemyLevel']} - "
                                                 f"{alert['mission']['maxEnemyLevel']}", inline=True)

    return embed_card


def get_conclave_api_embed(conclave, embed_card):
    embed_card.add_field(name="Description: ", value=conclave['description'], inline=True)
    embed_card.add_field(name="Expires: ", value=f"{conclave['eta']}", inline=True)
    embed_card.add_field(name="Node: ", value=conclave['node'], inline=True)
    return embed_card


def get_darvo_api_embed(darvo, embed_card):
    embed_card.add_field(name='Item Name:', value=darvo['item'])
    embed_card.add_field(name='Original Price:', value=darvo['originalPrice'])
    embed_card.add_field(name='Sale Price:', value=darvo['salePrice'])
    embed_card.add_field(name='Time Left:', value=darvo['eta'])
    return embed_card


def get_event_api_embed(event, embed_card):
    embed_card.add_field(name=event['description'], value=event['asString'], inline=False)
    return embed_card


def get_sale_api_embed(sale, embed_card):
    embed_card.add_field(name="Item", value=sale['item'], inline=True)
    return embed_card
