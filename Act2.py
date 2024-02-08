import random
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import hashlib

g = 2
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF

#Claves privadas para Alice, Bob, Eve
private_key_A = random.getrandbits(256)
private_key_B = random.getrandbits(256)
private_key_C = random.getrandbits(256)

#Simular cambio de números
A = pow(g, private_key_A, p) #Alice
B = pow(g, private_key_B, p) #Bob
C = pow(g, private_key_C, p) #Eve

#Calculos claves compartidas por Eve a Alice y Bob
key1 = pow(C, private_key_A, p)
key2 = pow(A, private_key_C, p)
key3 = pow(C, private_key_B, p)
key4 = pow(B, private_key_C, p)


print("Claves compartidas Eve - Alice: ", hashlib.sha256(str(key1).encode()).hexdigest())
print("Claves compartidas Alice - Eve: ", hashlib.sha256(str(key2).encode()).hexdigest())
print("Claves compartidas Eve - Bob: ", hashlib.sha256(str(key3).encode()).hexdigest())
print("Claves compartidas Bob - Alice: ", hashlib.sha256(str(key4).encode()).hexdigest())

if key1 == key2 and key3 == key4:
    print("Las claves compartidas SI son iguales. ")
else:
    print("Las claves compartidas NO son iguales. ")

if key1 == key4:
     print("Las claves compartidas SI son iguales. ")
else:
    print("Las claves compartidas NO son iguales. ")



