import string
import random
import numpy as np
import time
from datetime import timedelta
import matplotlib.pyplot as plt


# Détermine à partir de la liste de liste des vainqueurs le pourcentage de chance de gagner
def probaWin(liste):
  listeWin = []
  for cand in A:
    cptWin = 0
    for l in liste:
      cptWin+=l.count(cand)
    listeWin.append(round((cptWin/(nhiter*len(liste))), 3))
  return listeWin


# Prend en paramètre la partie 1 pour le nombre de votants qui varie ou 2 pour le nombre de candidats qui varie et la liste demandée et renvoit la probabilité qu'il n'y ait pas de vainqueur de Condorcet
def question1(liste, partie):
  listeProba=[]
  #cpt_nombre contient le nombre minimum de votants ou candidats selon la partie
  if (partie == 1):
    cpt_nombre = 3
  else:
    cpt_nombre = 2
  for l in liste:
    cpt = 0
    tp1 = time.time()
    for i in range(nhiter):
       if(l[i]==0) :  cpt+=1
    listeProba.append(cpt/nhiter)
    tp2 = time.time()
    if (partie == 1):
      print("nombre de votants : ", cpt_nombre, ",temps Q1 :", tp2 - tp1)
      cpt_nombre +=2
    else:
      print("nombre de candidats : ", cpt_nombre, ",temps Q1 :", tp2 - tp1)
      cpt_nombre += 1
  return listeProba

#prend en paramètre les 2 listes ainsi que 1 ou 2 selon la partie et un entier nb qui défini le nombre de candidat ou votant différent pour normaliser et renvoit la probabilité d'être doublement vainqueur
def question2(listeTest, listeCond, nb, partie):
  listeProba1 = [0]*nb
  if (partie == 1):
    cpt_nombre = 3
  else:
    cpt_nombre = 2
  for l in listeCond:
    tp1 = time.time()
    cptWin = 0
    for i in range(nhiter):

      if (l[i] != 0):
        cptWin += 1
        if(l[i]==listeTest[listeCond.index(l)][i]) :
          listeProba1[listeCond.index(l)]=listeProba1[listeCond.index(l)]+1
    if(cptWin!=0) : listeProba1[listeCond.index(l)]= round(listeProba1[listeCond.index(l)]/cptWin, 3)
    tp2 = time.time()
    if (partie == 1):
      print("nombre de votants : ", cpt_nombre, ",temps Q2/Q3 :", tp2 - tp1)
      cpt_nombre += 2
    else:
      print("nombre de candidats : ", cpt_nombre, ",temps Q2/Q3 :", tp2 - tp1)
      cpt_nombre += 1
  return listeProba1

def question4(l1, l2, nb, partie):
  listeProba = [0]*nb
  if (partie == 1):
    cpt_nombre = 3
  else:
    cpt_nombre = 2
  for i in range(nb):
    tp1 = time.time()
    for j in range(nhiter) :
      if (l1[i][j]==l2[i][j] and l1[i][j]!=0) :
        listeProba[i] = listeProba[i] +1
    listeProba[i]=round(listeProba[i]/nhiter,3)
    tp2 = time.time()
    if (partie == 1):
      print("nombre de votants : ", cpt_nombre, ",temps Q4 :", tp2 - tp1)
      cpt_nombre += 2
    else :
      print("nombre de candidats : ", cpt_nombre, ",temps Q4 :", tp2 - tp1)
      cpt_nombre += 1
  return listeProba

# Prend en paramètre la liste des préférences des votants et renvoit si oui ou non le dernier votant peut modifier le résultat en sa faveur
# Pour ce faire, on vérifie que a n'est pas gagnant puis on regarde si la différence de score entre le vainqueur présumé et les éléments de son ordre de préférence est rattrapable pour modifier le résultat
def bonus(listeVote):
  scoreBordaRes=[]
  votemalin= []
  gagnant = bordaResult(scoreBordaRes, listeVote)
  if (gagnant=='a'):
    print("\nLe dernier votant n'a pas de manipulation à opérer pour que l'election respecte ses preferences\n")
    return False
  for cand in A:
    if(cand<gagnant) and (scoreBordaRes[A.index(cand)] < (min(scoreBordaRes) + len(A) -1)) :
      #mettre cand qui est un candidat que préfère le dernier votant en premier et le premier présumé en dernier dans la liste de préférence du dernier votant
      votemalin.append(cand)
      for perdant in A:
        if(perdant!= cand) and (perdant!=gagnant):
          votemalin.append(perdant)
      votemalin.append(gagnant)
      print("Le dernier votant peut modifier l'issue de l'election\n")
      print("Préférence du dernier :", votemalin)
      print("\n")
      return True
  print("Le dernier votant ne peut pas modifier l'issue de l'election\n")
  return False




