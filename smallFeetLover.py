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
    await ctx.channel.send('type in ~getwoke')

@bot.command(name = 'getwoke')
async def start(ctx):
    await ctx.channel.send('''press F to pay respects
    ~getwoke for this message
    ~nigga for cute poetry aka BARS
    ~bruh for surprise
    ~madarchod for haha very nice desi meme
    ~caps <text>
    say the word \"idiot\" for a strongly worded copypasta
    ~gay for the gayest picture you can ever find
    ~bop for a bop
    ~wonder for a retarded fuck portrait
    pigeon for something
    be horny
    ~engage to remove the big guns
    ~art for a personification of the internet
    nice for a ceaser
    muda
    ask him what bear is best
    what what what what
    bible time ezekiel boy''')

@bot.event
async def on_ready():
    print('logged in as '+(str(bot.user)))

bot.run(getToken())
