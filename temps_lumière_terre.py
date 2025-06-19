#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 00:24:09 2025

@author: Allan
"""

c = 299792458 #m / s

### Input utilisateur ###

distance = float(input("Entrez la distance entre l'astre et la Terre: "))
input_unit = input("Indiquez l'unité de distance entrée\n(pc, al, au, Gm, Mm, km, hm, dam, dm, cm, mm): ")

### Dictionnaire pour les conversions ###

unite_dict = {
    'pc' : 30856775814672000,
    'al' : 9460730472580800,
    'au' : 149597870700,
    'Gm' : 1e9,
    'Mm' : 1e6,
    'km' : 1e3,
    'hm' : 1e2,
    'dam' : 1e1,
    'm' : 1,
    'dm' : 1e-1,
    'cm' : 1e-2,
    'mm' : 1e-3,
    }

temps = {
    'seconde' : 1,
    'minute' : 60,
    'heure' : 3600,
    'jour' : 86400,
    'semaine' : 604800,
    'mois' : 2.628e6,
    'année' : 3.154e7,
    'décennie' : 3.154e8,
    'siècle' : 3.154e9
    }



if input_unit in unite_dict:
    distance_metre = distance * unite_dict[f'{input_unit}']
    temps_lumiere_seconde = distance_metre / c 
else:
    raise SystemExit("Unité non reconnue.")


def reste():
    if distance_metre % c != 0:
        return (distance_metre % c / c)
    return 0

if temps_lumiere_seconde < temps['minute']:
    temps_entier = (temps_lumiere_seconde / temps['seconde'])
    reste_temps = reste() * temps['seconde']
    unite = "seconde"
    unite_reste = ""

elif temps_lumiere_seconde < temps['heure']:
    temps_entier = int((temps_lumiere_seconde / temps['minute']))
    reste_temps = temps_lumiere_seconde - temps_entier * temps['minute']
    unite = "minute"
    unite_reste = "seconde"
    
elif temps_lumiere_seconde < temps['jour']*2:
    temps_entier = int(temps_lumiere_seconde / temps['heure'])
    reste_temps = temps_lumiere_seconde - temps_entier * temps['heure']
    reste_temps_converti = int(reste_temps / temps['minute'])
    unite = "heure"
    unite_reste = "minute"
    
elif temps_lumiere_seconde < temps['mois']*2:
    temps_entier = int(temps_lumiere_seconde / temps['jour'])
    reste_temps = temps_lumiere_seconde - temps_entier * temps['jour']
    reste_temps_converti = int(reste_temps / temps['heure'])
    unite = "jour"
    unite_reste = "heure"
    
elif temps_lumiere_seconde < temps['année']:
    temps_entier = int(temps_lumiere_seconde / temps['mois'])
    reste_temps = temps_lumiere_seconde - temps_entier * temps['mois']
    reste_temps_converti = int(reste_temps / temps['jour'])
    unite = "mois"
    unite_reste = "jour"
    
else:
    temps_entier = int(temps_lumiere_seconde / temps['année'])
    reste_temps = temps_lumiere_seconde - temps_entier * temps['année']
    reste_temps_converti = int(reste_temps / temps['mois'])
    unite = "année"
    unite_reste = "mois"    

temps_entier = int(temps_entier)
reste_temps = int(reste_temps)

if temps_entier > 1 and not unite == "mois":
    unite += "s"

if reste_temps > 1 and not unite_reste == "mois":
    unite_reste += "s"    
    
if reste_temps != 0:
    print(f'Pour une distance de {int(distance)}{input_unit}, la lumière met environ {temps_entier} {unite} et {reste_temps_converti} {unite_reste} à arriver.')
else:
    print(f'Pour une distance de {int(distance)}{input_unit}, la lumière met environ {temps_entier} {unite} à arriver.')
    
    
    
    