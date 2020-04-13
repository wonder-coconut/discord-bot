import discord
from discord.ext import commands

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
            await ctx.channel.send('i am alive')

bot.run (getToken())