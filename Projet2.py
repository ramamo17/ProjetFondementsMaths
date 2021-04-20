import string
import random


def question1(liste):
  listeProba=[]
  for i in range(9):
    cpt = 0
    for l in liste:
       if(l[i]==0) :  cpt+=1
    listeProba.append(cpt/50)
  return listeProba

'''def question2(liste):
  listeProba = []
  for i in range(9):
    cpt = 0
    for l in liste:
      if (l[i] != 0):  cpt += 1
    listeProba.append(cpt / 50)
  return listeProba'''
# ici on créer une fonction qui prend en argument deux candidats et qui va renvoyer True si c'est le premier qui gagne 
#x gagne par rapport à y si il est devant plus de la moitié du temps
def condorcet(x,y):
  testCond=0
  for v in listepreference:
    if (v.index(x)<=v.index(y)):
      testCond+=1
  if testCond > nombrevotant/2 :
    return True
  else : return False

#une fonciton qui nous donne le vainqueur par condorcet
#un candidat est vainqueur par condorcet si il est gagant par rapport à tous les autres
def winCondorcet():
  for cand1 in A:
    cpt = 0
    for cand2 in A:
      if (cand1!=cand2):
        if (condorcet(cand1,cand2) != True) :
          break
        cpt+=1
        if cpt ==len(A)-1 :
          return cand1
  return 0

#On calcul le score de x pour copeland
def copelandScore(x):
  score1 = 0
  score2 = 0
  for y in A:
    if (y!=x):
      if condorcet(x,y) : score1+=1
      elif condorcet(y,x) : score2+=1
  return score1 - score2

#On appelle notre fonction de calcul du score et on trouve le gagnant par copeland, c'est celui avec le meilleur score
def copelandResult():
  result=[]
  for cand in A:
    result.append(copelandScore(cand))
  maximum = max(result)
  if (result.count(maximum)!=1) : return 0
  return A[result.index(maximum)]

#On retourne le score de borda du candidat passé en parametre de la fonction
def bordaScore(x):
  score=0
  for v in listepreference :
    score+=v.index(x)+1
  return score

#On procède de la même façon que pour copeland pour retourner le vainqueur par borda
def bordaResult():
  result = []
  for cand in A:
    result.append(bordaScore(cand))
  minimum = min(result)
  if (result.count(minimum) != 1): return 0
  return A[result.index(minimum)]

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
    for element in A:
      listebis.append(element)
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


for i in range(50):
  #nb candidat fixe et nb votant qui varie
  print("nb candidat fixe et nb votant qui varie")
  listeCondorcetTMP=[]
  listeCopelandTMP=[]
  listeBordaTMP=[]
  for nombrevotant in range(3,20, 2):
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
    initialisation(nombrecandidat, 19)
    print("DEBUT BOUCLE")
    #print(listepreference)
    print("5 candidats, ", nombrevotant, "votants")
    print("Condorcet :", winCondorcet())
    print("Copeland :", copelandResult())
    print("Borda :", bordaResult())'''
  print("CONDORCEEEEEEET", listeCondorcet)
  print(len(listeCondorcet))
  print("\n\nCOPELAAAAAAAAAND", listeCopeland)
  print("\n\nBORDAAAAAAAAAAAAAAA", listeBorda)
  print(question1())
