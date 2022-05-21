#########################################
#####     Some martian message     ######
#########################################

"""

The objective of this script is to decode the Caesar cipher with a brute force method until 
a keyword is found. If no keyword is found, all solutions will be displayed to the user
"""

alphabet = { "A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9,
             "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17,
             "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25,
             "Z":26}


## Functions

def CaesarCipher(input:str, key:int):
    decoded = ""
    key_list = list(alphabet.keys())
    val_list = list(alphabet.values())
    for i in range(0,len(input)):
        position = val_list.index(alphabet[input[i].upper()]) + key
        if position > 25:
            position = position-26
        if input[i].lower() == input[i]:
            decoded = decoded + key_list[position]
        else:
            decoded = decoded + key_list[position].upper()
    return decoded

def BruteForceCaesar(input:str, key_word=""):
    solutions = []
    for i in range(1,27):
        decoded = CaesarCipher(input=input, key=i)
        if len(key_word) > 0:
            if key_word.upper() in decoded or key_word.lower() in decoded:
                print(f"The Caesar key is : {i}")
                return decoded
            else:
                solutions.append(decoded + '\n')
        else:
            solutions.append(decoded + '\n')
    return solutions

## Main

if __name__ == "__main__":
    answer = BruteForceCaesar(input="SYNTPrfneVfPbbyOhgAbgFrpher", key_word="FLAG")
    print("".join(answer))