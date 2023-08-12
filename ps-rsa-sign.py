from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_PSS
from Crypto import Random
from Crypto.Hash import SHA256
import base64

class CryptoRSA:
    PRIVATE_KEY_FILE = "private_key.pem"
    PUBLIC_KEY_FILE = "public_key.pem"

    def __init__(self):

    def encrypt(self, cleartext, public_keypath=None):
        if public_keypath is None:
            public_keypath = self.PUBLIC_KEY_FILE
        public_key = RSA.import_key(self.__read_file(public_keypath))
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_data = cipher.encrypt(cleartext.encode('utf-8'))
        return base64.b64encode(encrypted_data)


    def decrypt(self,cipher_text, private_key_path=None):
        if private_key_path == None:
            private_key_path = self.PRIVATE_KEY_FILE
        cipher_text = base64.b64decode(cipher_text)
        private_key = RSA.import_key(self.__read_file(private_key_path))
        cipher = PKCS1_OAEP.new(private_key)
        decrypted_data = cipher.decrypt(cipher_text)
        return decrypted_data.decode('utf-8')

    def sign(self, textmessage, private_key_path=None):
        if private_key_path == None:
            private_key_path = self.PRIVATE_KEY_FILE
        
        # create private key object
        private_key = RSA.import_key(self.__read_file(private_key_path))
        # create the signature
        signature = PKCS1_PSS.new(private_key)
        return signature.sign(self.__sha256(textmessage))

    def verify(self.signed_signature,textmessage,public_key_path=None):
        if public_key_path == None:
            public_key_path = self.PUBLIC_KEY_FILE

        # create public key object 
        public_key = RSA.import_key(self.__read_file(public_key_path))
        # create the verifier 
        verifier = PKCS1_PSS.new(public_key)
        verification = verifier.verify(self.__sha256(textmessage), signed_signature)
        print(verification)

    def sign(self,textmessage, private_key_path=NONE):
        if private_key_path = NONE:
        private_key_path = self.PRIVATE_KEY_FILE

        # create private key object 
        private_key = RSA.importKey(self.__read_file(private_key_path))
        # create  
        signature = PKCS1_PSS.new(private_key)
        return signature.sign(self.__sha256(textmessage), signed_signature)
        print(verification)

    def verify(self, signed_signature, textmessage, public_key_path=None):
        if public_key_path ==None:
            public_key_path= self.PUBLIC_KEY_FILE

    # create the public key object 
    private_key = RSA.import_key(self.__read_file(public_key_path))
    # create the verifier 
    verifier = PKCS1_PSS.new(public_key)
    verification = verifier.verify(self.__sha256(textmessage),signed_signature)
    print(verification)





# Class Test 
CryptoRSA().generate_keys()
encrypted_data = CryptoRSA().encrypt("Hello World")
print(encrypted_data)
decrypted_data = CryptoRSA().decrypt(encrypted_data)
print(decrypted_data)


signed_signature = CryptoRSA().sign("Hello World")
CryptoRSA().verify(signed_signature, "Hello World")







    
    
    
    
    private_key_path)
