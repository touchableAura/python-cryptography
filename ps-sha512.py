# $ SHA-3 is considered the most secure hashing algorithm 

from Crypto.Hash import SHA512
message = "Hello World"            # var holding msg value
h = SHA512.new()                   # create new SHA class object
h.update(message.encode('utf-8'))  # update function creates the hash 
                            # and pass the input message to be hashed
print(h.hexdigest())

# prints: hex output of 512 bits 
# 2c74fd17edafd80e8447b0d46741ee243b7eb74dd2149a0ab1b9246fb30382f27e853d8585719e0e67cbda0daa8f51671064615d645ae27acb15bfb1447f459b