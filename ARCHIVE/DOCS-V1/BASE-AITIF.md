# BASE AITIF - Fondation pour batir plus tard - 12 Nov 2026

## Principe
L'interface viendra plus tard. Maintenant, on batit la base.
Si la base est propre, l'application de demain sera facile.
Si la base est sale, l'application de demain sera impossible.

## Entites de base - ce que Aitif gere
1. PRODUIT - ex: Riz, Cafe, Miel, Vanille
   - Champs : nom, categorie, unite (kg, L, kapoaka), saison
   - Pas de prix en dur. Le prix vient de PRIX.
2. PRIX - ex: 1 ligne = 1 observation reelle
   - Champs : date, produit, categorie, region, ville, lieu, prix_ar, source, vu_par, note
   - Regle : incomplet = refuse. Internet = tendance, jamais dans PRIX.
3. STOCK - ex: Miel 1L en main
   - Champs : produit, quantite, unite, lieu, date_entree
   - Regle : 0 = 0, pas de faux stock.
4. VENTE - ex: 1 vente, quand elle sera reelle
   - Champs : date, produit, quantite, prix_vente, prix_achat, frais, marge, acheteur_anonyme, lieu
   - Regle : pas de vente sans vrai prix + vrai stock.
5. SAVOIR - ex: Marge = Vente - Achat - Frais
   - Champs : titre, contenu_malgache, contenu_francais, domaine, date
   - But : faire evoluer Madagascar, 1 savoir a la fois.
6. DOMAINE - 7 domaines
   - Agriculture, Education, Sante, Energie/Eau, Environnement, Numerique, Commerce
   - Chacun : mission, responsable Agent, regles, etat.
7. AGENT - 00 a 07
   - Champs : id, domaine, mission, etat, derniere_action
   - Regle : ne pousse jamais seul, ne ment jamais.

## Regles de base - ne changent jamais
- REEL = vu par quelqu'un, avec date + lieu + source. Sinon, c'est SIMULATION ou IDEE.
- SIMULATION = pour s'entrainer, dans SIMULATION/, marque SIMULATION - PAS REEL.
- IDEE = a verifier, pas a vendre.
- 1 brique = 1 dossier + 1 test + 1 commit + 1 push.
- Si ca ne se verifie pas tout seul, ce n'est pas de la base, c'est du vent.

## Ce que la base sait faire aujourd'hui
- Se verifier (check-sante, bilan)
- Se relancer toute seule (auto-start, fond)
- Simuler sans mentir (SIMULATION separee)
- Se souvenir (MEMOIRE-AGENT-00, PLAN demain)
- Refuser le faux (04 Data)

## Ce que la base doit savoir faire demain, pour batir l'application
- 1 API simple : lire PRIX, STOCK, SAVOIR, DOMAINES - en JSON, sans recoder
- 1 sauvegarde qui ne depend pas de Termux
- 1 historique : chaque changement = date + qui + quoi

## Prochaine evolution de la base
- Creer les fichiers de base vides, propres, prets : produits.csv, stock.csv, savoirs.csv
- Pas de fausses lignes. Juste la structure, prete a recevoir le reel.
