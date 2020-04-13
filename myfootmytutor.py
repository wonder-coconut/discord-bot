import praw

def getToken():
    tokenFile = open('/home/wondercoconut/python3/botshit/token.txt','r')
    tokentxt = tokenFile.read()
    Token = tokentxt.split('\n')
    return Token[1]

def getPass():
    passFile = open('/home/wondercoconut/python3/botshit/pwd.txt')
    passtxt = passFile.read()
    return passtxt


#reddit api login
reddit = praw.Reddit(client_id='HW6AYqkTBgEgyQ',
                     client_secret=getToken(),
                     username='myfoot_mytutor',
                     password='03Rishab',#getPass()
                     user_agent='myfootmytutor by u/wonder_coconut')




def url():

    subreddit = reddit.subreddit('pigeon')

    for submission in subreddit.top(limit = None):

        url = str(submission.url)
        break
    
    return url

