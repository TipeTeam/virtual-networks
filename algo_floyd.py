#!/usr/bin/python3
# coding: iso-8859-1

# Algorithme de Floyd-Warshall, en O(n^3), permet de trouver tous les plus courts chemins dans un graphe
# Rq: Dijkstra ne trouvait que les plus courts chemins issus d'UNE seule origine.
 
import os
inf = float("inf")

def floyd(g, multi = False):
  n = len(g)
  w = []
  for i in range (n):
    w.append([])
    for j in range (n):
      distance = g[i][j]
      w[i].append({
        "distance": distance,  # distance : inf si pas de liaison, +petit c'est meilleur, 0 si osef
        "direction": ([j] if multi else j) # voisin par lequel passer. Au début, on suppose qu'on peut aller direct de i à j 
      })

  for k in range (n): # points atteints en passant par les sommets intermédiaires d'indice <= k
    for i in range (n): # traitement de chaque ordi comme point de départ
      for j in range (n): # test de toutes les destinations
        if i != j and i != k: # on va pas chercher la merde en demandant si c'est rapide d'aller de Paris à Paris...
          distance_testee = w[i][k]["distance"] + w[k][j]["distance"]
          if (distance_testee < w[i][j]["distance"]):
            w[i][j] = {
              "distance": distance_testee,
              "direction": w[i][k]["direction"]
            }
          elif (multi and distance_testee == w[i][j]["distance"]):
            w[i][j]["direction"] = list(set(w[i][j]["direction"] + w[i][k]["direction"])) # ce sont des listes
          #print(k, " ", i, " ", j, " ", w[i][j]["direction"])
  """for i in range (n):
    for j in range (i+1,n):
      print("Trajet de "+str(i)+" à "+str(j)+" : "+str(w[i][j]["distance"])+"km.\nDirigez-vous vers "+str(w[i][j]["direction"])+".\n\n")"""
  return w


"""floyd(
[
  [ 0 , 1 ,inf,inf],
  [ 1 , 0 , 9 , 1 ],
  [inf, 9 , 0 , 5 ],
  [inf, 1 , 5 , 0 ]
]
)"""

"""
Le graphe testé ci-dessus est :

  [1] ---1km--- [2] ---9km--- [3] ---5km--- [0]
                 |                           |
                 |____________1km____________|
"""
#print("\n\n\n\n")
#os.system("pause")
