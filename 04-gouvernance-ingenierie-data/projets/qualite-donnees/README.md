# Data Aitif - Qualite Donnees - V4.8

## Probleme Madagascar
Beaucoup de donnees a Madagascar sont sales : doublons, prix a 0, noms vides.
On decide avec de fausses donnees, on perd de l'argent.

## Solution Aitif
Outil qui controle tes donnees commerce : ventes, depenses, stock.
Il dit ce qui est propre et ce qui est sale, en 1 commande.
Petit a petit, toujours bien organise. On ne promet pas, on prouve.

## Comment lancer
python3 main.py
python3 nettoyage_doublons.py
python3 rapport_mensuel.py
python3 export_propre.py
python3 regles_gouvernance.py

## Structure - plusieurs fichiers, pas trop de code dans un fichier
- `main.py` - controle qualite, score / 100
- `nettoyage_doublons.py` - detecte et fusionne les doublons, ne supprime jamais les ventes
- `rapport_mensuel.py` - bilan du mois, meilleur produit avec vraie marge
- `export_propre.py` - export propre pour Excel, donnees verifiees seulement
- `regles_gouvernance.py` - 8 regles qui protegent tes donnees

## Fonctions
- Compte les ventes, depenses, produits
- Detecte prix a 0, quantite negative, produit vide
- Donne un score de qualite / 100
- Signale les ventes en double exact, sans les supprimer
- Rapport mensuel avec vraie marge

## Regles Aitif
Verification ne compte pas comme version, seule une amelioration compte comme Vx.x.
Sans frais, la marge ment. Avec frais, on sait vraiment.
1 seul fichier verite : commerce.db est la verite, les CSV sont des copies.

## Pour qui
Pour tout commerce a Madagascar qui veut decider sur des donnees propres, pas sur des fausses donnees.
