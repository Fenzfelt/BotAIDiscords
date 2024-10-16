import discord
from discord.ext import commands
import os, random
from get_model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            nama_file = file.filename
            url_file = file.url
            await file.save(f'./{nama_file}')
            await ctx.send(f'file telah disimpan dengan nama {nama_file}')

            nama, skor = get_class(image=nama_file, model='keras_model.h5',label='labels.txt')

            #inferensi
            if nama == 'telurbebek\n' and skor >= 0.6:
                await ctx.send('Ini adalah telur bebek')
                await ctx.send('telur ini biasanya dijadikan telur asin')
            elif nama == 'telurayam\n' and skor >= 0.6:
                await ctx.send('ini adalah telur ayam')
                await ctx.send('telur ini biasanya digoreng untuk dijadikan telur mata sapi/ telur dadar')
            else:
                await ctx.send('tidak tahu karena tempe')
    else:
        await ctx.send('Tidak ada file yang dikirimkan')            

bot.run("isi tokenmu")
