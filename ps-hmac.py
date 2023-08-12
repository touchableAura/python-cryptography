from Crypto.Hash import HMAC

# password = 'secret'
# h = HMAC.new(password) # pass to new HMAC object
# h.update('Gus')        # create hash of the message 
# print(h.hexdigest())

password = 'secret'
password_bytes = password.encode('utf-8')  # Encode the password as bytes
h = HMAC.new(password_bytes)  # Pass the bytes to new HMAC object
h.update('Gus'.encode('utf-8'))  # Create hash of the message (also encoded as bytes)
print(h.hexdigest()) #print: 7e5091084739e61def86eb991768b1ff
