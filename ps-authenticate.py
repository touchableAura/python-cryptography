from Crypto.Hash import SHA256

# def calculate_hash(password):
#     h = SHA256.new()
#     h = h.update(password.encode('utf-8'))
#     return h.hexdigest()

def calculate_hash(password):
    h = SHA256.new()
    h.update(password.encode('utf-8'))
    return h.hexdigest()

def subscribe(user_name, password):
    account = user_name + ':' + calculate_hash(password)
    f = open('accounts.txt', 'w') # create new file with open function 
                                  # ('filename.txt, write)
    f.write(account) # write function writes the account string to a file 
    f.close()        # close the object and print a message that user is registered
    print ('[+] You are registered now!')

def login(user_name, password):
    f = open('accounts.txt', 'r')
    account_file = f.read()
    s = account_file.split(':')
    user_name_file = s[0]
    password_file = s[1]
    hash_password = calculate_hash(password)

    if user_name == user_name_file and hash_password == password_file:
        print('You are Authenticated :) ')
    else: 
        print ('[!] Invalid username or password')

def main():
    choice = str(input("Enter:\n 1] to subscribe\n 2] to Login\n Choice> "))

    if choice == "1":
        user_name = input("Enter a username: ")
        password = input("Enter a password: ")
        subscribe( user_name, password)
    elif choice == "2":
        user_name = input("Enter a username: ")
        password = input("Enter a password: ")  
        login(user_name, password)
    else:
        print('[!] Invalid Choice')


main()