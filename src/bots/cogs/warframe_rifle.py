import discord
from src.bots.cogs.warframe_helper_functions import get_relics_drop_locations, get_build_requirements

components_name = ['Barrel', 'Blueprint', 'Receiver', 'Stock']


def filter_components(components):
    return list(filter(lambda x: x['name'] in components_name, components))


def get_weapon_damage(damage_types):
    weapon_damage_value = " "
    for damage_type, damage_value in damage_types.items():
        weapon_damage_value += f"**{damage_type.title()}**: {damage_value} \n"
    return weapon_damage_value


def display(result, is_prime):
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
        components = filter_components(result['components'])
        drop_locations = get_relics_drop_locations(components)
        embed_card.add_field(name=f"Drop Locations", value=', '.join(drop_locations), inline=False)
    return embed_card
