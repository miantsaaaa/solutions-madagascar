#!/bin/bash
# AITIF SIMULATION - Je m'entraine avec la tendance, je ne mens pas sur le reel
echo "=== SIMULATION AITIF - $(date +%d-%m-%Y_%H:%M) ==="
echo "ATTENTION : ceci est une SIMULATION avec prix TENDANCE INTERNET."
echo "Le REEL reste a 0. Ce fichier ne touche JAMAIS prix-locaux.csv."
echo ""
python3 << 'PY'
import csv
rows = list(csv.DictReader(open("/root/SIMULATION/prix-tendance-simulation.csv")))
print("--- Simulation Commerce : si je vendais a prix tendance ---")
for r in rows:
    prix = int(r["prix_ar"])
    # Hypothese simulation : achat = 60% du prix tendance, frais = 2000
    achat = int(prix * 0.6)
    marge = prix - achat - 2000
    print(f"{r['produit']:8} : Vente {prix} Ar - Achat {achat} Ar - Frais 2000 Ar = Marge {marge} Ar {'(BENEFICE)' if marge>0 else '(PERTE)'}")
print("")
print("--- Simulation IA : que j'apprends ? ---")
print("Si Miel tendance = 18000 Ar, et mon achat reel = 12000 Ar (10000+2000),")
print(f"alors marge simulee = {18000-12000} Ar. Quand le vrai prix arrivera, je compare :")
print("Si vrai prix > simulation -> je gagne plus que prevu. Si vrai prix < simulation -> j'apprends.")
print("")
print("--- Simulation 01/03/05 : ---")
print("01 Commerce : je m'entraine a calculer, a proposer, a noter.")
print("03 IA : je m'entraine a predire avec 4 produits, meme si c'est de la tendance.")
print("05 ESP : je simule capteur 28C Toamasina pour tester l'alerte, sans dire que c'est vrai.")
print("")
print("REEL : 0 prix. SIMULATION : 4 produits. Les 2 mondes sont separes.")
PY
echo "=== FIN SIMULATION - Pret pour le reel ==="
