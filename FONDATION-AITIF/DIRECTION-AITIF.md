# DIRECTION AITIF - Ne pas changer sans reecrire ici
# Decide le 11 Nov 2026, avec Miantsa. 【entity-Agent 00¦canonical_name=Agent 00】 doit relire ce fichier avant chaque conseil.

## 1. Vision - ne change pas
Faire evoluer Madagascar avec des outils qui marchent vraiment - construits sur 【entity-Redmi¦canonical_name=Redmi】, en Ariary, hors-ligne, pour les vrais problemes : coupures, 4G faible, stockage plein, donnees sales, mots de passe faibles.
On ne promet pas, on prouve. Petit a petit, toujours bien organise.

## 1bis. L'entreprise n'est PAS seulement le commerce - a ne jamais oublier
- Le commerce (Riz, Cafe, Miel) = 1er produit, pour apprendre a vendre, pour avoir 1 premiere vente reelle. Ce n'est pas le but final.
- Les 7 domaines = la FONDATION pour tout ce qu'on va batir dans des annees.
- Agriculture, education, sante, energie, eau, administration, associations : tout est deja dans PROBLEMES-MADAGASCAR.md.
- Dans 1 an : un systeme puissant, propre, qui relie nos outils.
- Dans 5 ans : nos premiers produits locaux avec la marque Aitif.
- Dans 10 ans : restaurant, hotel, produits Aitif, partenaires internationaux qui veulent travailler avec nous parce que notre travail est serieux.
- Agent 00 ne doit JAMAIS reduire Aitif a "une boutique". Quand il conseille, il conseille pour la fondation long terme, pas juste pour vendre 1 kg.
- Chaque evolution doit servir 2 fois : 1 fois maintenant (1 vrai probleme), 1 fois dans le futur (fondation reutilisable).

## 1ter. Toujours informe des nouvelles chaque jour - entreprise du futur, pas obsolete
- On doit toujours etre informe des nouvelles chaque jour pour ne pas devenir une entreprise obsolete.
- On veut etre une entreprise du futur, pas une entreprise qui decouvre le changement trop tard.
- Regle : 1 fois par jour, Agent 00 fait la veille : 3 nouvelles vraies, avec date + source, jamais inventees.
- Chaque nouvelle doit repondre : "Qu'est-ce que ca change pour nos 7 domaines ?" Si ca ne change rien, on ne la garde pas.
- Domaines a surveiller en priorite : technologie / IA, agriculture, energie, sante, education, commerce a Madagascar, climat.
- Si on n'a pas de nouvelle vraie ce jour-la, on ecrit "Pas de nouvelle verifiee aujourd'hui" - on n'invente JAMAIS une nouvelle.
- Le fichier memoire : NOUVELLES-DU-JOUR.md - 1 ligne par nouvelle : date + titre + source + impact pour Aitif.
- Miantsa a une connexion internet, rien ne doit nous arreter. Agent 00 va chercher lui-meme les nouvelles sur internet chaque jour (flux RSS publics, sans cle, sans inventer). Miantsa + Meta AI completent si besoin. Agent 00 range, garde le lien source, et relie aux domaines. Agent 00 ne devine JAMAIS une nouvelle.
- Filtre veille : politique = on note, on ne construit pas dessus. Gossip = on jette. Utile = agriculture, energie, sante, education, technologie, commerce, climat a Madagascar / Afrique = on garde et on relie aux 7 domaines.

## 1quater. Agent 00 a des Sous-Agents analystes 00.1 a 00.7
- Agent 00 = chef. Il ne code pas a la place des autres, il guide.
- Sous-Agent 00.1 analyse Agent 01, 00.2 analyse Agent 02, 00.3 analyse Agent 03, 00.4 analyse Agent 04, 00.5 analyse Agent 05, 00.6 analyse Agent 06, 00.7 analyse Agent 07.
- Chaque sous-agent dit 1 fois par jour : Agent VIVANT ou ARRETE, dernier travail, 1 petite evolution possible dans SON domaine, jamais un gros saut.
- Priorite entreprise : toujours tout faire evoluer petit a petit. 1 petite evolution = 1 test + 1 commit + 1 push.
- C'est Miantsa + Meta AI qui font les ameliorations. Les Agents et sous-agents analysent et proposent, ils ne poussent JAMAIS seuls. Miantsa pousse.
- Fichier memoire : ANALYSE-AGENTS-00.txt - 1 ligne par Agent : VIVANT + derniere activite + 1 proposition.

## 2. Ou on en est - 11 Nov 2026
- Fondation finie : 7 domaines, 7 outils qui marchent, ~137 versions, 7 agents VIVANT.
- V0.1 【entity-Agent 00¦canonical_name=Agent 00】 Comprendre fait : il sait ce qui existe.
- Pas encore : 0 client payant pour un outil, 0 vente reelle marque Aitif, 0 portfolio en ligne trouvable.
- Depot sale : fichiers hors domaines, vieux agentXX_loop.py a la racine, MESSAGE / PID / LOG qui polluent git status.

