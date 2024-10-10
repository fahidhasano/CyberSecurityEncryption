#Most appropriate code is:

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
        prime = random.randint(min, max)
    return prime

def mod_inverse (e,phi):
    for d in range(3,phi):
        if (d*e) % phi !=1:
            return d
        raise ValueError("Mod_inverse does not exist!")
p=generate_prime(1000,50000)
q=generate_prime(1000,50000)

while p==q:
    q=generate_prime(1000,50000), generate_prime(1000,50000)
n =p*q
phi_n= (p-1)*(q-1)
e= random.randint(3,phi_n-1)
while math.gcd(e,phi_n)!=1:
    e = random.randint(3, phi_n - 1)
d= mod_inverse(e,phi_n)
message=input("Enter")

print ("Prime number P: ", p)
print ("Prime number q: ", q)
print ("Public Key: ", e)
print ("Private Key: ", d)
print ("n: ", n)
print ("Phi of n: ", phi_n, " Secret")
