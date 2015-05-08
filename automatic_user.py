#!/usr/bin/python3
# coding: iso-8859-1

"""user"""

import os, time, sys , select, random
from msvcrt import getch

# routeurprécédent<>adressefinale<>expéditeur<>message
#      0                   1           2          3

"""il faudra traiter le cas où l'ordinateur destination n'est pas (du tout) accessible"""

def rand(a,b):
  return random.randint(a,b)

def url(num): return "automatic/joueur"+ str(num)+".txt"

def lire_table():
  fichier = open("automatic/_table.txt",'r')
  table = fichier.read()
  fichier.close()
  return table

fichier=open("automatic/_infos.txt",'r')
nombre = fichier.readline()
taux_connexion = fichier.readline()
tps_traitement = fichier.readline()
frequence_envoi = fichier.readline()
fichier.close()

class Ordi :
  def __init__(self, num):
    self.num = num
    self.url = url(num)
    #os.remove(self.url) # on vire l'ancien fichier
    self.fichier = open(self.url, "w")
    self.fichier.close()
    self.table = (lire_table())[num] 
  
  def envoi(self, param): # le facteur sera forcément un voisin de self
    phrase = str(self.num) +"<>"+ param[1] +"<>"+ param[2] +"<>"+ param[3]
    facteur = self.route(int(param[1]))  # on cherche par qui il faut passer
    f=open(url(facteur),"a")
    f.write(phrase + "\n")
    f.close()
    return True
  
  def route(self, dest): #renvoie la prochaine étape pour aller à Dest
    t = lire_table()
    self.table = (eval(t))[self.num]
    return self.table[dest]["direction"]
  
  def traitement(self):
    f=open(self.url, "r")
    tache = f.readline()
    contenu = f.read()
    f.close()
    f=open(self.url, "w")
    f.write(contenu)
    f.close()
    
    if tache != "":
      print (tache)
      print(self.table)
      param = tache.split("<>") # /!\ là c'est param[0...] et pas param['dest'...]
      # for i in range (2): param[i] = int(param[i])
      if(int(param[1]) == self.num):
        print("L'ordi "+param[2]+" vous envoie : \""+ param[3] +"\".")
        return ""
      # else:
      param[0] = self.num
      print("Vous transmettez un message de "+param[2]+" vers "+param[1]+".\n")
      self.envoi(param)

def ecrire():
    phrase = str(time())
    dest = rand(0,nombre-2)
    dest += (dest >= ordi.num)
    ordi.envoi([str(ordi.num), str(dest), str(ordi.num), phrase])
    main()
  
def main():
  global QUITTER, chargement
  chargement[0] = chargement[0]%(len(chargement)-1) + 1
  print(chargement[chargement[0]], end="\r")
  ordi.traitement()   
  try:
    if(QUITTER):
      os.remove(url(num))
      sys.exit(0)
    time.sleep(1)
    main()
  except KeyboardInterrupt:
    print("Echap pour quitter, Espace pour revenir en arrière, ailleurs pour écrire")
    z=getch()
    if ord(z)==27: #Echap   # Y avait plein de bugs donc j'ai dû faire des trucs louches
      QUITTER = True
      os.remove(url(num))
      sys.exit(0)
    elif ord(z)==32: #Espace
      main()
    else:
      ecrire()

QUITTER = False
chargement = [0,"  ...   ","  ....  ","  ..... ","  ......","  ..... ","  ....  ","  ...   ","  ..    "]
tmp=0
#os.system("cls")
while 1: #insertion dans le réseau + lancement
  try:
    fichier = open(url(tmp), "r")
  except IOError: #le fichier n'existe pas
    nombre = tmp
    num=tmp
    fichier=open(url(num),'w') #on le crée
    fichier.close()
    os.system("title Auto" + str(num))
    print("Vous êtes l'Ordi automatique " + str(num))
    ordi = Ordi(num)
    main()
  tmp+=1

  
"""fin user"""