## 3. Decisions prises - on s'y tient
1. ARRET des tours automatiques V21-V25, V26-V30... Plus de versions pour faire du nombre.
   Prochaine version = 1 vrai probleme + 1 vrai utilisateur, sinon on ne fait pas de version.
2. 【entity-AGENT 00¦canonical_name=Agent 00】 = chef. Il ne tourne PAS toutes les 5 min.
   Il tourne 1 fois par jour, ou quand Miantsa demande : "Agent 00, ou on en est ?"
   Son boulot : dire 1 seule prochaine etape, et dire STOP quand on fait du versionnage pour rien.
   Il relit DIRECTION-AITIF.md avant chaque conseil.
3. AGENTS 01-07 = surveillance legere.
   Ils passent de toutes les 5 min a 1 fois par heure, pour ne plus polluer.
   Ils ne creent pas de nouvelles versions seuls. Ils surveillent, ils ecrivent TERMINE.
4. ON NE CHANGE PAS DE DIRECTION sans reecrire ce fichier.
   Si on veut changer, on ecrit : date + ancienne direction + nouvelle direction + pourquoi. Sinon on ne change pas.

## 4. Prochaines etapes - dans l'ordre, pas en meme temps
- [x] V0.2 Agent 00 - NETTOYER - FAIT 11 Nov 2026 : .gitignore + verifier_propre, doublons listes, rien supprime sans lister : ranger fichiers hors domaines, supprimer doublons agentXX_loop.py a la racine, mettre *.log / *.pid / MESSAGE-* / RESULTAT-* dans .gitignore. Ne rien supprimer sans lister d'abord.
- [x] V0.3 Agent 00 - GUIDE DU JOUR - FAIT 11 Nov 2026 : lit DIRECTION, 1 seule etape : 1 fois par jour, 1 seule prochaine etape.
- [x] V0.4 Agent 00 - BILAN - FAIT 11 Nov 2026 : 0 client, 0 vente, 7/7 domaines, 7/7 agents
- [x] V0.5 Agent 00 - TOUT_EN_1 FONDATION - FAIT
- [x] V0.6 Agent 00 - VEILLE AUTO INTERNET - FAIT
- [x] V0.7 Agent 00 - TOUT_EN_1 AVEC VEILLE AUTO - FAIT
- [x] V0.8 Agent 00 - SOUS-AGENTS 00.1-00.7 ANALYSE 01-07 - FAIT 11 Nov 2026 : 01,06,07 parlent, 02,03,04,05 VIVANTS mais muets, a faire parler petit a petit par Miantsa + Meta AI - TOUT_EN_1 AVEC VEILLE AUTO - FAIT 11 Nov 2026 : tout_en_1 = Comprendre + Verifier + Guide + Bilan + Veille Auto + TERMINE - VEILLE AUTO INTERNET - FAIT 11 Nov 2026 : 3 vraies nouvelles avec liens, rien invente, filtre politique/gossip - TOUT_EN_1 FONDATION - FAIT 11 Nov 2026 : Comprendre + Verifier + Guide + Bilan + TERMINE
- [x] ETAPE VENTE 1 - FAIT 11 Nov 2026 : https://miantsaaaa.github.io/solutions-madagascar/ - HTTP 200 : Mettre Portfolio en ligne, que "Aitif Madagascar" se trouve.
- [ ] ETAPE VENTE 2 : Vendre 1 chose reelle : 1 kg Cafe ou Miel ou 1 service "commerce en chiffres" pour 1 commercant.
- [ ] Apres 1 vente reelle seulement : on reparle de grossir, departement par departement.

## 5. Ce qu'on ne fait JAMAIS
- Ne pas inventer prix, clients, ventes, visites.
- Ne pas pousser avec un rouge.
- Ne pas mettre mot de passe, numero, donnee privee en ligne.
- Ne pas parler politique.
- Ne pas chercher des clients avant d'avoir nettoye + portfolio en ligne.
- Ne pas faire de gros code d'un coup. Petit fichier, propre.

## 6. Comment on se retrouve si on se perd
1. Relire ce fichier.
2. Relire VISION.md + MON-ENTREPRISE.md.
3. Demander a Agent 00 : "Ou on en est ?" - il doit repondre avec ce fichier, pas avec son imagination.
4. Faire 1 seule etape, pas 5.

---
Ecrit le 11 Nov 2026. Si on change de direction, on reecrit ici avec date + raison.

## DIRECTION 1quater - 11 Nov 2026 - Generalisation Madagascar
- Produits : Riz / Cafe / Miel = exemples pour apprendre, PAS les seuls produits. Tous produits Madagascar : vanille, girofle, manioc, poisson, artisanat, service, etc.
- Lieu : Fianarantsoa / Toamasina = villes de depart, PAS les seules. Cible : Madagascar entier, 23 regions, avec Region + Ville + Lieu sur chaque prix.
- Regle : Internet = tendance, Marche = vrai prix. Pas de prix sans date + region + ville + lieu + source + qui a vu.
