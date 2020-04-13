import discord
from discord.ext import commands

from random import seed
from random import randint

import datetime

bot = commands.Bot(command_prefix='$')
BOT = discord.Client()

def getToken():
    tokenFile = open('/home/wondercoconut/python3/botshit/token.txt','r')
    tokentxt = tokenFile.read()
    Token = tokentxt.split('\n')
    return Token[3]

@bot.event
async def on_ready():
    print('logged in as '+str(bot.user))

@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        word =  ctx.content.lower()
        if word.find('xd') != -1:
            await ctx.channel.send(xdRandom())

def xdRandom():
    time = datetime.datetime.now()
    mic = time.microsecond
    seed(mic)
    i = randint(1,5)
    if(i<=4):
        xd =  open('/home/wondercoconut/python3/botshit/discord_bot/xD text/XD2.txt')
        xd = xd.read()
        xd = xd.split('\n')
        return xd[i-1]
    elif (i>=5):
        xd =  open('/home/wondercoconut/python3/botshit/discord_bot/xD text/XD1.txt')
        xd = xd.read()
        return xd

bot.run (getToken())

