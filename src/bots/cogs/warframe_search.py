import json

import discord
from discord.ext import commands
import requests

with open('./cogs/cog_resources/lex_search.json') as json_file:
    lex_json = json.load(json_file)

with open('./cogs/cog_resources/lex_prime_search.json') as json_file:
    lex_prime_json = json.load(json_file)

with open('./cogs/cog_resources/soma_search.json') as json_file:
    soma_json = json.load(json_file)

with open('./cogs/cog_resources/vasto_search.json') as json_file:
    vasto_json = json.load(json_file)

with open('./cogs/cog_resources/vasto_prime_search.json') as json_file:
    vasto_prime_json = json.load(json_file)

with open('./cogs/cog_resources/lato_search.json') as json_file:
    lato_json = json.load(json_file)

with open('./cogs/cog_resources/lato_prime_search.json') as json_file:
    lato_prime_json = json.load(json_file)

with open('./cogs/cog_resources/magnus_search.json') as json_file:
    magnus_json = json.load(json_file)

with open('./cogs/cog_resources/viper_search.json') as json_file:
    viper_json = json.load(json_file)

with open('./cogs/cog_resources/dera_search.json') as json_file:
    dera_json = json.load(json_file)

with open('./cogs/cog_resources/war_search.json') as json_file:
    war_json = json.load(json_file)

with open('./cogs/cog_resources/nukor_search.json') as json_file:
    nukor_json = json.load(json_file)

with open('./cogs/cog_resources/talons_search.json') as json_file:
    talons_json = json.load(json_file)

with open('./cogs/cog_resources/wukong_search.json') as json_file:
    wukong_json = json.load(json_file)

with open('./cogs/cog_resources/ash_search.json') as json_file:
    ash_json = json.load(json_file)

with open('./cogs/cog_resources/chroma_search.json') as json_file:
    chroma_json = json.load(json_file)

with open('./cogs/cog_resources/volt_search.json') as json_file:
    volt_json = json.load(json_file)

with open('./cogs/cog_resources/volt_prime_search.json') as json_file:
    volt_prime_json = json.load(json_file)

with open('./cogs/cog_resources/equinox_search.json') as json_file:
    equinox_json = json.load(json_file)

with open('./cogs/cog_resources/equinox_prime_search.json') as json_file:
    equinox_prime_json = json.load(json_file)

with open('./cogs/cog_resources/excalibur_search.json') as json_file:
    excalibur_json = json.load(json_file)

with open('./cogs/cog_resources/gara_search.json') as json_file:
    gara_json = json.load(json_file)

with open('./cogs/cog_resources/guass_search.json') as json_file:
    gauss_json = json.load(json_file)

with open('./cogs/cog_resources/harrow_search.json') as json_file:
    harrow_json = json.load(json_file)

with open('./cogs/cog_resources/ivara_frame_search.json') as json_file:
    ivara_json = json.load(json_file)

with open('./cogs/cog_resources/limbo_search.json') as json_file:
    limbo_json = json.load(json_file)

with open('./cogs/cog_resources/mag_search.json') as json_file:
    mag_json = json.load(json_file)

with open('./cogs/cog_resources/nezha_search.json') as json_file:
    nezha_json = json.load(json_file)

with open('./cogs/cog_resources/nova_search.json') as json_file:
    nova_json = json.load(json_file)

with open('./cogs/cog_resources/nova_prime_search.json') as json_file:
    nova_prime_json = json.load(json_file)

with open('./cogs/cog_resources/nyx_search.json') as json_file:
    nyx_json = json.load(json_file)

with open('./cogs/cog_resources/nyx_prime_search.json') as json_file:
    nyx_prime_json = json.load(json_file)

with open('./cogs/cog_resources/oberon_search.json') as json_file:
    oberon_json = json.load(json_file)

with open('./cogs/cog_resources/oberon_prime_search.json') as json_file:
    oberon_prime_json = json.load(json_file)

with open('./cogs/cog_resources/octavia_search.json') as json_file:
    octavia_json = json.load(json_file)

with open('./cogs/cog_resources/revenant_search.json') as json_file:
    revenant_json = json.load(json_file)

with open('./cogs/cog_resources/rhino_search.json') as json_file:
    rhino_json = json.load(json_file)

with open('./cogs/cog_resources/rhino_prime_search.json') as json_file:
    rhino_prime_json = json.load(json_file)

with open('./cogs/cog_resources/saryn_search.json') as json_file:
    saryn_json = json.load(json_file)

with open('./cogs/cog_resources/saryn_prime_search.json') as json_file:
    saryn_prime_json = json.load(json_file)

with open('./cogs/cog_resources/titania_search.json') as json_file:
    titania_json = json.load(json_file)

with open('./cogs/cog_resources/trinity_search.json') as json_file:
    trinity_json = json.load(json_file)

with open('./cogs/cog_resources/trinity_prime_search.json') as json_file:
    trinity_prime_json = json.load(json_file)

