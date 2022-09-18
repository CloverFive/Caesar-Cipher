
# Caesar Cipher

# Here is a sample run of the Caesar Cipher program encrypting a message:

# Do you wish to encrypt or decrypt a message?
# encrypt
# Enter your message:
# The sky above the port was the color of television, tuned to a dead channel.
# Enter the key number (1-52)
# 13
# Your translated text is:
# gur FxL noBIr Gur CBEG JnF Gur pByBE Bs GryrIvFvBA, GHArq GB n qrnq punAAry.

# Now run the program and decrypt the text that you just encrypted:

# Do you wish to encrypt or decrypt a message?
# decrypt
# Enter your message:
# gur FxL noBIr Gur CBEG JnF Gur pByBE Bs GryrIvFvBA, GHArq GB n qrnq punAAry.
# Enter the key number (1-52)
# 13
# Your translated text is:
# The sky above the port was the color of television, tuned to a dead channel.

# If you do not decrypt with the correct key, the text will not decrypt properly:

# Do you wish to encrypt or decrypt a message?
# decrypt
# Enter your message:
# gur FxL noBIr Gur CBEG JnF Gur pByBE Bs GryrIvFvBA, GHArq GB n qrnq punAAry.
# Enter the key number (1-52)
# 15
# Caesar Cipher 201
# Your translated text is:
# Rfc qiw YZmtc rfc nmpr uYq rfc amjmp md rcjctgqgml, rslcb rm Y bcYb afYllcj.



# Psuedo code!

# Ask player wether they want to encrypt or decrypt their message
player_responce = input('Do you wish to encrypt or decrypt a message?\n')

# Ask for the message
message = input('Enter your message:\n')

# Ask what their key is
player_key = int(input('Enter the key number (1-52)\n'))

# use a for loop too make a list of the alfabet by using ascii starting with 65 as A and 122 as z
alphabet = []
counter = 65

for i in range(26):
   alphabet.append(chr(counter + i))

counter = 97
for i in range(26):
   alphabet.append(chr(counter + i))

    
#print(len(alphabet))
#print('a' in alphabet)
    
def find_index(alphabet, letter, key):
    
    for i in range(len(alphabet)): 
        if alphabet[i] == letter:

            temp = i + key
            while temp > len(alphabet) or temp == len(alphabet):
                temp -= len(alphabet)
                #print(f'interating over the temps {temp}')
            return temp

def encrypt_letter(alphabet, letter, key):
    
    encrypted_index = find_index(alphabet, letter, key)
    # print(alphabet[encrypted_index])
    return alphabet[encrypted_index]

def encrypt_message(alphabet, message, key):

    encrypted_message = ''
    for i in message:

        if i in alphabet:
            # print(i, end = '')
            encrypted_message = encrypted_message + encrypt_letter(alphabet, i, key)
        
        else:
            
            encrypted_message = encrypted_message + i

                
    print(encrypted_message)
    return encrypted_message

def find_decrypt_index(alphabet, letter, key):
    
    for i in range(len(alphabet)): 
        if alphabet[i] == letter:

            index = i - key
            while index > len(alphabet) or index == len(alphabet):
                index += len(alphabet)
                #print(f'interating over the temps {temp}')
            return index

def decrypt_letter(alphabet, letter, key):
    
    decrypted_index = find_decrypt_index(alphabet, letter, key)
    # print(decrypted_index)
    # print(alphabet[encrypted_index])
    return alphabet[decrypted_index]

def decrypt_message(alphabet, message, key):

    decrypted_message = ''
    for i in message:

        if i in alphabet:
            # print(i, end = '')
            decrypted_message = decrypted_message + decrypt_letter(alphabet, i, key)
        
        else:
            
            decrypted_message = decrypted_message + i

                
    print(decrypted_message)
    return decrypted_message

if player_responce == 'encrypt':
    encrypt_message(alphabet, message, player_key)

else:
    decrypt_message(alphabet, message, player_key)
    


# the program should use a for loop, the key, and the list of the alfabet to make a diconarty 
# the diconary should be composd of the letters of the alghabet as the keys and the corosponding letters
#reference = {}
#for i in range(52):
    # it should also check if the key pluse the loop number is less than 122
#    if player_key + i < 122:
#        reference = alphabet[i]: alphabet[i + player_key]
    # if it wasn't then it should add the key pluse 65 instead
#    else:
#        reference = alphabet[i]: alphabet[i + 65]

# if the player chose to encrypt
# if player_responce == 'encrypt':
#     # then it will use the diconary as a reference to encryp  the message
#     encrypted_message = ''
#     print(' ')
#     for i in range(len(message)):
        
#         if message[i] != ' ':

#             if ord(message[i]) + int(player_key) > 122:
#                 temp = chr(ord(message[i]) + 6 + int(player_key))     
            
#             elif ord(message[i]) + int(player_key) == 90 or ord(message[i]) + int(player_key) > 90 and ord(message[i]) + int(player_key) < 96:
#                 temp = chr(96 + int(player_key))
                
                
#             else:
#                 temp = chr(ord(message[i]) + int(player_key))

#             # print(' ')
#             # print(i)
#             # print('temp')
#             # print(temp)
#             # print('encrypted_message + temp')
#             # print(encrypted_message + temp)
#             # print('encrypted_message')
#             # print(encrypted_message)
            
#             encrypted_message = encrypted_message + temp
#             # print('encrypted_message after')
#             # print(encrypted_message)
            

#         else:
#             encrypted_message = encrypted_message + ' '

#     # print('encrypted_message out of for loop')
#     print(encrypted_message)

# if the player chose to decrypt 
# else:
#     decrypted_message = ''
#     print(' ')
#     for i in range(len(message)):
        
#         if message[i] != ' ':

#             if ord(message[i]) - int(player_key) < 65:
#                 temp = chr(122 - int(player_key) - i)    
            
#             elif ord(message[i]) + int(player_key) == 97 or ord(message[i]) + int(player_key) > 97 and ord(message[i]) + int(player_key) < 91:
#                 temp = chr(90 + int(player_key))
                
                
#             else:
#                 temp = chr(ord(message[i]) - int(player_key))

            # print(' ')
            # print(i)
            # print('temp')
            # print(temp)
            # print('encrypted_message + temp')
            # print(encrypted_message + temp)
            # print('encrypted_message')
            # print(encrypted_message)
            
            # decrypted_message = decrypted_message + temp
            # print('encrypted_message after')
            # print(encrypted_message)
            

        # else:
        #     decrypted_message = decrypted_message + ' '

    # print('encrypted_message out of for loop')
    # print(decrypted_message)
    

# i = chr(65)
# print(i)