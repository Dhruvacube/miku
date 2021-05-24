from os.path import join
from pathlib import Path
from random import choice

import discord
import requests
from discord.ext import commands


class Vocaloid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.endpoint = 'https://api.meek.moe/'
        self.description = 'Get some kawai pictures of the vocaloids.'
    
    async def meek_api(self,ctx, name):
        print(Path(__file__).resolve(
                strict=True).parent / join('util','images_list.txt'))
        l = choice([self.endpoint, 'https://mikuapi.predeactor.net/random',False]) if name.lower() == 'miku' else self.endpoint
        e=discord.Embed(title=name.capitalize(),color=discord.Color.random())
        try:
            if name=='miku' and l:
                data = requests.get(url = l + name if l=='https://api.meek.moe/' else 'https://mikuapi.predeactor.net/random').json()['url']
            else:
                data = requests.get(url = l + name).json()['url']
            e.set_image(url=data)
        except:
            imageslistdir = Path(__file__).resolve(
                strict=True).parent.parent / join('util','images_list.txt')
            filepointer = open(imageslistdir)
            imageslist = filepointer.readlines()
            if name == 'miku':
                e.set_image(url=choice(imageslist))
            else:
                e=discord.Embed(title='Sorry but currently there is some problem!',color=discord.Color.red())
                e.set_image(url=choice(imageslist))
        return e
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def rin(self, ctx):
        '''Rin kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'rin'))
        
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def una(self, ctx):
        '''Una kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'una'))
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def gumi(self, ctx):
        '''Gumi kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'gumi'))
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ia(self, ctx):
        '''Ia kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'ia'))
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def luka(self, ctx):
        '''Luka kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'luka'))
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def fukase(self, ctx):
        '''Fukase kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'fukase'))
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def miku(self, ctx):
        '''Hatsune Miku kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'miku'))
    
    @commands.command(name='len')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def _len(self, ctx):
        '''Len kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'len'))
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def kaito(self, ctx):
        '''Kaito kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'kaito'))
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def teto(self, ctx):
        '''Teto kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'teto'))
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def meiko(self, ctx):
        '''Meiko kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'meiko'))
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def yukari(self, ctx):
        '''Yukari kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'yukari'))
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def miki(self, ctx):
        '''Miki kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'miki'))
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def lily(self, ctx):
        '''Lily kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'lily'))
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def mayu(self, ctx):
        '''Mayu kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'mayu'))
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def aoki(self, ctx):
        '''Aoki kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'aoki'))
        
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def zola(self, ctx):
        '''Zola kawai picture'''
        await ctx.send(embed = await self.meek_api(ctx,'zola'))
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def diva(self, ctx):
        '''Random picturs from Project Diva'''
        await ctx.send(embed = await self.meek_api(ctx,'diva'))

def setup(bot):
    bot.add_cog(Vocaloid(bot))
