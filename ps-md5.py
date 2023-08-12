# message digest 5 
# outputs 128 bit (32 hex chars)
# do not use MD5 to store passwords!

from Crypto.Hash import MD5
message = "Hello World"           # var holding msg value
h = MD5.new()                     # created new MD5 class object 
h.update(message.encode('utf-8')) # update function creates the hash 
                            # and passes the input msg to be hashed
print(h.hexdigest())

# print:
# b10a8db164e0754105b7a99be72e3fe5



