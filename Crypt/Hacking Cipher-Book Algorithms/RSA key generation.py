import random,math
def rabin(num):
    if(num==2 or num==3):
        return True
    if(num<2 or num%2==0):
        return False
    s=num-1
    t=0
    while s%2==0:
        s=s//2
        t+=1
    trial=0
    while trial<6:
        a=random.randrange(2,num-1)
        v=pow(a,s,num)
        if v!=1:
            i=0
            while v!=num-1:
                if i==t-1:
                    return False
                else:
                    i+=1
                    v=(v**2)%num
        trial+=1
    return True
def findModInverse(a,m):
    if gcd(a,m)!=1:
        return None
    u1,u2,u3=1,0,a
    v1,v2,v3=0,1,m
    while v3!=0:
        q=u3//v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1%m
key=input('Enter Key Size\n')
def generate(key):
    while True:
        num=random.randrange(2**(key-1),2**key)
        if rabin(num)==True:
            return num
p=generate(key)
q=generate(key)
n=p*q
s=(p-1)*(q-1)
def gcd(a,b):
    while a!=0:
        a,b=b%a,a
    return b
while True:
    e=random.randrange(2**(key-1),2**key)
    if gcd(s,e)==1:
        break
d=findModInverse(e,s)
print "Public Key:"
print "n="+str(n)+"\n"+"e="+str(e)
print "Private Key:"
print "n="+str(n)+"\n"+"d="+str(d)


    
    
