#!/usr/bin/python3
# coding: iso-8859-1

import os, time, sys, urllib.request, select, string, webbrowser, param
from randint import rand
from pprint import pprint
from msvcrt import getch
from algo_floyd import floyd, inf # on importe l'algorithme de Floyd pour trouver les +courts chemins

# routeurprécédent<>adressefinale<>expéditeur<>message
#      0                   1           2          3

"""il faudra traiter le cas où l'ordinateur destination n'est pas (du tout) accessible"""
_p = param.Param("automatic")
def url(num): return "automatic/joueur"+ str(num)+".txt"
  
def creer_tableau(lignes, colonnes, value):
  t = []
  for i in range (lignes):
    t.append([value]*colonnes)
  return t

def connecter(o1, o2, distance=1):
  global adjacence
  #print(o1,o2,distance)
  adjacence[o1][o2] = distance
  adjacence[o2][o1] = distance

def sont_connectes(o1, o2): return (adjacence[o1][o2] < inf)

def rompre(o1, o2):
  global adjacence
  r = sont_connectes(o1, o2)
  adjacence[o1][o2] = inf
  adjacence[o2][o1] = inf
  return r

def actualiser_table():
  global adjacence, tableF
  print(adjacence)
  tableF = floyd(adjacence, multi = True)
  _p.set(table = tableF)
  phrase = ""
  for i in range(1,len(adjacence)):
    phrase += "_"
    for j in range(0,i):
      if adjacence[i][j] == 0 or adjacence[i][j] == inf:
        phrase += "0"
      else: phrase += "1"
  _p.set(adj = phrase)  #phrase = str(tmpt).replace("inf", '0').replace(" ", '').replace(",", '').replace("][", '_').replace("]", '').replace("[", '')
  webbrowser.open('http://rannios.free.fr/?/tipe/'+ phrase)

def allumer_ordi():
  os.system("start automatic_user.py")
  pass

def creer_reseau(nombre, taux_connexion):
  _p.set(nombre = nombre, connectivite = taux_connexion, tpsTraitement = 0.25, frequenceEnvoi = 0.5)
  for i in range(nombre):
    if(os.path.isfile(url(i))):
      os.remove(url(i))
  
  global adjacence
  adjacence = creer_tableau(nombre, nombre, inf)
  connecter(0, 0, 0)
  
  # créer les liaisons afin d'avoir un graphe connexe :
  for o1 in range (1,nombre): # le zéro se connecte à personne, c'est les autres qui s'y connectent
    connecter(o1, o1, 0)
    k = min(2*o1-1, rand(1,max(1, round(o1 * taux_connexion / 100)))) # c'est le nombre de voisins inférieurs auxquels o1 sera connecté
    while k > 0:
      k -= 1
      o2 = rand(0,o1-1) # on le connecte avec qqn au pif, tant pis si ils étaient déjà potes
      if(not sont_connectes(o1, o2)):
        distance = 1 # ou rand(1,nombre) si l'on veut des distances variées
        connecter(o1, o2, distance)
  actualiser_table()
  pprint(adjacence)
  print(taux_connexion)
  
  for i in range (nombre):
    allumer_ordi()

adjacence = []
tableF = []

os.system("cls")

args = []
if not(int(sys.argv[1])>0): nombre = 6
else: nombre = int(sys.argv[1])
if not(int(sys.argv[2])>0): taux = 30
else: taux = int(sys.argv[2])
creer_reseau(nombre, taux)

while 1:
  print("\n\nEchap: quitter\nEspace: revenir en arrière\n+: ajouter liaison\n-: supprimer liaison") #\n0: éteindre un ordi")
  z=ord(getch())
  if z==27: #Echap
    for i in range(nombre):
      os.remove(url(i))
    os.system("cls")
    sys.exit(0)
  elif z==32: #Espace  
    pass
  elif z==43: #+
    connecter(int(input("Premier ordi")), int(input("Second ordi")))
    actualiser_table()
  elif z==45: #-
    print("Attention ! Le réseau doit rester connexe !")
    rompre(int(input("Premier ordi")), int(input("Second ordi")))
    actualiser_table()
  elif z==48: #0
    print("Attention ! Le réseau doit rester connexe !")
    rompre(int(input("Premier ordi")), int(input("Second ordi")))
    actualiser_table()
  else:
    pass