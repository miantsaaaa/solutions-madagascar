#!/bin/bash
# 02 SURVEILLANCE - Puissant : je survis, je relance, je sauvegarde
echo "=== 02 SURVEILLANCE - $(date +%d-%m-%Y_%H:%M) ==="
echo "--- 1. Agents vivants ? ---"
VIVANTS=$(for i in 00 01 02 03 04 05 06 07; do pgrep -f "agent${i}_loop" >/dev/null && echo 1; done | wc -l)
echo "Agents : $VIVANTS / 8 attendus"
if [ "$VIVANTS" -lt 8 ]; then
  echo "ALERTE : il manque des agents - je relance..."
  bash ~/relancer_agents.sh 2>/dev/null | tail -3 || echo "Relance : verifier relancer_agents.sh"
else
  echo "OK : tous vivants, je ne touche a rien."
fi
echo "--- 2. Batterie / Termux ---"
termux-wake-lock 2>/dev/null && echo "Wake-lock : ON" || echo "Wake-lock : a verifier dans Termux"
echo "--- 3. Sauvegarde : si Redmi meurt, Aitif ne meurt pas ---"
mkdir -p ~/SAUVEGARDE-AITIF
cp ~/check-sante-aitif.sh ~/systeme-intelligent-aitif.sh ~/aitif-evolue.sh ~/ARCHITECTURE-AITIF.md ~/SAUVEGARDE-AITIF/ 2>/dev/null
cp -r ~/07-metier-digital/projets/prix-locaux/*.csv ~/SAUVEGARDE-AITIF/ 2>/dev/null
cp -r ~/FONDATION-AITIF/MEMOIRE-AGENT-00.md ~/SAUVEGARDE-AITIF/ 2>/dev/null
ls -lh ~/SAUVEGARDE-AITIF/ | head -8
echo "Sauvegarde : OK - $(date +%d-%m-%Y_%H:%M)"
echo "=== FIN 02 - Je surveille, donc Aitif vit ==="
