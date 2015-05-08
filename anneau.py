"""anneau"""

import os, time, sys
from msvcrt import getch

#   destinataire<>expéditeur<>message
#        0            1           2

def main():
  traitement()
  
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
      
def ecrire():
    phrase = input("phrase ? ")
    dest = int(input("destinataire ?"))
    envoi([str(dest), str(num), phrase])
    main()
  
def traitement():
  f=open(str(num%nombre) + ".txt",'r')
  tache=f.readline()
  contenu=f.read()
  f.close()
  f=open(str(num%nombre) + ".txt",'w')
  f.write(contenu)
  f.close()
  if tache=='':
    return(True)
  param=tache.split("<>")
  if param[0]==str(num):
    print("L'ordi "+param[1]+" vous envoie :   "+param[2])
  else:
    envoi(param) #retransmet au voisin
    print('Je transmets : "' + param[2] + '" de ' + "l'ordi " + param[1] + " à destination de l'ordi " + param[0])
  return("")
      
def envoi(param): # la direction est le voisin de droite !
    phrase = str(param[0]) +"<>"+ str(param[1]) +"<>"+ str(param[2])
    f=open(str((num+1)%nombre) + ".txt","a")
    f.write(phrase)
    f.close()
    return True

cmp=0
os.system("cls")
while 1: #insertion dans le réseau
  try:
    fichier = open(str(cmp) + ".txt", "r")
  except IOError: #le fichier n'existe pas
    nombre = cmp + 1
    num=cmp
    fichier=open(str(num) +'.txt','w') #on le crée
    fichier.close()
    print("vous êtes l'Ordi " + str(num) + " "+ str(time.time()))
    print("Faites Ctrl+C pour quitter ou écrire",'\n')
    main() # les choses sérieuses commencent, on quitte la place.
  cmp+=1
  
"""fin anneau"""
