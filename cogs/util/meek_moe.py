import discord
from pathlib import Path
from random import choice
import requests
from os.path import join

async def meek_api(ctx, name):
    l = choice(['https://api.meek.moe/', 'https://mikuapi.predeactor.net/random',False]) if name.lower() == 'miku' else 'https://api.meek.moe/'
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