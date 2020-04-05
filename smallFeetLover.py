import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='~')

def getToken():
    tokenFile = open('/home/wondercoconut/python3/botshit/token.txt','r')
    tokentxt = tokenFile.read()
    Token = tokentxt.split('\n')
    return Token[1]


@bot.command(name = 'start')
async def test(ctx):
    await ctx.channel.send('type in ~getwoke to get started')

@bot.command(name = 'getwoke')
async def start(ctx):
    await ctx.channel.send('''
    press F to pay respects
    ~getwoke for this message
    ~nigga for cute poetry aka BARS
    ~bruh for surprise
    ~madarchod for haha very nice desi meme
    say the word \"idiot\" for a strongly worded copypasta
    ~bop for a bop
    pigeon for something
    be horny
    ~engage to remove the big guns
    ~art for a personification of the internet
    nice for a ceaser
    muda
    ask him what bear is best
    what what what what
    bible time ezekiel boy
    ~formula for the greatest lego oc ever''')

#commands list 

@bot.command(name = 'nigga')
async def nigga(ctx):
    await ctx.channel.send('fuck bitches get money nigga cat nigga cat')

@bot.command(name = 'bruh')
async def bruh(ctx):
    s1='bruh'
    s2='moment'
    i=1
    while i<=2:
        j=1
        while j<=10:
            if(j<=5):
                s=s1+j*5*' '+s2
            else:
                s=s1+(10-j)*5*' '+s2
            await ctx.channel.send(s)
            j+=1
        i+=1

@bot.command(name = 'madarchod')
async def madarchod(ctx):
    await ctx.channel.send('mai madarchod hoon jo isme aaya')

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return
    else:
        word=ctx.content
        word=word.split()
        await ctx.channel.send(word[0])
        i=0
        #while(True):
        #    try:
        #        s=word[i].lower()
        #        if(s=='idiot'):
        #            await ctx.channel.send('idiot')
        #    except:
        #        break


@bot.event
async def on_ready():
    print('logged in as '+(str(bot.user)))

bot.run(getToken())
