
import string
import random
compteurvotant=1
nombrecandidat=5
nombrevotant=10
V=[]
listepreference=[]
A=list(string.ascii_lowercase)
A=A[0:nombrecandidat]
print(A)

while compteurvotant<=nombrevotant:
  V.append("v"+str(compteurvotant))
  compteurvotant+=1
print(V)

(for votant in V:
  listecandidataleatoire=[]
  while (len(listecandidataleatoire) != nombrecandidat) :
    candidataleatoire=chr(random.randint(97,nombrecandidat+96))
    print(candidataleatoire)
    if candidataleatoire not in listecandidataleatoire:
      listecandidataleatoire.append(candidataleatoire)
  print(votant)
  print(listecandidataleatoire)
  listepreference.append(listecandidataleatoire)
listepreference)  >>> voir + bas
