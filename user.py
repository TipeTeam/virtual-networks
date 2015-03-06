"""user"""

import os, time, sys , select
from msvcrt import getch

# routeurprécédent<>adressefinale<>expéditeur<>message
#      0                   1           2          3

"""il faudra traiter le cas où l'ordinateur destination n'est pas (du tout) accessible"""


def url(num): return str(num)+".txt"
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
	ordi.traitement()	
	def copain():
		global nombre
		try: # déterminer si un nouveau copain est arrivé
			fichier = open(str(nombre) + ".txt", "r")
			print("l'Ordi " + str(nombre) + " a rejoint le réseau !")		
			nombre+=1
			main()
		except IOError:
			return(True)	
	copain()		
	try:
		time.sleep(1)
		main()
	except KeyboardInterrupt:
		print("Echap pour quitter, Espace pour revenir en arrière, ailleurs pour écrire")
		z=getch()
		if ord(z)==27: #Echap
			os.remove(str(num%nombre)+".txt")
			sys.exit(0)
		elif ord(z)==32: #Espace
			main()
		else:
			ecrire()

cmp=1
os.system("cls")
while 1: #insertion dans le réseau + lancement
	try:
		fichier = open(str(cmp) + ".txt", "r")
	except IOError: #le fichier n'existe pas
		nombre = cmp
		num=cmp
		fichier=open(str(num) +'.txt','w') #on le crée
		fichier.close()
		print("vous êtes l'Ordi " + str(num))
		ordi=Ordi(num)
		print("Faites Ctrl+C pour quitter ou écrire",'\n')
		main() # les choses sérieuses commencent, on quitte la place.
	cmp+=1
	
"""fin user"""
