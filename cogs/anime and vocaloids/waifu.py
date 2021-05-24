from discord.ext import commands
import discord
import asyncio
from discord_slash import cog_ext, SlashContext

class Waifu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.dagpi = bot.dagpi
        self.description = 'Get waifu ! UwU'
    
    async def get_waifu(self):
        waifu = await self.bot.dagpi.waifu() 
        pic = waifu['display_picture']
        name = waifu['name']
        likes_rank = waifu['like_rank']
        trash_rank = waifu['trash_rank']
        anime = waifu['appearances'][0]['name']
                
        e = discord.Embed(color=discord.Color.random(),title=name)
        e.add_field(name="**Anime**",value=anime,inline=True)
        e.add_field(name="**:heartbeat:**",value=likes_rank,inline=True)
        e.add_field(name="**:wastebasket:**",value=trash_rank,inline=True)
        e.set_image(url=pic)
        e.set_footer(text=f'React with any emoji in 30 sec to claim him/her')
        return e,name
    
    @commands.command(aliases=['w','wfu','wa'])
    async def waifu(self, ctx):
        '''Get random waifu and marry them! UwU!'''
        waifu = await self.get_waifu()
        message = await ctx.send(embed = waifu[0])
        await message.add_reaction('💓')
        
        def check(reaction, user):
            return user != self.bot.user and message.id == reaction.message.id
        
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0,check=check)
            await ctx.send(f'**{user.mention}** has *married* **{waifu[-1]}**! UwU :ring:')
        except asyncio.TimeoutError:
            pass
    
    @cog_ext.cog_slash(name="waifu", description='Get random waifu and marry them! UwU!')
    async def waifu_slash(self, ctx: SlashContext):
        '''Get random waifu and marry them! UwU!'''
        waifu = await self.get_waifu()
        message = await ctx.send(embed = waifu[0])
        await message.add_reaction('💓')
        
        def check(reaction, user):
            return user != self.bot.user and message.id == reaction.message.id
        
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0,check=check)
            await ctx.send(f'**{user.mention}** has *married* **{waifu[-1]}**! UwU :ring:')
        except asyncio.TimeoutError:
            pass
        

def setup(bot):
    bot.add_cog(Waifu(bot))