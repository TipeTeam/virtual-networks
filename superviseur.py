"""superviseur"""

import os, time, sys
from msvcrt import getch

def main():
	def copain():
		global nombre
		try: # déterminer si un nouveau copain est arrivé
			fichier = open(str(nombre) + ".txt", "r")
			print("l'Ordi " + str(nombre) + " a rejoint le réseau !")
			ajout(nombre)
			nombre+=1
			main()
		except IOError:
			return(True)	
	copain()		
	try:
		time.sleep(1)
		main()
	except KeyboardInterrupt:
		print("Echap pour quitter, Espace pour revenir en arrière, t pour consulter la table, c pour effectuer un changement")
		z=getch()
		if ord(z)==27: #Echap
			os.remove("table.txt")
			sys.exit(0)
		elif ord(z)==32: #Espace
			
			main()
		elif ord(z)==116: #t
			print(table)
		else:
			changement()

def ajout(nombre): # l'ordi Nombre débarque sur le réseau ; renseignement de ses liaisons
	for i in range(1,nombre):
		a=int(input("liaison de Ordi " + str(nombre) + ' vers Ordi ' + str(i) + '?'))
		assert a==0 or a==1
		table[i-1].append(a)
	liste=[]
	for i in range(1,nombre):
		a=int(input("liaison de Ordi " + str(i) + ' vers Ordi ' + str(nombre) + '?'))
		assert a==0 or a==1
		liste.append(a)
	liste.append(1)
	table.append(liste)

	os.remove("table.txt") #méthode ptêt un peu radicale...
	fichier=open("table.txt","w")
	fichier.write(str(table))
	fichier.close()
	return True
	
def changement(): #une liaison apparait ou disparait
	base=int(input("à partir de quel ordi ?"))
	dest=int(input("vers quel ordi ?"))
	assert base<nombre and dest<nombre
	a=table[base-1][dest-1]
	print(table)
	print("l'état actuel de la liaison de "+str(base)+" vers "+str(dest)+" est "+str(a))
	print("Voulez-vous changer cette liaison ? Enter <-> oui ; autre <-> non")
	if ord(getch())==13: #Enter
		print('avant ' + str(a))
		print((a+1)%2)
		table[base-1][dest-1]=(a+1)%2
		print('après ' + str(table[base-1][dest-1]))
		print(table)
		os.remove("table.txt") #méthode ptêt un peu radicale...
		fichier=open("table.txt","w")
		fichier.write(str(table))
		fichier.close()
		print(table)
		return True
	else:
		return True
		
cmp=1
while 1:
	try:
		os.remove(str(cmp)+".txt")
	except IOError:
		table=[]
		fichier=open("table.txt","w")
		fichier.write(str(table))
		fichier.close()
		nombre=1 #nécessité d'ouvrir en premier superviseur
		main()
	cmp+=1
	
"""fin superviseur"""
