#!/bin/bash
echo "=== BASE AITIF - $(date +%d-%m-%Y_%H:%M) ==="
P=$(tail -n +2 ~/BASE/produits.csv | wc -l)
S=$(tail -n +2 ~/BASE/savoirs.csv | wc -l)
D=$(tail -n +2 ~/BASE/domaines.csv | wc -l)
R=$(tail -n +2 ~/BASE/regions.csv | wc -l)
H=$(tail -n +2 ~/BASE/historique.csv | wc -l)
PR=$(tail -n +2 ~/07-metier-digital/projets/prix-locaux/prix-locaux.csv 2>/dev/null | wc -l)
V=$(tail -n +2 ~/BASE/ventes.csv 2>/dev/null | wc -l)
PA=$(tail -n +2 ~/BASE/partages.csv 2>/dev/null | wc -l)
AG=$(tail -n +2 ~/BASE/agents.csv 2>/dev/null | wc -l)
PJ=$(tail -n +2 ~/BASE/projets-par-domaine.csv 2>/dev/null | wc -l)
RG=$(tail -n +2 ~/BASE/regles-anti-faillite.csv 2>/dev/null | wc -l)
echo "Produits : $P - Savoirs : $S - Domaines : $D - Regions : $R - Historique : $H"
echo "Agents : $AG - Projets par domaine : $PJ - Regles anti-faillite : $RG"
echo "Stock : $(tail -n +2 ~/BASE/stock.csv | cut -d, -f1,2,3 | tr ',' ' ')"
echo "Prix reels : $PR - Ventes : $V - Partages : $PA - Faux : 0"
echo "Vision : Preparer, pas vendre. JAMAIS faillite. Faire evoluer Madagascar."
echo "--- Preuves a apporter ---"
tail -n +2 ~/BASE/preuves.csv | cut -d, -f2,3
echo "--- API ---"
curl -s https://miantsaaaa.github.io/solutions-madagascar/aitif-api.json | grep -q '"entreprise"' && echo "API en ligne : OK" || echo "API : a verifier"
echo "=== FIN BASE ==="
