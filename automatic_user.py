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
  return eval(_p.get("table"))

_p.get("nombre", "connectivite", "tpsTraitement", "frequenceEnvoi", fonction="float")
print(_p.nombre, _p.connectivite, _p.tpsTraitement, _p.frequenceEnvoi)
vitesse = 40 #actualisations par seconde


class Ordi :
  def __init__(self, num):
    self.num = num
    self.url = url(num)
    #os.remove(self.url) # on vire l'ancien fichier
    self.fichier = open(self.url, "w")
    self.fichier.close()
    self.table = (lire_table())[num]
    if(self.num == 0 and os.path.exists(url("0stat"))):
      os.remove(url("0stat")) 
  
  def add_stat(self, *colonnes):
    if(self.num == 0):
      phrase = ""
      for val in colonnes:
        phrase += str(val).replace(".", ",") + "\t"
      f=open(url("0stat"),"a")
      f.write(phrase + "\n")
      f.close()
  

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
    self.table = (lire_table())[self.num]
    r = self.table[dest]["direction"]
    if(type(r) is list):
      if(int(_p.get("multi"))):
        return r[rand(0, len(r)-1)]
      else: return r[0]
    else:
      return r
  
  def traitement(self):
    f=open(self.url, "r")
    tache = f.readline()
    contenu = f.read()
    f.close()
    f=open(self.url, "w")
    f.write(contenu)
    f.close()
    
    if tache != "" and tache != "\n":
      param = tache.split("<>") # /!\ là c'est param[0...] et pas param['dest'...]
      param[3] = ((param[3]).split("\n"))[0] # on vire le saut de ligne final
      if(int(param[1]) == self.num):
        retard = time.time() - float(param[3])
        print("Réception de "+param[2]+", retard : "+ str(retard) +" secondes")
        self.add_stat(param[3], param[2], retard)
        return ""
      # else:
      param[0] = self.num
      print("Transmission "+ param[2] +"->"+ param[1] +", délai : "+ str(_p.tpsTraitement))
      time.sleep(_p.tpsTraitement) # délai de transmission
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
      time.sleep(1/vitesse)
      if(not rand(0, _p.frequenceEnvoi*vitesse)):
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