f = open('C:\\Users\\USER\\Documents\\Projects\\IRCat\\IRDB.ir','r')
big = open('C:\\Users\\USER\\Documents\\Projects\\IRCat\\big.ir','w')
print("I am reading")
protocols = ['type: raw\n','protocol: NEC\n','protocol: SIRC\n','protocol: MAX\n','protocol: Samsung32\n','protocol: RC6\n','protocol: RC5\n']
ircommands = ["name: VOL+\n","name:: VOL-\n","name: CH+\n","name: CH-","name: POWER\n","name: MUTE\n"]
i = 0
j = 0
content = f.readlines()
maxi = len(content) - 1
signalsP = []
signalsR = []
print(protocols)
writes = 0

class signalParsed:
    def _init_(self,name, parse, protocol, address, command):
        self.name = name
        self.parse = "type: parsed\n"
        self.protocol = protocol
        self.address = address
        self.command = command

class signalRaw:
    def _init_(self, name, raw, freq, dutyCycle, commandData):
        self.name = name
        self.raw = "type: raw\n"
        self.freq = freq
        self.dutyCycle = dutyCycle
        self.commandData = commandData          

def writerParsed():
    writes = 0
    for element in signalsP:
        if "name: NUKE\n" == str(element.name): break
        big.write('#\n')
        big.write(element.name)
        big.write(element.parse)
        big.write(element.protocol)
        big.write(element.address)
        big.write(element.command)
        writes = writes + 1
    return writes

def writerRaw():
    writes = 0
    for element in signalsR:
        if "name: NUKE\n" == str(element.name): break
        big.write('#\n')
        big.write(element.name)
        big.write(element.raw)
        big.write(element.freq)
        big.write(element.dutyCycle)
        big.write(element.commandData)
        writes = writes + 1
    return writes

##def signalValidationP(signal):
##    if 'name:' in signal.name and 'protocol: ' in signal.protocol and 'address: ' in signal.address and 'command: ' in signal.command: return
##    else: signalsP.pop()
##
##def signalValidationR(signal):
##    if 'name: ' in signal.name and 'frequency: ' in signal.freq and 'duty_cycle ' in signal.dutyCycle and 'data: ' in  signal.commandData: print('success') ;return
##    else: signalsR.pop(); print('fail!')
    
def createParsed(lo):
    a = lo+1
    if '#' not in content[lo] : raise SyntaxError('PARSED CREATION SHIT BROKE')
    b = signalParsed()
    b.name = str(content[a])
    b.parse = str(content[a+1])
    b.protocol = str(content[a+2])
    b.address = str(content[a+3])
    b.command = str(content[a+4])
    signalsP.append(b)
##    signalValidationP(b)
    
def createRaw(lo):
    a = lo+1
    if '#' not in content[lo]: raise SyntaxError('RAW CREATION SHIT BROKE')
    b = signalRaw()
    b.name = str(content[a])
    b.raw = str(content[a+1])
    b.freq = str(content[a+2])
    b.dutyCycle = str(content[a+3])
    b.commandData = str(content[a+4])
    signalsR.append(b)
##    signalValidationR(b)

def nukeGeneration(lo,hi):
    lo = lo + 1
    checki(lo)
    chunk = str(content[lo])
    check = chunk in ircommands
    if check == False :content[lo] = "name: NUKE\n"
    
def signalGeneration(lo,hi):
    checki(lo)
    x = lo
    while x <= hi:
        if "parsed" in content[x]: createParsed(lo); return
        if "raw" in content[x]: createRaw(lo); return
        x = x + 1
    else: raise SyntaxError('What type is it moron?' + str(content[lo+2]) + str(lo))


def getHigh(lowSpot):
    checki(lowSpot)
    count = False
    highSpot = lowSpot + 1
    while count != True:
        checki(highSpot)
        if "#" in content[highSpot]:
            if 'name' not in content[highSpot]: return highSpot
        highSpot = highSpot + 1
    

def dataValidation(lo,hi):
    nukeGeneration(lo,hi)
    x = 0
    x = hi-lo
    if x == 6:return True
    return False

def checkProtocol(lo, hi):
    while lo <= hi:
        if content[lo] in protocols: return True
        lo = lo+1
    return False

def generate():
    a = writerParsed()
    b = writerRaw()
    finishEarly(a,b)

def finishEarly(a, b):
    print('we out')
    print(a) ; print(b)
    print(i)
    print(len(content))
    f.close()
    big.close()
    quit()


def checki(chk):
    a = maxi-6
    if chk >= a: generate()

while f:
    c=False;v=False
    checki(i)
    if "#" in content[i]: j = getHigh(i);c = checkProtocol(i, j);v = dataValidation(i,j)
    if c == True:
        if v == True:signalGeneration(i,j);i=j
    i = i+1
    
    
print("I am no longer reading")


















