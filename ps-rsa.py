from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
from Crypto.Hash import SHA256 
import base64

class CryptoRSA:
    PRIVATE_KEY_FILE = "private_key.pem"
    PUBLIC_KEY_FILE = "public_key.pem"

    def __init__(self):
        return
    
    #__double_underlined() functions 
    # are internal private functions that will not be calle outside this class
    def __save_file(self, contents, file_name):
        with open(file_name, 'wb') as f:  # Open in binary write mode
            f.write(contents)

    def __read_file(self, file_name):
        with open(file_name, 'rb') as f:  # Open in binary read mode
            contents = f.read()
        return contents

    def __generate_random(self): 
        return Random.new().read()

    def generate_keys(self):
        keys = RSA.generate(4096)
        private_key = keys.export_key('PEM')
        public_key = keys.publickey().export_key('PEM')
        self.__save_file(private_key, self.PRIVATE_KEY_FILE)
        self.__save_file(public_key, self.PUBLIC_KEY_FILE)
        print('Public and Private Keys; generated and saved successfully!')

    # def encrypt(self, cleatext, public_keypath=None):
    #     if(public_keypath==None):
    #         public_keypath = self.PUBLIC_KEY_FILE
    #     public_key = RSA.import_key(self.__read_file(public_keypath))
    #     cipher = PKCS1_OAEP.new(public_key)
    #     encrypted_data = cipher.encrypt(cleatext.encode('utf-8'))
    #     return base64.b64encode(encrypted_data.decode('utf-8'))

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
        
                



CryptoRSA().generate_keys()
encrypted_data = CryptoRSA().encrypt("Hello World")
print(encrypted_data)
decrypted_data = CryptoRSA().decrypt(encrypted_data)
print(decrypted_data)


# > py ps-rsa.py
# Public and Private Keys; generated and saved successfully!
# b'REsgfuJ1Dj7Fh2di7hgjNh4FZHB9ouPBbRmvW1mDGKJ10+ZeAQtCvht6M1YthT+vVatAXCzx55va78Dm7E/Gbuh9ls5qglDWswdHSiZ1pvn0fccxpQQolqt155vTeOCamJX2QQSp+/osv13nCpHM1cXcANilB5pT2Pb7I41YEVoixMiEtjV+3swrryF6dEobsY3/N+9rcxn/0/yWAhioLoFfoZNokSXkK/y9aj5BQijhj8seEi24z+JfX00ZrYW55bD5Ofy4Rg30aycvnQCc4oRk/pg5wuLCv5Ehebavc5/NhRVEAJ7d2OHPlPyJZjkZ65ig63O9g7hT2QZMWmuPKKzjJ2je+xrxg10jr0sgCSaLNw51ZBnTt2XK0LBLGAB92W7/McGkdEGrBCGTZXw3O8gXySxNi05TX/JD0IBlZBcuMun2xU2RVzzE/7l+D3QMsf6k1n0CLvZJykH8k/IxDuylvMD0FN+a2vXPcaWbSVs6QlM/ouhsIqoCmYcALCZlbxI0H8U0OnImGw76dAB5OhMvPbKweWOWlngKStlu8FJs/kXK7AehBLv/TE5OFlV+3Eso7k1CMzYGgv1mm4KTwzQziPqM7L4DJEIgC4J0HJSZ4yRKAW50Ij6XRE5WQGlrqmZDoHytnFtBtr4J1JcvfMKxijtivH+AM+gotoh5ZDU='
# Hello World



