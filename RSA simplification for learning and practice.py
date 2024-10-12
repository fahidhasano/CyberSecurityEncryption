import  random
import math
def is_prime(number):
    if number<2:
        return False
    for i in range(2,number//2+1):
        if number%i==0:
            return False
    return True

def rand(min,max):
    prime= random.randint(min,max)
    while not is_prime(prime):
        prime = random.randint(min, max)
    return prime

p,q= rand(10,20),rand(10,20)
if p==q:
    q=rand(10,20)

n=p*q
phi_n=(p-1)*(q-1)
e=random.randint(3,phi_n-1)
while math.gcd(e,phi_n)!=1:
    e = random.randint(3, phi_n - 1)


def inverse(e,phi):
    for d in range(3,phi):
        if (d*e)%phi==1:
            return d
    raise ValueError

d= inverse(e,phi_n)

mess= input("Enter a text u want to encrypt:")
print("Public key:",e)
print("private key:",d)
print("p is",p)
print("q is ",q)
print("n is :",n)
encrypt= [ord(c) for c in mess]
cyph=[pow(c,e,n) for c in encrypt]
print(cyph)
decrypt= [pow(ch,d,n) for ch in cyph]
text= "".join(chr(ch) for ch in decrypt)
print("Decoded text is:",text)




