import discord
from discord.ext import commands
from .util import post_stats_log

class BotEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.posting = post_stats_log.PostStats(self.bot)
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        '''
        try:
            img=random.choice(self.minato_gif)
            file = discord.File(join(self.minato_dir, 'minato',img), filename=img)
            await guild.system_channel.send('https://i.imgur.com/j6j7ob7.mp4')
            f=open(Path(__file__).resolve(strict=True).parent.parent.parent / join('welcome_message.txt'),'r')
            f1=f.read()
            await guild.system_channel.send(f1.format(guild.name, self.bot.user.mention, self.bot.user.mention, self.bot.user.mention, guild.owner.mention))
            img=random.choice(self.minato_gif)
            file = discord.File(join(self.minato_dir, 'minato',img), filename=img)
            await guild.system_channel.send(file=file)
        except: pass
        '''

        e34= discord.Embed(title=f'{guild.name}', color= 0x2ecc71,description='Added')
        if guild.icon:
            e34.set_thumbnail(url=guild.icon_url)
        if guild.banner:
            e34.set_image(url=guild.banner_url_as(format="png"))
        c = self.bot.get_channel(844548967127973888)
        e34.add_field(name='**Total Members**',value=guild.member_count)
        e34.add_field(name='**Bots**',value=sum(1 for member in guild.members if member.bot))
        e34.add_field(name="**Region**", value=str(guild.region).capitalize(), inline=True)
        e34.add_field(name="**Server ID**", value=guild.id, inline=True)
        await c.send(embed=e34)
        await c.send(f'We are now currently at **{len(self.bot.guilds)+1} servers**')
        await self.posting.post_guild_stats_all()

    #when bot leaves the server
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        e34= discord.Embed(title=f'{guild.name}', color= 0xe74c3c,description='Left')
        if guild.icon:
            e34.set_thumbnail(url=guild.icon_url)
        if guild.banner:
            e34.set_image(url=guild.banner_url_as(format="png"))
        c = self.bot.get_channel(844548967127973888)
        e34.add_field(name='**Total Members**',value=guild.member_count)
        e34.add_field(name='**Bots**',value=sum(1 for member in guild.members if member.bot))
        e34.add_field(name="**Region**", value=str(guild.region).capitalize(), inline=True)
        e34.add_field(name="**Server ID**", value=guild.id, inline=True)
        await c.send(embed=e34)
        await c.send(f'We are now currently at **{len(self.bot.guilds)+1} servers**')
        await self.posting.post_guild_stats_all()

    #on message event
    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user.mentioned_in(message) and message.mention_everyone is False and message.content.lower() in ('<@!840276343946215516>', '<@840276343946215516>') or message.content.lower() in ('<@!840276343946215516> prefix', '<@840276343946215516> prefix'):
            if not message.author.bot:
                await  message.channel.send('The prefix is **m$** ,A full list of all commands is available by typing ```m$help```')
    
    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        guild = ctx.guild
        if isinstance(error, commands.CommandOnCooldown):
            e1 = discord.Embed(title="Command Error!", description=f"`{error}`")
            e1.set_footer(text=f"{ctx.author.name}")
            await ctx.channel.send(embed=e1, delete_after=3)
        elif isinstance(error, commands.MissingPermissions):
            e3 = discord.Embed(title="Command Error!", description=f"`{error}`")
            e3.set_footer(text=f"{ctx.author.name}")
            await ctx.send(embed=e3, delete_after=3)
        elif isinstance(error, commands.MissingRequiredArgument):
            e4 = discord.Embed(title="Command Error!", description=f"`{error}`")
            e4.set_footer(text=f"{ctx.author.name}")
            await ctx.channel.send(embed=e4, delete_after=2)
        elif isinstance(error, commands.CommandNotFound):
            e2 = discord.Embed(title="Command Error!", description=f"`{error}`")
            e2.set_footer(text=f"{ctx.author.name}")
            await ctx.channel.send(embed=e2, delete_after=3)

        elif isinstance(error, commands.CommandInvokeError): 
            e7 = discord.Embed(title="Oh no, I guess I have not been given proper access! Or some internal error", description=f"`{error}`")
            e7.add_field(name="Command Error Caused By:", value=f"{ctx.command}")
            e7.add_field(name="By", value=f"{ctx.author.name}")
            e7.set_thumbnail(url=f"https://i.imgur.com/p8fLFQ4.jpg")
            e7.set_footer(text=f"{ctx.author.name}")
            await ctx.channel.send(embed=e7, delete_after=5)
        else:
            c = self.bot.get_channel(844539081979592724)
            
            haaha = ctx.author.avatar_url
            e9 = discord.Embed(title="Oh no there was some error", description=f"`{error}`")
            e9.add_field(name="**Command Error Caused By**", value=f"{ctx.command}")
            e9.add_field(name="**By**", value=f"**ID** : {ctx.author.id}, **Name** : {ctx.author.name}")
            e9.set_thumbnail(url=f"{haaha}")
            e9.set_footer(text=f"{ctx.author.name}")
            await ctx.channel.send(embed=e9, delete_after=2)
            await c.send(embed=e9)
            
            await ctx.send('**Sending the error report info to my developer**', delete_after=2)
            e = discord.Embed(title=f'In **{ctx.guild.name}**',description=f'User affected {ctx.message.author}' , color= 0x2ecc71)
            if ctx.guild.icon:
                e.set_thumbnail(url=ctx.guild.icon_url)
            if ctx.guild.banner:
                e.set_image(url=ctx.guild.banner_url_as(format="png"))
            e.add_field(name='**Total Members**',value=ctx.guild.member_count)
            e.add_field(name='**Bots**',value=sum(1 for member in ctx.guild.members if member.bot))
            e.add_field(name="**Region**", value=str(ctx.guild.region).capitalize(), inline=True)
            e.add_field(name="**Server ID**", value=ctx.guild.id, inline=True)
            await ctx.send('**Error report was successfully sent**', delete_after=2)
            await c.send(embed=e)

def setup(bot):
    bot.add_cog(BotEvents(bot))