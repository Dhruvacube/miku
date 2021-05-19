import discord
from discord.ext import commands
import os
import dotenv
import DiscordUtils
import sentry_sdk

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
bot.music = DiscordUtils.Music()

#Sentry Init
sentry_sdk.init(
    SENTRY_LINK,
    traces_sample_rate=1.0
)
try:
    division_by_zero = 1 / 0
except:
    pass