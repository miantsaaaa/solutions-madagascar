# Gestion Commerce Aitif - V1.10

## Probleme Madagascar
Les petits commerces partout a Madagascar gerent tout en cahier.
Cahier perdu = tout perdu. Pas de suivi ventes / depenses / stock.

## Solution Aitif
Outil CLI sur Redmi, hors-ligne, en Ariary, base SQLite locale.
Il marche a Fianarantsoa, Antananarivo, Toamasina, Mahajanga, Toliara, Antsiranana, partout.
Petit a petit, toujours bien organise. On ne promet pas, on prouve.

## Comment lancer
python3 main.py

## Structure - plusieurs fichiers, pas trop de code dans un fichier
- `main.py` - menu + ventes + depenses + stock
- `db.py` - base de donnees SQLite, `init_db()` + `connect()`
- `produits_aitif.py` - produits Aitif, prix observes 09 Nov 2026
- `test_stabilite.py` - test de stabilite, preuve que tout tient
- `config.py` - ville
- `commerce.db` - base locale, ne pas pousser
- `ventes.csv` / `depenses.csv` / `stock.csv` - exports locaux

## Fonctions
- Ajouter vente
- Ajouter depense
- Ajouter / maj stock
- Bilan du jour + stock
- Rapport 7 jours
- Exporter CSV / Sauvegarde
- Voir produits Aitif : Riz 2500 Ar, Cafe 25000 Ar, Miel 23000 Ar
- Marche hors-ligne, en Ariary

## Verifier la stabilite
python3 test_stabilite.py
Resultat attendu : STABLE

## Pour qui
Tout petit commerce a Madagascar, qui veut suivre ses ventes sans internet, sans PC, sans cahier.
