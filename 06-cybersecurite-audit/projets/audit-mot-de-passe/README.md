# Audit Mot de Passe - V6.1
## Probleme Madagascar
Beaucoup de comptes Facebook, Gmail, Mobile Money sont piratés à Madagascar
parce que le mot de passe est faible : 123456, madagascar, date de naissance.

## Solution
Outil qui teste la force de ton mot de passe, 100% hors-ligne, sur Redmi.
Il ne sauvegarde JAMAIS ton mot de passe, il te donne juste un score.

## Comment lancer
python3 main.py

## Fonctions V6.1
- Longueur, majuscule, chiffre, caractere special
- Detecte les mots de passe connus (123456, password, madagascar)
- Score / 100 + conseil

## Prochaines versions
- V6.2 : generateur mot de passe fort
- V6.3 : audit des fichiers sensibles (ne jamais pousser .env, cles)
- V6.4 : scan ports ouverts sur ton reseau
- V6.5 : rapport audit securite complet