with open('./cogs/cog_resources/valkyr_search.json') as json_file:
    valkyr_json = json.load(json_file)

with open('./cogs/cog_resources/valkyr_prime_search.json') as json_file:
    valkyr_prime_json = json.load(json_file)

with open('./cogs/cog_resources/wisp_search.json') as json_file:
    wisp_json = json.load(json_file)

with open('./cogs/cog_resources/zephyr_search.json') as json_file:
    zephyr_json = json.load(json_file)

with open('./cogs/cog_resources/zephyr_prime_search.json') as json_file:
    zephyr_prime_json = json.load(json_file)

with open('./cogs/cog_resources/vauban_search.json') as json_file:
    vauban_json = json.load(json_file)

with open('./cogs/cog_resources/vauban_prime_search.json') as json_file:
    vauban_prime_json = json.load(json_file)

with open('./cogs/cog_resources/tetra_search.json') as json_file:
    tetra_json = json.load(json_file)

with open('./cogs/cog_resources/latron_search.json') as json_file:
    latron_json = json.load(json_file)

with open('./cogs/cog_resources/quartakk_search.json') as json_file:
    quartakk_json = json.load(json_file)

with open('./cogs/cog_resources/sybaris_search.json') as json_file:
    sybaris_json = json.load(json_file)

with open('./cogs/cog_resources/tigris_search.json') as json_file:
    tigris_json = json.load(json_file)

with open('./cogs/cog_resources/quanta_search.json') as json_file:
    quanta_json = json.load(json_file)

with open('./cogs/cog_resources/ogris_search.json') as json_file:
    ogris_json = json.load(json_file)

with open('./cogs/cog_resources/tonkor_search.json') as json_file:
    tonkor_json = json.load(json_file)

with open('./cogs/cog_resources/seer_search.json') as json_file:
    seer_json = json.load(json_file)

with open('./cogs/cog_resources/kraken_search.json') as json_file:
    kraken_json = json.load(json_file)

with open('./cogs/cog_resources/bronco_search.json') as json_file:
    bronco_json = json.load(json_file)

with open('./cogs/cog_resources/spira_search.json') as json_file:
    spira_json = json.load(json_file)

with open('./cogs/cog_resources/machete_search.json') as json_file:
    machete_json = json.load(json_file)

with open('./cogs/cog_resources/nikana_search.json') as json_file:
    nikana_json = json.load(json_file)

with open('./cogs/cog_resources/lacera_search.json') as json_file:
    lacera_json = json.load(json_file)

with open('./cogs/cog_resources/furax_search.json') as json_file:
    furax_json = json.load(json_file)

with open('./cogs/cog_resources/bo_search.json') as json_file:
    bo_json = json.load(json_file)


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
        components = filter_components(['Barrel', 'Blueprint', 'Receiver'], result['components'])
        drop_locations = get_relics_drop_locations(components)
        embed_card.add_field(name=f"Drop Locations", value=', '.join(drop_locations), inline=False)
    return embed_card


def secondary_no_build_display(result):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}",
                               url=result['wikiaUrl'])
    embed_card.set_thumbnail(url=result['wikiaThumbnail'])
    embed_card.add_field(name="Mastery Rank", value=result['masteryReq'], inline=True)
    embed_card.add_field(name="Riven Deposition", value=result['disposition'], inline=True)
    embed_card.add_field(name=f"Damage", value=get_weapon_damage(result['damageTypes']), inline=False)
    return embed_card


