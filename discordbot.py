import os
import time
from os.path import join
from pathlib import Path

import discord
import dotenv
from discord.ext import commands
from pretty_help import PrettyHelp
from discord_slash import SlashCommand


def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    prefixes = ['m$', 'miku ', 'miku', '&', 'm&']

    if not message.guild:
        return 'm!'
    if message.author.id == 571889108046184449 or message.guild.id == 747480356625711204:
        return prefixes + ['*']

    return commands.when_mentioned_or(*prefixes)(bot, message)


dotenv_file = os.path.join(".env")


def token_get(tokenname):
    if os.path.isfile(dotenv_file):
        dotenv.load_dotenv(dotenv_file)
    return os.environ.get(tokenname, 'False').strip('\n')


intents = discord.Intents.all()
intents.reactions = True
intents.guilds = True
intents.presences = False

# Bot Init
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
    strip_after_prefix=True,
    description="Hi I am Hatsune Miku. こんにちは、初音ミクです。"
)
bot.start_time = time.time()
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
    e = discord.Embed(title=f"Bot Loaded!",
                      description=f"Bot ready by **{time.ctime()}**, loaded all cogs perfectly! Time to load is {difference} secs :)", color=discord.Color.random())
    e.set_thumbnail(url=bot.user.avatar_url)
    print('Started The Bot')
    await stats.send(embed=e)
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='over Miku Expo'))


try:
    bot.run(token_get('TOKEN'))
except discord.PrivilegedIntentsRequired:
    print(
        "[Login Failure] You need to enable the server members intent on the Discord Developers Portal."
    )
except discord.errors.LoginFailure:
    print("[Login Failure] The token inserted in config.ini is invalid.")
