#
# SE578-Assignment #1
# Abhilasha Jayaswal
# knapsack.py
#
#This code implements knapsack cryptosystem
#
#Calculating modular inverse
def modInverse(a, b):
    a = a % b;
    for x in range(1, b):
        if ((a * x) % b == 1) :
            return x
    return 1

public_key = [18, 30, 7, 26];
n = 47;

#For part a given m=6
m = 6;
private_key = [None]*len(public_key);
for index in list(range(len(public_key))):
    private_key[index] = (public_key[index]*modInverse(m , n)) % n;
print "Private key: ", private_key;

#For part b given plaintext=1101

plaintext = [1, 1, 0, 1]
ciphertext=0;
if len(plaintext)==len(public_key):
    for index in list(range(len(plaintext))):
        if plaintext[index] == 1:
            ciphertext = ciphertext+public_key[index];
print "Ciphertext for the plaintext ", plaintext, "is ", ciphertext;



