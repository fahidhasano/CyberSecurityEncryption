"""def encrypt(tex,s):
    result= " "
    for i in range(len(tex)):
        char=tex[i]
        if(char.isupper()):
            result += chr((ord(char)+s-65)%26+65)
        else:
            result+= chr((ord(char)+s-97)%26+97)
    return result


print(encrypt("THISMESSAGEISTOPSECRET",3))
"""

"""x=36%26+9
print(x)"""
"""
g=(ord("B")+3-65)%26+65
i=(ord("B")+3-65)%26+65
h=chr(g)
print(g)
print(h)"""


"""
m=[[1,2,3,4],[5,6,9,7],[10,13,11,12]]
l=[]
for i in m:
    print()


"""



"""
print(m[0][3])"""
"""for i in m:
    print(i[0] ,i[1] ,i [2] ,i[3])"""



"""





nested_list = [[1, 2, 3, 4], [5, 6, 9, 7], [10, 13, 11, 12]]
flattened_list = []
for sublist in nested_list:
    for item in sublist:
        flattened_list.append(item)
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 9, 7, 10, 13, 11, 12]

"""





"""
m=[[1,2,3,4],[5,6,9,7],[10,13,11,12]]
l=[]
for i in m:
    for j in i:
        l.append(j)

print(l)


"""



"""
y=[1,2,3,4,5,6]

o=map(lambda x: x**2,y)
t=list(o)
print(t)

"""

"""
a=3
b=2
a,b=b,a




print("a=",a)
print("b=",b)

"""




def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')
            encrypted_char = chr((offset + shift) % 26 + ord('A'))
            result += encrypted_char
        else:
            result += char
    return result

print(encrypt("I am a man", 3))






























































