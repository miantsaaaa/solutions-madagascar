#!/bin/bash
# AITIF FOND - CALME V2 - Je travaille en fond, chaque heure, sans salir
# Regle V2 : 1 seule ecriture autorisee = BASE. FONDATION et SAUVEGARDE ne sont pas BASE.
# On ecrit dans /tmp, jamais dans FONDATION, jamais de copie vers SAUVEGARDE.
while true; do
  DATE=$(date +%d-%m-%Y_%H:%M)
  AGENTS=$(for i in 00 01 02 03 04 05 06 07; do pgrep -f "agent${i}_loop" >/dev/null && echo 1; done | wc -l)
  PRIX=$(tail -n +2 ~/BASE/prix-reels.csv 2>/dev/null | grep -c .)
  echo "$DATE - FOND : Agents $AGENTS/8, Prix reels $PRIX, Je travaille. Meilleure action : Partager 1 savoir." >> /tmp/aitif-fond.log
  sleep 3600
done
