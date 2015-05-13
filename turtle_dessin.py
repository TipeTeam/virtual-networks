#!/usr/bin/python3
# coding: iso-8859-1

"""ceci est un programme contenant des fonctions générant des graphes et des fonctions les affichant (tableau et schéma de liaisons) via turtle"""

import turtle as tt
import math
import os
import random
import time

pi=math.pi
inf=float("inf")

def graphique(graphe): #pour une bonne utilisation, len(graphe)<=20
	tt.speed('fastest')
	tt.setup(width=1300,height=700)
	tt.up()
	tableau(graphe)
	tt.goto(320,-275)
	tt.down()
	tt.circle(285)
	place_graphe(graphe)
	tt.up()
	tt.goto(160,-300)
	tt.down()
	tt.write("soient i<j.")
	tt.up()
	tt.forward(60)
	tt.down()
	tt.color('red')
	tt.write('rouge: lien i<-->j    ')
	tt.up()
	tt.forward(100)
	tt.down()
	tt.color('blue')
	tt.write('bleu: lien i-->j    ')
	tt.up()
	tt.forward(90)
	tt.down()
	tt.color('green')
	tt.write('vert: lien i<--j')
	tt.color('black')	
	tt.up()
	tt.goto(320,0)

def place_point(nbre):
	for i in range(0,nbre):
		tt.up()
		tt.goto(320+250*math.cos(2*pi*i/nbre),250*math.sin(2*pi*i/nbre))
		tt.down()		
		tt.write(i+1)
		tt.up()
		tt.right(90)
		tt.forward(5)
		tt.down()
		tt.left(90)
		tt.circle(15)
		tt.up()

def place_graphe_binaire_1(g): #relation double : 3 relié à 2 ssi 2 relié à 3
	nbre=len(g)
	place_point(nbre)
	for i in range(0,nbre):
		for j in range(0,nbre): #on peut faire mieux ? j in range(i+1,nbre)
			if i!=j and g[i][j]==1: # prendre le 2e paramètre en compte dans un graphe non binaire : <infini.
				tt.up()
				tt.goto(320+220*math.cos(2*pi*i/nbre),220*math.sin(2*pi*i/nbre))	
				tt.down()
				tt.goto(320+220*math.cos(2*pi*j/nbre),220*math.sin(2*pi*j/nbre))
	tt.up()
	tt.goto(320,0)

def tableau(g):
	nbre=len(g)
	tt.up()
	for i in range(0,nbre+2):
		tt.up()
		tt.goto(-630,342-30*i)
		tt.down()
		tt.forward(30*(nbre+1))
	for i in range(0,nbre+2):
		tt.up()
		tt.goto(-631+30*i,342)
		tt.down()
		tt.right(90)
		tt.forward(30*(nbre+1))
		tt.left(90)
	tt.up()
	tt.goto(-630,314)
	tt.down()
	tt.forward(30*nbre+30)
	
	tt.up()
	tt.goto(-599,342)
	tt.down()
	tt.right(90)
	tt.forward(30*nbre+30)
	tt.left(90)
	
	for i in range(0,nbre+1):
		ord=320-i*30
		for j in range(0,nbre+1):
			abs=-620+30*j
			tt.up()
			tt.goto(abs,ord)
			if i==0:
				if j!=0:
					tt.down()
					tt.write(j)
					tt.up()
			else:
				if j==0:
					tt.down()
					tt.write(i)
					tt.up()
				else:
					tt.down()
					tt.write(g[i-1][j-1])
					tt.up()
						
def generateur_bi_1(nbre):
	g=[[1 for j in range(nbre)] for i in range(nbre)]
	for i in range(nbre-1):
		for j in range(i+1,nbre):
			a=random.randint(0,1)
			if a==0:
				g[i][j]=0
				g[j][i]=0
	return(g)
		
def place_graphe_binaire_2(g):
	nbre=len(g)
	place_point(nbre)
	for i in range(0,nbre):
		for j in range(0,nbre):
			if i!=j and g[j][i]==1: # <=inf
				tt.up()
				if i<j and g[i][j]!=g[j][i]: tt.color('blue')
				if j<i and g[i][j]!=g[j][i]: tt.color('green')
				if g[i][j]==g[j][i]: tt.color('red')
				tt.goto(320+220*math.cos(2*pi*i/nbre),220*math.sin(2*pi*i/nbre))	
				tt.down()
				tt.goto(320+220*math.cos(2*pi*j/nbre),220*math.sin(2*pi*j/nbre))
	tt.up()
	tt.color('black')

def generateur_bi_2(nbre):
	g=[[1 for j in range(nbre)] for i in range(nbre)]
	for i in range(nbre):
		for j in range(nbre):
			if i!=j:
				a=random.randint(0,1)
				if a==0:
					g[i][j]=0
	return(g)
	
def generateur(nbre,tps,proba): #nbre d'ordis et tps max entre chaque liaison (0,...,tps,inf), proba de n'être pas inf (ie pourcentage d'ordis interconnectés), proba dans [0,1]
	g=[[inf for j in range(nbre)] for i in range(nbre)]
	for i in range(nbre):
		g[i][i]=0
	for i in range(nbre):
		for j in range(nbre):
			if i!=j:
				b=random.random()
				if b<proba:
					a=random.randint(0,tps) #ptêt 1 à la place de 0 ?
					g[i][j]=a
	return(g)
	
def place_graphe(g):
	nbre=len(g)
	place_point(nbre)
	for i in range(0,nbre):
		for j in range(0,nbre):
			if i!=j and g[j][i]!=inf: # <=inf
				tt.up()
				if i<j and g[i][j]==inf: tt.color('blue')
				if j<i and g[i][j]==inf: tt.color('green')
				if g[i][j]!=inf: tt.color('red')
				tt.goto(320+220*math.cos(2*pi*i/nbre),220*math.sin(2*pi*i/nbre))	
				tt.down()
				tt.goto(320+220*math.cos(2*pi*j/nbre),220*math.sin(2*pi*j/nbre))
	tt.up()
	tt.color('black')

graphe=generateur(8,10,0.5)
graphique(graphe)
os.system('pause')
