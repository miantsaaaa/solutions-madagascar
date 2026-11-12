#!/bin/bash
# AITIF - Chaque matin, 1 seule meilleure action, celle qui fait le plus gagner
echo "=== MEILLEURE ACTION DU JOUR - $(date +%d-%m-%Y) ==="
echo ""
# Logique autonome, simple et honnete :
# - Si 0 prix reel -> meilleure action = preparer + simuler, pas vendre a l'aveugle
# - Si simulation dit PERTE -> eviter ce produit
# - Si site lourd -> alleger. Si agents morts -> relancer. Sinon -> eduquer.
PRIX_REEL=$(tail -n +2 ~/07-metier-digital/projets/prix-locaux/prix-locaux.csv | grep -c .)
AGENTS=$(for i in 00 01 02 03 04 05 06 07; do pgrep -f "agent${i}_loop" >/dev/null && echo 1; done | wc -l)
echo "Etat : Prix reel $PRIX_REEL | Agents $AGENTS/8"
echo ""
if [ "$AGENTS" -lt 8 ]; then
  echo "MEILLEURE ACTION : Relancer les agents - sans eux, rien ne marche."
  echo "Commande : bash ~/relancer_agents.sh"
elif [ "$PRIX_REEL" -eq 0 ]; then
  echo "MEILLEURE ACTION : Partager 1 savoir Aitif aujourd'hui."
  echo "Pourquoi ? Pas de prix = pas de vente juste. Mais 1 savoir partage = 1 personne qui apprend"
  echo "a calculer sa marge, a ne pas vendre a perte comme le Riz simule -1200 Ar."
  echo ""
  echo "Action concrete :"
  echo "  Marge = Vente - Achat - Frais"
  echo "  Exemple Miel : 18000 - 12000 = 6000 Ar de marge simulee."
  echo "  Si tu vends sans calculer, tu peux perdre. Si tu calcules, tu gagnes."
  echo "  Partage ca a 1 personne, en malgache + francais, aujourd'hui."
else
  echo "MEILLEURE ACTION : Verifier le vrai prix, calculer la vraie marge, proposer 1 vente."
  echo "Commande : bash ~/aitif-evolue.sh"
fi
echo ""
echo "2eme action (si tu as le temps) : Verifier que le pot Miel est propre, etiquette prete."
echo "=== FIN - 1 action, pas 100, celle qui compte ==="
