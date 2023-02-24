#Caesar Cypher
def encryptCaesar(plaintext):

    #you must also initialize ciphertext as an empty string
    ciphertext = ""

    #let's assume only lowercase letters can be encrypted
    #so we convert plaintext to all lowercase letters just in case
    plaintext = plaintext.lower()

    alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    listSize = len(alphabetList)
    print('size of alphabetList= ', listSize)

    for letter in plaintext:
        print(letter)
        if( letter == ' ' or letter == '1' or letter == '2' or 
            letter == '3' or letter == '4' or letter == '5' or 
            letter == '6' or letter == '7' or letter == '8' or
            letter == '9' or letter == '0'):
            indexLetter = letter
            print('none array char detected: ')
            ciphertext = ciphertext + indexLetter
            print(ciphertext)
        else:
            #let's find the position of the letter in our alphabetList array
            indexLetter = alphabetList.index(letter)
            #a good debuggin tool in Python is to print so you can see what you just did
            print('indexLetter= ', indexLetter)

            #now let's do the shift by 3 modulo total number of letters
            newIndex = (indexLetter + 3)%listSize
            print('newIndex= ', newIndex)

            #now we go to the alphabetList and find which letter is in the newIndex position
            encryptedLetter = alphabetList[newIndex]
            print(encryptedLetter)

            #now we append the encrypted letter to the ciphertext
            ciphertext = ciphertext + encryptedLetter
            print(ciphertext)

    #after we loop through all the letters, we return the ciphertext to the main program 
    return ciphertext

def decryptCaesar(ciphertext):
    
    #you must also initialize plaintext as an empty string
    plaintext = ""

    #let's assume only lowercase letters can be encrypted
    #so we convert plaintext to all lowercase letters just in case
    ciphertext = ciphertext.lower()

    alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    listSize = len(alphabetList)
    print('size of alphabetList= ', listSize)

    for letter in ciphertext:
        print(letter)
        if( letter == ' ' or letter == '1' or letter == '2' or 
            letter == '3' or letter == '4' or letter == '5' or 
            letter == '6' or letter == '7' or letter == '8' or
            letter == '9' or letter == '0'):
            indexLetter = letter
            print('none array char detected: ')
            plaintext = plaintext + indexLetter
            print(plaintext)
        else:
            #let's find the position of the letter in our alphabetList array
            indexLetter = alphabetList.index(letter)
            #a good debuggin tool in Python is to print so you can see what you just did
            print('indexLetter= ', indexLetter)

            #now let's do the shift by 3 modulo total number of letters
            newIndex = (indexLetter - 3)%listSize
            print('newIndex= ', newIndex)

            #now we go to the alphabetList and find which letter is in the newIndex position
            encryptedLetter = alphabetList[newIndex]
            print(encryptedLetter)

            #now we append the encrypted letter to the plaintext
            plaintext = plaintext + encryptedLetter
            print(plaintext)

    #after we loop through all the letters, we return the plaintext to the main program 
    return plaintext

#ROT13 encryption
def ROT13(message):
    
    #you must also initialize ciphertext as an empty string
    ciphertext = ""

    #let's assume only lowercase letters can be encrypted
    #so we convert message to all lowercase letters just in case
    message = message.lower()

    alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    listSize = len(alphabetList)
    print('size of alphabetList= ', listSize)

    for letter in message:
        print(letter)
        if( letter == ' ' or letter == '1' or letter == '2' or 
            letter == '3' or letter == '4' or letter == '5' or 
            letter == '6' or letter == '7' or letter == '8' or
            letter == '9' or letter == '0'):
            indexLetter = letter
            print('none array char detected: ')
            ciphertext = ciphertext + indexLetter
            print(ciphertext)
        else:
            #let's find the position of the letter in our alphabetList array
            indexLetter = alphabetList.index(letter)
            #a good debuggin tool in Python is to print so you can see what you just did
            print('indexLetter= ', indexLetter)

            #now let's do the shift by 3 modulo total number of letters
            newIndex = (indexLetter + 13)%listSize
            print('newIndex= ', newIndex)

            #now we go to the alphabetList and find which letter is in the newIndex position
            encryptedLetter = alphabetList[newIndex]
            print(encryptedLetter)

            #now we append the encrypted letter to the ciphertext
            ciphertext = ciphertext + encryptedLetter
            print(ciphertext)

    #after we loop through all the letters, we return the ciphertext to the main program 
    return ciphertext

#Substitution Box (S-Box)
def sBox(plaintext):
    ##here you should add your code
    ciphertext = ""
    return ciphertext

def inv_sBox(ciphertext):
    ##here you should add your code
    plaintext = ""
    return plaintext

        
############# testing #########
#call the function to encryp here to test (or in your client and server program
phrase = "College"
encrypted = encryptCaesar(phrase)
final = decryptCaesar(encrypted)

#plaintext = "xray"
#ciphertext = encryptCaesar(plaintext)
#print("ciphertext is: ", ciphertext)




    


     

