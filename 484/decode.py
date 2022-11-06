import binascii as bs
from python_math import *

e = 65537
c = 684151956678815994103733261966890872908254340972007896833477109225858676207046453897176861126186570268646592844185948487733725335274498844684380516667587
n = 14783703403657671882600600446061886156235531325852194800287001788765221084107631153330658325830443132164971084137462046607458019775851952933254941568056899
p = 121588253559534573498320028934517990374721243335397811413129137253981502291629
q = 121588253559534573498320028934517990374721243335397811413129137253981502291631

#decryption:
#d = e^-1 mod(Փ(n))
phi_N = (p-1) * (q-1)
d = pow(e,-1,phi_N)
decrypted = pow(c,d,n)
decrypted = hex(decrypted)[2:]
print(decrypted)
print(bs.unhexlify(decrypted))
