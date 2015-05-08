#!/usr/bin/python3
# coding: iso-8859-1

"""user"""

import os, time, sys , select, random
from msvcrt import getch
from pprint import pprint
from algo_floyd import floyd, inf # on importe l'algorithme de Floyd pour trouver les +courts chemins

# routeurprécédent<>adressefinale<>expéditeur<>message
#      0                   1           2          3

"""il faudra traiter le cas où l'ordinateur destination n'est pas (du tout) accessible"""

def rand(a,b):
  return random.randint(a,b)

def url(num): return "automatic/joueur"+ str(num)+".txt"
  
def creer_tableau(lignes, colonnes, value):
  t = []
  for i in range (lignes):
    t.append([value]*colonnes)
  return t

def connecter(o1, o2, distance):
  global adjacence
  print(o1,o2,distance)
  adjacence[o1][o2] = distance
  adjacence[o2][o1] = distance

def sont_connectes(o1, o2): return (adjacence[o1][o2] < inf)

def rompre(o1, o2):
  global adjacence
  r = sont_connectes(o1, o2)
  adjacence[o1][o2] = inf
  return r

def actualiser_table():
  global adjacence, tableF
  tableF = floyd(adjacence)
  fichier = open("automatic/_table.txt","w")
  fichier.write(str(tableF))
  fichier.close()

def allumer_ordi():
  os.system("start automatic_user.py")

def creer_reseau(nombre, taux_connexion):
  fichier = open("automatic/_infos.txt","w")
  fichier.write(str(nombre) + "\n"+ str(taux_connexion) + "\n"+ str(0.1) + "\n"+ str(5))
  fichier.close()
  
  for i in range(nombre):
    if(os.path.isfile(url(i))):
      os.remove(url(i))
  
  global adjacence
  adjacence = creer_tableau(nombre, nombre, inf)
  connecter(0, 0, 0)
  #chemins = [[0]*nombre]*nombre
  
  # créer les liaisons afin d'avoir un graphe connexe :
  for o1 in range (1,nombre): # le zéro se connecte à personne, c'est les autres qui s'y connectent
    connecter(o1, o1, 0)
    k = rand(1,max(o1-1, 1+round(o1 * taux_connexion / 100))) # c'est le nombre de voisins inférieurs auxquels o1 sera connecté
    while k > 0:
      k -= 1
      o2 = rand(0,o1-1)
      if(not sont_connectes(o1, o2)):
        distance = 1 # ou rand(1,nombre) si l'on veut des distances variées
        connecter(o1, o2, distance)
  actualiser_table()
  pprint(adjacence)
  #pprint(tableF)
  
  for i in range (nombre):
    allumer_ordi()
  


adjacence = []
tableF = []
#liaisons = [] pourra servir à autoriser plusieurs lisaisons directes entre 2 mêmes ordis

os.system("cls")

creer_reseau(3, 10)

  
"""fin user"""