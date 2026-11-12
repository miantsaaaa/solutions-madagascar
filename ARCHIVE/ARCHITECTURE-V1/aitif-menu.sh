#!/bin/bash
# AITIF MENU - A l'ouverture de Termux, tu choisis
# Fond : toujours vivant, meme si tu choisis $
pgrep -f "aitif-fond.sh" >/dev/null || (nohup bash ~/aitif-fond.sh > ~/aitif-fond.log 2>&1 &)

echo ""
echo "=============================="
echo "  BONJOUR MIANTISA - AITIF"
echo "  $(date +%d-%m-%Y_%H:%M) - Madagascar"
echo "=============================="
echo ""
echo "  1) $  - Terminal normal"
echo "     Je veux juste taper mes commandes."
echo ""
echo "  2) AITIF - Entrer dans mon entreprise"
echo "     Bilan + Meilleure action + Simulation + Plan demain"
echo ""
echo "  0) Quitter"
echo ""
read -p "Ton choix [1/2/0] : " CHOIX
case "$CHOIX" in
  1)
    echo ""
    echo "OK - Terminal normal. Aitif continue en fond."
    echo "Si tu changes d'avis : bash ~/aitif-menu.sh"
    ;;
  2)
    echo ""
    echo "=== TU ENTRES DANS AITIF ==="
    bash ~/aitif-matin.sh 2>/dev/null
    echo ""
    echo "Tu es dans Aitif. Pour revoir le menu : bash ~/aitif-menu.sh"
    ;;
  0)
    echo "A demain, Miantsa. Aitif continue en fond."
    ;;
  *)
    echo "Choix non compris - je te laisse en Terminal $. Tape bash ~/aitif-menu.sh pour revoir."
    ;;
esac
