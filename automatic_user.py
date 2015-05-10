#!/usr/bin/python3
# coding: iso-8859-1

import os, time, sys , select, param
from randint import rand

# routeurprécédent<>adressefinale<>expéditeur<>message
#      0                   1           2          3
os.system("cls")
"""il faudra traiter le cas où l'ordinateur destination n'est pas (du tout) accessible"""
_p = param.Param("automatic")
def url(num): return "automatic/joueur"+ str(num)+".txt"

def lire_table():
  return _p.get("table")

_p.get("nombre", "connectivite", "tpsTraitement", "frequenceEnvoi", fonction="float")
delai = 1
print(_p.nombre, _p.connectivite, _p.tpsTraitement, _p.frequenceEnvoi, " coucou")

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
    if os.path.exists(url(facteur)):
      f=open(url(facteur),"a")
      f.write(phrase + "\n")
      f.close()
      return True
    return False
  
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
    
    if tache != "" and tache != "\n":
      #print (tache)
      #print(self.table)
      param = tache.split("<>") # /!\ là c'est param[0...] et pas param['dest'...]
      param[3] = ((param[3]).split("\n"))[0] # on vire le saut de ligne final
      # for i in range (2): param[i] = int(param[i])
      if(int(param[1]) == self.num):
        retard = time.time() - float(param[3])
        print("Réception de "+param[2]+", retard : "+ str(retard) +" secondes")
        return ""
      # else:
      param[0] = self.num
      print("Transmission "+ param[2] +"->"+ param[1] +", délai : "+ str(delai))
      time.sleep(delai) # délai de transmission
      self.envoi(param)

def ecrire():
    phrase = str(time.time())
    dest = rand(0,_p.nombre-2)
    dest += (dest >= ordi.num)
    print("   Envoi à   "+ str(dest) +"  :  "+ str(phrase))
    ordi.envoi([str(ordi.num), str(dest), str(ordi.num), phrase])
  
def main():
  try:
    while 1:
      ordi.traitement()   
      time.sleep(0.2)
      if(rand(0, _p.frequenceEnvoi)):
        ecrire()
  except KeyboardInterrupt:
    os.remove(url(ordi.num))
    sys.exit(0)

tmp=0

while 1: #insertion dans le réseau + lancement
  try:
    fichier = open(url(tmp), "r")
    fichier.close()
  except IOError: #le fichier n'existe pas
    if(tmp >= _p.nombre): print("Vous êtes trop nombreux sur ce réseau."); break
    else:
      fichier=open(url(tmp),'w') #on le crée
      fichier.close()
      os.system("title Auto" + str(tmp))
      print("Vous êtes l'Ordi automatique " + str(tmp))
      ordi = Ordi(tmp)
      main()
  tmp+=1