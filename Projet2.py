import string
import random

def condorcet(x,y):
  testCond=0
  for v in listepreference:
    if (v.index(x)<=v.index(y)):
      testCond+=1
  if testCond > nombrevotant/2 :
    return True
  else : return False

def winCondorcet():
  for cand1 in A:
    cpt = 0
    for cand2 in A:
      if (cand1!=cand2):
        print(cand1, cand2)
        if cpt == nombrevotant :
          return cand1
        if (condorcet(cand1,cand2) != True) :
          break
        cpt+=1

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

for votant in V:
  listecandidataleatoire=[]
  listebis=[]
  for element in A:
    listebis.append(element)
  while (len(listebis) != 0) :
    x=random.choice(listebis)
    listecandidataleatoire.append(x)
    listebis.remove(x)
  print(votant)
  print(listecandidataleatoire)
  listepreference.append(listecandidataleatoire)


print(winCondorcet())
