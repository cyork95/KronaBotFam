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


def get_invasion_api_embed(invasion, embed_card):
    embed_card.add_field(name="Name: ", value=invasion['desc'], inline=True)
    if invasion['attackerReward']['itemString'] != "":
        embed_card.add_field(name="Attacking Faction and Reward: ", value=f"Help {invasion['attackingFaction']} for "
                                                                          f"{invasion['attackerReward']['itemString']}"
                             , inline=True)
    else:
        embed_card.add_field(name="Attacking Faction and Reward: ", value=f"Help {invasion['attackingFaction']} for "
                                                                          f"No Reward", inline=True)
    if invasion['defenderReward']['itemString'] != "":
        embed_card.add_field(name="Defending Faction and Reward: ", value=f"Help {invasion['defendingFaction']} for "
                                                                          f"{invasion['defenderReward']['itemString']}",
                             inline=True)
    else:
        embed_card.add_field(name="Defending Faction and Reward: ", value=f"Help {invasion['defendingFaction']} for "
                                                                          f"No Reward",
                             inline=True)
    return embed_card


def get_sale_api_embed(sale, embed_card):
    embed_card.add_field(name="Item", value=sale['item'], inline=True)
    return embed_card


def get_sortie_api_embed(sortie, embed_card):
    embed_card.add_field(name="Sortie Boss", value=sortie['boss'], inline=False)
    embed_card.add_field(name="First Mission: ", value=f"{sortie['variants'][0]['missionType']} on "
                                                       f"{sortie['variants'][0]['node']}", inline=True)
    embed_card.add_field(name="Sortie Modifier", value=sortie['variants'][0]['modifier'],
                         inline=True)
    embed_card.add_field(name="Sortie Modifier Description", value=sortie['variants'][0]['modifierDescription'],
                         inline=True)
    embed_card.add_field(name="Second Mission: ", value=f"{sortie['variants'][1]['missionType']} on "
                                                        f"{sortie['variants'][1]['node']}", inline=True)
    embed_card.add_field(name="Sortie Modifier", value=sortie['variants'][1]['modifier'],
                         inline=True)
    embed_card.add_field(name="Sortie Modifier Description", value=sortie['variants'][1]['modifierDescription'],
                         inline=True)
    embed_card.add_field(name="Third Mission: ", value=f"{sortie['variants'][2]['missionType']} on "
                                                       f"{sortie['variants'][2]['node']}", inline=True)
    embed_card.add_field(name="Sortie Modifier", value=sortie['variants'][2]['modifier'],
                         inline=True)
    embed_card.add_field(name="Sortie Modifier Description", value=sortie['variants'][2]['modifierDescription'],
                         inline=True)
    return embed_card


def get_news_api_embed(news, embed_card):
    embed_card.add_field(name=news['message'], value=news['link'], inline=True)
    return embed_card


def get_nightwave_api_embed(nw, embed_card):
    embed_card.add_field(name=nw['title'], value=nw['desc'], inline=True)
    embed_card.add_field(name="Expires: ", value=nw['expiry'], inline=True)
    embed_card.add_field(name="Reputation: ", value=nw['reputation'], inline=True)
    return embed_card


def get_sentient_api_embed(sentient, embed_card):
    embed_card.add_field(name="Mission Type: ", value=sentient['type'], inline=True)
    embed_card.add_field(name="Mission Node: ", value=sentient['node'], inline=True)
    embed_card.add_field(name="Mission Faction: ", value=sentient['faction'], inline=True)

    return embed_card


def get_syndicate_api_embed(syndicate, embed_card):
    job_iterator = 0
    if syndicate['jobs']:
        for job in syndicate['jobs']:
            embed_card.add_field(name="Job Name: ", value=f"{syndicate['jobs'][job_iterator]['type']} with levels "
                                                          f"{syndicate['jobs'][job_iterator]['enemyLevels']}", inline=True)
            embed_card.add_field(name="Rewards: ", value=syndicate['jobs'][job_iterator]['rewardPool'], inline=False)
            job_iterator += 1
    if syndicate['nodes']:
        embed_card.add_field(name="Nodes: ", value=syndicate['nodes'], inline=False)

    return embed_card
