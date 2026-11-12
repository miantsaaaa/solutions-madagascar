# Architecture Aitif - 11 Nov 2026 - Stable, Performant, Evolutif, Puissant

## Principe
1 brique = 1 dossier + 1 script + 1 test + 1 push.
On peut changer 1 brique sans casser les autres.

## Briques - 11 Nov 2026
1. Portfolio - docs/ - HTML statique, 2-6 Ko/page, 4G faible, hors-ligne
   - index.html, catalogue.html, cv.html, journal.html, prix.html, ajouter-prix.html
2. Prix Locaux - 07-metier-digital/projets/prix-locaux/
   - prix-locaux.csv - seuls vrais prix, Region + Ville + Lieu + Source
   - ajouter-prix.py - 1 commande = 1 prix
   - generer-prix-html.py - CSV -> prix.html, filtres Region + Categorie
   - calculer-marge.py - marge = dernier vrai prix - (achat + frais)
   - veille-auto.py - 1 fois/jour, VEILLE A FAIRE si tendance > 1 jour
   - TENDANCE-INTERNET-*.md - Internet = tendance, JAMAIS dans CSV
3. Vente - 07-metier-digital/projets/portfolio-entreprise/VENTE-2-1-MIEL.md
   - 1 chose : 1 L Miel, marge calculee par calculer-marge.py
4. Agent 00 - FONDATION-AITIF/
   - DIRECTION-AITIF.md - 1quater : Madagascar entier, tous produits
   - MEMOIRE-AGENT-00.md - Veille Prix branchee
   - NOUVELLES-DU-JOUR.md
5. Agents 01-07 - chacun dans son dossier, STATUS, 1 fois/heure, ne poussent jamais
6. Sante - check-sante-aitif.sh - 1 commande : site 200 + CSV + veille + agents + poids

## Regles de stabilite
- Pas de prix sans date + region + ville + lieu + source + qui a vu
- Pas de marge sans vrai prix
- Pas de push avec un rouge
- 1 version = 1 test + 1 commit + 1 push
- On ne promet pas, on prouve.

## Performance
- Pages < 6 Ko, pas de framework, pas d'image lourde, pas de JS externe.
- Cible : Redmi Note 14 Pro, 4G faible, coupures.

## Evolutivite
- Pour ajouter un produit : rien a coder, juste ajouter un prix.
- Pour ajouter une region : 1 ligne dans ajouter-prix.html + 1 ligne dans generer-prix-html.py.
- Pour ajouter une categorie : 1 ligne dans les 2 fichiers.
- Pour ajouter un domaine Agent : 1 dossier + 1 STATUS + 1 ligne dans check-sante.

## Puissance
- Puissance = plus de vrais prix, plus de vraies marges, plus de vraies ventes.
- Pas plus de code.
