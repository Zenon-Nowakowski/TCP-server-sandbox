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
    #for loop of plaintext
    for letter in plaintext:
        print(letter)
        #if statement to catch none letter entries 
        if( letter == ' ' or letter == '1' or letter == '2' or 
            letter == '3' or letter == '4' or letter == '5' or 
            letter == '6' or letter == '7' or letter == '8' or
            letter == '9' or letter == '0'):
            print('none array char detected: ')
            #translate none letter entry as 1-1
            ciphertext = ciphertext + letter
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
    #ciphertext loop
    for letter in ciphertext:
        #if statement to catch none letter entries 
        if( letter == ' ' or letter == '1' or letter == '2' or 
            letter == '3' or letter == '4' or letter == '5' or 
            letter == '6' or letter == '7' or letter == '8' or
            letter == '9' or letter == '0'):
            print('none array char detected: ')
            #translate none letter entry as 1-1
            plaintext = plaintext + letter
            print(plaintext)
        else:
            #let's find the position of the letter in our alphabetList array
            indexLetter = alphabetList.index(letter)
            #a good debuggin tool in Python is to print so you can see what you just did
            print('indexLetter= ', indexLetter)

            #now let's do the shift by 3 again modulo total number of letters, and get the plaintext
            newIndex = (indexLetter - 3)%listSize
            print('newIndex= ', newIndex)

            #now we go to the alphabetList and find which letter is in the newIndex position
            encryptedLetter = alphabetList[newIndex]
            print(encryptedLetter)

            #now we append the plaintext letter to the plaintext
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
        #if statement to catch none letter entries 
        if( letter == ' ' or letter == '1' or letter == '2' or 
            letter == '3' or letter == '4' or letter == '5' or 
            letter == '6' or letter == '7' or letter == '8' or
            letter == '9' or letter == '0'):
            print('none array char detected: ')
            #translate none letter entry as 1-1
            ciphertext = ciphertext + letter
            print(ciphertext)
        else:
            #let's find the position of the letter in our alphabetList array
            indexLetter = alphabetList.index(letter)
            #a good debuggin tool in Python is to print so you can see what you just did
            print('indexLetter= ', indexLetter)

            #now let's do the shift by 13 modulo total number of letters
            newIndex = (indexLetter + 13)%listSize
            print('newIndex= ', newIndex)

            #now we go to the alphabetList and find which letter is in the newIndex position
            encryptedLetter = alphabetList[newIndex]
            print(encryptedLetter)

            #now we append the encrypted letter to the ciphertext
            ciphertext = ciphertext + encryptedLetter
            print(ciphertext)

    #after we loop through all the letters, we return the ciphertext to the main program, this is also the decrypt algorithm so naming
    #is a little misleading
    return ciphertext

#Substitution Box (S-Box)
def sBox(plaintext):
    plaintext = plaintext.lower()
    ciphertext = ""
    #sboxarr is the array full of the encrypt values
    sboxarr = ['c','l','i','m','h','x','e','z','s','t','b','p','v','o','u','d','r','y','j','q','k','a','g','w','n','f']
    alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in plaintext:
        print(letter)
        #if statement to catch none letter entries 
        if( letter == ' ' or letter == '1' or letter == '2' or 
            letter == '3' or letter == '4' or letter == '5' or 
            letter == '6' or letter == '7' or letter == '8' or
            letter == '9' or letter == '0'):
            print('none array char detected: ')
            #translate none letter entry as 1-1
        else:
            #this encryption is fairly straight forward, all we need to do is:
            #find the index, or letter number, of the plaintext messages letter
            index = alphabetList.index(letter)
            #find that same index in the encryption array (sboxarr)
            #and input that letter found in the sboxarr array into a new char value
            encryptedLetter = sboxarr[index]
            print(encryptedLetter)
            #then we input that new encrypted letter into the soon-to-be returned cypher text
            ciphertext = ciphertext + encryptedLetter


    return ciphertext

def inv_sBox(ciphertext):
    ciphertext = ciphertext.lower()
    plaintext = ""
    sboxarr = ['c','l','i','m','h','x','e','z','s','t','b','p','v','o','u','d','r','y','j','q','k','a','g','w','n','f']
    alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in ciphertext:
        print(letter)
        #if statement to catch none letter entries 
        if( letter == ' ' or letter == '1' or letter == '2' or 
            letter == '3' or letter == '4' or letter == '5' or 
            letter == '6' or letter == '7' or letter == '8' or
            letter == '9' or letter == '0'):
            print('none array char detected: ')
            #translate none letter entry as 1-1
            print('none array char detected: ')
            plaintext = plaintext + letter
            print(plaintext)
        else:
            #in order to decrypt the sBox algorithm all we need to do: 
            #find the index of the sboxarr array for the letter in the encrypted message
            index = sboxarr.index(letter)
            #input that index into the alphabetlist array
            #and input it into a temp char container
            dencryptedLetter = alphabetList[index]
            print(dencryptedLetter)
            #finally, input that stored char value into plaintext, slowly revealing the encrypted message
            plaintext = plaintext + dencryptedLetter


    return plaintext

        
############# testing #########
#call the function to encryp here to test (or in your client and server program
#est sBox
# phrase = "csci458" 
# ciphertext = sBox(phrase)
# print("ciphertext is: ", ciphertext)
# plain = inv_sBox(ciphertext)
# print("plaintext is: ", plain)

#dest Caesar
# phrase = "Zoo"
# encrypted = encryptCaesar(phrase)
# final = decryptCaesar(encrypted)

#test ROT13
# phrase = "College station"
# encrypt = ROT13(phrase)
# final = ROT13(encrypt)



    


     

