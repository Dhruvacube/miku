import asyncio

import discord
from discord.ext import commands
from discord_slash import SlashContext, cog_ext
import aiohttp


async def waifu_get(token):
    session = aiohttp.ClientSession()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'

    }
    request_made = await session.get('https://api.dagpi.xyz/data/waifu', headers=headers)
    await session.close()
    return await request_made.json()


class Waifu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.dagpi = bot.dagpi
        self.description = 'Get waifu ! UwU'

    async def get_waifu(self):
        waifu = await waifu_get(self.bot.dagpi)
        pic = waifu['display_picture']
        name = waifu['name']
        likes_rank = waifu['like_rank']
        trash_rank = waifu['trash_rank']
        anime = waifu['appearances'][0]['name']

        e = discord.Embed(color=discord.Color.random(), title=name)
        e.add_field(name="**Anime**", value=anime, inline=True)
        e.add_field(name="**:heartbeat:**", value=likes_rank, inline=True)
        e.add_field(name="**:wastebasket:**", value=trash_rank, inline=True)
        e.set_image(url=pic)
        e.set_footer(text=f'React with any emoji in 30 sec to claim him/her')
        return e, name

    @commands.command(aliases=['w', 'wfu', 'wa'])
    @commands.cooldown(1, 2, commands.BucketType.guild)
    async def waifu(self, ctx):
        '''Get random waifu and marry them! UwU!'''
        waifu = await self.get_waifu()
        message = await ctx.send(embed=waifu[0])
        await message.add_reaction('💓')

        def check(reaction, user):
            return user != self.bot.user and message.id == reaction.message.id

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
            await ctx.send(f'**{user.mention}** has *married* **{waifu[-1]}**! UwU :ring:')
        except asyncio.TimeoutError:
            pass

    @cog_ext.cog_slash(name="waifu", description='Get random waifu and marry them! UwU!')
    async def _waifu(self, ctx: SlashContext):
        '''Get random waifu and marry them! UwU!'''
        waifu = await self.get_waifu()
        message = await ctx.send(embed=waifu[0])
        await message.add_reaction('💓')

        def check(reaction, user):
            return user != self.bot.user and message.id == reaction.message.id

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
            await ctx.send(f'**{user.mention}** has *married* **{waifu[-1]}**! UwU :ring:')
        except asyncio.TimeoutError:
            pass


def setup(bot):
    bot.add_cog(Waifu(bot))
