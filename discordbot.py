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

from cogs.util import post_stats_log as posting


def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    prefixes = ['*', 'm$', 'miku ', 'miku', '&']

    if not message.guild:
        return 'm!'

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

@bot.event
async def on_ready():
    cog_dir = Path(__file__).resolve(strict=True).parent / join('cogs')
    for filename in os.listdir(cog_dir):
        if filename != 'util':
            if os.path.isdir(cog_dir / filename):
                for i in os.listdir(cog_dir / filename):
                    if i.endswith('.py'):
                        bot.load_extension(f'cogs.{filename.strip(" ")}.{i[:-3]}')
        else:
            if filename.endswith('.py'):
                if filename != '__init__.py':
                    bot.load_extension(f'cogs.{filename[:-3]}')

    current_time = time.time()
    difference = int(round(current_time - bot.start_time))
    stats = bot.get_channel(844534399500419092)
    e = discord.Embed(title=f"Bot Loaded!", description=f"Bot ready by **{time.ctime()}**, loaded all cogs perfectly! Time to load is {difference} secs :)")
    e.set_thumbnail(url=bot.user.avatar_url)
    print('Started The Bot')

    await posting.PostStats(bot).post_guild_stats_all()
    await stats.send(embed=e)
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='over Miku Expo'))

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
    bot.run(token_get('TOKEN'))
except RuntimeError:
    bot.logout()
except KeyboardInterrupt:
    bot.logout()
