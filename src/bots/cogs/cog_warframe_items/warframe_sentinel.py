import discord
from src.bots.cogs.warframe_helper_functions import get_build_requirements, get_relics_drop_locations

components_name = ['Blueprint', 'Carapace', 'Cerebrum', 'Systems']


def filter_components(components):
    return list(filter(lambda x: x['name'] in components_name, components))


def get_frame_attributes(result):
    frame_attributes_values = ""
    frame_attributes_values += f"**Health**: {result['health']}\n"
    frame_attributes_values += f"**Shield**: {result['shield']}\n"
    frame_attributes_values += f"**Armor**: {result['armor']}\n"
    frame_attributes_values += f"**Stamina**: {result['stamina']}\n"
    frame_attributes_values += f"**Power**: {result['power']}\n"

    return frame_attributes_values


async def display(result, is_prime):
    embed_card = discord.Embed(title=f"{result['name']}", description=f"{result['description']}")
    if 'masteryReq' in result:
        embed_card.add_field(name="Mastery Rank", value=result['masteryReq'], inline=True)
    embed_card.add_field(name="Build Price", value=result['buildPrice'], inline=True)
    embed_card.add_field(name="Build Time", value=f"{result['buildTime'] // 60 // 60} hrs", inline=True)
    embed_card.add_field(name="Attributes", value=get_frame_attributes(result), inline=False)
    embed_card.add_field(name=f"Build Requirements", value=get_build_requirements(result['components']),
                         inline=False)
    if is_prime:
        components = filter_components(result['components'])
        dropLocations = get_relics_drop_locations(components)
        embed_card.add_field(name=f"Drop Locations", value=', '.join(dropLocations), inline=False)
    return embed_card
