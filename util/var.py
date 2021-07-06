import os
from pathlib import Path

import dotenv

dotenv_file = Path(__file__).resolve().parent.parent / ".env"
def token_get(tokenname):
    if os.path.isfile(dotenv_file):
        dotenv.load_dotenv(dotenv_file)
    return os.environ.get(tokenname, 'False').strip('\n')

def get_blacklist_servers():
    with open(Path(__file__).resolve().parent/'blacklistservers.txt') as f:
        a=f.readlines()
    remove_new_line = lambda a: int(str(a).strip('\n'))
    return list(map(remove_new_line, a))
        

website = token_get('WEBSITE')
github = token_get('GITHUB')

statcord = token_get('STATCORD')
discord_id = token_get('DISCORD_CLIENT_ID')

dagpi = token_get('DAGPI')

dblst = token_get('DISCORDBOTLIST')
discordbotsgg = token_get('DISCORDBOTSGG')
topken = token_get('TOPGG')
bfd = token_get('BOTSFORDISCORD')
botlist = token_get('DISCORDLISTSPACE')
discordboats = token_get('DISCORDBOATS')
voidbot = token_get('VOIDBOTS')
fateslist = token_get('FATESLIST')
bladebot = token_get('BLADEBOTLIST')
spacebot = token_get('SPACEBOT')
extremelist = token_get('DISCORDEXTREMELIST')

version = token_get('VERSION')
