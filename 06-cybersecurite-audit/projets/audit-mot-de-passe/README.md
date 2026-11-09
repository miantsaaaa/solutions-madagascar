# Cyber Aitif - Audit Mot de Passe - V6.8

## Probleme Madagascar
Beaucoup de comptes Facebook, Gmail, Mobile Money sont pirates a Madagascar
parce que le mot de passe est faible : 123456, madagascar, date de naissance.

## Solution Aitif
Outil qui teste la force de ton mot de passe, 100% hors-ligne, sur Redmi.
Il ne sauvegarde JAMAIS ton mot de passe, il te donne juste un score.
Petit a petit, toujours bien organise. On ne promet pas, on prouve.

## Comment lancer
python3 main.py
python3 generateur.py
python3 audit_fichiers.py
python3 scan_ports.py
python3 rapport_audit.py
python3 checklist_aitif.py

## Structure - plusieurs fichiers, pas trop de code dans un fichier
- `main.py` - teste la force, score / 100 + conseil, jamais sauvegarde
- `generateur.py` - genere un mot de passe fort, hors-ligne, a copier 1 fois
- `audit_fichiers.py` - verifie que tu n'as pas de .env, cles, mots de passe dans ton depot
- `scan_ports.py` - scanne TON propre Redmi / localhost, jamais celui des autres
- `rapport_audit.py` - rapport complet : fichiers + .gitignore + ports + sauvegardes
- `checklist_aitif.py` - 5 checks rapides avant de pousser, VERT = tu peux pousser

## Fonctions
- Longueur, majuscule, chiffre, caractere special
- Detecte les mots de passe connus (123456, password, madagascar)
- Score / 100 + conseil
- Checklist rapide avant chaque push

## Regles Aitif
Verification ne compte pas comme version, seule une amelioration compte comme Vx.x.
Sans frais, la marge ment. Avec frais, on sait vraiment.
Aitif ne pousse jamais avec un rouge.
Ne scanne JAMAIS le reseau de quelqu'un d'autre sans son accord.

## Pour qui
Pour tout commercant a Madagascar qui veut proteger ses comptes, son depot, et son Redmi.
