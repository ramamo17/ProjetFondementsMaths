import string
import random
import numpy as np
import time
from datetime import timedelta
import matplotlib.pyplot as plt


def question1(liste):
  listeProba=[]
  cpt_nombrevotants = 3
  for l in liste:
    cpt = 0
    tp1 = time.time()
    for i in range(50):
       if(l[i]==0) :  cpt+=1
    listeProba.append(cpt/50)
    tp2 = time.time()
    print("nombre de votants : ", cpt_nombrevotants, ",temps :", tp2 - tp1)
    cpt_nombrevotants +=2
  return listeProba

def question2(listeTest, listeCond):
  listeProba1 = [0,0,0,0,0,0,0,0,0]
  cpt = 0
  cpt_nombrevotants = 3
  for l in listeCond:
    tp1 = time.time()
    cptWin = 0
    for i in range(50):

      if cpt>9 : break
      if (l[i] != 0):
        cptWin += 1
        if(l[i]==listeTest[cpt][i]) :
          listeProba1[cpt]=listeProba1[cpt]+1
    if(cptWin!=0) : listeProba1[cpt]= round(listeProba1[cpt]/cptWin, 3)
    tp2 = time.time()
    print("nombre de votants : ", cpt_nombrevotants, ",temps :", tp2 - tp1)
    cpt_nombrevotants += 2
    cpt += 1
  return listeProba1


#donne True si x bat y par condorcet
def condorcet(x,y):
  testCond=0
  for v in listepreference:
    if (v.index(x)<=v.index(y)):
      testCond+=1
  if testCond > nombrevotant/2 :
    return True
  else : return False

#Donnne le candidat qui gagne par condorcet par rapport à tous les autres ou alors 0 si il y a pas de vainqueur
def winCondorcet():
  for cand1 in A:  #A est la liste des candidats
    cpt = 0
    for cand2 in A:
      if (cand1!=cand2):
        if (condorcet(cand1,cand2) != True) :
          break
        cpt+=1
        if cpt ==len(A)-1 :
          return cand1
  return 0

#donne le scorde de copeland de x passé en paramètre
def copelandScore(x):
  score1 = 0
  score2 = 0
  for y in A:
    if (y!=x):
      if condorcet(x,y) : score1+=1
      elif condorcet(y,x) : score2+=1
  return score1 - score2

#Donne le candidat vainqueur pas copeland ou 0 si il n'y en a pas que 1
#On a une liste result ou on va append les score de borda dans l'ordre des candidast dans A
#puis on regarde à quel index on trouve le score le plus élevé et on voit à qui ca correspond dans A
def copelandResult():
  result=[]
  for cand in A:
    result.append(copelandScore(cand))
  maximum = max(result)
  if (result.count(maximum)!=1) : return 0
  return A[result.index(maximum)]

#donne le scorde de borda d'un candidat x passé en parametre
def bordaScore(x):
  score=0
  for v in listepreference :
    score+=v.index(x)+1
  return score


#tout pareil que pour copeland result
def bordaResult():
  result = []
  for cand in A:
    result.append(bordaScore(cand))
  minimum = min(result)
  if (result.count(minimum) != 1): return 0
  return A[result.index(minimum)]


#initialisation prend en parametre le nombre de candidat et de votants 
#creer la liste des candidats A constituee de lettres minuscules 
# et la liste des votants V représenté par des nombres convertis en str
# ensuite on va creer des bulletins de votes listecandidataleatoire
# on va les stocker dans listepreference
def initialisation(nombrecandidat, nombrevotant):
  V = []
  compteurvotant=1

  #liste de candidat
  A = list(string.ascii_lowercase)
  A = A[0:nombrecandidat]

  #liste de votant
  while compteurvotant <= nombrevotant:
    V.append("v" + str(compteurvotant))
    compteurvotant += 1

  #vote des candidats
  for votant in V:
    listecandidataleatoire = []
    listebis = []
    for candidat in A:
      listebis.append(candidat)
    while (len(listebis) != 0):
      x = random.choice(listebis)
      listecandidataleatoire.append(x)
      listebis.remove(x)
    listepreference.append(listecandidataleatoire)
  return A

#random.seed()
A=[]
listeCondorcet = []
listeCopeland = []
listeBorda = []
liste_nombre_votants = np.array([3, 5, 7, 9, 11, 13, 15, 17, 19]) #????????????????????

#nb candidat fixe et nb votant qui varie
print("nb candidat fixe et nb votant qui varie")
for nombrevotant in range(3,20, 2):
  listeCondorcetTMP = []
  listeCopelandTMP = []
  listeBordaTMP = []
  for i in range(50): #??????????????????????????
    listepreference = []
    A = initialisation(5, nombrevotant)
    #print("DEBUT BOUCLE")
    #print(listepreference)
    '''print("5 candidats, ", nombrevotant, "votants")
    print("Condorcet :", winCondorcet())
    print("Copeland :", copelandResult())
    print("Borda :", bordaResult())'''
    listeCondorcetTMP.append(winCondorcet())
    listeCopelandTMP.append(copelandResult())
    listeBordaTMP.append(bordaResult())
  listeCondorcet.append(listeCondorcetTMP)
  listeCopeland.append(listeCopelandTMP)
  listeBorda.append(listeBordaTMP)


#nb votant fixe et nb candidat qui varie
'''print("\nnb votant fixe et nb candidat qui varie")
for nombrecandidat in range(2,8):
  listeCondorcetTMP = []
  listeCopelandTMP = []
  listeBordaTMP = []
  for i in range(50):
    initialisation(nombrecandidat, 19)
    print("DEBUT BOUCLE")
    #print(listepreference)
    print("5 candidats, ", nombrevotant, "votants")
    print("Condorcet :", winCondorcet())
    print("Copeland :", copelandResult())
    print("Borda :", bordaResult())
  print("CONDORCEEEEEEET", listeCondorcet)
  print("\n\nCOPELAAAAAAAAAND", listeCopeland)
  print("\n\nBORDAAAAAAAAAAAAAAA", listeBorda)'''


print("CONDORCEEEEEEET", listeCondorcet)
print("\n\nCOPELAAAAAAAAAND", listeCopeland)
print("\n\nBORDAAAAAAAAAAAAAAA", listeBorda)
resQ1 = question1(listeCondorcet)
resQ2 = question2(listeBorda, listeCondorcet)
resQ3 = question2(listeCopeland, listeCondorcet)
print("\n Question 1 : ", resQ1)
plt.plot(liste_nombre_votants, resQ1, c="g")
print("\n Question 2 : ", resQ2)
plt.plot(liste_nombre_votants, resQ2, c="b")
print("\n Question 3 : ", resQ3)
plt.plot(liste_nombre_votants, resQ3, c="r")
plt.show()
