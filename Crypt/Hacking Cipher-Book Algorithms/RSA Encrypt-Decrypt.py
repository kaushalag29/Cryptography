import random,sys
dbs=128
byte=256
while True:
    mode=raw_input('E-Encrypt/D-Decrypt\n')
    if(mode=='E' or mode=='D'):
        break
    else:
        print "INVALID"
while True:
    key=input('Enter Key\n')
    if(key>=0 and key>=dbs*8):
        break
    else:
        print "INVALID"
def getblockfromtext(msg):
    msb=list(msg.encode('ascii'))
    blockints=[]
    for blockstart in range(0,len(msb),dbs):
        blockint=0
        for i in range(blockstart,min(blockstart+dbs,len(msb))):
            blockint+=(ord(msb[i])*(byte**(i%dbs)))
        blockints.append(blockint)
    return blockints
def gettextfromblock(blockints,length):
    message=[]
    for block in blockints:
        blockmsg=[]
        for i in range(dbs-1,-1,-1):
            if len(message)+i<length:
                ascii=block//(byte**i)
                block=block%(byte**i)
                blockmsg.insert(0, chr(ascii))
        message.extend(blockmsg)
    return ''.join(message)

def encrypt(msg,n,e):
    l=len(msg)
    encblock=[]
    for block in getblockfromtext(msg):
        encblock.append(pow(block,e,n))
    for i in range(len(encblock)):
        encblock[i]=str(encblock[i])
    encryptcontent=','.join(encblock)
    return encryptcontent
def decrypt(msg,n,d,l):
    encblock=[]
    for block in msg.split(','):
        encblock.append(int(block))
    decblock=[]
    for block in encblock:
        decblock.append(pow(block,d,n))
    lis=[]
    lis=gettextfromblock(decblock,l)
    return lis    
if mode=='E':
    msg=raw_input('Enter message to be encrypted\n')
    n=input('Enter n\n')
    e=input('Enter e\n')
    text=encrypt(msg,n,e)
    print "Encrypted Text:"
    print text
else:
    msg=raw_input('Enter message to be decrypted\n')
    n=input('Enter n\n')
    d=input('Enter d\n')
    l=len(msg)
    text=decrypt(msg,n,d,l)
    print "Decrypted Text:"
    print text
