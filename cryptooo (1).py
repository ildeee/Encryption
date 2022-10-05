def imp(words , sentence , CODE):
    ''' A function used in crypt

Arguements :
    words : list
        all letters in passcode
    sentence : list
        letters in sliced sentence
    CODE : list
        tuples can be appended

Returns :
    CODE : list
        list of tuples where tuple first is from words
        and second from sentence '''
    for keyLet , senLet in zip(words,sentence):
        CODE.append((keyLet , senLet))
    return CODE

def sort(x):
    '''Function used as a key for sorted

Arguements :
    x : tuple
        tuple with two items

Returns :
    x[0] : anything
        first element of tuple'''
    return x[0]
            
def crypt(sentence,passcode):
    '''Main procedure

Arguements :
    sentence : string or list
        sentence to be encrypted
    passcode : string
        passcode used for encryption

Returns :
    List : List
        encrypted message in a list form'''

    CODE=[]
    time =len(sentence)//len(passcode) + 1

    for i in range(time):
        slice = sentence[i*len(passcode):(i+1)*len(passcode)]
        imp(list(passcode) , slice , CODE)

    thing = sorted(CODE , key = sort)
    List = [str(i[1]) for i in thing]

    return List

def encrypt(sentence,passcode):
    ''' Encrypts the given sentence

Arguement :
    sentence : string
        sentence to be encrypted
    passcode : string
        password used for encrypting

Returns : string
        The encrypted message
        '''
    List = crypt(sentence,passcode)
    string = ''.join(List)
    return string

def decrypt(sentence , passcode):
    ''' Decrypts the given sentence
Arguement :
    sentence : string
        sentence to be encrypted
    passcode : string
        password used for encrypting

Returns : string
        The decrypted message
        '''

    senList = list(sentence)
    key = [ str(i) for i in range(len(senList))]
    jumKey = crypt(key , passcode)

    A = [(int(num),letter) for letter,num in zip(senList , jumKey)]
    final = sorted(A , key = sort)
    thing = ''.join([ i[1] for i in final])

    return thing
        

# SAMPLE -

sentence = 'Hello World , This should work'
passcode = 'Trial'

encryptMsg = encrypt(sentence,passcode)
decryptMsg = decrypt(encryptMsg,passcode)

print(encryptMsg)
print(decryptMsg)
           
