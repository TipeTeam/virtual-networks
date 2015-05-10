#!/usr/bin/python3
# coding: iso-8859-1

"""
  La class Param permet de stocker des paramètres dans un fichier.
  Initialisation : nécessite un chemin d'accès au dossier
  Set : définit un paramètre en l'inscrivant dans un fichier et en l'ajoutant à la classe.
    param, val : crée le fichier _param.txt, ou le remplace, avec pour contenu val
    {p1:v1, p2:v2, ...} : définit les paramètres p1, p2,... avec pour valeurs respectives v1, v2,...
  Get : récupère un paramètre et modifie la variable dans la classe.
    param : retourne un le texte du fichier _param.txt, ou False s'il n'existe pas
    [p1, p2, ...] : retourne une liste contenant les valeurs de p1, p2,...
"""

import os
class Param :
  def __init__(self, dossier):
    self.path = dossier +"/"

  def set(self, **doublets):
    l = []
    for parametre, valeur in doublets.items():
      f = open(self.path + "_"+ parametre +".txt","w")
      f.write(str(valeur))
      f.close()
      self.__dict__[parametre] = valeur
      l.append(valeur)
    if len(l) == 1 : return l[0]
    else: return l

  def get(self, *parametres, fonction = ""):
    l = []
    for doublet in parametres:
      fun = ""
      if type(doublet) is tuple:
        parametre = doublet[0]
        fun = doublet[1]
      else: parametre = doublet
      fichier = self.path + "_"+ parametre +".txt"
      if os.path.exists(fichier):
        f = open(fichier,'r')
        valeur = f.read()
        f.close()
        if fun:
          valeur = eval(fun +"('"+ valeur +"')")
        elif fonction:
          valeur = eval(fonction +"('"+ valeur +"')")
        self.__dict__[parametre] = valeur
        l.append(valeur)
      else:
        l.append(False)
    if len(l) == 1 : return l[0]
    else: return l