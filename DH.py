import getpass 
import re

# I. Preliminary. We define a function as follows.

# 1. The function generators(p) finds all generators of the multiplicative group Z_{p} of integers mod prime p. 
# Note that the complexity of generators() is exponential.
# Ex. Let p = 5. Then generators(p) = {2, 3}.
def generators(p) :
    L = set()
    for x in range(1,p) : # 1 <= x <= p-1
        #print(x)
        S_x = set()
        for i in range(1,p) : 
            #print(x,"to",i)
            y = (x**i)%p # y = x^{i} mod p
            #print(y)
            S_x.add(y)
        print("<",x,"> =",S_x)
        if len(S_x) == p-1 :
            L.add(x)
    print("\nGenerators of Z mod",p,"are",L)
    
# II. The Diffie-Hellman protocol.

print()
print("------------------------------------------------------------")
print("     The Diffie-Hellman public key exchange protocol        ")
print("------------------------------------------------------------")
print()

# 1. Public: a prime p and generator g s.t. <g> = Z_{p}
p = input("Choose a prime: ")
p = int(p)
print()
generators(p)
print()
g = input("Choose a generator: ")
g = int(g)

print()

# 2. Alice (or Bob) picks a secret integer a (or b, respectively) in [1,p-1].
q = p-1
while True :
    print("Choose an integer in [",1,",",q,"]")
    a = getpass.getpass() 
    if re.findall("[a-zA-Z]",a) or int(a) <= 0 or int(a) > q:
        print("Wrong format!")
    else :
        a = int(a)
        break

print()

# 3. Alice (or Bob) sends g^{a} (or g^{b}, respectively) publicly to Bob (or Alice, respectively).
s = (g**a)%p # s = g^{a} mod p
print("Send:",s)
r = input("Receive: ") # r is the received element from Bob (or Alice)
r = int(r)

print()

# 4. The secret common key k = g^{ab} = g^{ba} mod p.
k = (r**a)%p
print("The secret common key:",k)

print()
