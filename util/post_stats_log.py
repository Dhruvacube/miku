import random
from os.path import join
from pathlib import Path

import discord
import requests
from dbl import *


class PostStats:
    def __init__(self, bot):
        self.bot = bot

    async def post_guild_stats_all(self):
        guildsno = len(self.bot.guilds)+1
        members = len(set(self.bot.get_all_members()))
        imageslistdir = Path(__file__).resolve(
            strict=True).parent / join('util','images_list.txt')
        filepointer = open(imageslistdir)
        imageslist = filepointer.readlines()

        dblpy = DBLClient(self.bot, self.bot.topken)
        await dblpy.post_guild_count(guildsno)
        b = requests.post(f'https://discordbotlist.com/api/v1/bots/{self.bot.discord_id}/stats',
                          headers={'Authorization': self.bot.dblst},
                          data={'guilds': guildsno, 'users': members}
                          )
        c = requests.post(f'https://botsfordiscord.com/api/bot/{self.bot.discord_id}',
                          headers={'Authorization': self.bot.bfd,
                                   'Content-Type': 'application/json'},
                          json={'server_count': guildsno}
                          )
        d = requests.post(f'https://api.botlist.space/v1/bots/{self.bot.discord_id}',
                          headers={'Authorization': self.bot.botlist,
                                   'Content-Type': 'application/json'},
                          json={'server_count': guildsno}
                          )
        e = requests.post(f'https://discord.boats/api/bot/{self.bot.discord_id}',
                          headers={'Authorization': self.bot.discordboats},
                          data={'server_count': guildsno}
                          )
        f = requests.post(f'https://discord.bots.gg/api/v1/bots/{self.bot.discord_id}/stats',
                          headers={'Authorization': self.bot.discordbotsgg,
                                   'Content-Type': 'application/json'},
                          json={'guildCount': guildsno}
                          )

        h = requests.post(f'https://space-bot-list.xyz/api/bots/{self.bot.discord_id}',
                          headers={"Authorization": self.bot.spacebot,
                                   "Content-Type": "application/json"},
                          json={"guilds": guildsno, "users": members})
        i = requests.post(f'https://api.voidbots.net/bot/stats/{self.bot.discord_id}',
                          headers={"Authorization": self.bot.voidbot,
                                   "Content-Type": "application/json"},
                          json={"server_count": guildsno})
        j = requests.post(f'https://fateslist.xyz/api/v2/bots/{self.bot.discord_id}/stats',
                          headers={"Authorization": self.bot.fateslist,
                                   "Content-Type": "application/json"},
                          json={"guild_count": guildsno, "user_count": members})
        k = requests.post(f'https://bladebotlist.xyz/api/bots/{self.bot.discord_id}/stats',
                          headers={"Authorization": self.bot.bladebot,
                                   "Content-Type": "application/json"},
                          json={"servercount": guildsno})

        r = self.bot.get_channel(844534346815373322)
        e1 = discord.Embed(title='Status posted successfully',
                           description='[Widgets Link](https://dhruvacube.github.io/yondaime-hokage/widgets)', color=0x2ecc71)
        e1.set_image(url=random.choice(imageslist).strip('\n'))
        e1.set_thumbnail(url='https://i.imgur.com/Reopagp.jpg')
        e1.add_field(
            name='TopGG', value=f'200 : [TopGG](https://top.gg/bot/{self.bot.discord_id})')
        e1.add_field(name='DiscordBotList', value=str(b.status_code) +
                     ' : [DiscordBotList](https://discord.ly/minato-namikaze)')
        e1.add_field(name='BotsForDiscord', value=str(
            c.status_code)+f' : [BotsForDiscord](https://botsfordiscord.com/bot/{self.bot.discord_id})')
        e1.add_field(name='DiscordListSpace', value=str(
            d.status_code)+f' : [DiscordListSpace](https://discordlist.space/bot/{self.bot.discord_id})')
        e1.add_field(name='DiscordBoats', value=str(
            e.status_code)+f' : [DiscordBoats](https://discord.boats/bot/{self.bot.discord_id})')
        e1.add_field(name='DiscordBots', value=str(
            f.status_code)+f' : [DiscordBots](https://discord.bots.gg/bots/{self.bot.discord_id}/)')
        e1.add_field(name='Space Bots', value=str(
            h.status_code)+f' : [Space Bots](https://space-bot-list.xyz/bots/{self.bot.discord_id})')
        e1.add_field(name='Void Bots', value=str(
            i.status_code)+f' : [Void Bots](https://voidbots.net/bot/{self.bot.discord_id}/)')
        e1.add_field(name='Fates List', value=str(
            j.status_code)+f' : [Fates List](https://fateslist.xyz/minato/)')
        e1.add_field(name='BladeBotList', value=str(
            k.status_code)+f' : [BladeBotList](https://bladebotlist.xyz/bot/{self.bot.discord_id}/)')
        await r.send(embed=e1)
