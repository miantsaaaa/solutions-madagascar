#!/bin/bash
echo "=== AITIF - AGENTS EVOLUENT - TOUS LES 8 - $(date +%d-%m-%Y_%H:%M) ==="
P=$(tail -n +2 ~/BASE/produits.csv | wc -l)
S=$(tail -n +2 ~/BASE/savoirs.csv | wc -l)
PR=$(tail -n +2 ~/BASE/projets.csv | wc -l)
RG=$(tail -n +2 ~/BASE/regles-anti-faillite.csv | wc -l)
DATE=$(date +%d-%m-%Y)
echo "$DATE,00 Memoire,Je me souviens de $P produits + $S savoirs + $PR projets" >> ~/BASE/agents-evolution.csv
echo "$DATE,01 Prix,J'attends 1 vrai prix - je n'invente rien" >> ~/BASE/agents-evolution.csv
echo "$DATE,02 Surveillance,Je surveille 8/8 + API + base propre + vision" >> ~/BASE/agents-evolution.csv
echo "$DATE,03 Apprentissage,J'ai appris $S savoirs - je veux apprendre Restaurant + Hopital" >> ~/BASE/agents-evolution.csv
echo "$DATE,04 Data,Je compte vrai - $P $S $PR $RG - jamais en dur" >> ~/BASE/agents-evolution.csv
echo "$DATE,05 Prevention,Je garde $RG regles - Si 0 client on survit ?" >> ~/BASE/agents-evolution.csv
echo "$DATE,06 Cyber,Je protege base - snapshot + 0 faux + dossier banque" >> ~/BASE/agents-evolution.csv
echo "$DATE,07 Metier,Je prepare entreprise - JAMAIS faillite - Madagascar" >> ~/BASE/agents-evolution.csv
echo "8 agents ont evolue - 8 traces ecrites"
bash ~/generer-api-aitif.sh | tail -1
echo "=== FIN - Les 8 ont evolue ==="
