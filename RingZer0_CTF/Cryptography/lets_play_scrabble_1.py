########################################
#####     Let's Play Scrabble     ######
########################################

"""
This cryptographic method consists in mixing the letters of an alphabet 
using a keyword in order to obtain an encryption key. The message is then 
encoded with the encryption key. This script is used to encode and decode 
a message knowing, or not, the encryption key.
"""

## Loading libraries
from english_words import english_words_alpha_set

digits = {"ZERO":0, "ONE":1, "TWO":2, "THREE":3, "FOUR":4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9}


## Functions

def GetKey(keyword:str, alphabet:str):
    key = list(alphabet.upper())
    for i in keyword:
        key = key[key.index(i)+1:] + [i] + key[:key.index(i)]
    return key

def EncryptMessage(message:str, keyword:str, alphabet:str):
    key = GetKey(keyword, alphabet)
    encrypted =""
    for i in message.upper() :
        encrypted = encrypted + key[alphabet.index(i)]
        key = key[key.index(i)+1:] + [i] + key[:key.index(i)]
    return encrypted

def DecryptMessage(input:str, keyword:str, alphabet:str):
    key = GetKey(keyword, alphabet)
    message = ""
    for i in input.upper():
        char = alphabet[key.index(i)]
        message = message + char
        key = key[key.index(char)+1:] + [char] + key[:key.index(char)]
    return message

def BruteForceEncrypted(input:str, alphabet:str, clue:str):
    for keyword in english_words_alpha_set:
        keyword = keyword.upper().replace("&","").replace(".", "")
        decrypted = DecryptMessage(input,keyword, alphabet)
        if clue in decrypted:
            print(f"Keyword is : {keyword}")
            return decrypted
    return "ANY KEYWORD MATCHING"
    
def ConvertAnswer(answer:str):
    answer = answer.replace("FLAG", "  FLAG").replace("HYPHEN",'-')
    for digit in digits.keys():
        answer = answer.replace(digit, str(digits[digit]))
    return answer


## Main

if __name__ == "__main__":
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    input = "TQSBAODTTABMRUHDKNVUORAKATOZLFBFDWPHQLANSZIKOSEDESXZLDYEUBJRROAVZRBSLWESCEGGOCEMLFMAHAYSRNMCXATHGNZQBCLSCEMKIVELCRXCJTBBTXGBRNDQTLJMLUOEQWTHWVBAZHAABXPZELKBNWSNCZLNSBELFFKDLVFWOWNDQWMLFXEQWAQOQRIAAVSXAADYEUUAMTHYLSCVILMNE"
    decrypted = BruteForceEncrypted(input = input, alphabet=alphabet, clue="FLAGHYPHEN")
    decrypted = ConvertAnswer(answer=decrypted)
    print(f"Flag is : {decrypted.split(' ')[2]}")
