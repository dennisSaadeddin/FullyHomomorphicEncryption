#!/usr/bin/env python3
import random
# Alice's Private/Public key pair, hard coded for simplicity
class PrivateKey():
    lambdA=73842165240981452554905699590449542088961757004289873177979834078905122488912
    mu=14623866067924162049758185900912462985982902037214491087468255488155427133263

class PublicKey():
    n=73842165240981452554905699590449542089513117936657660262085094366199671389241
    n2=5452665367476409421070096932669081750981552257584472365472731868555542659457163641469759175897028833132670904633495629764635203858875472896093430930556081
    g=73842165240981452554905699590449542089513117936657660262085094366199671389242

# Alice's Implementation of a fully homomorphic Paillier cipher
class FullyHomoCipher():
    def __init__(self, a1, b1):
        self.a = a1
        self.b = b1

    def expCalc(self, base,exponent,modulus):
        result = 1
        while exponent > 0:
            if exponent & 1 == 1:
                result = (result * base) % modulus
            exponent = exponent >> 1
            base = (base * base) % modulus
        return result

    def encrypt(self, pub, plain):
        while True:
            r = random.getrandbits(128)
            if r > 0 and r < pub.n:
                break
        x = self.expCalc(r, pub.n, pub.n2)
        cipher = (self.expCalc(pub.g, plain, pub.n2) * x) % pub.n2
        return cipher

    def decrypt(self, priv, pub, cipher):
        x = self.expCalc(cipher, priv.lambdA, pub.n2) - 1
        plain = ((x // pub.n) * priv.mu) % pub.n
        return plain

    def encrypt_message(self, pub, m):
        r = random.randrange(256, pub.n)
        b = self.encrypt(pub, r)
        a = (m-r) % pub.n
        self.a = a
        self.b = b

    def decrypt_message(self, priv, pub):
        val = (self.a + self.decrypt(priv, pub, self.b)) % pub.n
        return val

# Bob's encrypted calculation service
class BobsCalculationService():
    # Add two encrypted numbers
    def encrypted_add(self, pub, a, b):
        return a * b % pub.n2

    def sum (self, c1, c2, pub):
        a = (c1.a + c2.a) % pub.n
        b = self.encrypted_add(pub, c1.b, c2.b)
        c = FullyHomoCipher(a, b)
        return c

    # Multiply two encrypted numbers with a constant (Bob)
    def encrypted_mult(self, pub, a, n):
        return FullyHomoCipher(-1,-1).expCalc(a, n, pub.n2)

    def product(self, const, c1, pub):
        a = (c1.a * const) % pub.n
        b = self.encrypted_mult(pub, c1.b, const)
        c = FullyHomoCipher(a,b)
        return c

# THE SAAS EXAMPLE BEGINS HERE
if __name__ == '__main__':
    # Alice's Key Pair
    pub=PublicKey
    priv=PrivateKey

    # The top secret numbers Alice wants to use
    secretNumber1=5
    secretNumber2=10
    secretNumber3=6
    const=3

    # The Cipher objects Alice uses for encryption
    alice1 = FullyHomoCipher(-1,-1)
    alice2 = FullyHomoCipher(-1,-1)
    alice3 = FullyHomoCipher(-1,-1)

    # Alice performs encryption
    print ("SaaS Example:")
    print ("Alice wants to use Bob's calculation service to calculate ", secretNumber1,"+",secretNumber2)
    print ("She encrypts ", secretNumber1)
    alice1.encrypt_message(pub, secretNumber1)
    print ("...and the encrypted value is ",alice1.a,alice1.b)
    print ("She then encrypts ",secretNumber2)
    alice2.encrypt_message(pub, secretNumber2)
    print ("...and the encypted value is ",alice2.a,alice2.b)
    print ("")
    print ("Alice also wants to to multiply ",secretNumber3," with the constant ",const)
    print ("She encrypts ", secretNumber3)
    alice3.encrypt_message(pub, secretNumber3)
    print ("...and the encrypted value is ",alice3.a,alice3.b)
    print ("")
    print ("Then Alice sends the encrypted values to Bob along with her public key")
    print ("")

    # These are the encrypted values Alice sends to Bob
    encr1_a=alice1.a
    encr1_b=alice1.b
    encr2_a=alice2.a
    encr2_b=alice2.b
    encr3_a=alice3.a
    encr3_b=alice3.b

    # Bob's Cipher objects, initialized with Alice's encrypted numbers
    # Since Bob doesn't have the private key he can't decrypt the numbers
    bob1 = FullyHomoCipher(encr1_a,encr1_b)
    bob2 = FullyHomoCipher(encr2_a,encr2_b)
    bob3 = FullyHomoCipher(encr3_a,encr3_b)

    # Addition
    print ("Bob adds the two encrypted values without knowing what they are")
    result1=BobsCalculationService().sum(bob1, bob2, pub)
    print ("the encrypted result is ",result1.a,result1.b)

    # Multiplication with a constant
    print ("Bob multiplies the third encrypted value with the constant")
    result2=BobsCalculationService().product(const, bob3, pub)
    print ("the encrypted result is ",result2.a,result2.b)
    print ("")
    print ("Bob sends the encrypted results back to Alice")
    print ("Alice uses her private key to view the plain text results:")
    print ("Addition: ",result1.decrypt_message(priv, pub))
    print ("Multiplication: ",result2.decrypt_message(priv, pub))
