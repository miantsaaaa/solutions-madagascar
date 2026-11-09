# Config simple pour V1.1 - ville du commerce
import os
FICHIER = "ville.txt"
def get_ville():
    if os.path.exists(FICHIER):
        with open(FICHIER) as f:
            return f.read().strip()
    ville = input("Ville de ton commerce (ex: Fianarantsoa, Antananarivo, Toamasina) : ").strip()
    if not ville:
        ville = "Madagascar"
    with open(FICHIER, "w") as f:
        f.write(ville)
    return ville
