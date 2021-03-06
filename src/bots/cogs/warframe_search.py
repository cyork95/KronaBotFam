import discord
from discord.ext import commands
import requests
from datetime import datetime


def filter_components(components_name, components):
    return list(filter(lambda x: x['name'] in components_name, components))


def get_weapon_damage(damage_types):
    weapon_damage_value = " "
    for damage_type, damage_value in damage_types.items():
        weapon_damage_value += f"**{damage_type.title()}**: {damage_value} \n"
    return weapon_damage_value


def get_build_requirements(components):
    build_requirements_value = " "
    for component in components:
        build_requirements_value += f"**{component['name']}:** {component['itemCount']}\n"
    return build_requirements_value


def get_relics_drop_locations(components):
    drop_locations = []
    for component in components:
        if 'drops' in component:
            drop_locations.extend(list(map(lambda x: ' '.join(x['location'].split(' ')[:-1]), component['drops'])))
    return sorted(set(drop_locations))


def get_drop_locations(drops):
    drop_value = ''
    for drop in drops[:5]:
        for key, values in drop.items():
            drop_value += f"**{key.title()}:** {values}\n"
        drop_value += '\n'
    return drop_value


def get_stats(level_stats):
    stats_values = " "
    i = 0
    for stat in level_stats:
        stats_values += f"**Level {i + 1}**: {', '.join(stat['stats'])}\n"
        i += 1
    return stats_values


def get_abilities(abilities):
    ability_values = " "
    for ability in abilities:
        ability_values += f"**{ability['name']}**: {ability['description']}\n\n"
    return ability_values


def get_frame_attributes(result):
    frame_attributes_values = ""
    frame_attributes_values += f"**Health**: {result['health']}\n"
    frame_attributes_values += f"**Shield**: {result['shield']}\n"
    frame_attributes_values += f"**Armor**: {result['armor']}\n"
    frame_attributes_values += f"**Stamina**: {result['stamina']}\n"
    frame_attributes_values += f"**Sprint Speed**: {result['sprintSpeed']}\n"

    return frame_attributes_values


def arcane_display(result):
    embed_card = discord.Embed(title=f"{result['name']}")
    if 'rarity' in result:
        embed_card.add_field(name="Rarity", value=result['rarity'], inline=False)
    statsValue = get_stats(result['levelStats'])
    embed_card.add_field(name="Stats", value=statsValue, inline=True)
    if 'drops' in result:
        embed_card.add_field(name=f"Drop Locations", value=get_drop_locations(result['drops']), inline=False)
    return embed_card


def archgun_display(result, is_prime):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}",
                               url=result['wikiaUrl'])
    embed_card.set_thumbnail(url=result['wikiaThumbnail'])
    embed_card.add_field(name="Mastery Rank", value=result['masteryReq'], inline=True)
    embed_card.add_field(name="Build Price", value=result['buildPrice'], inline=True)
    embed_card.add_field(name="Build Time", value=f"{result['buildTime'] // 60 // 60} hrs", inline=True)
    embed_card.add_field(name="Riven Deposition", value=result['disposition'], inline=True)
    embed_card.add_field(name=f"Damage", value=get_weapon_damage(result['damageTypes']), inline=False)
    embed_card.add_field(name=f"Build Requirements", value=get_build_requirements(result['components']),
                         inline=False)
    if is_prime:
        components = filter_components(['Barrel', 'Blueprint', 'Receiver', 'Stock'], result['components'])
        drop_locations = get_relics_drop_locations(components)
        embed_card.add_field(name=f"Drop Locations", value=', '.join(drop_locations), inline=False)
    return embed_card


def archmelee_display(result, is_prime):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}",
                               url=result['wikiaUrl'])
    embed_card.set_thumbnail(url=result['wikiaThumbnail'])
    embed_card.add_field(name="Mastery Rank", value=result['masteryReq'], inline=True)
    embed_card.add_field(name="Build Price", value=result['buildPrice'], inline=True)
    embed_card.add_field(name="Build Time", value=f"{result['buildTime'] // 60 // 60} hrs", inline=True)
    embed_card.add_field(name="Riven Deposition", value=result['disposition'], inline=True)
    embed_card.add_field(name=f"Damage", value=get_weapon_damage(result['damageTypes']), inline=False)
    embed_card.add_field(name=f"Build Requirements", value=get_build_requirements(result['components']),
                         inline=False)
    if is_prime:
        components = filter_components(['Barrel', 'Blueprint', 'Receiver', 'Stock', 'Chain', 'Handle'],
                                       result['components'])
        drop_locations = get_relics_drop_locations(components)
        embed_card.add_field(name=f"Drop Locations", value=', '.join(drop_locations), inline=False)

    return embed_card


