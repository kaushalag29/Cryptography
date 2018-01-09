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
    if(key>=1 and key<=26):
        break
    else:
        print "INVALID"
trans=""
text=text.upper()
for ch in text:
    ascii=ord(ch)
    if ascii>=65 and ascii<=90:
        if mode=='E':
            ascii+=key
            if ascii>90:
                ascii-=26
            trans+=chr(ascii)
        else:
            ascii-=key
            if ascii<65:
                ascii+=26
            trans+=chr(ascii)
    else:
        trans+=chr(ascii)
print trans
pyperclip.copy(trans)
            
        
        
    
