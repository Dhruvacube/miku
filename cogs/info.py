import datetime
import platform
import time

import discord
from discord.ext import commands
from discord.ext.commands import command
from util.var import *

from util.privacy_vote import VotingMenu, WhoMenu


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = "Get information about me"

    @command(name="stats", description="A usefull command that displays bot statistics.")
    async def stats(self, ctx):
        '''Get the stats for the me'''
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))

        embed = discord.Embed(
            title=f"{self.bot.user.name} Stats",
            description="\uFEFF",
            colour=ctx.author.colour,
            timestamp=ctx.message.created_at,
        )

        embed.set_thumbnail(url=self.bot.user.avatar_url)

        embed.add_field(name="**Bot Version:**", value=version)
        embed.add_field(name="**Python Version:**", value=pythonVersion)
        embed.add_field(name="**Discord.Py Version**", value=dpyVersion)
        embed.add_field(name="**Total Guilds:**", value=serverCount+1)
        embed.add_field(name="**Total Users:**", value=memberCount)
        embed.add_field(name="**Bot Developer:**",
                        value="[DHRUVA SHAW#0550](https://discord.com/users/571889108046184449/)")
        embed.add_field(name="**Website:**",
                        value="[Click Here](https://hatsunemikubot.weebly.com/)")
        # embed.add_field(name="**More Info:**",
        #                 value=f"[Click Here](https://statcord.com/bot/{self.bot.discord_id})")
        embed.add_field(name="**Incidents/Maintenance Reports:**",
                        value="[Click Here](https://hatsunemiku.statuspage.io/)")

        embed.set_footer(text=f"{ctx.author} | {self.bot.user.name}")
        embed.set_author(name=self.bot.user.name,
                         icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def who(self, ctx):
        '''Get the Privacy Policy'''
        m = WhoMenu(bot=self.bot)
        await m.start(ctx)

    @commands.command()
    async def vote(self, ctx):
        '''Get the Voting Lists'''
        m = VotingMenu(bot=self.bot)
        await m.start(ctx)

    @commands.command()
    async def uptime(self, ctx):
        '''Get the uptime in hours for me'''
        current_time = time.time()
        difference = int(round(current_time - self.bot.start_time))
        text = str(datetime.timedelta(seconds=difference)) + ' mins' if str(datetime.timedelta(seconds=difference)
                                                                            )[0] == '0' or str(datetime.timedelta(seconds=difference))[0:1] != '00' else ' hours'
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text=f"{ctx.author} | {self.bot.user}")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Current uptime: " + text)

    # @cog_ext.cog_slash(name="ping")
    @commands.command()
    async def ping(self, ctx):
        '''Get the Latency'''
        starttime = time.time()
        msg = await ctx.send("Ping...")
        async with ctx.channel.typing():
            e = discord.Embed(
                title="Pong!", description=f"Heartbeat : {round(self.bot.latency * 1000, 2)} ms", color=discord.Color.random())
            endtime = time.time()
            difference = float(int(starttime - endtime))
            e.add_field(name="Script Speed", value=f"{difference}ms")
            await msg.edit(content="", embed=e)

    @commands.command()
    async def source(self, ctx):
        """ Displays source code """
        e = discord.Embed(
            title="You didn't provide a command (because you cant), so here's the source!",
            description=f"[Source]({github})",
            color=discord.Color.random()
        )
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Info(bot))