def archwing_display(result, is_prime):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}")
    embed_card.add_field(name="Attributes", value=get_frame_attributes(result), inline=False)
    embed_card.add_field(name="Mastery Rank", value=result['masteryReq'], inline=True)
    embed_card.add_field(name="Abilities", value=get_abilities(result['abilities']), inline=False)
    if 'components' in result:
        embed_card.add_field(name="Build Price", value=result['buildPrice'], inline=True)
        embed_card.add_field(name="Build Time", value=f"{result['buildTime'] // 60 // 60} hrs", inline=True)
        embed_card.add_field(name=f"Build Requirements", value=get_build_requirements(result['components']),
                             inline=False)
    if is_prime and 'components' in result:
        components = filter_components(['Chassis', 'Blueprint', 'Neuroptics', 'Systems'], result['components'])
        drop_locations = get_relics_drop_locations(components)
        embed_card.add_field(name=f"Drop Locations", value=', '.join(drop_locations), inline=False)
    return embed_card


def bow_display(result, is_prime):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}",
                               url=result['wikiaUrl'])
    embed_card.set_thumbnail(url=result['wikiaThumbnail'])
    embed_card.add_field(name="Mastery Rank", value=result['masteryReq'], inline=True)
    if 'buildPrice' in result:
        embed_card.add_field(name="Build Price", value=result['buildPrice'], inline=True)
    if 'buildTime' in result:
        embed_card.add_field(name="Build Time", value=f"{result['buildTime'] // 60 // 60} hrs", inline=True)
    embed_card.add_field(name="Riven Deposition", value=result['disposition'], inline=True)
    embed_card.add_field(name=f"Damage", value=get_weapon_damage(result['damageTypes']), inline=False)
    if 'components' in result:
        embed_card.add_field(name=f"Build Requirements", value=get_build_requirements(result['components']),
                             inline=False)
    if is_prime and 'components' in result:
        components = filter_components(['Blueprint', 'Grip', 'Lower Limb', 'String', 'Upper Limb'],
                                       result['components'])
        drop_locations = get_relics_drop_locations(components)
        embed_card.add_field(name=f"Drop Locations", value=', '.join(drop_locations), inline=False)
    return embed_card


def fish_display(result):
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


def frame_display(result, is_prime):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}",
                               url=result['wikiaUrl'])

    print(result)
    if result['name'] != "Wukong Prime":
        embed_card.set_thumbnail(url=result['wikiaThumbnail'])

    embed_card.add_field(name="Passive Ability", value=result['passiveDescription'], inline=False)
    embed_card.add_field(name="Attributes", value=get_frame_attributes(result), inline=False)
    embed_card.add_field(name="Mastery Rank", value=result['masteryReq'], inline=True)
    embed_card.add_field(name="Abilities", value=get_abilities(result['abilities']), inline=False)
    if 'components' in result:
        embed_card.add_field(name="Build Price", value=result['buildPrice'], inline=True)
        embed_card.add_field(name="Build Time", value=f"{result['buildTime'] // 60 // 60} hrs", inline=True)
        embed_card.add_field(name=f"Build Requirements", value=get_build_requirements(result['components']),
                             inline=False)
    if is_prime and 'components' in result:
        components = filter_components(['Chassis', 'Blueprint', 'Neuroptics', 'Systems'], result['components'])
        drop_locations = get_relics_drop_locations(components)
        embed_card.add_field(name=f"Drop Locations", value=', '.join(drop_locations), inline=False)
    return embed_card


def gear_display(result):
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


def melee_display(result, is_prime):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}",
                               url=result['wikiaUrl'])
    embed_card.set_thumbnail(url=result['wikiaThumbnail'])
    embed_card.add_field(name="Mastery Rank", value=result['masteryReq'], inline=True)
    embed_card.add_field(name="Build Price", value=result['buildPrice'], inline=True)
    embed_card.add_field(name="Build Time", value=f"{result['buildTime'] // 60 // 60} hrs", inline=True)
    embed_card.add_field(name="Riven Deposition", value=result['disposition'], inline=True)
    embed_card.add_field(name=f"Damage", value=get_weapon_damage(result['damageTypes']), inline=False)
    embed_card.add_field(name=f"Build Requirements", value=get_build_requirements(result['components']),
                         inline=False)
    if is_prime:
        components = filter_components(['Barrel', 'Blueprint', 'Receiver', 'Stock', 'Chain', 'Handle'],
                                       result['components'])
        drop_locations = get_relics_drop_locations(components)
        embed_card.add_field(name=f"Drop Locations", value=', '.join(drop_locations), inline=False)

    return embed_card


def mod_display(result):
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


def relic_display(result):
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
        embed_card.add_field(name="Vaulted", value="True", inline=True)
    return embed_card


