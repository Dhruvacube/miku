from os.path import join
from pathlib import Path
from random import choice

import discord
import requests
from discord.ext import commands
from discord_slash import cog_ext


class Vocaloid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.endpoint = 'https://api.meek.moe/'
        self.description = 'Get some kawai pictures of the vocaloids.'
    
    async def meek_api(self,ctx, name):
        l = choice([self.endpoint, 'https://mikuapi.predeactor.net/random',False]) if name.lower() == 'miku' else self.endpoint
        e=discord.Embed(title=name.capitalize(),color=discord.Color.random())
        try:
            data = requests.get(url = l + name).json()['url']
            e.set_image(url=data)
        except:
            imageslistdir = Path(__file__).resolve(
                strict=True).parent / join('util','images_list.txt')
            filepointer = open(imageslistdir)
            imageslist = filepointer.readlines()
            if name == 'miku':
                e.set_image(url=choice(imageslist))
            else:
                e=discord.Embed(title='Sorry but currently there is some problem!',color=discord.Color.red())
                e.set_image(url=choice(imageslist))
        return e
    
    @cog_ext.cog_slash(name="rin",description='Rin kawai picture')
    @commands.command()
    async def rin(self, ctx):
        '''Rin kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'rin'))
        
    @cog_ext.cog_slash(name="una",description='Una kawai picture')
    @commands.command()
    async def una(self, ctx):
        '''Una kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'una'))
    
    @cog_ext.cog_slash(name="gumi",description='Gumi kawai picture')
    @commands.command()
    async def gumi(self, ctx):
        '''Gumi kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'gumi'))
    
    @cog_ext.cog_slash(name="ia",description='Ia kawai picture')
    @commands.command()
    async def ia(self, ctx):
        '''Ia kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'ia'))
    
    @cog_ext.cog_slash(name="luka",description='Luka kawai picture')
    @commands.command()
    async def luka(self, ctx):
        '''Luka kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'luka'))
    
    @cog_ext.cog_slash(name="fukase",description='Fukase kawai picture')
    @commands.command()
    async def fukase(self, ctx):
        '''Fukase kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'fukase'))
    
    @cog_ext.cog_slash(name="miku",description='Hatsune Miku kawai picture')
    @commands.command()
    async def miku(self, ctx):
        '''Hatsune Miku kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'miku'))
    
    @cog_ext.cog_slash(name="len",description='Len kawai picture')
    @commands.command(name='len')
    async def _len(self, ctx):
        '''Len kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'len'))
    
    @cog_ext.cog_slash(name="kaito",description='Kaito kawai picture')
    @commands.command()
    async def kaito(self, ctx):
        '''Kaito kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'kaito'))
    
    @cog_ext.cog_slash(name="teto",description='Teto kawai picture')
    @commands.command()
    async def teto(self, ctx):
        '''Teto kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'teto'))
    
    @cog_ext.cog_slash(name="meiko",description='Meiko kawai picture')
    @commands.command()
    async def meiko(self, ctx):
        '''Meiko kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'meiko'))
    
    @cog_ext.cog_slash(name="yukari",description='Yukari kawai picture')
    @commands.command()
    async def yukari(self, ctx):
        '''Yukari kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'yukari'))
    
    @cog_ext.cog_slash(name="miki",description='Miki kawai picture')
    @commands.command()
    async def miki(self, ctx):
        '''Miki kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'miki'))
    
    @cog_ext.cog_slash(name="lily",description='Lily kawai picture')
    @commands.command()
    async def lily(self, ctx):
        '''Lily kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'lily'))
    
    @cog_ext.cog_slash(name="mayu",description='Mayu kawai picture')
    @commands.command()
    async def mayu(self, ctx):
        '''Mayu kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'mayu'))
    
    @cog_ext.cog_slash(name="aoki",description='Aoki kawai picture')
    @commands.command()
    async def aoki(self, ctx):
        '''Aoki kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'aoki'))
        
    @cog_ext.cog_slash(name="zola",description='Zola kawai picture')
    @commands.command()
    async def zola(self, ctx):
        '''Zola kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'zola'))
    
    @cog_ext.cog_slash(name="diva",description='Random picturs from Project Diva')
    @commands.command()
    async def diva(self, ctx):
        '''Random picturs from Project Diva'''
        await ctx.send(embed = await self.meek_api(ctx,'diva'))

def setup(bot):
    bot.add_cog(Vocaloid(bot))
