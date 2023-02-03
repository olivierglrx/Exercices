import os
import re

exercices=[f for f in os.listdir('exercices/new') if f[-3:]=='tex']



def get_preambule(nom_fichier):
    d={}
    fich=open('exercices/new/'+nom_fichier)
    while True:
        line=fich.readline()
        if ':' in line:
            i=line.index(":")
            d[line[2:i-1]]=line[i+1:-1]
        else:
            return(d)

def get_titre(nom_fichier):
    d=get_preambule(nom_fichier)
    return(d['Titre'])

def get_diff(nom_fichier):
    d=get_preambule(nom_fichier)
    return(d['Difficulte'])

def get_type(nom_fichier):
    d=get_preambule(nom_fichier)
    return([t.strip() for t in d['Type'].split(',')])

def get_cat(nom_fichier):
    d=get_preambule(nom_fichier)
    return([c.strip() for c in d['Categories'].split(',')])

def get_subcat(nom_fichier):
    d=get_preambule(nom_fichier)
    return([sc.strip() for sc in d['Subcategories'].split(',')])

def get_key(nom_fichier):
    d=get_preambule(nom_fichier)
    return([kw.strip() for kw in d['Keywords'].split(',')])
