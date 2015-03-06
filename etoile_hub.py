"""hub"""
import os, time, sys
#   destinataire<>expéditeur<>message
#        0            1          2

def envoi(param): # la direction est le destinataire !
    desti = param[0]  # on cherche par qui il faut passer
    phrase = str(param[0]) +"<>"+ str(param[1]) +"<>"+ str(param[2])
    print('Le hub transmet : "' + param[2] + '" de ' + "l'ordi " + param[1] + " à destination de l'ordi " + param[0])
    f=open(str(desti)+".txt","a")
    f.write(phrase + "\n")
    f.close()
    return True
  
def traitement():
    f=open("hub.txt", "r")
    tache = f.readline()
    contenu = f.read()
    f.close()
    f=open("hub.txt", "w")
    f.write(contenu)
    f.close()
    param = tache.split("<>")
    if param!=[""]: envoi(param)
	
def main():
	traitement()
	time.sleep(1)
	main()

os.system('cls')
fichier=open("hub.txt","w") #création
fichier.close()
main()

"""fin hub"""
