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
                s=s1+j*3*' '+s2
            else:
                s=s1+(10-j)*3*' '+s2
            await ctx.channel.send(s)
            j+=1
        i+=1



@bot.event
async def on_ready():
    print('logged in as '+(str(bot.user)))

bot.run(getToken())
