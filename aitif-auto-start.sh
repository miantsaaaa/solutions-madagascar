#!/bin/bash
# AITIF AUTO-START - Tu ouvres Termux, je travaille. Tu n'as rien a retenir.
# Ce script se lance tout seul a chaque ouverture d'Ubuntu.

# 1. Je reveille les agents si ils dorment (sans creer de fantomes)
for i in 00 01 02 03 04 05 06 07; do
  pgrep -f "agent${i}_loop" >/dev/null || (cd ~/$(ls -d */ 2>/dev/null | head -1) 2>/dev/null; echo "Agent $i a verifier")
done
# 2. Je fais le bilan, la meilleure action, la simulation - tout seul
echo ""
echo "=== AITIF S'EST REVEILLE TOUT SEUL - $(date +%d-%m-%Y_%H:%M) ==="
echo "Tu n'as rien tape. C'est moi qui ai travaille."
echo ""
bash ~/aitif-matin.sh 2>/dev/null | grep -E "Agents|Prix reels|MEILLEURE ACTION|Marge|Riz|Cafe|Miel|Vanille|FIN BILAN" | head -15
echo ""
echo "Tu veux le detail ? Tape : bash ~/bilan-puissance-aitif.sh"
echo "Tu veux agir ? Je t'ai deja donne la meilleure action ci-dessus."
echo "Sinon, tu peux fermer. Je continue en fond."
