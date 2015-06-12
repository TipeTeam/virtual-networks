# Algorithme de Ford-Fulkerson, en O(m^2*n), permet de trouver le flot maximal dans un graphe.
#   Z : tableau Z[x] = True ssi x a été traité
#   L : inclus au tableau Z[x] avec une valeur intermédiaire
#   L\Z : file
#   l : tableau de valeurs (à fusionner avec Z et L ??)
 
import os, math
from queue import Queue
inf = float("inf")
couleurs = [[0,0,0],[7,0,15],[0,0,15],[0,8,20],[0,14,14],[0,17,0],[13,25,0],[25,25,0],[25,23,0],[25,0,0]]
def couleur(val, maxi):
  taux = val / maxi * (len(couleurs)-1)
  bas = math.floor(taux)
  haut = math.ceil(taux)
  couleur = [0,0,0]
  for i in range(3):
    couleur[i] = str(( couleurs[bas][i]*(haut - taux) + couleurs[haut][i]*(taux - bas) ) * 10)
  return "rgb("+ couleur[0] +", "+ couleur[1] +", "+ couleur[2] +")"
    
  
def recherche_chaine_augmentante(R, s, t, f):
  l = [inf]*(len(f))
  L = Queue(); L.put(s)
  Z = [0]*(len(f))
  pred = [""]*(len(f))
  resultat = "rien"
  while resultat == "rien":
    x = L.get()
    Z[x] = 2
    for y in range(0,len(f)):
      if Z[y]: pass
      elif R[x][y] > 0 and f[x][y] < R[x][y]: # capacité de x vers y non saturée
        l[y] = min(l[x], R[x][y] - f[x][y])
        L.put(y)
        pred[y] = (x, +1)
      elif R[y][x] > 0 and f[y][x] > 0: # capacité de y vers x non nulle
        l[y] = min(l[x], f[y][x])
        L.put(y)
        pred[y] = (x, -1)
    if(Z[t]): resultat = True
    elif(L.empty()): resultat = False
  return {
    "trouve": resultat,
    "pred": pred,
    "insat": l[t]
  }

def flot_max(R, s, t):
  n = len(R)
  f = []
  for i in range (n):
    f.append([])
    for j in range (n):#capacite = g[i][j]
      f[i].append(0)  # flot initial nul
  chaine = recherche_chaine_augmentante(R, s, t, f)
  while chaine["trouve"]:
    #augmenter flot
    y = t; x = t
    while x != s:
      (x, e) = chaine["pred"][y]
      if(e > 0): f[x][y] += chaine["insat"]
      else: f[y][x] -= chaine["insat"]
      y = x
    chaine = recherche_chaine_augmentante(R, s, t, f)
  return f
