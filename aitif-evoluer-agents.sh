#!/bin/bash
echo "=== AITIF - AGENTS EVOLUENT - $(date +%d-%m-%Y_%H:%M) ==="
P=$(tail -n +2 ~/BASE/produits.csv | wc -l)
S=$(tail -n +2 ~/BASE/savoirs.csv | wc -l)
PR=$(tail -n +2 ~/BASE/projets-futurs.csv | wc -l)
RG=$(tail -n +2 ~/BASE/regles-anti-faillite.csv | wc -l)
DATE=$(date +%d-%m-%Y)
echo "$DATE,00 Memoire,Je me souviens de $P produits + $S savoirs + $PR projets" >> ~/BASE/agents-evolution.csv
echo "$DATE,05 Prevention,Je garde $RG regles - Si 0 client 1 jour on survit ?" >> ~/BASE/agents-evolution.csv
echo "00 Memoire : Je me souviens de $P produits + $S savoirs + $PR projets"
echo "05 Prevention : Je garde $RG regles - jamais faillite"
echo "Agents ont evolue - trace ecrite dans agents-evolution.csv"
bash ~/generer-api-base-v6.sh | tail -1
echo "=== FIN - Agents ont evolue ==="
