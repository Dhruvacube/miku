import random
from os.path import join
from pathlib import Path

import discord
import aiohttp


class PostStats:
    def __init__(self, bot):
        self.bot = bot

    async def post(url, headers, data: dict = None, json: dict = None):
        session = aiohttp.ClientSession()
        request_made = await session.post(url, headers=headers, json=data or json)
        await session.close()
        return await request_made.json()

    async def post_guild_stats_all(self):
        guildsno = len(self.bot.guilds)
        members = len(set(self.bot.get_all_members()))

        imageslistdir = Path(__file__).resolve(
            strict=True).parent / join('images_list.txt')
        filepointer = open(imageslistdir)
        imageslist = filepointer.readlines()

        a = await self.post(f'https://top.gg/api/bots/{self.bot.discord_id}/stats',
                            headers={'Authorization': self.bot.topken},
                            data={'server_count': guildsno}
                            )
        b = await self.post(f'https://discordbotlist.com/api/v1/bots/{self.bot.discord_id}/stats',
                            headers={'Authorization': self.bot.dblst},
                            data={'guilds': guildsno, 'users': members}
                            )
        c = await self.post(f'https://botsfordiscord.com/api/bot/{self.bot.discord_id}',
                            headers={'Authorization': self.bot.bfd,
                                     'Content-Type': 'application/json'},
                            json={'server_count': guildsno}
                            )
        d = await self.post(f'https://api.botlist.space/v1/bots/{self.bot.discord_id}',
                            headers={'Authorization': self.bot.botlist,
                                     'Content-Type': 'application/json'},
                            json={'server_count': guildsno}
                            )
        e = await self.post(f'https://discord.boats/api/bot/{self.bot.discord_id}',
                            headers={'Authorization': self.bot.discordboats},
                            data={'server_count': guildsno}
                            )
        f = await self.post(f'https://discord.bots.gg/api/v1/bots/{self.bot.discord_id}/stats',
                            headers={'Authorization': self.bot.discordbotsgg,
                                     'Content-Type': 'application/json'},
                            json={'guildCount': guildsno}
                            )
        h = await self.post(f'https://space-bot-list.xyz/api/bots/{self.bot.discord_id}',
                            headers={"Authorization": self.bot.spacebot,
                                     "Content-Type": "application/json"},
                            json={"guilds": guildsno, "users": members})

        i = await self.post(f'https://api.voidbots.net/bot/stats/{self.bot.discord_id}',
                            headers={"Authorization": self.bot.voidbot,
                                     "Content-Type": "application/json"},
                            json={"server_count": guildsno})
        j = await self.post(f'https://fateslist.xyz/api/v2/bots/{self.bot.discord_id}/stats',
                            headers={"Authorization": self.bot.fateslist,
                                     "Content-Type": "application/json"},
                            json={"guild_count": guildsno, "user_count": members})
        k = await self.post(f'https://bladebotlist.xyz/api/bots/{self.bot.discord_id}/stats',
                            headers={"Authorization": self.bot.bladebot,
                                     "Content-Type": "application/json"},
                            json={"servercount": guildsno})
        l = await self.post(f'https://api.discordextremelist.xyz/v2/bot/{self.bot.discord_id}/stats',
                            headers={"Authorization": self.bot.extremelist,
                                     "Content-Type": "application/json"},
                            json={"guildCount": guildsno})

        r = self.bot.get_channel(844534346815373322)
        e1 = discord.Embed(title='Status posted successfully',
                           description=f'[Widgets Link]({self.bot.website}widgets) [Invite Stats](https://hatsunemiku-invitelogs.herokuapp.com/)', color=discord.Color.random())
        e1.set_image(url=random.choice(imageslist).strip('\n'))
        e1.set_thumbnail(url=self.bot.user.avatar_url)
        e1.add_field(
            name='TopGG', value=f'{a.status_code} : [TopGG](https://top.gg/bot/{self.bot.discord_id})')
        e1.add_field(name='DiscordBotList', value=str(b.status_code) +
                     ' : [DiscordBotList](https://discord.ly/hatsune-miku)')
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
            j.status_code)+f' : [Fates List](https://fateslist.xyz/hatsune-miku/)')
        e1.add_field(name='BladeBotList', value=str(
            k.status_code)+f' : [BladeBotList](https://bladebotlist.xyz/bot/{self.bot.discord_id}/)')
        e1.add_field(name='DiscordExtremeList', value=str(
            l.status_code)+f' : [DiscordExtremeList](https://discordextremelist.xyz/en-US/bots/{self.bot.discord_id}/)')
        await r.send(embed=e1)
