"""client"""

import os, time, sys
from msvcrt import getch

#   destinataire<>expéditeur<>message
#        0            1           2

def envoi(param): # la direction est le hub !
    phrase = str(param[0]) +"<>"+ str(param[1]) +"<>"+ str(param[2])
    f=open("hub.txt","a")
    f.write(phrase)
    f.close()
    return True
 
def traitement():
	f=open(str(numero)+".txt",'r')
	tache=f.readline()
	contenu=f.read()
	f.close()
	f=open(str(numero)+".txt",'w')
	f.write(contenu)
	f.close()
	if tache=='':
		return(True)
	param=tache.split("<>")
	print("L'ordi "+param[1]+" vous envoie :   "+param[2])
	return("")
	  
def ecrire():
    phrase = input("phrase ? ")
    dest = int(input("destinataire ?"))
    envoi([str(dest), numero, phrase])
    print('\n')
    main()

def main():
	traitement()
	try:
		time.sleep(1)
		main()
	except KeyboardInterrupt:
		print("Echap pour quitter, Espace pour revenir en arrière, ailleurs pour écrire")
		z=getch()
		if ord(z)==27: #Echap
			os.remove(str(numero) + ".txt")
			sys.exit(0)
		elif ord(z)==32: #Espace
			main()
		else:
			ecrire()
		

numero=int(input("numero ?"))
#os.remove(str(numero)+".txt")
fichier=open(str(numero)+".txt","w")
fichier.close()
print("Faites Ctrl+C pour quitter ou écrire",'\n')
main()

"""fin client"""
