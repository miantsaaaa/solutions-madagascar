#!/bin/bash
# AITIF V2 - J'evolue : 1 sens, 1 fois chacun, jamais de boucle
echo "=== AITIF EVOLUE V2 - $(date +%d-%m-%Y_%H:%M) ==="
bash ~/generer-api-aitif.sh
bash ~/verifier-base-aitif.sh 2>/dev/null | tail -5
bash ~/aitif-evoluer-agents.sh 2>/dev/null | tail -3
echo "=== FIN EVOLUTION V2 ==="
