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