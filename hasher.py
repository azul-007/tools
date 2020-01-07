#!ß/usr/bin/python3

import hashlib

#Author: Daniel Edwards
#Hashing user input with differing hash levels.

#MD5
hashvalue = input("Enter a string to hash: ")
hash1 = hashlib.md5()
hash1.update(hashvalue.encode())
print(hash1.hexdigest())


#SHA1
hash2 = hashlib.sha1()
hash2.update(hashvalue.encode())
print(hash2.hexdigest())


#SHA224
hash3 = hashlib.sha224()
hash3.update(hashvalue.encode())
print(hash3.hexdigest())


#SHA256
hash4 = hashlib.sha256()
hash4.update(hashvalue.encode())
print(hash4.hexdigest())


#SHA512
hash5 = hashlib.sha512()
hash5.update(hashvalue.encode())
print(hash5.hexdigest())