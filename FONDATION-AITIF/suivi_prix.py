# Suivi prix Aitif - V8.8
# 1 ligne = 1 observation, avec la date.
# Comme ca, dans 1 mois, on verra si le riz monte ou descend.

import csv, os
from datetime import datetime

FICHIER = "prix-historique.csv"

def ajouter(produit, prix, lieu, source):
    existe = os.path.exists(FICHIER)
    with open(FICHIER, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if not existe:
            w.writerow(["date", "produit", "prix_ar", "lieu", "source"])
        w.writerow([datetime.now().strftime("%Y-%m-%d"), produit, prix, lieu, source])
    print(f"Ajoute : {produit} {prix} Ar - {lieu} - {source}")

def voir():
    if not os.path.exists(FICHIER):
        print("Aucun prix note pour l'instant.")
        return
    print("=== HISTORIQUE PRIX AITIF ===")
    with open(FICHIER, encoding="utf-8") as f:
        for ligne in f:
            print(ligne.strip())

if __name__ == "__main__":
    # Premieres lignes : nos prix observes du 09 nov 2026
    ajouter("Riz 1kg", 2500, "Marche Madagascar", "Internet - nov 2026")
    ajouter("Cafe 1kg", 25000, "Producteur", "Internet - nov 2026")
    ajouter("Miel 1L", 23000, "Marche Madagascar", "Internet - nov 2026")
    print()
    voir()
