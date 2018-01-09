import pyperclip
text=raw_input('Enter The Text To Be Encrypted/Decrypted\n')
while True:
    mode=raw_input('E-Encrypt/D-Decrypt\n')
    if(mode=='E' or mode=='D'):
        break
    else:
        print "INVALID"
while True:
    key=input('Enter Key\n')
    if(key>=0 and key<len(text)):
        break
    else:
        print "INVALID"
trans=""
l=len(text)
text=text.upper()
if mode=='E':
    c=0
    while c<key:
        pos=c
        while pos<l:
            trans+=text[pos]
            pos+=key
        c+=1
    print trans
else:
    list=[0]*l
    d=l/key
    rem=l%key
    if rem==0:
        p=d
    else:
        p=d+1
    c=0
    while c<p:
        pos=c
        s=0
        while pos<l:
            if list[pos]==0:
                list[pos]=1
                trans+=text[pos]
            if s<rem:
                kp=d+1
            else:
                kp=d
            s+=1
            pos+=kp
        c+=1
print trans
pyperclip.copy(trans)
        
        
    
