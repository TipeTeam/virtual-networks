#!/usr/bin/python3
# coding: iso-8859-1 

def floyd(g):
  w = []
  #return w
  n = len(g)
  for i in range (n):
    w.append([])
    for j in range (n):
      bande = g[i][j]
      if bande == 0: bande = 4000000
      elif bande < 0: bande = 0
      else: bande = 1/bande
      w[i].append({
        "bande": bande,  # bande passante : 0 si pas de liaison, grand si cool, -1 si osef
        "direction": j # voisin par lequel passer. Au début, on suppose qu'on peut aller direct de i à j 
      })
  #return w
  for k in range (n): # points atteints en k étapes (n au max car on passe pas 2fois au même endroit)
    for i in range (n): # traitement de chaque ordi comme point de départ
      for j in range (n): # test de tous les voisins
        if i != j: # on va pas chercher la merde en demandant si c'est rapide d'aller de Paris à Paris...
          bande_testee = w[i][k]["bande"] + w[k][j]["bande"]
          if (bande_testee < w[i][j]["bande"]):
            w[i][j] = {
              "bande": bande_testee,
              "direction": w[i][k]["direction"]
            }
  return w

print(floyd(
[
  [-1, 1, 0, 0],
  [1, -1, 9, 1],
  [0, 9, -1, 5],
  [0, 1, 5, -1]
]
))
    
