# IA Aitif - Prediction Ventes - V3.9

## Probleme Madagascar
Un commercant a Fianarantsoa ne sait pas combien il va vendre demain.
Il achete trop ou pas assez, il perd de l'argent.

## Solution Aitif
Une IA simple qui apprend des ventes passees et predit les ventes de demain.
100% hors-ligne, sur telephone, en Ariary.
Petit a petit, toujours bien organise. On ne promet pas, on prouve.

## Comment lancer
python3 main.py
python3 conseil_achat.py
python3 alerte_stock.py
# Pour le graphique seulement, utiliser le venv :
/root/03-intelligence-artificielle/venv/bin/python graphique.py

## Structure - plusieurs fichiers, pas trop de code dans un fichier
- `main.py` - prediction avec jour de semaine
- `conseil_achat.py` - conseil achat avec vraie marge
- `alerte_stock.py` - alerte stock avec vraie marge
- `graphique.py` - graphique evolution ventes, besoin du venv
- `marge_aitif.py` - V3.7, un seul endroit pour la marge, pas de duplication
- `evolution-ventes.png` - courbe des ventes

## Fonctions
- Lit les ventes depuis commerce.db (Domaine 01)
- Prediction avec jour de semaine : samedi != lundi
- Conseil achat : n'achete que ce qu'il faut, avec vraie marge
- Alerte stock : quel produit va manquer, avec vraie marge
- Graphique : voir la courbe pour decider

## Regle Aitif
Verification ne compte pas comme version, seule une amelioration compte comme Vx.x.
Sans frais, la marge ment. Avec frais, on sait vraiment.

## Pour qui
Pour tout petit commerce a Madagascar qui veut acheter juste, sans gaspiller.
