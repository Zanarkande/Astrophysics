#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 02:42:35 2025

@author: Allan
"""
#Import de la constante gravitationnelle
from astropy.constants import G

# Définition de la fonction
def calcul_gravite_surface(M, R):
    gravite_surface = (G * M) / R**2
    return gravite_surface

# Entrée utilisateur et conversion en float
rayon = float(input("Entrez le rayon de l'astre: "))
masse = float(input("Entrez la masse de l'astre : "))

#Calcul du résultat
gravite_surface = round(calcul_gravite_surface(masse, rayon).value,3)

print(f"Pour un rayon de {rayon} mètres et avec une masse de {masse} kg,la gravité de surface est d'environ {gravite_surface} m / s^2.")
print(f"Cela signifie qu'à chaque seconde, cet objet en chute libre sans frottement augmenterait sa vitesse de {gravite_surface} mètres par seconde.")