#donne True si le candidat x bat le candidat y par condorcet selon la liste de préférence
def condorcet(x,y):
  testCond=0
  for v in listepreference:
    if (v.index(x)<=v.index(y)):
      testCond+=1
  if testCond > nombrevotant/2 :
    return True
  else : return False

#Donne le candidat qui gagne par condorcet ou alors 0 s'il n'y a pas de vainqueur, pour cela on regarde pour chaque candidat s'il gagne par Condorcet contre tous les autres

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

# donne le score de de copeland du candidat x passé en paramètre
def copelandScore(x):
  score1 = 0
  score2 = 0
  for y in A:
    if (y!=x):
      if condorcet(x,y) : score1+=1
      elif condorcet(y,x) : score2+=1
  return score1 - score2

#Donne le candidat vainqueur selon la méthode de copeland ou 0 s'il n'y a pas un vainqueur unique
#On utilise une liste result où on ajoute les score de copeland des candidats 
#puis on regarde à quel index on trouve le score le plus élevé et on obtient le candidat correspondant
def copelandResult():
  result=[]
  for cand in A:
    result.append(copelandScore(cand))
  maximum = max(result)
  if (result.count(maximum)!=1) : return 0
  return A[result.index(maximum)]

#donne le score de de borda d'un candidat x avec la liste des préférences passée en paramètre
def bordaScore(x, liste):
  score=0
  for v in liste :
    score+=v.index(x)+1
  return score


# Pareil que pour copelandResult mais avec le score de Borda
def bordaResult(result, liste):
  for cand in A:
    result.append(bordaScore(cand, liste))
  minimum = min(result)
  if (result.count(minimum) != 1): return 0
  return A[result.index(minimum)]





# initialisation prend en parametre le nombre de candidats et de votants et crée leur liste respective
# On modélise les préférences des votants en prenant une liste auxiliaire contenant tous les candidats possibles à laquelle on pioche (=enlève) aléatoirement un élément qu'on place dans une autre liste


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

  #préférence des candidats
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



# On initialise les listes ainsi que le nombre de simulations pour chaque scénario de vote
A=[]
global nhiter
nhiter = 500
listeCondorcet = []
listeCopeland = []
listeBorda = []
# Sert pour le plot
liste_nombre_votants = np.array([3, 5, 7, 9, 11, 13, 15, 17, 19])
liste_nombre_candidats= np.array([2, 3, 4, 5, 6, 7])

#nombre candidats fixé à 5 et nombre votants qui varie de 3 à 19
for nombrevotant in range(3,20, 2):
  listeCondorcetTMP = []
  listeCopelandTMP = []
  listeBordaTMP = []
  for i in range(nhiter): # pour chaque nombre de votants on réalise plusieurs simulations
    listepreference = []
    scoreBorda = []
    A = initialisation(5, nombrevotant)
    listeCondorcetTMP.append(winCondorcet())
    listeCopelandTMP.append(copelandResult())
    listeBordaTMP.append(bordaResult(scoreBorda, listepreference))
  listeCondorcet.append(listeCondorcetTMP)
  listeCopeland.append(listeCopelandTMP)
  listeBorda.append(listeBordaTMP)


