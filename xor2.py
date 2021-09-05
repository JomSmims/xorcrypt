import os
from hashlib import sha256
from tqdm import tqdm
entree = input ("File 2 crypt : ")
sortie =input ("Final file : ")
key = input ("Clé : ")

la_longueur = os.path.getsize (entree)
per_cent = int(la_longueur/100)

print (la_longueur)
KEYS = sha256(key.encode('utf-8')).digest()
affic= per_cent
with open(entree,'rb') as f_entree:
    with open (sortie, 'wb') as f_sortie:
        i=0
        for co in tqdm(range (0,la_longueur)):
            c= ord(f_entree.read(1))
            j = i % len(KEYS)
            b= bytes([c^KEYS[j]])
            f_sortie.write(b)
            i=i+1