def secondary_cannot_obtain_display(result):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}",
                               url=result['wikiaUrl'])
    embed_card.set_thumbnail(url=result['wikiaThumbnail'])
    embed_card.add_field(name="Mastery Rank", value=result['masteryReq'], inline=True)
    embed_card.add_field(name="Riven Deposition", value=result['disposition'], inline=True)
    embed_card.add_field(name=f"Damage", value=get_weapon_damage(result['damageTypes']), inline=False)
    embed_card.add_field(name=f"Build Requirements", value="Cannot Obtain unless founder.",
                         inline=False)
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
        if 'lex' in item:
            if is_prime:
                embedCard = secondary_display(lex_prime_json, is_prime)
                await ctx.send(embed=embedCard)
                return
            else:
                embedCard = secondary_no_build_display(lex_json[0])
                await ctx.send(embed=embedCard)
                return
        if 'lato' == item:
            if is_prime:
                embedCard = secondary_cannot_obtain_display(lato_prime_json)
                await ctx.send(embed=embedCard)
                return
            else:
                embedCard = secondary_no_build_display(lato_json)
                await ctx.send(embed=embedCard)
                return
        if 'soma' in item:
            embedCard = rifle_display(soma_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'vasto' == item:
            if is_prime:
                embedCard = secondary_display(vasto_prime_json, is_prime)
                await ctx.send(embed=embedCard)
                return
            else:
                embedCard = secondary_no_build_display(vasto_json)
                await ctx.send(embed=embedCard)
                return
        if 'magnus' == item:
            embedCard = secondary_display(magnus_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'viper' == item:
            embedCard = secondary_display(viper_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'dera' == item:
            embedCard = secondary_display(dera_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'war' == item:
            embedCard = melee_display(war_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'nukor' == item:
            embedCard = secondary_display(nukor_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'talons' == item:
            embedCard = melee_display(talons_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'wukong' == item:
            embedCard = frame_display(wukong_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'ash' == item:
            embedCard = frame_display(ash_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'chroma' == item:
            embedCard = frame_display(chroma_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'volt' == item:
            embedCard = frame_display(volt_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'volt prime' == item:
            embedCard = frame_display(volt_prime_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'equinox' == item:
            embedCard = frame_display(equinox_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'equinox prime' == item:
            embedCard = frame_display(equinox_prime_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'excalibur' == item:
            embedCard = frame_display(excalibur_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'gara' == item:
            embedCard = frame_display(gara_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'gauss' == item:
            embedCard = frame_display(gauss_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'harrow' == item:
            embedCard = frame_display(harrow_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'ivara' == item:
            embedCard = frame_display(ivara_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'limbo' == item:
            embedCard = frame_display(limbo_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'mag' == item:
            embedCard = frame_display(mag_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'nezha' == item:
            embedCard = frame_display(nezha_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'nova' == item:
            embedCard = frame_display(nova_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'nova prime' == item:
            embedCard = frame_display(nova_prime_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'nyx' == item:
            embedCard = frame_display(nyx_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'nyx prime' == item:
            embedCard = frame_display(nyx_prime_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'oberon' == item:
            embedCard = frame_display(oberon_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'oberon prime' == item:
            embedCard = frame_display(oberon_prime_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'octavia' == item:
            embedCard = frame_display(octavia_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'revenant' == item:
            embedCard = frame_display(revenant_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'rhino' == item:
            embedCard = frame_display(rhino_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'rhino prime' == item:
            embedCard = frame_display(rhino_prime_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'saryn' == item:
            embedCard = frame_display(saryn_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'saryn prime' == item:
            embedCard = frame_display(saryn_prime_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'titania' == item:
            embedCard = frame_display(titania_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'trinity' == item:
            embedCard = frame_display(trinity_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'trinity prime' == item:
            embedCard = frame_display(trinity_prime_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'valkyr' == item:
            embedCard = frame_display(trinity_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'valkyr prime' == item:
            embedCard = frame_display(trinity_prime_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'wisp' == item:
            embedCard = frame_display(wisp_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'zephyr' == item:
            embedCard = frame_display(zephyr_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'zephyr prime' == item:
            embedCard = frame_display(zephyr_prime_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'vauban' == item:
            embedCard = frame_display(vauban_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'vauban prime' == item:
            embedCard = frame_display(vauban_prime_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'tetra' == item:
            embedCard = rifle_display(tetra_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'latron' == item:
            embedCard = rifle_display(latron_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'quartakk' == item:
            embedCard = rifle_display(quartakk_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'sybaris' == item:
            embedCard = rifle_display(sybaris_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'quanta' == item:
            embedCard = rifle_display(quanta_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'ogris' == item:
            embedCard = rifle_display(ogris_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'tonkor' == item:
            embedCard = rifle_display(tonkor_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'tigris' == item:
            embedCard = frame_display(tigris_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'seer' == item:
            embedCard = rifle_display(seer_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'kraken' == item:
            embedCard = secondary_display(kraken_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'bronco' == item:
            embedCard = secondary_display(bronco_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'spira' == item:
            embedCard = secondary_display(spira_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'machete' == item:
            embedCard = melee_display(machete_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'nikana' == item:
            embedCard = melee_display(nikana_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'lacera' == item:
            embedCard = melee_display(lacera_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'furax' == item:
            embedCard = melee_display(furax_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        if 'bo' == item:
            embedCard = melee_display(bo_json, is_prime)
            await ctx.send(embed=embedCard)
            return
        request.raise_for_status()
        response = request.json()
        if len(response) > 0:
            result = response[0]
            if 'furis' == item:
                embedCard = secondary_no_build_display(result)
                await ctx.send(embed=embedCard)
                return
            if 'braton' == item:
                embedCard = secondary_no_build_display(result)
                await ctx.send(embed=embedCard)
                return
            if 'tetra' == item:
                embedCard = secondary_no_build_display(result)
                await ctx.send(embed=embedCard)
                return
            if 'sybaris' == item:
                embedCard = secondary_no_build_display(result)
                await ctx.send(embed=embedCard)
                return
            if 'strun' == item:
                embedCard = secondary_no_build_display(result)
                await ctx.send(embed=embedCard)
                return
            if 'tigris' == item:
                embedCard = secondary_no_build_display(result)
                await ctx.send(embed=embedCard)
                return
            if 'sicarus' == item:
                embedCard = secondary_no_build_display(result)
                await ctx.send(embed=embedCard)
                return
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
        print(error)
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you put the actual item name?')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(WarframeSearch(client))
