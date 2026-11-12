# ORGANISATION - solutions-madagascar
# Regle d'or : petit a petit, toujours bien organise.

## Structure du depot
- 1 domaine = 1 dossier (01, 02, 03, 04, 05, 06, 07)
- 1 outil = 1 dossier dans projets/ du domaine
  Ex : 01-genie-logiciel-et-bdd/projets/gestion-commerce-madagascar/
- 1 outil = toujours 3 fichiers minimum :
    - main.py (le code)
    - README.md (a quoi ca sert, comment lancer, pour qui)
    - .gitignore (pour ne pas pousser les .db, les logs)

## Comment on evolue
- On ne fait jamais un gros changement d'un coup.
- 1 petite amelioration = 1 commit = 1 push.
  Ex : V1 -> V1.1 ajout ville -> V1.2 rapport semaine -> V2
- On teste sur Redmi avant de pousser. Si ca ne marche pas sur Redmi, on ne pousse pas.

## Messages de commit
Toujours clair, toujours en francais :
- "V1 : ..." pour un nouvel outil
- "V1.1 : ajout ..." pour une petite amelioration
- "Fix : ..." pour corriger un bug
- "Docs : ..." pour la documentation

## Ce qu'on ne pousse JAMAIS
- *.db, *.log, venv/, __pycache__/
- Mots de passe, cles, donnees personnelles de clients

## Ce qu'on fait avant chaque push
1. Tester python3 main.py sur Redmi
2. Verifier ls -lh
3. git status pour voir ce qu'on pousse
4. git push

## Vision
Chaque outil doit repondre a : Quel probleme de Madagascar ? Pour qui ? Comment ca marche hors-ligne ?
Si on ne peut pas repondre, on ne le construit pas.
