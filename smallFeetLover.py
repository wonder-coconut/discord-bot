import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='~')
BOT = discord.Client()

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
    #~getwoke for this message 
    #~nigga for cute poetry aka BARS
    #~bruh for surprise
    #~madarchod for haha very nice desi meme
    ~engage to remove the big guns
    ~art for a personification of the internet
    ~bop for a bop
    ~formula for the greatest lego oc ever

    dont be shy say hello

    pigeon for something
    say the word \"idiot\" for a strongly worded copypasta
    be horny
    nice for a ceaser
    muda
    ask him what bear is best
    what what what what
    bible time ezekiel boy
    ''')

#commands list 

@bot.command(name = 'nigga')
async def nigga(ctx):
    await ctx.channel.send('fuck bitches get money nigga cat nigga cat')

@bot.command(name = 'bruh')
async def bruh(ctx):
    BRUH=open('/home/wondercoconut/python3/botshit/bruh.txt','r')
    BRUH=BRUH.read()
    await ctx.channel.send(BRUH)

@bot.command(name = 'madarchod')
async def madarchod(ctx):
    await ctx.channel.send('mai madarchod hoon jo isme aaya')

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return
    else:
        word=ctx.content.lower()
        if word.startswith('hello'):
            await ctx.channel.send('fuck off')
        else:
              try:
                  image=str(ctx.attachments[0])
                  if isImage(image):
                      await ctx.channel.send('img')
                  #await ctx.channel.send(isImage(image))

                  attachTest(Ctx.attachments)

                  #print(ctx.attachments)                    
              except:
                    pass    
        await bot.process_commands(ctx)
            
def isImage(image):
    image_ext = ['jpg','png','jpeg']
    x = False
    for ext in image_ext:
        if image.find(ext)!=-1:
            x=True
            break

    return x


#        i=0
#        while(True):
#            try:
#                s=word[i].lower()
#                if(s=='idiot'):
#                    await ctx.channel.send('idiot')
#            except:
#                break


@bot.event
async def on_ready():
    print('logged in as '+(str(bot.user)))

bot.run(getToken())

