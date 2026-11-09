# Prediction Ventes - V3.1
## Probleme Madagascar
Un commercant a Fianarantsoa ne sait pas combien il va vendre demain.
Il achete trop ou pas assez, il perd de l'argent.

## Solution
Une IA simple qui apprend des ventes passees et predit les ventes de demain.
100% hors-ligne, sur 【entity-Redmi¦canonical_name=Redmi】, en Ariary.

## Comment lancer
python3 main.py

## Fonctions V3.1
- Lit les ventes depuis commerce.db (Domaine 01)
- Calcule la moyenne des 7 derniers jours
- Predis la vente de demain

## Prochaines versions
- V3.2 : prediction avec jour de semaine (samedi vs lundi)
- V3.3 : alerte stock bas prevu
- V3.4 : graphique evolution ventes
- V3.5 : conseil achat auto
