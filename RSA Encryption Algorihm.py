import random
import math




def is_prime(number):
    if number<2:
        return False
    for i in range(2,number//2+1):
        if number%i==0:
            return False
    return True

def generate_prime(min,max):
    prime= random.randint(min,max)
    while not is_prime(prime):
        prime=random.randint(min,max)
    return prime
def mod_inverse(e,phi):
    for d in range(3,phi):
        if (d*e)% phi==1:
            return d
    raise ValueError("Mod_inverse does not exist")
p,q=generate_prime(10,20),generate_prime(10,20)

while p==q:
    q= generate_prime(10,20)
n=p*q
phi_n= (p-1)*(q-1)
e= random.randint(3,phi_n-1)
while not math.gcd(e,phi_n)==1:
    e = random.randint(3, phi_n - 1)
d= mod_inverse(e,phi_n)
messages=input("Enter your message to Encrypt:")
print("Public key:",e)
print("Private key:",d)
print("Phi of n :",phi_n)
print("p",p)
print("q",q)




message_encoded= [ord(c) for c in messages]
ciphertext= [pow(c,e,n) for c in message_encoded]
print("Cyphertext in unicodes in list form:",ciphertext)

txt= "".join(chr(ch) for ch in ciphertext )
print("The cyphertext is:",txt)
message_decoded= [pow(ch,d,n) for ch in ciphertext]
print("Decoded cyphertext unicodes in list form:",message_decoded)
text= "".join(chr(ch)for ch in message_decoded)
print("The decoded version of your message which you input before:",text)

