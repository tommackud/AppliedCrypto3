#################################################################
# Generate a "Strong" prime (script below) p
# Pick a "base" which can really just be the number g=2
# Generate a PRIVATE random number, a, which shares no factors with p−1 (recipe below)
# Calculate the public exponent: A:=ga(modp).
# Publish your public key (triplet): p,g,A (DO NOT PUBLISH a!)
#################################################################

from Crypto.Util.number import *


def get_good_randy():
    value = 0
    rand = 0
    while value != 1:
        rand = getRandomRange(2, p-2)
        value = GCD(rand, p-1)
    return rand


# ALICE
p = getStrongPrime(512)
a = get_good_randy()
base = 2
A = pow(base, a, p)

# BOB
b = get_good_randy()
B = pow(base, b, p)
BobsK = pow(A, b, p)

# ALICE
AlicesK = pow(B, a, p)

AliceS = a * B
BobS = b * A

# Public: base, p, A, B
# Private: a, b, K

print('Private Stuff: \na: ' + str(a) + '\nb: ' + str(a) + '\nK: ' + str(AlicesK))
print('AliceS: ' + str(AliceS))
print('BobS: ' + str(BobS))
print('\nPublic Stuff: \nbase: ' + str(base) + '\np: ' + str(p) + '\nA: ' + str(A) + '\nB: ' + str(B))
print('\nALICE triplet: ' + str(p) + ' ' + str(base) + ' ' + (str(A)))
