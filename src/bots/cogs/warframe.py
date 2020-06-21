import json
from urllib.request import Request, urlopen
import discord
from discord.ext import commands
import requests
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.bots.cogs.cog_warframe_items import warframe_arcanes, warframe_bow, warframe_frame, warframe_melee, \
    warframe_mods, warframe_relics, warframe_rifle, warframe_sentinel, warframe_secondary, warframe_arch_gun, \
    warframe_sigil, warframe_arch_melee, warframe_archwing, warframe_gear, warframe_sentinel_weapons, warframe_fish

with open('./cogs/cog_resources/languages.json') as json_file:
    lang = json.load(json_file)

with open('./cogs/cog_resources/sortiedata.json') as json_file:
    sortie_data = json.load(json_file)

with open('./cogs/cog_resources/missiontypes.json') as json_file:
    mission_types = json.load(json_file)

with open('./cogs/cog_resources/solnodes.json') as json_file:
    sol_nodes = json.load(json_file)

with open('./cogs/cog_resources/farming.json') as json_file:
    farming_data = json.load(json_file)


class Warframe(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def earth(self, ctx):
        await ctx.message.delete()
        req = Request('https://api.warframestat.us/xb1/cetusCycle', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        data = json.loads(webpage)
        if data['isDay']:
            await ctx.send(
                'It Is Currently **Day-time** On Earth With __{0}__ Left Until **Evening**.'.format(data['timeLeft']))
        if not data['isDay']:
            await ctx.send(
                'It Is Currently **Night-time** On Earth With __{0}__ Left Until **Morning**.'.format(data['timeLeft']))

    @earth.error
    async def earth_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you add parameters?')
        await ctx.send(embed=embed)

    @commands.command()
    async def baro(self, ctx):
        await ctx.message.delete()
        req = Request('https://api.warframestat.us/xb1/voidTrader', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        data = json.loads(webpage)
        embed = discord.Embed(title="Barro's Inventory", description='The Void Trader is currently at {0} and '
                                                                     'he will be leaving in {1}.\n\n'.format(
            data['location'], data['endString']))
        if not data['active']:
            await ctx.send('Baro Ki`Teer will be arriving at **{0}** in __{1}__.'.format(
                data['location'], data['startString']))
        if data['active']:
            baro_inventory = data['inventory']
            for disapointment in baro_inventory:
                item_name = disapointment['item']
                embed.add_field(name=f'{item_name}:', value='*Ducats:* __{1}__  *Credits:* __{2}__'.format(
                    disapointment['item'], disapointment['ducats'], disapointment['credits']))
            await ctx.send(embed=embed)

    @baro.error
    async def baro_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you add parameters?')
        await ctx.send(embed=embed)

    @commands.command(aliases=['vallis', 'orb'])
    async def orb_vallis(self, ctx):
        await ctx.message.delete()
        request = Request('https://api.warframestat.us/xb1/vallisCycle', headers={'User-Agent': 'Mozilla/5.0'})
        vallis_webpage = urlopen(request).read()
        json_data = json.loads(vallis_webpage)
        if not json_data['isWarm']:
            await ctx.send('It is **Cold** at Orb Vallis. {0} until it is **Warm**'.format(json_data['timeLeft']))
        if json_data['isWarm']:
            await ctx.send('It is **Warm** at Orb Vallis for the next __{0}__'.format(json_data['timeLeft']))

    @orb_vallis.error
    async def orb_vallis_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you add parameters?')
        await ctx.send(embed=embed)

    @commands.command(aliases=['endless', 'ef'])
    async def endless_fissure(self, ctx):
        await ctx.message.delete()
        req = Request('https://api.warframestat.us/xb1/fissures', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        data = json.loads(webpage)
        missionTypes = ('Defense', 'Survival', 'Interception', 'Excavation')
        embed = discord.Embed(title="Endless Fissures", description='Endless fissure missions currently available:')
        for mission in data:
            if mission['missionType'] in missionTypes:
                relic = mission['tier']
                embed.add_field(name=f'{relic}:', value='**{0}**  *{1}*  __{2}__'.format(mission['missionType'],
                                                                                         mission['node'],
                                                                                         mission['eta']))
            if 0 == mission['missionType']:
                await ctx.send('No Endless Fissure Missions available at this time.')
        await ctx.send(embed=embed)

    @endless_fissure.error
    async def endless_fissure_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you add parameters?')
        await ctx.send(embed=embed)

    @commands.command(aliases=['f'])
    async def fissure(self, ctx):
        await ctx.message.delete()
        req = Request('https://api.warframestat.us/xb1/fissures', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        data = json.loads(webpage)
        embed = discord.Embed(title="Fissures", description='Fissure missions currently available:')
        for mission in data:
            relic = mission['tier']
            embed.add_field(name=f'{relic}:', value='**{0}**  *{1}*  __{2}__'.format(mission['missionType'],
                                                                                     mission['node'],
                                                                                     mission['eta']))
        await ctx.send(embed=embed)

    @fissure.error
    async def fissure_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you add parameters?')
        await ctx.send(embed=embed)

    @commands.command()
    async def darvo(self, ctx):
        await ctx.message.delete()
        req = Request('https://api.warframestat.us/xb1/dailyDeals', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        dataPack = json.loads(webpage)
        embed = discord.Embed(title="Darvo Deal")
        for data in dataPack:
            totalLeft = int(data['total'] - data['sold'])
            if totalLeft == 0:
                await ctx.send('Darvo has sold out.  {0} is no longer available at a lower price.'.format(data['item']))
            else:
                darvo_item = data['item']
                original_price = data['originalPrice']
                sale_price = data['salePrice']
                time_left = data['eta']
                embed.add_field(name='Item Name:', value=darvo_item)
                embed.add_field(name='Original Price:', value=original_price)
                embed.add_field(name='Sale Price:', value=sale_price)
                embed.add_field(name='Time Left:', value=time_left)
        await ctx.send(embed=embed)

    @darvo.error
    async def darvo_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you add parameters?')
        await ctx.send(embed=embed)

    @commands.command(name='price', description='warframe.market price checker', brief='warframe.market price checker',
                      usage='<item>')
    async def price(self, ctx, *args):
        message = ' '.join(args)
        search = message.lower()
        if 'melee' == search:
            search = 'melee riven mod (veiled)'
        elif 'melee riven' in search:
            search = 'melee riven mod (veiled)'
        elif 'rifle' == search:
            search = 'rifle riven mod (veiled)'
        elif 'rifle riven' in search:
            search = 'rifle riven mod (veiled)'
        elif 'shotgun' == search:
            search = 'shotgun riven mod (veiled)'
        elif 'shotgun riven' in search:
            search = 'shotgun riven mod (veiled)'
        elif 'zaw' == search:
            search = 'zaw riven mod (veiled)'
        elif 'zaw riven' in search:
            search = 'zaw riven mod (veiled)'
        elif 'kitgun' == search:
            search = 'kitgun riven mod (veiled)'
        elif 'kitgun riven' in search:
            search = 'kitgun riven mod (veiled)'
        elif 'companion riven' in search:
            search = 'companion rifle riven mod (veiled)'
        item = requests.get('https://api.warframe.market/v1/items/' + search.replace(' ', '_') + '/statistics').json()
        image = requests.get('https://api.warframe.market/v1/items/' + search.replace(' ', '_')).json()
        item = item['payload']['statistics_closed']['48hours'][-1]['min_price']
        embed = discord.Embed(title='Click for orders',
                              colour=discord.Colour(0x9013fe),
                              url='https://xbox.warframe.market/items/' + search.replace(' ', '_'),
                              description=str(int(item)) + ' Platinum')
        embed.set_thumbnail(
            url='https://api.warframe.market/static/assets/' + image['payload']['item']['items_in_set'][-1]['icon'])
        embed.set_footer(text='Data retrieved from warframe.market',
                         icon_url='https://api.warframe.market/favicon.png')
        await ctx.send(embed=embed)

    @price.error
    async def price_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you mistype the item name?')
        await ctx.send(embed=embed)

    @commands.command(name='nightwave', aliases=['nw'])
    async def nw(self, ctx):
        nw_api = requests.get('http://content.warframe.com/dynamic/worldState.php').json()['SeasonInfo']
        print(nw_api)
        timestamp = datetime.fromtimestamp(int(nw_api['Expiry']['$date']['$numberLong']) / 1000)
        print(timestamp)
        nightwave = discord.Embed(title="Nightwave",
                                  colour=discord.Colour(0x900f0f),
                                  timestamp=timestamp)
        nightwave.set_footer(text='Season ' + str(nw_api['Season']) + ' - Phase ' + str(nw_api['Phase']) + ' ends')
        for i in nw_api['ActiveChallenges']:
            nightwave.add_field(name=lang[i['Challenge'].lower()]['value'] + ' - **' +
                                     str(lang[i['Challenge'].lower()]['standing']) + '**',
                                value=lang[i['Challenge'].lower()]['desc'], inline=True)
        await ctx.send(embed=nightwave)

    @nw.error
    async def nw_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you add parameters?')
        await ctx.send(embed=embed)

    @commands.command(name="sortie")
    async def sortie(self, ctx):
        await ctx.message.delete()
        sortie = request_sortie()
        timestamp = (datetime.fromtimestamp(int(sortie['expiry']) / 1000))
        arb = discord.Embed(title=sortie['boss'],
                            colour=discord.Colour(0x900f0f),
                            timestamp=timestamp)
        arb.add_field(name=sortie['missions'][0]['node']['node'] + ' ({})'.format(
            sortie['missions'][0]['node']['planet']) + ' - ' + sortie['missions'][0]['missionType'],
                      value=sortie['missions'][0]['modifierType'] + ':\n - ' + sortie['missions'][0][
                          'modifierDescription'], inline=False)
        arb.add_field(name=sortie['missions'][1]['node']['node'] + ' ({})'.format(
            sortie['missions'][1]['node']['planet']) + ' - ' + sortie['missions'][1]['missionType'],
                      value=sortie['missions'][1]['modifierType'] + ':\n - ' + sortie['missions'][1][
                          'modifierDescription'], inline=False)
        arb.add_field(name=sortie['missions'][2]['node']['node'] + ' ({})'.format(
            sortie['missions'][2]['node']['planet']) + ' - ' + sortie['missions'][2]['missionType'],
                      value=sortie['missions'][2]['modifierType'] + ':\n - ' + sortie['missions'][2][
                          'modifierDescription'], inline=False)
        arb.set_footer(text="Expires")
        arb.set_thumbnail(url='https://i.imgur.com/7Avse3e.png')
        await ctx.send(embed=arb)

    @sortie.error
    async def sortie_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you add parameters?')
        await ctx.send(embed=embed)

    @commands.command(name="arby")
    async def arbitration(self, ctx):
        current_arbi = requests.get('https://10o.io/kuvalog.json').json()[0]
        timestamp = datetime.fromisoformat(current_arbi['start'][:-1])
        arb = discord.Embed(title=current_arbi['solnodedata']['type'] + " - " + current_arbi['solnodedata']['enemy'],
                            description=current_arbi['solnodedata']['tile'], colour=discord.Colour(0x900f0f),
                            timestamp=timestamp)
        arb.set_thumbnail(url='https://i.imgur.com/2Lyw9yo.png')
        await ctx.send(embed=arb)

    @arbitration.error
    async def arbitration_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you add parameters?')
        await ctx.send(embed=embed)

    @commands.command(name='farm', help='Display preferred place to farm for resources', usage='<resource name>')
    async def farm_resources(self, ctx, item: str):
        if item.lower() in farming_data:
            item_json = farming_data[item]
            embed_card = discord.Embed(title=f'{item.title()}')
            embed_card.add_field(name='Best Location', value=item_json['BestLocationName'], inline=False)
            if len(item_json['OtherLocations']) > 0:
                embed_card.add_field(name='Other Locations', value=', '.join(item_json['OtherLocations']), inline=False)
            await ctx.send(embed=embed_card)
        else:
            await ctx.send("We need to add the resource that you requested (if it exists).")

    @farm_resources.error
    async def farm_resources_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you put the actual resource name?')
        await ctx.send(embed=embed)

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
                    embedCard = warframe_bow.display(result, is_prime)
                    await ctx.send(embed=embedCard)
                else:
                    embedCard = warframe_rifle.display(result, is_prime)
                    await ctx.send(embed=embedCard)
            elif result['category'] == 'Secondary':
                embedCard = warframe_secondary.display(result, is_prime)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Relics':
                embedCard = warframe_relics.display(result)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Arcanes':
                embedCard = warframe_arcanes.display(result)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Warframes':
                embedCard = warframe_frame.display(result, is_prime)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Melee':
                embedCard = warframe_melee.display(result, is_prime)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Sentinels':
                embedCard = warframe_sentinel.display(result, is_prime)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Mods':
                embedCard = warframe_mods.display(result)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Sigils':
                embedCard = warframe_sigil.display(result)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Arch-Gun':
                embedCard = warframe_arch_gun.display(result, is_prime)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Arch-Melee':
                embedCard = warframe_arch_melee.display(result, is_prime)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Archwing':
                embedCard = warframe_archwing.display(result, is_prime)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Gear':
                embedCard = warframe_gear.display(result)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Fish':
                embedCard = warframe_fish.display(result)
                await ctx.send(embed=embedCard)
            elif result['category'] == 'Sentinel Weapons':
                embedCard = warframe_sentinel_weapons.display(result, is_prime)
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


def request_sortie():
    sortie = requests.get('http://content.warframe.com/dynamic/worldState.php').json()['Sorties'][0]
    sortie = {"id": sortie['_id']['$oid'],
              "activation": sortie['Activation']['$date']['$numberLong'],
              "expiry": sortie['Expiry']['$date']['$numberLong'],
              "boss": sortie_data['bosses'][sortie['Boss']]['name'],
              "missions": [
                  {
                      "missionType": mission_types[sortie['Variants'][0]['missionType']],
                      "modifierType": sortie_data['modifierTypes'][sortie['Variants'][0]['modifierType']],
                      "modifierDescription": sortie_data['modifierDescription'][
                          sortie['Variants'][0]['modifierType']],
                      "node": sol_nodes[sortie['Variants'][0]['node']]
                  },
                  {
                      "missionType": mission_types[sortie['Variants'][1]['missionType']],
                      "modifierType": sortie_data['modifierTypes'][sortie['Variants'][1]['modifierType']],
                      "modifierDescription": sortie_data['modifierDescription'][
                          sortie['Variants'][1]['modifierType']],
                      "node": sol_nodes[sortie['Variants'][1]['node']]
                  },
                  {
                      "missionType": mission_types[sortie['Variants'][2]['missionType']],
                      "modifierType": sortie_data['modifierTypes'][sortie['Variants'][2]['modifierType']],
                      "modifierDescription": sortie_data['modifierDescription'][
                          sortie['Variants'][2]['modifierType']],
                      "node": sol_nodes[sortie['Variants'][2]['node']]
                  }
              ]
              }
    return sortie


def setup(client):
    client.add_cog(Warframe(client))
