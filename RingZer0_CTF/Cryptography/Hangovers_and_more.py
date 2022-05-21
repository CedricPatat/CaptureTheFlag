###############################################
#####     Hangovers and more : Bacon     ######
###############################################



BaconCipher = {"AAAAA":"A", "AAAAB":"B", "AAABA":"C", "AAABB":"D", "AABAA":"E",
        "AABAB":"F", "AABBA":"G", "AABBB":"H", "ABAAA":"I", "ABAAB":"J", "ABABA":"K", "ABABB":"L", 
        "ABBAA":"M", "ABBAB":"N", "ABBBA":"O", "ABBBB":"P", "BAAAA":"Q", "BAAAB":"R", "BAABA":"S",
        "BAABB":"T", "BABAA":"U", "BABAB":"V", "BABBA":"W", "BABBB":"X", "BBAAA":"Y", "BBAAB":"Z"}


## Functions 

def ComputeBacon(message:str):
    bacon = ""
    for i in message.replace(" ","").replace("!","").replace(".","").replace(",","").replace("'","") :
        if i == i.lower():
            bacon = bacon + 'A'
        else :
            bacon = bacon + 'B'
    return (bacon)

def DecodeBacon(bacon:str):
    decoded = ""
    for i in range(0, len(bacon), 5):
        if len(bacon[i:i+5]) == 5:
            decoded = decoded + BaconCipher[bacon[i:i+5]]
        else:
            decoded = decoded + '?'
    return decoded

## Main
if __name__ == "__main__":
    msg = "VoiCI unE SUpeRbe reCeTtE cONcontee pAR un GrouPe d'ArtistEs culinaiRe, dONT le BOn Gout et lE SeNs de LA cLasSe n'est limIteE qUe par LE nombre DE cAlOries qU'ils PeUVEnt Ingurgiter. Ces virtuoses de la friteuse vous presente ce petit clip plein de gout savoureux !!"
    print("")
    bcn = ComputeBacon(message = msg)
    asw = DecodeBacon(bacon = bcn)
    print("The solution is:")
    print(asw)
