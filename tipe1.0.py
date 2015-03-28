#!/usr/bin/python3
# coding: iso-8859-1 

import os, time, sys , select
from msvcrt import getch
import tkinter as tk
# routeurprécédent, adressefinale, expéditeur, message
#      0                   1                 2         3

Sep = "<>" # contient le §§§ ou autre
def url(num): return "taches\ordi"+str(num)+".txt"
class Ordi :
  def __init__(self, num, region):
    self.num = num
    self.voisins = []    # creates a new empty list for each computer
    self.url = url(num)
    #os.remove(self.url) # on vire l'ancien fichier
    self.fichier = open(self.url, "w")
    self.fichier.close()
    self.table = region
  
  def envoi(self, param): # le facteur sera forcément un voisin de self
    phrase = str(self.num) + Sep + param[1] + Sep + param[2] + Sep + param[3]
    facteur = self.table[int(param[1])]  # on cherche par qui il faut passer
    f=open(url(facteur),"a")
    f.write(phrase + "\n")
    f.close()
    return True
  
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
      param = tache.split(Sep) # /!\ là c'est param[0...] et pas param['dest'...]
      # for i in range (2): param[i] = int(param[i])
      if(int(param[1]) == self.num):
        print("L'ordi "+param[2]+" vous envoie : \""+ param[3] +"\".")
        return ""
      # else:
      param[0] = self.num
      print("Vous transmettez un message de "+param[2]+" vers "+param[1]+".\n")
      self.envoi(param)

def ecrire():
    dest = int(input("\nDestinataire ? "))
    phrase = input("Phrase ? ")
    print("Message envoyé.\n")
    ordi.envoi([str(ordi.num), str(dest), str(ordi.num), phrase])
    main()


def main():
	ordi.traitement()
	try:
		time.sleep(1)
		main()
	except KeyboardInterrupt:
		print("Echap pour quitter, Espace pour revenir en arrière, ailleurs pour écrire")
		z=getch()
		if ord(z)==27: #Echap
			os.remove(url(numero))
			sys.exit(0)
		elif ord(z)==32: #Espace
			main()
		else:
			ecrire()
		
numero = int(input("Numéro de l'ordinateur ? "))
os.system("title ordi"+str(numero))
t = {}
for i in range (1,4):
  t[(numero+i)%4] = input("comment vas-tu vers %d ? " %((numero+i)%4))
ordi = Ordi(numero, t)

#os.system("pause")
print("\nCa tourne... Ctrl+C pour écrire ou quitter\n")
#print(("2§§§0§§§3§§§tes con").split("§§§"))  
main()




 
  #print("tcon")
  #char = sys.stdin.read()
  #print("You pressed %s" % char)
  #if(char =="?????"):
  #  ecrire()"""
