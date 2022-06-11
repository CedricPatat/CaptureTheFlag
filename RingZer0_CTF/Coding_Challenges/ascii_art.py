#######################################
#####          Ascii Art         ######
#######################################

## Loading libraries
from lxml import html
import requests


## Functions
def GetMessage():
    page = requests.get('http://challenges.ringzer0team.com:10119/')
    tree = html.fromstring(page.content)
    message = tree.xpath('/html/body/main/div/text()')
    return message

def Decrypt(message:list):
    key = ""
    for m in range(2,len(message)-3,5):
        list = str(message[m:m+5]).replace("\\", "")
        if "['xa0xxxxa0', 'xxa0xa0xa0x', 'xxa0xa0xa0x', 'xxa0xa0xa0x', 'xa0xxxxa0']" in list:
            key = key + "0"
        elif "['xa0xxxa0xa0', 'xxa0xxa0xa0', 'xa0xa0xxa0xa0', 'xa0xa0xxa0xa0', 'xxxxx']" in list:
            key = key + "1"
        elif "['xa0xxxxa0', 'xxa0xa0xa0xxa0', 'xa0xa0xxxa0', 'xa0xxa0xa0xa0', 'xxxxx']" in list:
            key = key + "2"
        elif "['xa0xxxxa0', 'xxa0xa0xa0x', 'xa0xa0xxxa0', 'xxa0xa0xa0x', 'xa0xxxxa0']" in list :
            key = key + "3"
        elif "['xa0xxa0xa0xa0x', 'xxa0xa0xa0xa0x', 'xa0xxxxx', 'xa0xa0xa0xa0xa0x', 'xa0xa0xa0xa0x']" in list:
            key = key + "4"
        elif "['xxxxx', 'xxa0xa0xa0xa0', 'xa0xxxx', 'xa0xa0xa0xa0x', 'xxxxx']" in list:
            key = key + "5"
        else : 
            return "ERROR : unknown combinaison"  
    return key
    

def GetFlag(key):
    data = requests.get('http://challenges.ringzer0team.com:10119/?r=' + key)
    new_tree = html.fromstring(data.content)
    flag = new_tree.xpath('/html/body/main/div/text()')[0]
    return flag

## Main
if __name__ == "__main__":
    msg = GetMessage()
    key = Decrypt(message=msg)
    flag = GetFlag(key=key)
    print(flag)