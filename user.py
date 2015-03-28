#!/usr/bin/python3
# coding: iso-8859-1

"""user"""

import os, time, sys , select
from msvcrt import getch

# routeurprécédent<>adressefinale<>expéditeur<>message
#      0                   1           2          3

"""il faudra traiter le cas où l'ordinateur destination n'est pas (du tout) accessible"""


def url(num): return "taches/joueur"+ str(num)+".txt"
class Ordi :
  def __init__(self, num):
    self.num = num
    self.url = url(num)
    #os.remove(self.url) # on vire l'ancien fichier
    self.fichier = open(self.url, "w")
    self.fichier.close()
  
  def envoi(self, param): # le facteur sera forcément un voisin de self
    phrase = str(self.num) +"<>"+ param[1] +"<>"+ param[2] +"<>"+ param[3]
    facteur = self.route(int(param[1]))  # on cherche par qui il faut passer
    f=open(url(facteur),"a")
    f.write(phrase + "\n")
    f.close()
    return True
  
  def route(self, dest): #bricole moche pour commencer : le mec est un voisin direct !
    fichier=open("table.txt",'r')
    table=fichier.read()
    fichier.close()
    if str(table[self.num-1][dest-1])==1:
      return(dest)
  
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
    phrase = input("phrase ? ")
    dest = int(input("destinataire ?"))
    ordi.envoi([str(ordi.num), str(dest), str(ordi.num), phrase])
    main()
  
def main():
  global QUITTER, chargement
  chargement[0] = chargement[0]%(len(chargement)-1) + 1
  print(chargement[chargement[0]], end="\r")
  ordi.traitement()  
  def copain():
    #print("copain")
    global nombre
    try: # déterminer si un nouveau copain est arrivé
      fichier = open(url(nombre), "r")
      print("l'Ordi " + str(nombre) + " a rejoint le réseau !")    
      nombre+=1
      main()
    except IOError:
      return(True)  
  copain()    
  try:
    #print("try")
    if(QUITTER):
      os.remove(url(num))
      sys.exit(0)
    time.sleep(0.1)
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
chargement = [0,"     (O)c===8 ","     (O) c===8","     (O)c===8 ","     (Cc===8  "," A   (C===8   "," Ah  (C==8    "," Ah! (C===8   "," Ah! (Cc===8  "]
cmp=1
os.system("cls")
while 1: #insertion dans le réseau + lancement
  try:
    fichier = open(url(cmp), "r")
  except IOError: #le fichier n'existe pas
    nombre = cmp
    num=cmp
    fichier=open(url(num),'w') #on le crée
    fichier.close()
    os.system("title User" + str(num))
    print("vous êtes l'Ordi " + str(num))
    ordi=Ordi(num)
    print("Faites Ctrl+C pour quitter ou écrire",'\n')
    main() # les choses sérieuses commencent, on quitte la place.
  cmp+=1

  
"""fin user"""
