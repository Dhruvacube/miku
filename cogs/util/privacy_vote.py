import random
from asyncio import sleep as sl

import discord
from discord.ext import menus


class VotingMenu(menus.Menu):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.bot.owner = bot.owner

    async def send_initial_message(self, ctx, channel):
        e = discord.Embed(title="I see you want vote!",
                          description=f"{ctx.author.mention}, maybe react with your choice :)")
        return await channel.send(embed=e)

    @menus.button('\N{WHITE HEAVY CHECK MARK}')
    async def on_check_mark(self, payload):
        
        topgg =  f'\n - **[TopGG](https://top.gg/bot/{self.botdiscord_id})** '
        Discordbotlist = f'\n - **[Discordbotlist](https://discordbotlist.com/bots/minato-namikaze)**'
        Discordlist = f'\n - **[Discordlist.Space](https://discordlist.space/bot/{self.botdiscord_id}/upvote)**  '
        BotsForDiscord = f'\n - **[BotsForDiscord](https://botsfordiscord.com/bot/{self.botdiscord_id}/vote)**'
        Boats = f'\n - **[Discord.Boats](https://discord.boats/bot/{self.botdiscord_id}/vote)**  '
        Space = f'\n - **[Space Bots List](https://space-bot-list.xyz/bots/{self.botdiscord_id}/vote)**'
        fateslist = f'\n - **[Fates List](https://fateslist.xyz/bot/{self.botdiscord_id}/vote)**'
        voidbots = f'\n - **[Void Bots](https://voidbots.net/bot/{self.botdiscord_id}/vote)**'
        bladebotlist = f'\n - **[BladeBotList](https://bladebotlist.xyz/bot/{self.botdiscord_id}/vote)**'
        
        e1 = discord.Embed(title="Thanks!",
            description=f"Thanks {self.ctx.author.mention}! Here's the links:{topgg}{Discordbotlist}{Discordlist}{BotsForDiscord}{Boats}{Space}{fateslist}{voidbots}{bladebotlist}",
            color=discord.Color.random()
        )
        await self.message.edit(content="", embed=e1)
        self.stop()

    @menus.button('\N{NEGATIVE SQUARED CROSS MARK}')
    async def on_stop(self, payload):
        e2 = discord.Embed(title="Sorry to see you go!",
                           description="Remember you can always re-run the command :)")
        self.stop()
        await self.message.edit(content="", embed=e2)
        await sl(5)
        await self.message.delete()


class WhoMenu(menus.Menu):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    async def send_initial_message(self, ctx, channel):
        e = discord.Embed(title="I see you want to know more!",
                          description=f"{ctx.author.mention}, click the checkmark for the Privacy Policy or the crossmark for just info!",
                          color=discord.Color.random())
        return await channel.send(embed=e)

    @menus.button('\N{WHITE HEAVY CHECK MARK}')
    async def on_add(self, payload):
        e1 = discord.Embed(title="Well, Heres The Policy :)",
                           description=f"Well well well, Nothing is stored! Really nothing is stored! All is based on internal cache provided by Discord! For more please visit [THIS LINK](https://hatsunemikubot.weebly.com/)", color=discord.Colour.from_hsv(random.random(), 1, 1))
        await self.message.edit(content="", embed=e1)

    @menus.button('\N{NEGATIVE SQUARED CROSS MARK}')
    async def on_stop(self, payload):
        e2 = discord.Embed(title="Hey!", description=f"Hi, I'm {self.bot.user}, I am developed by {self.bot.owner}, Who is a great fan of me i.e. {self.bot.user} and always listens to my songs! UwU :ring: ", color=discord.Colour.from_hsv(
            random.random(), 1, 1))

        await self.message.edit(content="", embed=e2)


class MenuSource(menus.ListPageSource):
    def __init__(self, data):
        super().__init__(data, per_page=1)

    async def format_page(self, menu, data):
        embed = discord.Embed(description="\n".join(item for item in data),color=discord.Color.random())
        return embed
