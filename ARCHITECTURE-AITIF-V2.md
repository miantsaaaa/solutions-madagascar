# ARCHITECTURE AITIF V2 - PROPRE, SANS REDONDANT, SANS INCOHERENCE

Principe : 1 chose = 1 fichier. 1 appel = 1 sens. Toujours verifier avant de faire.

## ENTREE UNIQUE
- Termux -> 2) Aitif -> Ubuntu .bashrc -> relance agents 8/8 -> affiche base
- Puis : bash ~/aitif.sh - Menu 1-8, seule porte d'entree

## BASE - 1 seule verite
- BASE/*.csv = seule verite. Jamais de doublon.
- Projets : 1 seul fichier = projets-par-domaine.csv (7 domaines = 7 projets)
- Ancien projets-futurs.csv = ARCHIVE, ne plus utiliser
- Preparations : dans projets-par-domaine, pas de fichiers separes

## API - 1 seul generateur
- 1 seul fichier : generer-api-aitif.sh
- Anciens v1-v7 = ARCHIVES, ne plus utiliser
- API = lecture de BASE, jamais d'ecriture dans BASE

## AGENTS - 8, toujours
- 8 agents, chacun 1 mission, chacun 1 trace dans agents-evolution.csv
- Agents evoluent via aitif-evoluer-agents.sh, appele 1 fois par aitif-evolue.sh
- Agents ne rappellent jamais API en boucle

## APPELS - 1 sens, jamais de boucle
- aitif.sh -> aitif-base / ajouter-* / partager / evolue / evoluer-agents
- aitif-evolue.sh -> generer-api-aitif.sh + verifier-base + evoluer-agents (1 fois chacun)
- verifier-* ne cree rien, il verifie seulement
- Jamais : A appelle B qui appelle A

## SECURITE
- .bashrc JAMAIS dans git - prive Termux
- 0 faux prix - garde-fou verifier-base-aitif.sh

## REGLE D'OR
- Avant de creer : bash ~/verifier-avant-faire.sh + verifier architecture
- Si doublon -> on complete l'existant, on ne cree pas
- Si incoherence -> on corrige d'abord, on ne cree pas par-dessus
