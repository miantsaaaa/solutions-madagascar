#!/bin/bash
echo "=== AITIF - BASE ==="
echo "1) Voir la base"
echo "2) Ajouter 1 savoir"
echo "3) Ajouter 1 vrai prix"
echo "4) Partager 1 savoir"
echo "5) Faire evoluer la base"
echo "6) Ajouter 1 produit"
echo "7) Voir plan demain"
echo "8) Voir agents qui evoluent"
echo "0) Quitter"
read -p "Choix : " C
case $C in
  1) bash ~/aitif-base.sh ;;
  2) bash ~/aitif-ajouter-savoir.sh ;;
  3) bash ~/aitif-ajouter-prix.sh ;;
  4) bash ~/aitif-partager-savoir.sh ;;
  5) bash ~/aitif-evolue.sh ;;
  6) bash ~/aitif-ajouter-produit.sh ;;
  7) cat ~/PLAN-DEMAIN-13-11-2026.md ;;
  8) bash ~/aitif-evoluer-agents.sh ;;
  0) echo "Aitif dort. Base sauvee." ;;
  *) echo "Choix 0-8" ;;
esac
