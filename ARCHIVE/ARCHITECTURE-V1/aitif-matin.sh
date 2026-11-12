#!/bin/bash
# AITIF MATIN - 1 commande, tout le systeme se reveille
echo "=== BONJOUR MIANTISA - AITIF SE REVEILLE - $(date +%d-%m-%Y_%H:%M) ==="
bash ~/bilan-puissance-aitif.sh | grep -E "Prix reels|Agents|OK|Total|FIN"
echo ""
bash ~/aitif-meilleure-action.sh | grep -A 8 "MEILLEURE ACTION"
echo ""
bash ~/simuler-aitif.sh | grep -E "Riz|Cafe|Miel|Vanille" | head -4
echo ""
echo "Tu lances ca chaque matin : bash ~/aitif-matin.sh"
echo "Et Aitif te dit : je suis vivant, voila ma meilleure action, voila ce que j'ai appris."
