
#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
    result = ""

    for i in range(len(text)):

        char = text[i]
        # Encrypt uppercase characters
        if(char.isalpha()):
            if (char.isupper()):
                result += chr((ord(char) + s - 65) % 26 + 65)
            else:
                if (char.islower()):
                    result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result+=char
    return result

def decrypt(text,s):
    result=""
    for i in range(len(text)):

        char = text[i]

        if(char.isalpha()):
            if (char.isupper()):
                result += chr((ord(char) - s - 65) % 26 + 65)
            else:
                if (char.islower()):
                    result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result+=char
    return result


print(encrypt("I am a man",3))
print(decrypt("L dp d pdq",3))


    # traverse text


"""#check the above function
text = "ATTACKATONCE"
s = 3
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))
"""