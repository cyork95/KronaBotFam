import json
from urllib.request import Request, urlopen
import discord
from discord.ext import commands, tasks
import requests
from datetime import datetime
from .warframe_api import warframe_api as wf_api
from .warframe_api_embeds import *
import asyncio
from dhooks import Webhook

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

xbox_api_wrapper = wf_api('xb1')

hook = Webhook("https://discordapp.com/api/webhooks/729232543316181033/NKbfGyxaDJ2qRAbAd6GN515s18UDZmCCBP4TSgH2X"
               "Gg1DLKpB3v3A4ntC1vdbSHvMtmV")


class Warframe(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.darvo.start()

    @commands.command(aliases=['alert'])
    async def alerts(self, ctx):
        """This command returns the current Warframe Alerts"""
        await ctx.message.delete()
        alert_json = xbox_api_wrapper.get_alert_info()
        alert_embed = discord.Embed(title="Current Warframe Alerts")
        alert_iterator = 0
        if alert_json[alert_iterator]:
            for item in alert_json:
                alert_embed = get_alert_api_embed(alert_json[alert_iterator], alert_embed)
                alert_iterator += 1
        else:
            alert_embed.add_field(name="No Alerts", value="There are currently no Xbox Warframe alerts.", inline=True)
        await ctx.send(embed=alert_embed)

    @commands.command(aliases=['cetus'])
    async def earth(self, ctx):
        """This command returns the Day/Night Cycle for Plains of Eidolon"""
        await ctx.message.delete()
        earth_cycle_json = xbox_api_wrapper.get_cetus_info()
        if earth_cycle_json['isDay']:
            await ctx.send(
                'It Is Currently **Day-time** On Earth With __{0}__ Left Until **Evening**.'.format(
                    earth_cycle_json['timeLeft']))
        if not earth_cycle_json['isDay']:
            await ctx.send(
                'It Is Currently **Night-time** On Earth With __{0}__ Left Until **Morning**.'.format(
                    earth_cycle_json['timeLeft']))

    @commands.command(aliases=['cc', 'challenges'])
    async def conclave_challenges(self, ctx):
        """This command returns the current Conclave Challenges"""
        await ctx.message.delete()
        conclave_json = xbox_api_wrapper.get_conclave_challenge_info()
        conclave_embed = discord.Embed(title=f"Conclave Challenges")
        conclave_embed_overflow = discord.Embed(title=f"Conclave Challenges Continued")
        conclave_iterator = 0
        for conclave_item in conclave_json:
            if conclave_iterator > 7:
                conclave_embed_overflow = get_conclave_api_embed(conclave_json[conclave_iterator],
                                                                 conclave_embed_overflow)
                conclave_iterator += 1
            else:
                conclave_embed = get_conclave_api_embed(conclave_json[conclave_iterator], conclave_embed)
                conclave_iterator += 1

        await ctx.send(embed=conclave_embed)
        await ctx.send(embed=conclave_embed_overflow)

    @commands.command(aliases=['progress'])
    async def construction_progress(self, ctx):
        """This command returns Current Construction Progress on Xbox"""
        await ctx.message.delete()
        construction_json = xbox_api_wrapper.get_construction_progress_info()
        construction_embed = discord.Embed(title=f"Construction Progress")
        construction_embed.add_field(name="Fomorian Progress: ", value=construction_json['fomorianProgress'])
        construction_embed.add_field(name="Razorback Progress: ", value=construction_json['razorbackProgress'])
        await ctx.send(embed=construction_embed)

    @commands.command(aliases=['events', 'event'])
    async def current_events(self, ctx):
        """This command returns the current Warframe Events"""
        await ctx.message.delete()
        event_json = xbox_api_wrapper.get_event_info()
        event_embed = discord.Embed(title=f"Current Warframe Events")
        event_iterator = 0
        for event_item in event_json:
            event_embed = get_event_api_embed(event_json[event_iterator], event_embed)
            event_iterator += 1

        await ctx.send(embed=event_embed)

    @commands.command(aliases=['endless', 'ef'])
    async def endless_fissure(self, ctx):
        """This command shows the current endless fissure missions."""
        await ctx.message.delete()
        fissure_json = xbox_api_wrapper.get_fissure_info()
        mission_types = ('Defense', 'Survival', 'Interception', 'Excavation')
        embed = discord.Embed(title="Endless Fissures", description='Endless fissure missions currently available:')
        for mission in fissure_json:
            if mission['missionType'] in mission_types:
                relic = mission['tier']
                embed.add_field(name=f'{relic}:', value='**{0}**  *{1}*  __{2}__'.format(mission['missionType'],
                                                                                         mission['node'],
                                                                                         mission['eta']))
            if 0 == mission['missionType']:
                await ctx.send('No Endless Fissure Missions available at this time.')
        await ctx.send(embed=embed)

    @commands.command(aliases=['f'])
    async def fissure(self, ctx):
        """This command shows the current Warframe fissure missions."""
        await ctx.message.delete()
        fissure_json = xbox_api_wrapper.get_fissure_info()
        embed = discord.Embed(title="Fissures", description='Fissure missions currently available:')
        for mission in fissure_json:
            relic = mission['tier']
            embed.add_field(name=f'{relic}:', value='**{0}**  *{1}*  __{2}__'.format(mission['missionType'],
                                                                                     mission['node'],
                                                                                     mission['eta']))
        await ctx.send(embed=embed)

    @commands.command(aliases=['flash', 'sales', 'flash_sales', 'sale', 'marketplace'])
    async def marketplace_sales(self, ctx):
        """This command returns the current Warframe Marketplace Sales"""
        await ctx.message.delete()
        sale_json = xbox_api_wrapper.get_flash_sale_info()
        sale_embed = discord.Embed(title=f"Warframe Marketplace Flash Sales")
        sale_embed_continued = discord.Embed(title=f"Warframe Marketplace Flash Sales Continued")
        event_iterator = 0
        for sale_item in sale_json:
            if event_iterator > 24:
                sale_embed_continued = get_sale_api_embed(sale_json[event_iterator], sale_embed_continued)
            else:
                sale_embed = get_sale_api_embed(sale_json[event_iterator], sale_embed)
            event_iterator += 1

        await ctx.send(embed=sale_embed)
        await ctx.send(embed=sale_embed_continued)

    @commands.command(aliases=['i'])
    async def invasions(self, ctx):
        """This command returns the current Warframe Invasions"""
        await ctx.message.delete()
        invasion_json = xbox_api_wrapper.get_invasion_info()
        event_embed = discord.Embed(title=f"Current Warframe Events")
        event_iterator = 0
        for event_item in invasion_json:
            event_embed = get_event_api_embed(invasion_json[event_iterator], event_embed)
            event_iterator += 1

        await ctx.send(embed=event_embed)

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
    async def farm_resources(self, ctx, *, item: str):
        if item in farming_data:
            item_json = farming_data[item]
            embed_card = discord.Embed(title=f'{item.title()}')
            embed_card.add_field(name='Best Location', value=item_json['BestLocationName'], inline=False)
            if len(item_json['OtherLocations']) > 0:
                embed_card.add_field(name='Other Locations', value=', '.join(item_json['OtherLocations']), inline=False)
            else:
                pass
            await ctx.send(embed=embed_card)
        else:
            await ctx.send("We need to add the resource that you requested (if it exists).")

    @farm_resources.error
    async def farm_resources_error(self, ctx, error):
        embed = discord.Embed(title='Syntax Error',
                              colour=discord.Colour(0x9013fe),
                              description='Did you put the actual resource name?')
        await ctx.send(embed=embed)

    @tasks.loop(hours=9)
    async def darvo(self):
        """This command returns the Daily Darvo Deal in Warframe."""
        darvo_json = xbox_api_wrapper.get_daily_deals_info()
        darvo_embed = discord.Embed(title="Darvo Deal")
        total_left = int(darvo_json[0]['total'] - darvo_json[0]['sold'])
        if total_left == 0:
            hook.send(
                'Darvo has sold out.  {0} is no longer available at a lower price.'.format(darvo_json['item']))
        else:
            darvo_embed = get_darvo_api_embed(darvo_json[0], darvo_embed)
            hook.send(embed=darvo_embed)


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
