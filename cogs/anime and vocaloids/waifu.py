from discord.ext import commands
import discord
import asyncio

class Waifu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.dagpi = bot.dagpi
        self.description = 'Get waifu ! UwU'
    
    @commands.command()
    async def waifu(self, ctx):
        '''Get wqaifu and marry them! UwU!'''
        waifu = await self.bot.dagpi.waifu() 
        pic = waifu['display_picture']
        name = waifu['name']
        likes_rank = waifu['like_rank']
        trash_rank = waifu['trash_rank']
        anime = waifu['appearances'][0]['name']
        
        his_or_her = 'him' if waifu['husbando'] else 'her'
        
        e = discord.Embed(color=discord.Color.random(),title=name)
        e.add_field(name="**Anime**",value=anime,inline=True)
        e.add_field(name="**:heartbeat:**",value=likes_rank,inline=True)
        e.add_field(name="**:wastebasket:**",value=trash_rank,inline=True)
        e.set_image(url=pic)
        e.set_footer(text=f'React with any emoji in 30 sec to claim {his_or_her}')
        message = await ctx.send(embed=e)
        await message.add_reaction('💓')
        
        def check(reaction, user):
            return user != self.bot.user
        
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0,check=check)
            await ctx.send(f'**{user.mention}** has *married* **{name}**! UwU :ring:')
        except asyncio.TimeoutError:
            pass
        

def setup(bot):
    bot.add_cog(Waifu(bot))