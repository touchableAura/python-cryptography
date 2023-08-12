from Crypto.Cipher import AES 
from Crypto.Hash import MD5   # ensure bits are 128 long
from Crypto import Random
import base64

class AESCrypto:

    def md5_hash(self, text):
        h = MD5.new()
        h.update(text.encode('utf-8'))
        return h.hexdigest()

    def __init__(self, key): 
        # key size is 128 bits
        self.key = self.md5_hash(key).encode('utf-8')  # Encode the key to bytes

    def encrypt(self, cleartext):
        # block size should be equal to 128 bits
        Block_Size = 16
        pad = lambda s: s + (Block_Size - len(s) % Block_Size) * b'\0'
        cleartext_blocks = pad(cleartext.encode('utf-8'))  # Encode the cleartext to bytes

        # create a random IV
        iv = Random.new().read(Block_Size)   # secure random funtion from crypto library
        crypto = AES.new(self.key, AES.MODE_CBC, iv) # create AES object
        return base64.b64encode(iv + crypto.encrypt(cleartext_blocks))
        # encoding adds complixity for hackers to have to figure out 
        
    def decrypt(self, enctext):
        enctext = base64.b64decode(enctext) # first: decode the encoded results
        iv = enctext[:16] # next the iv bc it is in the first 16 bytes 
        crypto = AES.new(self.key, AES.MODE_CBC, iv) # initialize the AES object to prepare for the decryption process
        # unpad the blocks before decrypting
        unpad = lambda s: s.rstrip(b'\0')
        return unpad(crypto.decrypt(enctext[16:])).decode('utf-8')


aes = AESCrypto('password123')
encrypted = aes.encrypt('Hello World')
print(encrypted)
decrypted = aes.decrypt(encrypted)
print(decrypted)

## Secure AES Cipher should be working 
# b'Ypk63e8REFoqdFrBXPOoIw3a1yDFQEnSO2w7/VJZQMI='
# Hello World















# from Crypto.Cipher import AES 
# from Crypto.Hash import MD5
# from Crypto import Random
# import base64

# class AESCrypto:

#     def md5_hash(self, text):
#         h = MD5.new()
#         h.update(text.encode('utf-8'))
#         return h.hexdigest()

#     def __init__(self,key):
#         # key size is 128 bits
#         self.key = self.md5_hash(key)

#     # def encrypt(self, cleartext):
#     #     # block size should be equal to 128 bits
#     #     Block_Size = 16
#     #     # pad = lambda s: a + (Block_Size - len (s) % Block_Size) * chr 
#     #     pad = lambda s: s + (Block_Size - len(s) % Block_Size) * b'\0'

#     #     (Block_Size - len (s) % Block_Size)
#     #     cleartext_blocks = pad(cleartext)

#     def encrypt(self, cleartext):
#         # block size should be equal to 128 bits
#         Block_Size = 16
#         pad = lambda s: s + (Block_Size - len(s) % Block_Size) * b'\0'
#         cleartext_blocks = pad(cleartext.encode('utf-8'))

#         # create a random IV
#         iv = Random.new().read(Block_Size)
#         crypto = AES.new(self.key, AES.MODE_CBC, iv)
#         return base64.b64encode(iv + crypto.encrypt(cleartext_blocks))
        
#     def decrypt(self,enctext):
#         enctext = base64.b64decode(enctext)
#         iv = enctext[:16]
#         crypto = AES.new(self.key,AES.MODE_CBC,iv)
#         # unpad the blocks before decrypting 
#         unpad = lambda s : s[0:-ord(s[-1])]
#         return unpad(crypto.decrypt(enctext[16:]))

# aes = AESCrypto('password123')
# encrypted = aes.encrypt('Hello World')
# print(encrypted)
# decrypted = aes.decrypt(encrypted)
# print (decrypted)