resQ1 = question1(listeCondorcet, 1)
resQ2 = question2(listeBorda, listeCondorcet, 9, 1)
resQ3 = question2(listeCopeland, listeCondorcet, 9, 1)
resQ4 = question4(listeBorda, listeCopeland, 9, 1)
print("\n Question 1 : ", resQ1)
plt.plot(liste_nombre_votants, resQ1, c="g", label='Pas de vainqueur de Condorcet')
print("\n Question 2 : ", resQ2)
plt.plot(liste_nombre_votants, resQ2, c="b", label='Existe vainqueur de Condorcet : vainqueur Borda = vainqueur Condorcet')
print("\n Question 3 : ", resQ3)
plt.plot(liste_nombre_votants, resQ3, c="r", label='Existe vainqueur de Condorcet : vainqueur Copeland = vainqueur Condorcet')
print("\n Question 4 : ", resQ4)
plt.plot(liste_nombre_votants, resQ4, c="orange", label='vainqueur Copeland = vainqueur Condorcet')
pbWinCondorcet = probaWin(listeCondorcet)
pbWinCopeland = probaWin(listeCopeland)
pbWinBorda = probaWin(listeBorda)
print("\n----------Resultat electoral----------")
for cand in A:
  print("\n----",cand, "----\n")
  print("Condorcet :", pbWinCondorcet[A.index(cand)])
  print("Copeland :", pbWinCopeland[A.index(cand)])
  print("Borda :", pbWinBorda[A.index(cand)])
plt.legend()
plt.show()


#nombre votants fixé à 19 et nombre candidats qui varie de 2 à 7
listeCondorcetbis = []
listeCopelandbis = []
listeBordabis = []
for nombrecandidat in range(2,8):
  listeCondorcetTMPbis = []
  listeCopelandTMPbis = []
  listeBordaTMPbis = []
  for i in range(nhiter):
    listepreference = []
    scoreBordabis = []
    A= initialisation(nombrecandidat, 19)
    listeCondorcetTMPbis.append(winCondorcet())
    listeCopelandTMPbis.append(copelandResult())
    listeBordaTMPbis.append(bordaResult(scoreBordabis, listepreference))
  listeCondorcetbis.append(listeCondorcetTMPbis)
  listeCopelandbis.append(listeCopelandTMPbis)
  listeBordabis.append(listeBordaTMPbis)


resQ1bis = question1(listeCondorcetbis, 2)
resQ2bis = question2(listeBordabis, listeCondorcetbis, 6, 2)
resQ3bis = question2(listeCopelandbis, listeCondorcetbis, 6, 2)
resQ4bis = question4(listeBordabis, listeCopelandbis, 6, 2)
print("\n Question 1 : ", resQ1bis)
plt.plot(liste_nombre_candidats, resQ1bis, c="g", label='Pas de vainqueur de Condorcet')
print("\n Question 2 : ", resQ2bis)
plt.plot(liste_nombre_candidats, resQ2bis, c="b", label='Existe vainqueur de Condorcet : vainqueur Borda = vainqueur Condorcet')
print("\n Question 3 : ", resQ3bis)
plt.plot(liste_nombre_candidats, resQ3bis, c="r", label='Existe vainqueur de Condorcet : vainqueur Copeland = vainqueur Condorcet')
print("\n Question 4 : ", resQ4bis)
plt.plot(liste_nombre_candidats, resQ4bis, c="orange", label='vainqueur Copeland = vainqueur Condorcet')
pbWinCondorcetbis = probaWin(listeCondorcetbis)
pbWinCopelandbis = probaWin(listeCopelandbis)
pbWinBordabis = probaWin(listeBordabis)
plt.legend()
plt.show()


# Section bonus : exécuter la fonction initialisation avec les bonnes valeurs puis fournir la liste de préférence
A= initialisation(5, 10)
listevotes = [['b', 'c', 'd', 'a', 'e'],
 ['b', 'c', 'd', 'e', 'a'],
 ['e', 'c', 'd', 'b', 'a'],
 ['d', 'e', 'a', 'b', 'c'],
 ['d', 'a', 'e', 'b', 'c'],
 ['d', 'c', 'b', 'a', 'e'],
 ['a', 'c', 'b', 'd', 'e'],
 ['e', 'c', 'a', 'd', 'b'],
 ['d', 'b', 'c', 'a', 'e'],
 ['b', 'a', 'd', 'c', 'e']]
bonus(listevotes)
