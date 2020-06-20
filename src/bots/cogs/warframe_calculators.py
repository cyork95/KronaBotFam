import json
import discord
from discord.ext import commands


with open('./cogs/cog_resources/Primary.json') as json_file:
    primary = json.load(json_file)

with open('./cogs/cog_resources/Secondary.json') as json_file:
    secondary = json.load(json_file)

with open('./cogs/cog_resources/Secondary.json') as json_file:
    melee = json.load(json_file)

with open('./cogs/cog_resources/Warframes.json') as json_file:
    warframes = json.load(json_file)

with open('./cogs/cog_resources/Enemy.json') as json_file:
    enemy = json.load(json_file)


class WarframeCalculators(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="specter", description='Specter Scaling Calculator', brief='Specter Scaling Calculator',
                      usage='<Warframe> <Weapon Name or TotalDMG> <CurrentLevel> <MissionLevel>')
    async def specter(self, ctx, specter, damage, current_level, mission_level, *args):
        damage = damage.title()
        specter = specter.title()
        if not damage.isdigit():
            for i in primary:
                if damage == i['name']:
                    damage = int(i['totalDamage']) * int(i['multishot'])
                    fire_rate = float(i['fireRate'])
            for i in secondary:
                if damage == i['name']:
                    damage = int(i['totalDamage']) * int(i['multishot'])
                    fire_rate = float(i['fireRate'])
            for i in melee:
                if damage == i['name']:
                    damage = int(i['totalDamage'])
                    fire_rate = float(i['fireRate'])
        try:
            mission_level = mission_level.split('-')
            mission_level = ((int(mission_level[0]) + int(mission_level[1])) / 2)
        except:
            mission_level = mission_level[0]
        level_diff = float(current_level) - float(mission_level)
        multi = 1 + 0.015 * (float(level_diff)) ** 1.55
        damage = float(multi) * float(damage) * float(fire_rate)
        for i in warframes:
            if specter in i['name']:
                if 'old' in args:
                    health_multi = (1 + float(level_diff) ** 1.75 * 0.005)
                    shield_multi = (1 + float(level_diff) ** 2 * 0.0075)
                    armor_multi = (1 + float(level_diff) ** 1.75 * 0.005)
                    health_value_old = int(i['health']) * health_multi
                    shield_value_old = int(i['shield']) * shield_multi
                    armor_value_old = int(i['armor']) * armor_multi
                    current_shield_value = shield_value_old
                    current_health_value = health_value_old
                    current_armor_value = armor_value_old
                    if not i['shield'] == 0 and i['armor'] == 0:
                        ehp = i['health'] * (health_multi + shield_multi * (i['shield'] / i['health']))
                        damage_reduction = 0
                    elif i['shield'] == 0 and not i['armor'] == 0:
                        ehp = i['health'] * (health_multi * (1 + ((i['armor'] * armor_multi) / 300)))
                        damage_reduction = round((current_armor_value / (current_armor_value + 300)), 5) * 100
                    elif not i['shield'] == 0 and not i['armor'] == 0:
                        ehp = i['health'] * (health_multi * (1 + ((i['armor'] * armor_multi) / 300)) + shield_multi * (
                                (i['shield']) / (i['health'])))
                        damage_reduction = round((current_armor_value / (current_armor_value + 300)), 5) * 100
                    damage_reduction = round(damage_reduction, 5)
                    embed = discord.Embed(title=i['name'],
                                          description='**DPS:** {:,}'.format(int(damage)) + '\n**Health:** {:,}'.format(
                                              int(current_health_value)) + '\n**Armor:** {:,}'.format(
                                              int(current_armor_value)) + '\n**Shields:** {:,}'.format(
                                              int(current_shield_value)) + '\n**DR:** {}%'.format(
                                              damage_reduction) + '\n**EHP:** {:,}'.format(int(ehp)),
                                          colour=discord.Colour(0x7ed321))
                    embed.set_footer(text='This does not take into account damage types.')
                    await ctx.send(embed=embed)
                else:
                    health_multi_low = (1 + float(level_diff) ** 2 * 0.015)
                    shield_multi_low = (1 + float(level_diff) ** 1.75 * 0.02)
                    armor_multi_low = (1 + float(level_diff) ** 1.75 * 0.005)
                    health_multi_high = (1 + float(level_diff) ** 0.5 * 10.7331)
                    shield_multi_high = (1 + float(level_diff) ** 0.75 * 1.6)
                    armor_multi_high = (1 + float(level_diff) ** 0.75 * 0.4)
                    health_value_low = int(i['health']) * health_multi_low
                    shield_value_low = int(i['shield']) * shield_multi_low
                    armor_value_low = int(i['armor']) * armor_multi_low
                    health_value_high = int(i['health']) * health_multi_high
                    shield_value_high = int(i['shield']) * shield_multi_high
                    armor_value_high = int(i['armor']) * armor_multi_high
                    if int(level_diff) <= 70:
                        health_multi = health_multi_low
                        shield_multi = shield_multi_low
                        armor_multi = armor_multi_low
                        current_shield_value = shield_value_low
                        current_health_value = health_value_low
                        current_armor_value = armor_value_low
                        if not i['shield'] == 0 and i['armor'] == 0:
                            ehp = i['health'] * (health_multi + shield_multi * (i['shield'] / i['health']))
                            damage_reduction = 0
                        elif i['shield'] == 0 and not i['armor'] == 0:
                            ehp = i['health'] * (health_multi * (1 + ((i['armor'] * armor_multi) / 300)))
                            damage_reduction = round((current_armor_value / (current_armor_value + 300)), 5) * 100
                        elif not i['shield'] == 0 and not i['armor'] == 0:
                            ehp = i['health'] * (
                                    health_multi * (1 + ((i['armor'] * armor_multi) / 300)) + shield_multi * (
                                    (i['shield']) / (i['health'])))
                            damage_reduction = round((current_armor_value / (current_armor_value + 300)), 5) * 100
                        damage_reduction = round(damage_reduction, 5)
                    if int(level_diff) >= 80:
                        health_multi = health_multi_high
                        shield_multi = shield_multi_high
                        armor_multi = armor_multi_high
                        current_shield_value = shield_value_high
                        current_health_value = health_value_high
                        current_armor_value = armor_value_high
                        damage_reduction = 0
                        ehp = current_health_value
                        if not i['shield'] == 0 and i['armor'] == 0:
                            ehp = i['health'] * (health_multi + shield_multi * (i['shield'] / i['health']))
                            damage_reduction = 0
                        elif i['shield'] == 0 and not i['armor'] == 0:
                            ehp = i['health'] * (health_multi * (1 + ((i['armor'] * armor_multi) / 300)))
                            damage_reduction = round((current_armor_value / (current_armor_value + 300)), 5) * 100
                        elif not i['shield'] == 0 and not i['armor'] == 0:
                            ehp = i['health'] * (
                                    health_multi * (1 + ((i['armor'] * armor_multi) / 300)) + shield_multi * (
                                    (i['shield']) / (i['health'])))
                            damage_reduction = round((current_armor_value / (current_armor_value + 300)), 5) * 100
                        damage_reduction = round(damage_reduction, 5)
                    if 70 <= level_diff <= 80:
                        x = (level_diff - 70) / (80 - 70)
                        s = (3 * x ** 2) - (2 * x ** 3)
                        health_multi = shield_value_low + s * shield_value_high
                        shield_multi = health_value_low + s * health_value_high
                        armor_multi = armor_value_low + s * armor_value_high
                        current_shield_value = (1 - s) * shield_value_low + s * shield_value_high
                        current_health_value = (1 - s) * health_value_low + s * health_value_high
                        current_armor_value = (1 - s) * armor_value_low + s * armor_value_high
                        if not i['shield'] == 0 and i['armor'] == 0:
                            ehp = i['health'] * (health_multi + shield_multi * (i['shield'] / i['health']))
                            damage_reduction = 0
                        elif i['shield'] == 0 and not i['armor'] == 0:
                            ehp = i['health'] * (health_multi * (1 + ((i['armor'] * armor_multi) / 300)))
                            damage_reduction = round((current_armor_value / (current_armor_value + 300)), 5) * 100
                        elif not i['shield'] == 0 and not i['armor'] == 0:
                            ehp = i['health'] * (health_multi * (1 + ((i['armor'] * armor_multi) / 300)) + shield_multi
                                                 * ((i['shield']) / (i['health'])))
                            damage_reduction = round((current_armor_value / (current_armor_value + 300)), 5) * 100
                        damage_reduction = round(damage_reduction, 5)
                    embed = discord.Embed(title=i['name'],
                                          description='**DPS:** {:,}'.format(int(damage)) + '\n**Health:** {:,}'.format(
                                              int(current_health_value)) + '\n**Armor:** {:,}'.format(
                                              int(current_armor_value)) + '\n**Shields:** {:,}'.format(
                                              int(current_shield_value)) + '\n**DR:** {}%'.format(
                                              damage_reduction) + '\n**EHP:** {:,}'.format(int(ehp)),
                                          colour=discord.Colour(0x7ed321))
                    embed.set_footer(text='This does not take into account damage types.')
                    await ctx.send(embed=embed)

    @specter.error
    async def specter_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              description='>specter <Warframe> <Base Dmg / Weapon> <CurrentLevel> <MissionLevel>\nUse '
                                          '`""` to use weapons with multiple words.\nUse the base mission level. Ex. '
                                          'Mot = 40\n`!specter Nidus "Prisma Gorgon" 1000 40`',
                              colour=discord.Colour(0x900f0f))
        await ctx.send(embed=embed)

    @commands.command(name="enemy")
    async def enemy(self, ctx, enemy_usr, damage, current_level, mission_level, *args):
        old = ''.join(args)
        damage = damage.title()
        enemy_x = enemy_usr.title()
        fire_rate = ''
        try:
            if damage == 'Primary':
                for i in enemy:
                    if enemy_x == i['name']:
                        weapon = i['primary']
                        for x in primary:
                            if weapon == x['name']:
                                damage = int(x['totalDamage']) * int(x['multishot'])
                                fire_rate = float(x['fireRate'])
                                for i in enemy:
                                    if enemy_x == i['name']:
                                        weapon = i['primary']
                                        for x in secondary:
                                            if weapon == x['name']:
                                                damage = int(x['totalDamage']) * int(x['multishot'])
                                                fire_rate = float(x['fireRate'])
            if damage == 'Melee':
                for i in enemy:
                    if enemy_x == i['name']:
                        weapon = i['melee']
                        for x in melee:
                            if weapon == x['name']:
                                damage = int(x['totalDamage'])
                                fire_rate = float(x['fireRate'])
        except:
            damage = 0
        level_diff = float(current_level) - float(mission_level)
        multi = 1 + 0.015 * (float(level_diff)) ** 1.55
        if fire_rate:
            damage = float(multi) * float(damage) * float(fire_rate)
        else:
            damage = float(multi) * float(damage)
        count = 0
        for i in enemy:
            if enemy_x == i['name']:
                if count == 0:
                    if 'old' in old:
                        count += 1
                        health_multi = (1 + float(level_diff) ** 1.75 * 0.005)
                        shield_multi = (1 + float(level_diff) ** 2 * 0.0075)
                        armor_multi = (1 + float(level_diff) ** 1.75 * 0.005)
                        health_value_old = int(i['health']) * health_multi
                        shield_value_old = int(i['shield']) * shield_multi
                        armor_value_old = int(i['armor']) * armor_multi
                        current_shield_value = shield_value_old
                        current_health_value = health_value_old
                        current_armor_value = armor_value_old
                        if not i['shield'] == 0 and i['armor'] == 0:
                            ehp = i['health'] * (health_multi + shield_multi * (i['shield'] / i['health']))
                            damage_reduction = 0
                        elif i['shield'] == 0 and not i['armor'] == 0:
                            ehp = i['health'] * (health_multi * (1 + ((i['armor'] * armor_multi) / 300)))
                            damage_reduction = round((current_armor_value / (current_armor_value + 300)), 5) * 100
                        elif not i['shield'] == 0 and not i['armor'] == 0:
                            ehp = i['health'] * (
                                        health_multi * (1 + ((i['armor'] * armor_multi) / 300)) + shield_multi * (
                                        (i['shield']) / (i['health'])))
                            damage_reduction = round((current_armor_value / (current_armor_value + 300)), 5) * 100
                        damage_reduction = round(damage_reduction, 5)
                        embed = discord.Embed(title=i['name'],
                                              description='**DPS:** {:,}'.format(
                                                  int(damage)) + '\n**Health:** {:,}'.format(
                                                  int(current_health_value)) + '\n**Armor:** {:,}'.format(
                                                  int(current_armor_value)) + '\n**Shields:** {:,}'.format(
                                                  int(current_shield_value)) + '\n**DR:** {}%'.format(
                                                  damage_reduction) + '\n**EHP:** {:,}'.format(int(ehp)),
                                              colour=discord.Colour(0x7ed321))
                        embed.set_footer(text='This does not take into account damage types.')
                        await ctx.send(embed=embed)
                    else:
                        count += 1
                        health_multi_low = (1 + float(level_diff) ** 2 * 0.015)
                        shield_multi_low = (1 + float(level_diff) ** 1.75 * 0.02)
                        armor_multi_low = (1 + float(level_diff) ** 1.75 * 0.005)
                        health_multi_high = (1 + float(level_diff) ** 0.5 * 10.7331)
                        shield_multi_high = (1 + float(level_diff) ** 0.75 * 1.6)
                        armor_multi_high = (1 + float(level_diff) ** 0.75 * 0.4)
                        health_value_low = int(i['health']) * health_multi_low
                        shield_value_low = int(i['shield']) * shield_multi_low
                        armor_value_low = int(i['armor']) * armor_multi_low
                        health_value_high = int(i['health']) * health_multi_high
                        shield_value_high = int(i['shield']) * shield_multi_high
                        armor_value_high = int(i['armor']) * armor_multi_high
                        if int(level_diff) <= 70:
                            health_multi = health_multi_low
                            shield_multi = shield_multi_low
                            armor_multi = armor_multi_low
                            current_shield_value = shield_value_low
                            current_health_value = health_value_low
                            current_armor_value = armor_value_low
                            if not i['shield'] == 0 and i['armor'] == 0:
                                ehp = i['health'] * (health_multi + shield_multi * (i['shield'] / i['health']))
                                damage_reduction = 0
                            elif i['shield'] == 0 and not i['armor'] == 0:
                                ehp = i['health'] * (health_multi * (1 + ((i['armor'] * armor_multi) / 300)))
                                damage_reduction = round((current_armor_value / (current_armor_value + 300)), 5) * 100
                            elif not i['shield'] == 0 and not i['armor'] == 0:
                                ehp = i['health'] * (
                                        health_multi * (1 + ((i['armor'] * armor_multi) / 300)) + shield_multi * (
                                        (i['shield']) / (i['health'])))
                                damage_reduction = round((current_armor_value / (current_armor_value + 300)), 5) * 100
                            damage_reduction = round(damage_reduction, 5)
                        if int(level_diff) >= 80:
                            health_multi = health_multi_high
                            shield_multi = shield_multi_high
                            armor_multi = armor_multi_high
                            current_shield_value = shield_value_high
                            current_health_value = health_value_high
                            current_armor_value = armor_value_high
                            damage_reduction = 0
                            ehp = current_health_value
                            if not i['shield'] == 0 and i['armor'] == 0:
                                ehp = i['health'] * (health_multi + shield_multi * (i['shield'] / i['health']))
                                damage_reduction = 0
                            elif i['shield'] == 0 and not i['armor'] == 0:
                                ehp = i['health'] * (health_multi * (1 + ((i['armor'] * armor_multi) / 300)))
                                damage_reduction = round((current_armor_value / (current_armor_value + 300)), 5) * 100
                            elif not i['shield'] == 0 and not i['armor'] == 0:
                                ehp = i['health'] * (
                                        health_multi * (1 + ((i['armor'] * armor_multi) / 300)) + shield_multi * (
                                        (i['shield']) / (i['health'])))
                                damage_reduction = round((current_armor_value / (current_armor_value + 300)), 5) * 100
                            damage_reduction = round(damage_reduction, 5)
                        if 70 <= level_diff <= 80:
                            x = (level_diff - 70) / (80 - 70)
                            s = (3 * x ** 2) - (2 * x ** 3)
                            health_multi = shield_value_low + s * shield_value_high
                            shield_multi = health_value_low + s * health_value_high
                            armor_multi = armor_value_low + s * armor_value_high
                            current_shield_value = (1 - s) * shield_value_low + s * shield_value_high
                            current_health_value = (1 - s) * health_value_low + s * health_value_high
                            current_armor_value = (1 - s) * armor_value_low + s * armor_value_high
                            if not i['shield'] == 0 and i['armor'] == 0:
                                ehp = i['health'] * (health_multi + shield_multi * (i['shield'] / i['health']))
                                damage_reduction = 0
                            elif i['shield'] == 0 and not i['armor'] == 0:
                                ehp = i['health'] * (health_multi * (1 + ((i['armor'] * armor_multi) / 300)))
                                damage_reduction = round((current_armor_value / (current_armor_value + 300)), 5) * 100
                            elif not i['shield'] == 0 and not i['armor'] == 0:
                                ehp = i['health'] * (
                                        health_multi * (1 + ((i['armor'] * armor_multi) / 300)) + shield_multi * (
                                        (i['shield']) / (i['health'])))
                                damage_reduction = round((current_armor_value / (current_armor_value + 300)), 5) * 100
                            damage_reduction = round(damage_reduction, 5)
                        embed = discord.Embed(title=i['name'],
                                              description='**DPS:** {:,}'.format(
                                                  int(damage)) + '\n**Health:** {:,}'.format(
                                                  int(current_health_value)) + '\n**Armor:** {:,}'.format(
                                                  int(current_armor_value)) + '\n**Shields:** {:,}'.format(
                                                  int(current_shield_value)) + '\n**DR:** {}%'.format(
                                                  damage_reduction) + '\n**EHP:** {:,}'.format(int(ehp)),
                                              colour=discord.Colour(0x7ed321))
                        embed.set_footer(text='This does not take into account damage types.')
                        await ctx.send(embed=embed)

    @enemy.error
    async def enemy_error(self, ctx, error):
        print(error)
        embed = discord.Embed(title='Syntax Error',
                              description='!enemy "Enemy" <primary/melee> <CurrentLevel> <Mission Level>\n`Primary` = '
                                          'Normal weapon\n`Melee` = Disarmed\nUse the base mission level. Ex. Mot = '
                                          '40\nSome enemies may not have known weapon references and will show 0 damage'
                                          '.\n!enemy "Corrupted Heavy Gunner" primary 1000 40',
                              colour=discord.Colour(0x900f0f))
        await ctx.send(embed=embed)

    @commands.command(name="ehp")
    async def ehp(self, ctx, health, armor):
        calc = int(health) * (1 + int(armor) / 300)
        ehpe = discord.Embed(title="Effective Health Calculation",
                             description="**Armor:** *" + str(armor) + "*\n**Health:** *" + str(
                                 health) + "* \n**Effective Health:** *" + str(int(calc)) + "*",
                             colour=discord.Colour(0x900f0f))
        ehpe.set_footer(text="This does not take into account damage types.")
        await ctx.send(embed=ehpe)

    @ehp.error
    async def ehp_error(self, ctx, error):
        await ctx.send("Invalid syntax.\n>ehp <total health> <total armor> <total shields>")

    @commands.command(name="status")
    async def status(self, ctx, base, status):
        bs = int(base)
        st = float(status)
        calc = bs + (bs * (float(st) / 100))
        await ctx.send(calc)

    @status.error
    async def status_error(self, ctx, error):
        await ctx.send("Invalid Syntax.\n!status <base status> <status to add>")


def setup(client):
    client.add_cog(WarframeCalculators(client))
