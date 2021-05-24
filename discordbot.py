import os
import time
from os.path import join
from pathlib import Path

import discord
import DiscordUtils
import dotenv
import sentry_sdk
from discord.ext import commands
from pretty_help import PrettyHelp
from discord_slash import SlashCommand
from asyncdagpi import Client

from cogs.util import post_stats_log as posting


def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    prefixes = ['m$', 'miku ', 'miku', '&', 'm&']

    if not message.guild:
        return 'm!'
    if message.guild.id == 747480356625711204:
        return prefixes + ['*']

    return commands.when_mentioned_or(*prefixes)(bot, message)

dotenv_file = os.path.join(".env")
def token_get(tokenname):
    if os.path.isfile(dotenv_file):
        dotenv.load_dotenv(dotenv_file)
    return os.environ.get(tokenname, 'False').strip('\n')

intents = discord.Intents.default()
SENTRY_LINK = token_get('SENTRY_LINK')

#Bot Init
bot = commands.Bot(
    command_prefix=get_prefix,
    intents=intents, 
    help_command=PrettyHelp(show_index=True),  
    
    allowed_mentions=discord.AllowedMentions(
        users=True, 
        roles=False, 
        everyone=False
    ),
    
    case_insensitive=True,
    description="Hi I am **Hatsune Miku**"
)
bot.statcord = token_get('STATCORD')
bot.discord_id = token_get('DISCORD_CLIENT_ID')
bot.start_time = time.time()
bot.music = DiscordUtils.Music()
bot.token = token_get('TOKEN')
bot.dagpi = Client(token_get('DAGPI'))
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)

cog_dir = Path(__file__).resolve(strict=True).parent / join('cogs')
for filename in os.listdir(cog_dir):
    if os.path.isdir(cog_dir / filename) and filename != 'util':
        for i in os.listdir(cog_dir / filename):
            if i.endswith('.py'):
                bot.load_extension(f'cogs.{filename.strip(" ")}.{i[:-3]}')
    else:
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    current_time = time.time()
    difference = int(round(current_time - bot.start_time))
    stats = bot.get_channel(844534399500419092)
    e = discord.Embed(title=f"Bot Loaded!", description=f"Bot ready by **{time.ctime()}**, loaded all cogs perfectly! Time to load is {difference} secs :)", color=discord.Color.random())
    e.set_thumbnail(url=bot.user.avatar_url)
    print('Started The Bot')

    await posting.PostStats(bot).post_guild_stats_all()
    await stats.send(embed=e)
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='over Miku Expo'))


# Vocaloids Slash Commands
# @slash.slash(name="rin",description='Rin kawai picture')
# async def rin(ctx: SlashContext):
#     '''Rin kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'rin'))
        
# @slash.slash(name="una",description='Una kawai picture')
# async def una(ctx: SlashContext):
#     '''Una kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'una'))
    
# @slash.slash(name="gumi",description='Gumi kawai picture')
# async def gumi(ctx: SlashContext):
#     '''Gumi kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'gumi'))
    
# @slash.slash(name="ia",description='Ia kawai picture')
# async def ia(ctx: SlashContext):
#     '''Ia kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'ia'))
    
# @slash.slash(name="luka",description='Luka kawai picture')
# async def luka(ctx: SlashContext):
#     '''Luka kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'luka'))
    
# @slash.slash(name="fukase",description='Fukase kawai picture')
# async def fukase(ctx: SlashContext):
#     '''Fukase kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'fukase'))
    
# @slash.slash(name="miku",description='Hatsune Miku kawai picture')
# async def miku(ctx: SlashContext):
#     '''Hatsune Miku kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'miku'))
    
# @slash.slash(name="len",description='Len kawai picture')
# async def _len(ctx: SlashContext):
#     '''Len kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'len'))
    
# @slash.slash(name="kaito",description='Kaito kawai picture')
# async def kaito(ctx: SlashContext):
#     '''Kaito kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'kaito'))
    
# @slash.slash(name="teto",description='Teto kawai picture')
# async def teto(ctx: SlashContext):
#     '''Teto kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'teto'))
    
# @slash.slash(name="meiko",description='Meiko kawai picture')
# async def meiko(ctx: SlashContext):
#     '''Meiko kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'meiko'))
    
# @slash.slash(name="yukari",description='Yukari kawai picture')
# async def yukari(ctx: SlashContext):
#     '''Yukari kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'yukari'))
    
# @slash.slash(name="miki",description='Miki kawai picture')
# async def miki(ctx: SlashContext):
#     '''Miki kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'miki'))
    
# @slash.slash(name="lily",description='Lily kawai picture')
# async def lily(ctx: SlashContext):
#     '''Lily kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'lily'))
        
# @slash.slash(name="mayu",description='Mayu kawai picture')
# async def mayu(ctx: SlashContext):
#     '''Mayu kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'mayu'))

# @slash.slash(name="aoki",description='Aoki kawai picture')
# async def aoki(ctx: SlashContext):
#     '''Aoki kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'aoki'))
        
# @slash.slash(name="zola",description='Zola kawai picture')
# async def zola(ctx: SlashContext):
#     '''Zola kawai picture'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'zola'))
    
# @slash.slash(name="diva",description='Random picturs from Project Diva')
# async def diva(ctx: SlashContext):
#     '''Random picturs from Project Diva'''
#     await ctx.send(embed = await meek_moe.meek_api(ctx,'diva'))
    



#Sentry Init
sentry_sdk.init(
    SENTRY_LINK,
    traces_sample_rate=1.0
)
try:
    division_by_zero = 1 / 0
except:
    pass



try:
    bot.run(bot.token)
except RuntimeError:
    bot.logout()
except KeyboardInterrupt:
    bot.logout()
