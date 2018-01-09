import random,pyperclip,sys
msg=raw_input('Enter The Message To Be Hacked\n')
print "Hacking..."
l=len(msg)
msg=msg.upper()
def decrypt(msgs,keys):
    trans=""
    lo=len(msgs)
    list=[0]*lo
    d=lo/keys
    rem=lo%keys
    if rem==0:
        p=d
    else:
        p=d+1
    c=0
    while c<p:
        pos=c
        s=0
        while pos<lo:
            if list[pos]==0:
                list[pos]=1
                trans+=msgs[pos]
            if s<rem:
                kp=d+1
            else:
                kp=d
            s+=1
            pos+=kp
        c+=1
    return trans

def store():
    fil=open("words.txt")
    words=[]
    for w in fil.read().split('\n'):
        words.append(w)
    fil.close()
    return words

lis=[]
lis=store()
nonletter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NON=nonletter.lower()+nonletter+'\t\n'+' '
def remov(msg):
    letter=[]
    for symbol in msg:
        if symbol==' ' or symbol=='.' or symbol=='?' or symbol=='!':
            letter.append(' ')
        elif symbol in NON:
            letter.append(symbol)
    return ''.join(letter)
key=1
while(key<l):
    dtext=""
    dtext=decrypt(msg,key)
    print str(key)+" "+str(l)
    print dtext
    orig=dtext
    dtext=remov(dtext)
    print dtext
    possible=[]
    possible=dtext.split()
    count=0
    pp=0
    for w in possible:
        if w in lis:
            count+=1
        pp+=1
    calc=float(count)/float(pp)
    calc=calc*100.0
    if calc>=75:
        print "Possible Hacked Cipher:\n"+str(orig)+"\n Key="+key
        pyperclip.copy(orig)
        print "Press C to continue else Press Q to quit"
        while True:
            ch=raw_input()
            if ch=='Q':
                sys.exit()
            elif ch=='C':
                break
            else:
                print "Invalid Choice.Please Re-enter."
    else:
        print str(count)+" "+str(pp)
        print "Trying...."
    key+=1
    
    
