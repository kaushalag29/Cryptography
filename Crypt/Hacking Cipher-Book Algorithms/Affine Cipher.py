import pyperclip,sys,cryptomath
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]
^_`abcdefghijklmnopqrstuvwxyz{|}~"""
msg=raw_input('Enter The Message To Be Encrypted/Decrypted\n')
l=len(SYMBOLS)
while True:
    mode=raw_input('E-Encrypt/D-Decrypt\n')
    if(mode=='E' or mode=='D'):
        break
    else:
        print "INVALID"
key=input('Enter The Key\n')
def encrypt(ms,k):
    keya=k//l
    keyb=k%l
    trans=""
    if keya == 1 or keyb==0 or keya < 0 or keyb < 0 or keyb >l-1 or cryptomath.gcd(keya, l) != 1:
        sys.exit('The affine cipher becomes incredibly weak when key A is set to 1.Choose a different key.')
    for sym in ms:
        if sym in SYMBOLS:
            index=SYMBOLS.find(sym)
            trans+=SYMBOLS[(index * keya + keyb) %l]
        else:
            trans+=sym
    return trans
#bcd!jt!b!gvdl
#key=9313
def decrypt(ms,k):
    keya=k//l
    keyb=k%l
    trans=""
    if keya < 0 or keyb < 0 or keyb >l-1 or cryptomath.gcd(keya, l) != 1:
        sys.exit('The affine cipher cannot be decrypted.Choose a different key.')
    modInverseOfKeyA = cryptomath.findModInverse(keya, l)
    for sym in ms:
        if sym in SYMBOLS:
            index=SYMBOLS.find(sym)
            trans+= SYMBOLS[(index - keyb) * modInverseOfKeyA %l]
        else:
            trans+=sym
    return trans
if mode=='E':
    t=encrypt(msg,key)
    print t
else:
    t=decrypt(msg,key)
    print t




