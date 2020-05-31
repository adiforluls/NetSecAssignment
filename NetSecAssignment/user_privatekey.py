from Crypto.Util.number import *
from Crypto import Random
import Crypto
import libnum
import sys

bits=30
msg = ""

def keygenerate():
    p = Crypto.Util.number.getPrime(bits,randfunc = Crypto.Random.get_random_bytes)
    q = Crypto.Util.number.getPrime(bits,randfunc= Crypto.Random.get_random_bytes)

    phi = (p-1)*(q-1)
    n = p*q

    e = 65537
    d = (libnum.invmod(e,phi))
    return (d,n)

f = open("user_priv.txt","a")

for i in range(0,6):
	key,n = keygenerate()
	msg = str(key) + " " + str(n)
	f.write(msg + '\n')

f.close()
