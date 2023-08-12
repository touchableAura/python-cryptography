# notes from :
#
# Practical Encryption and 
# Cryptograhy Using Python 



# one way hash function

# h = Hx # h is called digest or checksum
# H is the hashing algo, like MD% ir SHA=2
# hasing for generating checksums for a file 
# hasing passwords in the fatabase 
# ahsing for digital signatures 
# hashing for intrusion detection and malware 

# input can be anything
# output must be of fixed lengths 
# ex: SHA-256 is always 256 in length
# the output should be easy to compute 
# the output should not be reversible to its og state
# Hx = Hy (collision resistant)

# message digest  - MD5
# output of MD5 is 128 bit (32 hex chars)
# do not use MD5 to store passwords 


# checksum
# ensures integrity
# lets you know if someone tampered with file 
# how does this happen?
# before posting the file, the website admin will calc the hash of a file, and post the hash as an MD5 checksum
# you are not limited to MD5, you can use other algos
 

 # secure password methods 
 # do not use MD5 or SHA1
 # use SHA2 or SHA3 
 # user salt against password brute-force attacks 

# HMAC (MD5 and SHA1)
# use MD5 hash for integrity
# use a key to compute another hash for the authenition 

# MD5 outputs 128 bits and is not for password 
# Secure Hash Algorithm SHA2, SHA3, and SHA512
# HMAC - Authenticity and Integrity 
# Long & Complex passwords between 12 and 18 chars long 


# symmetric encryption
# using other methods: like phone and clouds \
# help to add layers (incase email or web had issues)

# block and stream: symmetric encryption types

# block ciphers
# encrypts in fixed block sizes 
# used in predictable sizes (ex: files)
# algorithims: AES
# AES: block size of 128bit and supports 3 block sizes
#      128, 192, 256 bits
# 3DES: 168 bits, block 64 bits
# DES: 56 bit key, block 64 bits
# Blowfish 
# Twofish 


# stream cipher 
# encrypts each bit/ byte
# used in unpredicatable sizes (ex: video streaming)
# algorithms: RC4 (key: 40 - 2048 bits)

# AES Principals 
# key char



# cryptography in practice 

# digital signatures 
# certificates have public key and other important info
# certificate authorities: create, validate, revoke
# root > intermediate > child > servers
# you will probably only see the root 

# certificate types
# self-signed 
# wildcard:
#
# ethicalhackingblog.compile

# TLS 
# public key, private key, certificates, + more

# browser sends a request for a secuer session to the server
# https request and ssl certs are symmetric encryption
# certificate (RSA Pubk), RSA Pubk(AESk)
# Symmetric Encryption Communication 

# on command prompt:
# sslscan https://ethicalhackingblog.com
# returns SSL certification information 


# practical mail encryption 
# sign > mailvelope(-> gmail, yahoo, outlook) -> encrypt 

# practical email signature 
# 



