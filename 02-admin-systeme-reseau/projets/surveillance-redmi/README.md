# Surveillance Aitif - V2.8

## Probleme Madagascar
A Madagascar, coupures electricite, 4G faible, stockage plein sans prevenir.
Si ton telephone tombe, ton entreprise tombe.

## Solution Aitif
Outil qui surveille ton telephone : batterie, stockage, reseau, en 1 commande, hors-ligne.
Petit a petit, toujours bien organise. On ne promet pas, on prouve.

## Comment lancer
python3 main.py
python3 rapport.py
python3 simuler_nettoyage.py

## Structure - plusieurs fichiers, pas trop de code dans un fichier
- `main.py` - batterie + stockage + reseau
- `rapport.py` - rapport etat systeme complet
- `alerte.py` - alerte batterie / stockage
- `sauvegarde.py` - sauvegarde auto
- `nettoyage.py` - nettoyage cache + logs, ne touche jamais .db / .csv / .md
- `simuler_nettoyage.py` - V2.7, voir avant de supprimer, plus sur
- `test_stabilite.py` - verification, ne compte pas comme version

## Fonctions
- Batterie : niveau, en charge ou pas
- Stockage : espace libre / total, alerte si > 80%
- Reseau : test 4G / WiFi
- Rapport : projets, sauvegardes, bases de donnees
- Simulation nettoyage : voir avant de supprimer

## Regle Aitif
Verification ne compte pas comme version, seule une amelioration compte comme Vx.x.
Sans frais, la marge ment. Avec frais, on sait vraiment.

## Pour qui
Pour toi, pour Aitif, pour tout petit commerce qui ne veut pas perdre ses donnees.
