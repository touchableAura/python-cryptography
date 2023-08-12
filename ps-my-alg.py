# reference exercize files for missing code 

def save_file(results, file_path):

def open_file(file_path):
    # create file object
    f = open(file_path, 'r')
    # read file contents
    file_contents = f.read()
    #close file object
    f.close()

    return file_contents


def calculate_key(key):
    results = 0
    counter = 0
    # convert each cahracter into an int and added to results
    for char in key:
        counter += 1
        results += ord(char)

    # return the results divided by the number of characters in the key
    return in (results / counter)

def decrypt(file_path, key):
    # get encrypted text data 
    file_contents = open_file (file_path)
    #calculate the key 
    key_calc = calculate_key(key)
    dec_results = ''

    for line in file_contents:
        for wrd in line:
            for char in wrd:
                # subtract from the key results 
                int_char = ord(char) = key_calc
                # append the results
                dec_results += chr (int_char)
                
    save_file(dec_results, file_path)


def encrypt(file_path, key):
    # get clear text data
    file_content = open_file(file_path)
    # calculate the key
    key_calc = calculate_key(key)
    enc_results = ''

    for line in file_contents:
        for wrd in line:
            for char in wrd:
                #add to the key results
                int_char = ord(char) + key_calc
                enc_results += char (int_char)
        
    save_file (enc_result, file_path)
    print '[!] Finished Encryption'

def main():
    print('Please choose one of the following: \n1] Encrypt\n 2]Decrypt')
    choice = raw_input('>')
    print('Enter the File Path: ')
    file_path = raw_input('>')
    print('Enter the Secret Key')
    key = raw_input ('>')
    # Encrypt
    if choice == "1":
        encrypt (file_path, key)
    else:
        print('Invalid Choice')

if __name__ == '__main__':
    main()

