#!/bin/bash
echo "=== BILAN PUISSANCE AITIF - $(date +%d-%m-%Y_%H:%M) ==="
echo "00 CHEF :"; bash ~/systeme-intelligent-aitif.sh | grep -E "Prix reels|Je ne sais"
echo "02 SURVEILLANCE :"; bash ~/02-surveillance-puissant.sh | grep -E "Agents|Wake|OK"
echo "04 DATA :"; bash ~/04-data-puissant.sh | grep -E "Prix reels|OK|REFUSEE"
echo "06 CYBER :"; bash ~/06-cyber-puissant.sh | grep -E "OK|Ports"
echo "07 METIER :"; bash ~/07-metier-puissant.sh | grep -E "Portfolio|Total|OK"
echo "01/03/05 : Prets, en attente du reel - voir 01-03-05-en-attente.md"
echo "=== FIN BILAN - 5 puissants, 3 prets ==="
