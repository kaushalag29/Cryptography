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
        
t=input()
while t>0:
    t-=1
    n=input()
    if(rabin(n)==True):
        print "YES"
    else:
        print "NO"
