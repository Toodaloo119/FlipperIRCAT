big = open('C:\\Users\\USER\\Documents\\Projects\\IRCat\\big.ir','r')
bb = open('C:\\Users\\USER\\Documents\\Projects\\IRCat\\baseBig.ir','w')
ircommands = ["VOL+","VOL-","CH+","CH-","POWER","MUTE"]
content = big.readlines()
i = 2

def generate(lo,hi):
   big.writelines(content[lo:hi:1])
   return

def getHigh(lowSpot):
    count = False
    highSpot = lowSpot + 1
    while count != True:
        if "#" in content[highSpot]: count = True
        else: highSpot = highSpot + 1
    return highSpot

def checkProtocol(lo, hi):
    chunk = content[lo:hi]
    check = any(item in ircommands for item in content[i])
    return check




while big:
    bb.writelines(content)
    if checkProtocol(i, j) is True:if checkProtocol(i, j) is True:
        i = i + 6
    elif content[i] == "":
        big.close()
        bb.close()
    else: 
    i = i + 1


            