def rifle_display(result, is_prime):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}",
                               url=result['wikiaUrl'])
    embed_card.set_thumbnail(url=result['wikiaThumbnail'])
    embed_card.add_field(name="Mastery Rank", value=result['masteryReq'], inline=True)
    embed_card.add_field(name="Build Price", value=result['buildPrice'], inline=True)
    embed_card.add_field(name="Build Time", value=f"{result['buildTime'] // 60 // 60} hrs", inline=True)
    embed_card.add_field(name="Riven Deposition", value=result['disposition'], inline=True)
    embed_card.add_field(name=f"Damage", value=get_weapon_damage(result['damageTypes']), inline=False)
    embed_card.add_field(name=f"Build Requirements", value=get_build_requirements(result['components']),
                         inline=False)
    if is_prime:
        components = filter_components(['Barrel', 'Blueprint', 'Receiver', 'Stock'], result['components'])
        drop_locations = get_relics_drop_locations(components)
        embed_card.add_field(name=f"Drop Locations", value=', '.join(drop_locations), inline=False)
    return embed_card


def secondary_display(result, is_prime):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}",
                               url=result['wikiaUrl'])
    embed_card.set_thumbnail(url=result['wikiaThumbnail'])
    embed_card.add_field(name="Mastery Rank", value=result['masteryReq'], inline=True)
    embed_card.add_field(name="Build Price", value=result['buildPrice'], inline=True)
    embed_card.add_field(name="Build Time", value=f"{result['buildTime'] // 60 // 60} hrs", inline=True)
    embed_card.add_field(name="Riven Deposition", value=result['disposition'], inline=True)
    embed_card.add_field(name=f"Damage", value=get_weapon_damage(result['damageTypes']), inline=False)
    embed_card.add_field(name=f"Build Requirements", value=get_build_requirements(result['components']),
                         inline=False)
    if is_prime:
        components = filter_components(['Barrel', 'Blueprint', 'Receiver', 'Stock'], result['components'])
        drop_locations = get_relics_drop_locations(components)
        embed_card.add_field(name=f"Drop Locations", value=', '.join(drop_locations), inline=False)
    return embed_card


def sentinel_display(result, is_prime):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}")
    if 'masteryReq' in result:
        embed_card.add_field(name="Mastery Rank", value=result['masteryReq'], inline=True)
    embed_card.add_field(name="Build Price", value=result['buildPrice'], inline=True)
    embed_card.add_field(name="Build Time", value=f"{result['buildTime'] // 60 // 60} hrs", inline=True)
    embed_card.add_field(name="Attributes", value=get_frame_attributes(result), inline=False)
    embed_card.add_field(name=f"Build Requirements", value=get_build_requirements(result['components']),
                         inline=False)
    if is_prime:
        components = filter_components(['Blueprint', 'Carapace', 'Cerebrum', 'Systems'], result['components'])
        dropLocations = get_relics_drop_locations(components)
        embed_card.add_field(name=f"Drop Locations", value=', '.join(dropLocations), inline=False)
    return embed_card


def sentinel_weapons_display(result):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}",
                               url=result['wikiaUrl'])
    embed_card.set_thumbnail(url=result['wikiaThumbnail'])
    embed_card.add_field(name=f"Damage", value=get_weapon_damage(result['damageTypes']), inline=False)
    embed_card.add_field(name=f"Build Requirements", value=get_build_requirements(result['components']),
                         inline=False)
    return embed_card


def sigil_display(result):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}")
    return embed_card


class WarframeSearch(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='search', help='search for any item', usage='<item name>')
    async def search(self, ctx, *, item: str):
        item = item.lower()
        request = requests.get(f'https://api.warframestat.us/items/search/{item}')
        is_prime = False
        if 'prime' in item:
            is_prime = True
        request.raise_for_status()
        response = request.json()
        if len(response) > 0:
            result = response[0]
            if result['category'] == 'Primary':
                if result['type'] == 'Bow':
                    embedCard = bow_display(result, is_prime)
                    await ctx.send(embed=embedCard)
                else:
                    embedCard = rifle_display(result, is_prime)
                    await ctx.send(embed=embedCard)
            elif result['category'] == 'Secondary':
                embedCard = secondary_display(result, is_prime)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Relics':
                embedCard = relic_display(result)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Arcanes':
                embedCard = arcane_display(result)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Warframes':
                embedCard = frame_display(result, is_prime)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Melee':
                embedCard = melee_display(result, is_prime)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Sentinels':
                embedCard = sentinel_display(result, is_prime)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Mods':
                embedCard = mod_display(result)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Sigils':
                embedCard = sigil_display(result)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Arch-Gun':
                embedCard = archgun_display(result, is_prime)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Arch-Melee':
                embedCard = archmelee_display(result, is_prime)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Archwing':
                embedCard = archwing_display(result, is_prime)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Gear':
                embedCard = gear_display(result)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Fish':
                embedCard = fish_display(result)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Sentinel Weapons':
                embedCard = sentinel_weapons_display(result)
                await ctx.send(embed=embedCard)
            else:
                await ctx.send("Can't find that item.")

        else:
            await ctx.send(f"No results found for the item {item}")

    @search.error
    async def search_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you put the actual item name?')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(WarframeSearch(client))
