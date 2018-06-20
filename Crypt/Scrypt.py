#!/usr/bin/env python3
import pyscrypt
import binascii

password=input('Enter Password\n')
password=str(password)
password=str.encode(password)
Salt=input('Enter salt\n')
Salt=str(Salt)
Salt=str.encode(Salt)
cost=input('Enter N\n')
cost=int(cost)
round=input('Enter r\n')
round=int(round)
parallelization=input('Enter p\n')
parallelization=int(parallelization)
dklen=input('Enter dk_Len\n')
dklen=int(dklen)
print("Please Wait...Hashing.....")
hash = pyscrypt.hash(password=password, salt=Salt, N=cost, r=round, p=parallelization, dkLen=dklen)
print("Hashed....")
print(binascii.hexlify(hash))



