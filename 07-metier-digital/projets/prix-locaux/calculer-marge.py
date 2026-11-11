import argparse, csv, pathlib, sys
p = argparse.ArgumentParser()
p.add_argument("--produit", required=True, help="Ex: Miel 1L")
p.add_argument("--achat", required=True, type=int, help="Prix achat en Ar")
p.add_argument("--frais", required=True, type=int, help="Frais totaux en Ar : transport + emballage")
p.add_argument("--region", default="", help="Optionnel : filtrer sur une region")
a = p.parse_args()
f = pathlib.Path(__file__).parent / "prix-locaux.csv"
rows = list(csv.DictReader(open(f, encoding="utf-8")))
# Dernier prix de vente reel pour ce produit, eventuellement dans 1 region
cands = [r for r in rows if r["produit"].lower() == a.produit.lower()]
if a.region:
    cands = [r for r in cands if r["region"].lower() == a.region.lower()]
if not cands:
    print("PAS DE PRIX REEL - Pas de marge calculee.")
    print("Ajoute d'abord 1 vrai prix avec ajouter-prix.py ou ajouter-prix.html")
    sys.exit(0)
dernier = cands[-1]
vente = int(dernier["prix_ar"])
cout = a.achat + a.frais
marge = vente - cout
pct = round(marge / cout * 100, 1) if cout else 0
print(f"Produit : {a.produit} - Vente {vente} Ar ({dernier['ville']} / {dernier['region']} / {dernier['date']})")
print(f"Cout : achat {a.achat} Ar + frais {a.frais} Ar = {cout} Ar")
print(f"Vraie marge : {marge} Ar ({pct} %)")
print("Regle : Internet = tendance, Marche = vrai prix.")
