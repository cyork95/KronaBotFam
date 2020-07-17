import json
import discord
from discord.ext import commands, tasks
import requests
from cogs.warframe_api import warframe_api as wf_api
from cogs.warframe_api_embeds import *
from dhooks import Webhook

with open('./cogs/cog_resources/farming.json') as json_file:
    farming_data = json.load(json_file)

xbox_api_wrapper = wf_api('xb1')

hook = Webhook("https://discordapp.com/api/webhooks/729232543316181033/NKbfGyxaDJ2qRAbAd6GN515s18UDZmCCBP4TSgH2X"
               "Gg1DLKpB3v3A4ntC1vdbSHvMtmV")
orokin_vault_hook = Webhook("https://discordapp.com/api/webhooks/731180983549689937/tI8yJjRkH8Oy9rdKkU-VqIRjbFwEGY-"
                            "YUHC_nIIz5laIz3v2T-pxyUCnQZVDp8OB19gh")


class Warframe(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.darvo_deal.start()
        self.sortie_time.start()
        self.barro_store.start()

    @commands.command(aliases=['alert'])
    async def alerts(self, ctx):
        """This command returns the current Warframe Alerts"""
        await ctx.message.delete()
        alert_json = xbox_api_wrapper.get_alert_info()
        alert_embed = discord.Embed(title="Current Warframe Alerts", color=discord.Colour(0xfbfb04))
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
        earth_embed = discord.Embed(title="Earth Day/Night Cycle", color=discord.Colour(0xfbfb04))
        if earth_cycle_json['isDay']:
            earth_embed.add_field(name="Cycle: ", value=f"It Is Currently **Day-time** On Earth With __"
                                                        f"{earth_cycle_json['timeLeft']}__ Left Until **Evening**.")
            await ctx.send(embed=earth_embed)
        if not earth_cycle_json['isDay']:
            earth_embed.add_field(name="Cycle: ", value=f"It Is Currently **Night-time** On Earth With __"
                                                        f"{earth_cycle_json['timeLeft']}__ Left Until **Morning**.")
            await ctx.send(embed=earth_embed)

    @commands.command(aliases=['cc', 'challenges'])
    async def conclave_challenges(self, ctx):
        """This command returns the current Conclave Challenges"""
        await ctx.message.delete()
        conclave_json = xbox_api_wrapper.get_conclave_challenge_info()
        conclave_embed = discord.Embed(title=f"Conclave Challenges", color=discord.Colour(0xfbfb04))
        conclave_embed_overflow = discord.Embed(title=f"Conclave Challenges Continued")
        conclave_iterator = 0
        for conclave_item in conclave_json:
            if conclave_iterator > 7:
                conclave_embed_overflow = get_conclave_api_embed(conclave_json[conclave_iterator],
                                                                 conclave_embed_overflow)
            else:
                conclave_embed = get_conclave_api_embed(conclave_json[conclave_iterator], conclave_embed)
            conclave_iterator += 1
        await ctx.send(embed=conclave_embed)
        if conclave_iterator > 8:
            await ctx.send(embed=conclave_embed_overflow)

    @commands.command(aliases=['progress'])
    async def construction_progress(self, ctx):
        """This command returns Current Construction Progress on Xbox"""
        await ctx.message.delete()
        construction_json = xbox_api_wrapper.get_construction_progress_info()
        construction_embed = discord.Embed(title=f"Construction Progress", color=discord.Colour(0xfbfb04))
        construction_embed.add_field(name="Fomorian Progress: ", value=construction_json['fomorianProgress'])
        construction_embed.add_field(name="Razorback Progress: ", value=construction_json['razorbackProgress'])
        await ctx.send(embed=construction_embed)

    @commands.command(aliases=['events', 'event'])
    async def current_events(self, ctx):
        """This command returns the current Warframe Events"""
        await ctx.message.delete()
        event_json = xbox_api_wrapper.get_event_info()
        event_embed = discord.Embed(title=f"Current Warframe Events", color=discord.Colour(0xfbfb04))
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
        embed = discord.Embed(title="Endless Fissures", description='Endless fissure missions currently available:',
                              color=discord.Colour(0xfbfb04))
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
        embed = discord.Embed(title="Fissures", description='Fissure missions currently available:',
                              color=discord.Colour(0xfbfb04))
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
        sale_embed = discord.Embed(title=f"Warframe Marketplace Flash Sales", color=discord.Colour(0xfbfb04))
        sale_embed_continued = discord.Embed(title=f"Warframe Marketplace Flash Sales")
        event_iterator = 0
        for sale_item in sale_json:
            if event_iterator > 24:
                sale_embed_continued = get_sale_api_embed(sale_json[event_iterator], sale_embed_continued)
            else:
                sale_embed = get_sale_api_embed(sale_json[event_iterator], sale_embed)
            event_iterator += 1
        await ctx.send(embed=sale_embed)
        if event_iterator > 25:
            await ctx.send(embed=sale_embed_continued)

    @commands.command(aliases=['i'])
    async def invasions(self, ctx):
        """This command returns the current Warframe Invasions"""
        await ctx.message.delete()
        invasion_json = xbox_api_wrapper.get_invasion_info()
        invasion_embed = discord.Embed(title=f"Current Warframe Invasions", color=discord.Colour(0xfbfb04))
        invasion_embed_continued = discord.Embed(title=f"Current Warframe Invasions", color=discord.Colour(0xfbfb04))
        invasion_iterator = 0
        for invasion_item in invasion_json:
            if invasion_iterator > 7:
                invasion_embed_continued = get_invasion_api_embed(invasion_json[invasion_iterator],
                                                                  invasion_embed_continued)
            else:
                invasion_embed = get_invasion_api_embed(invasion_json[invasion_iterator], invasion_embed)
            invasion_iterator += 1
        await ctx.send(embed=invasion_embed)
        if invasion_iterator > 8:
            await ctx.send(embed=invasion_embed_continued)

    @commands.command(aliases=['n'])
    async def news(self, ctx):
        """This command returns the current Warframe News"""
        await ctx.message.delete()
        news_json = xbox_api_wrapper.get_news_info()
        news_embed = discord.Embed(title=f"Current Warframe News", color=discord.Colour(0xfbfb04))
        news_embed_continued = discord.Embed(title=f"Current Warframe News", color=discord.Colour(0xfbfb04))
        news_iterator = 0
        for news_item in news_json:
            if news_iterator > 12:
                news_embed_continued = get_news_api_embed(news_json[news_iterator], news_embed_continued)

            else:
                news_embed = get_news_api_embed(news_json[news_iterator], news_embed)
            news_iterator += 1
        await ctx.send(embed=news_embed)
        if news_iterator > 12:
            await ctx.send(embed=news_embed_continued)

    @commands.command(aliases=['nw'])
    async def nightwave(self, ctx):
        """This command returns the weekly Nightwave challenges."""
        await ctx.message.delete()
        nw_json = xbox_api_wrapper.get_nightwave_info()
        nw_embed = discord.Embed(title="Nightwave", color=discord.Colour(0xfbfb04))
        nw_embed_continued = discord.Embed(title="Nightwave", color=discord.Colour(0xfbfb04))
        nw_iterator = 0
        for nw_item in nw_json['activeChallenges']:
            if nw_iterator > 7:
                nw_embed_continued = get_nightwave_api_embed(nw_json['activeChallenges'][nw_iterator],
                                                             nw_embed_continued)
            else:
                nw_embed = get_nightwave_api_embed(nw_json['activeChallenges'][nw_iterator], nw_embed)
            nw_iterator += 1
        nw_embed.set_footer(text='Season ' + str(nw_json['season']) + ' - Phase ' + str(nw_json['phase']))
        nw_embed_continued.set_footer(text='Season ' + str(nw_json['season']) + ' - Phase ' + str(nw_json['phase']))
        await ctx.send(embed=nw_embed)
        if nw_iterator > 7:
            await ctx.send(embed=nw_embed_continued)

    @commands.command(aliases=['so'])
    async def sentient_outpost(self, ctx):
        """This command returns the current Sentient Outpost"""
        await ctx.message.delete()
        sentient_json = xbox_api_wrapper.get_sentient_outpost_info()
        sentient_embed = discord.Embed(title="Sentient Outpost", color=discord.Colour(0xfbfb04))
        sentient_embed = get_sentient_api_embed(sentient_json['mission'], sentient_embed)
        sentient_embed.add_field(name="Mission Expires: ", value=sentient_json['expiry'], inline=True)
        await ctx.send(embed=sentient_embed)

    @commands.command(aliases=['hunter_target', 'sanctuary'])
    async def simaris(self, ctx):
        """This command returns the current Cephalon Simaris target info."""
        await ctx.message.delete()
        simaris_json = xbox_api_wrapper.get_sanctuary_status_info()
        simaris_embed = discord.Embed(title="Sanctuary Status", color=discord.Colour(0xfbfb04))
        simaris_embed.add_field(name="Sanctuary Target: ", value=simaris_json['asString'], inline=True)
        await ctx.send(embed=simaris_embed)

    @commands.command(aliases=['sm', 'syndicate'])
    async def syndicate_missions(self, ctx, *, syndicate):
        """This command returns the current Syndicate Missions"""
        await ctx.message.delete()
        syndicate = syndicate.lower()
        syndicate_json = xbox_api_wrapper.get_syndicate_info()
        if syndicate == "ostrons" or syndicate == "cetus":
            syndicate_embed = discord.Embed(title=f"Cetus Bounties", color=discord.Colour(0xfbfb04))
            syndicate_number = 0
        elif syndicate == "solaris" or syndicate == "solaris united":
            syndicate_embed = discord.Embed(title=f"Solaris United Bounties", color=discord.Colour(0xfbfb04))
            syndicate_number = 1
        elif syndicate == "arbiters of hexis" or syndicate == "arbiters":
            syndicate_embed = discord.Embed(title=f"Arbiters of Hexis Missions", color=discord.Colour(0xfbfb04))
            syndicate_number = 2
        elif syndicate == "assassin":
            syndicate_embed = discord.Embed(title=f"Assassin Missions", color=discord.Colour(0xfbfb04))
            syndicate_number = 3
        elif syndicate == "suda" or syndicate == "cephalon suda":
            syndicate_embed = discord.Embed(title=f"Cephalon Suda Missions", color=discord.Colour(0xfbfb04))
            syndicate_number = 4
        elif syndicate == "loka" or syndicate == "new loka":
            syndicate_embed = discord.Embed(title=f"New Loka Missions", color=discord.Colour(0xfbfb04))
            syndicate_number = 6
        elif syndicate == "perrin" or syndicate == "perrin sequence":
            syndicate_embed = discord.Embed(title=f"Perrin Sequence Missions", color=discord.Colour(0xfbfb04))
            syndicate_number = 7
        elif syndicate == "red veil" or syndicate == "red":
            syndicate_embed = discord.Embed(title=f"Red Veil Missions", color=discord.Colour(0xfbfb04))
            syndicate_number = 15
        elif syndicate == "steel meridian" or syndicate == "steel":
            syndicate_embed = discord.Embed(title=f"Steel Meridian Missions", color=discord.Colour(0xfbfb04))
            syndicate_number = 16
        else:
            syndicate_embed = discord.Embed(title=f"Syndicate Missions", color=discord.Colour(0xfbfb04))
            syndicate_embed.add_field(name="Failure: ", value="Cannot find the syndicate requested. Please use *cetus* "
                                                              "for earth missions, *solaris* for orb vallis missions, "
                                                              "*arbiters* for arbiters of hexis, *assasssin* for "
                                                              "assassin missions, *suda* for cephalon suda, *loka*"
                                                              " for the new loka missions, *perrin* for the perrin"
                                                              " sequence missions, *red* for red veil missions, and "
                                                              "*steel* for steel meridian missions.")
            await ctx.send(embed=syndicate_embed)
            return
        syndicate_embed = get_syndicate_api_embed(syndicate_json[syndicate_number], syndicate_embed)
        await ctx.send(embed=syndicate_embed)

    @commands.command(aliases=['vallis', 'orb', 'ov'])
    async def orb_vallis(self, ctx):
        """This returns the current Hot/Cold Cycle on Orb Vallis"""
        await ctx.message.delete()
        vallis_data = xbox_api_wrapper.get_vallis_info()
        vallis_embed = discord.Embed(title="Vallis Heat/Cold Cycle", color=discord.Colour(0xfbfb04))
        if not vallis_data['isWarm']:
            vallis_embed.add_field(name="Cycle: ", value=f"It is **Cold** at Orb Vallis. {vallis_data['timeLeft']} "
                                                         f"until it is **Warm**")
            await ctx.send(embed=vallis_embed)
        if vallis_data['isWarm']:
            vallis_embed.add_field(name="Cycle: ", value=f"It is **Warm** at Orb Vallis for the next __"
                                                         f"{vallis_data['timeLeft']}__")
            await ctx.send(embed=vallis_embed)

    @commands.command(aliases=['cycle', 'temp', 'world'])
    async def world_cycles(self, ctx):
        await ctx.message.delete()
        """This returns both Orb Vallis and Cetus Cycles"""
        vallis_data = xbox_api_wrapper.get_vallis_info()
        earth_cycle_json = xbox_api_wrapper.get_cetus_info()
        world_embed = discord.Embed(title="Earth Night/Day and Vallis Heat/Cold Cycle", color=discord.Colour(0xfbfb04))
        if earth_cycle_json['isDay']:
            world_embed.add_field(name="Earth Cycle: ", value=f"It Is Currently **Day-time** On Earth With __"
                                                              f"{earth_cycle_json['timeLeft']}__ Left Until **Evening**.")
        if not earth_cycle_json['isDay']:
            world_embed.add_field(name="Earth Cycle: ", value=f"It Is Currently **Night-time** On Earth With __"
                                                              f"{earth_cycle_json['timeLeft']}__ Left Until **Morning**.")
        if not vallis_data['isWarm']:
            world_embed.add_field(name="Vallis Cycle: ",
                                  value=f"It is **Cold** at Orb Vallis. {vallis_data['timeLeft']} "
                                        f"until it is **Warm**")
        if vallis_data['isWarm']:
            world_embed.add_field(name="Vallis Cycle: ", value=f"It is **Warm** at Orb Vallis for the next __"
                                                               f"{vallis_data['timeLeft']}__")
        await ctx.send(embed=world_embed)

    @commands.command(aliases=['kuva', 'km'])
    async def kuva_missions(self, ctx):
        """This returns the current Kuva Missions"""
        await ctx.message.delete()
        kuva_data = xbox_api_wrapper.get_kuva_info()
        kuva_embed = discord.Embed(title="Current Kuva Nodes", color=discord.Colour(0xfbfb04))
        if not kuva_data:
            kuva_embed.add_field(name="No Data", value=f"The API currently has no data.")
            await ctx.send(embed=kuva_embed)
        else:
            kuva_embed.add_field(name="Nodes: ", value=f"{kuva_data['node']}")
            await ctx.send(embed=kuva_embed)

    @commands.command()
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
        if not item['error']:
            item = item['payload']['statistics_closed']['48hours'][-1]['min_price']
            embed = discord.Embed(title='Click for orders',
                                  color=discord.Colour(0xfbfb04),
                                  url='https://xbox.warframe.market/items/' + search.replace(' ', '_'),
                                  description=str(int(item)) + ' Platinum')
            embed.set_footer(text='Data retrieved from warframe.market',
                             icon_url='https://api.warframe.market/favicon.png')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Item not found.",
                                  color=discord.Colour(0xfbfb04),
                                  description="Make sure you are searching for something that can be traded!")
            await ctx.send(embed=embed)

    @commands.command(aliases=['farm'])
    async def farm_resources(self, ctx, *, item: str):
        """This returns where to farm the given resource"""
        if item in farming_data:
            item_json = farming_data[item]
            embed_card = discord.Embed(title=f'{item.title()}', color=discord.Colour(0xfbfb04))
            embed_card.add_field(name='Best Location', value=item_json['BestLocationName'], inline=False)
            if len(item_json['OtherLocations']) > 0:
                embed_card.add_field(name='Other Locations', value=', '.join(item_json['OtherLocations']), inline=False)
            else:
                pass
            await ctx.send(embed=embed_card)
        else:
            await ctx.send("We need to add the resource that you requested (if it exists).")

    @commands.command(name="arby")
    async def arbitration(self, ctx):
        """Returns the current arbitration missions"""
        current_arby = requests.get('https://10o.io/kuvalog.json').json()[0]
        arby_embed = discord.Embed(
            title=current_arby['solnodedata']['type'] + " - " + current_arby['solnodedata']['enemy'],
            description=current_arby['solnodedata']['tile'], color=discord.Colour(0xfbfb04))
        arby_embed.set_thumbnail(url='https://i.imgur.com/2Lyw9yo.png')
        await ctx.send(embed=arby_embed)

    @commands.command(aliases=['dd'])
    async def darvo(self, ctx):
        """This command returns the Daily Darvo Deal in Warframe."""
        darvo_json = xbox_api_wrapper.get_daily_deals_info()
        darvo_embed = discord.Embed(title="Darvo Deal", color=discord.Colour(0xfbfb04))
        total_left = int(darvo_json[0]['total'] - darvo_json[0]['sold'])
        if total_left == 0:
            hook.send(
                'Darvo has sold out.  {0} is no longer available at a lower price.'.format(darvo_json['item']))
        else:
            darvo_embed = get_darvo_api_embed(darvo_json[0], darvo_embed)
            hook.send(embed=darvo_embed)

    @commands.command(aliases=['s'])
    async def sortie(self, ctx):
        """Returns the daily sortie missions"""
        sortie_json = xbox_api_wrapper.get_sortie_info()
        sortie_embed = discord.Embed(title="Daily Sortie",
                                     colour=discord.Colour(0xfbfb04))
        sortie_embed = get_sortie_api_embed(sortie_json, sortie_embed)
        hook.send(embed=sortie_embed)

    @commands.command(aliases=['b'])
    async def barro(self, ctx):
        """Returns Barro's Inventory and status"""
        barro_json = xbox_api_wrapper.get_void_trader_info()
        embed = discord.Embed(title="Barro's Inventory", description='The Void Trader is currently at {0} and '
                                                                     'he will be leaving in {1}.\n\n'.format(
            barro_json['location'], barro_json['endString']), color=discord.Colour(0xfbfb04))
        if not barro_json['active']:
            embed = discord.Embed(title="Barro's Inventory", description=f"Baro Ki`Teer will be arriving at **"
                                                                         f"{barro_json['location']}** in __"
                                                                         f"{barro_json['startString']}__",
                                  color=discord.Colour(0xfbfb04))
            await hook.send(embed=embed)
        if barro_json['active']:
            baro_inventory = barro_json['inventory']
            for disapointment in baro_inventory:
                item_name = disapointment['item']
                embed.add_field(name=f'{item_name}:', value='*Ducats:* __{1}__  *Credits:* __{2}__'.format(
                    disapointment['item'], disapointment['ducats'], disapointment['credits']))
            await hook.send(embed=embed)

    @tasks.loop(hours=24)  # should be triggered at 12:05 because thats when the sorties reset
    async def sortie_time(self, ctx):
        sortie_json = xbox_api_wrapper.get_sortie_info()
        sortie_embed = discord.Embed(title="Daily Sortie",
                                     colour=discord.Colour(0xfbfb04))
        sortie_embed = get_sortie_api_embed(sortie_json, sortie_embed)
        orokin_vault_hook.send(embed=sortie_embed)
        hook.send(embed=sortie_embed)

    @tasks.loop(hours=24)  # Can be triggered with sorties
    async def darvo_deal(self):
        """This command returns the Daily Darvo Deal in Warframe."""
        darvo_json = xbox_api_wrapper.get_daily_deals_info()
        darvo_embed = discord.Embed(title="Darvo Deal", color=discord.Colour(0xfbfb04))
        total_left = int(darvo_json[0]['total'] - darvo_json[0]['sold'])
        if total_left == 0:
            await orokin_vault_hook.send('Darvo has sold out.  {0} is no longer available at a lower price.'
                                         .format(darvo_json['item']))
            await hook.send('Darvo has sold out.  {0} is no longer available at a lower price.'
                                         .format(darvo_json['item']))
        else:
            darvo_embed = get_darvo_api_embed(darvo_json[0], darvo_embed)
            await orokin_vault_hook.send(embed=darvo_embed)
            await hook.send(embed=darvo_embed)

    @tasks.loop(hours=168)  # send every 168 (7 days) hours form friday at Noon
    async def barro_store(self):
        barro_json = xbox_api_wrapper.get_void_trader_info()
        embed = discord.Embed(title="Barro's Inventory", description='The Void Trader is currently at {0} and '
                                                                     'he will be leaving in {1}.\n\n'.format(
            barro_json['location'], barro_json['endString']), color=discord.Colour(0xfbfb04))
        if not barro_json['active']:
            embed = discord.Embed(title="Barro's Inventory", description=f"Baro Ki`Teer will be arriving at **"
                                                                         f"{barro_json['location']}** in __"
                                                                         f"{barro_json['startString']}__",
                                  color=discord.Colour(0xfbfb04))
            await orokin_vault_hook.send(embed=embed)
            await hook.send(embed=embed)
        if barro_json['active']:
            baro_inventory = barro_json['inventory']
            for disapointment in baro_inventory:
                item_name = disapointment['item']
                embed.add_field(name=f'{item_name}:', value='*Ducats:* __{1}__  *Credits:* __{2}__'.format(
                    disapointment['item'], disapointment['ducats'], disapointment['credits']))
            await orokin_vault_hook.send(embed=embed)
            await hook.send(embed=embed)


def setup(client):
    client.add_cog(Warframe(client))
