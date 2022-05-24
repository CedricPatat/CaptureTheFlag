#######################################
#####     I hate mathematics     ######
#######################################

## Loading libraries
from lxml import html
import requests
import hashlib

## Functions
def GetMessage():
    page = requests.get('http://challenges.ringzer0team.com:10032/')
    tree = html.fromstring(page.content)
    message = tree.xpath('/html/body/main/div[2]/text()')
    message =  message[1].replace(' ','').replace('\n','').replace('=?','')
    return message

def ResultCalculation(message:str):
    num1 = int(message.split("+")[0])
    num2 = int(message.split("+")[1].split("-")[0], 16)
    num3 = int('0b'+ message.split("-")[1],2)
    result = num1 + num2 - num3
    return result
    

def GetFlag(result:int):
    data = requests.get('http://challenges.ringzer0team.com:10032/?r='+str(result))
    new_tree = html.fromstring(data.content)
    flag = new_tree.xpath('/html/body/main/div/text()')[0]
    return flag

## Main
if __name__ == "__main__":
    msg = GetMessage()
    res = ResultCalculation(message=msg)
    flag = GetFlag(result=res)
    print(flag)