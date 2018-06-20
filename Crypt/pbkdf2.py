#!/usr/bin/env python3
import passlib.utils.pbkdf2
import binascii
password=input("Enter your password\n")
salt=input("Enter your salt\n")
iteration=input('Enter c\n')
iteration=int(iteration)
dk_len=input("Enter dk_len\n")
dk_len=int(dk_len)
hash=passlib.utils.pbkdf2.pbkdf2(password,salt,iteration,keylen=dk_len,prf='hmac-sha256')
print(binascii.hexlify(hash))

