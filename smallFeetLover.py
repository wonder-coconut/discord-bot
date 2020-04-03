import discord

client = discord.Client()

def getToken():
    tokenFile = open('/home/wondercoconut/python3/botshit/token.txt','r')
    tokentxt = tokenFile.read()
    Token = tokentxt.split('\n')
    return Token[1]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('bonjour'):
        await message.channel.send('guten morgen')

def main():
    client.run(getToken())

if __name__ == '__main__':
    main()