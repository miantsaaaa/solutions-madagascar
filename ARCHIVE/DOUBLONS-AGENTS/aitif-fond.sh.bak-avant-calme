#!/bin/bash
# AITIF FOND - Je travaille en fond, chaque heure, sans que tu ouvres
# Agent 00 ecrit son rapport tout seul, comme un employe serieux
while true; do
  DATE=$(date +%d-%m-%Y_%H:%M)
  AGENTS=$(for i in 00 01 02 03 04 05 06 07; do pgrep -f "agent${i}_loop" >/dev/null && echo 1; done | wc -l)
  PRIX=$(tail -n +2 ~/BASE/prix-reels.csv 2>/dev/null | grep -c .)
  echo "$DATE - FOND : Agents $AGENTS/8, Prix reels $PRIX, Je travaille. Meilleure action : Partager 1 savoir (marge = vente - achat - frais)." >> ~/FONDATION-AITIF/NOUVELLES-DU-JOUR.md
  # Sauvegarde auto chaque heure
  cp ~/FONDATION-AITIF/MEMOIRE-AGENT-00.md ~/SAUVEGARDE-AITIF/ 2>/dev/null
  sleep 3600
done
