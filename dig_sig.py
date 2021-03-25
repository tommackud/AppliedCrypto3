#################################################################
# For each chunk of public information sent generate an RSA
# Digital Signature. (Module 6)
#################################################################

#########
# Part 1
#########
from Crypto.PublicKey import RSA
from hashlib import sha512

# Ignore this part for now, because rsa functions in lecture video are deprecated in Py3
# f = open('ds_key.pem','wb')
# f.write(keyPair.export_key('PEM'))
# f.close()

# Attempt at using built in key generation
keyPair = RSA.generate(bits=2048)
mod = keyPair.n
pub_exp = keyPair.e
pri_exp = keyPair.d
first_fac = keyPair.p
second_fac = keyPair.q
cin_remain = keyPair.u

print('Modulus: ' + str(mod))
print('Modulus len: ' + str(len(str(mod))))

print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
#print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

# RSA sign the message
msg = b'I solemnly swear to learn applied cryptography. Even though there are not enough graded assignments to ' \
      b'incentivize the needed hours I will: 1) work problems 2) ask questions 3) ponder start-ups 4) think in a ' \
      b'paranoid fashion 5) get it done without excuse '
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
signature = pow(hash, keyPair.d, keyPair.n)
print("Signature:", hex(signature))

# RSA verify signature
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
# print("Signature valid:", hash == hashFromSignature)

# Convert message to integer
int_arr = [int(a) for a in msg]
int_msg = ''.join([str(elem) for elem in int_arr])
print('Integer message: ' + str(int_msg))
print('Integer message len: ' + str(len(str(int_msg))))


