#!/bin/bash
# AITIF - Relance les 8 Agents en 1 commande, chacun depuis SON dossier
cd ~
for spec in "00:FONDATION-AITIF:agent00_loop.py" "01:01-genie-logiciel-et-bdd/projets/gestion-commerce-madagascar:agent01_loop.py" "02:02-admin-systeme-reseau/projets/surveillance-*/agent02_loop.py" "03:03-intelligence-artificielle/projets/prediction-ventes:agent03_loop.py" "04:04-gouvernance-ingenierie-data/projets/qualite-donnees:agent04_loop.py" "05:05-objets-connectes-iot/projets/capteur-temperature:agent05_loop.py" "06:06-cybersecurite-audit/projets/audit-mot-de-passe:agent06_loop.py" "07:07-metier-digital/projets/portfolio-entreprise:agent07_loop.py"; do
  n=${spec%%:*}; rest=${spec#*:}; d=${rest%%:*}; f=${rest#*:}
  (cd ~/$d && rm -f AGENT-${n}.pid && nohup python3 $f > agent${n}.log 2>&1 & echo $! > AGENT-${n}.pid && echo "Agent $n relance PID $(cat AGENT-${n}.pid)")
done
sleep 2
for i in 00 01 02 03 04 05 06 07; do pgrep -f "agent${i}_loop" >/dev/null && echo "Agent $i : VIVANT" || echo "Agent $i : ARRETE"; done
