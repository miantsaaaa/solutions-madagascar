# Marge reelle Aitif - V4.9
# Un seul endroit pour la marge dans Data Aitif, pour ne pas la dupliquer.
# Si le marche change, on change seulement ici.
# Regle Aitif : sans frais, la marge ment. Avec frais, on sait vraiment.

MARGE_REELLE = {"Riz": 700, "Cafe": 8033, "Miel": 11000}

def marge_pour(produit):
    for cle, val in MARGE_REELLE.items():
        if cle.lower() in produit.lower():
            return val
    return 0
