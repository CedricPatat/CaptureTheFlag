#######################################
#####     Hash me if you can     ######
#######################################

## Loading libraries
from lxml import html
import requests
import hashlib

## Functions
def GetMessage():
    page = requests.get('http://challenges.ringzer0team.com:10013/')
    tree = html.fromstring(page.content)
    message = tree.xpath('/html/body/main/div/text()')
    message =  message[1].replace(' ','').replace('\n','').encode('utf-8')
    return message

def HashMessage(message:str):
    hashedMessage = hashlib.sha512(message).hexdigest()
    return hashedMessage
    

def GetFlag(hashedMessage):
    data = requests.get('http://challenges.ringzer0team.com:10013/?r='+str(hashedMessage))
    new_tree = html.fromstring(data.content)
    flag = new_tree.xpath('/html/body/main/div/text()')[0]
    return flag

## Main
if __name__ == "__main__":
    msg = GetMessage()
    hash_msg = HashMessage(message=msg)
    flag = GetFlag(hashedMessage=hash_msg)
    print(flag)