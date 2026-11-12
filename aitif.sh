#!/bin/bash
echo "=== AITIF - BASE ==="
echo "1) Voir la base"
echo "2) Ajouter 1 savoir"
echo "3) Ajouter 1 vrai prix"
echo "4) Partager 1 savoir"
echo "5) Faire evoluer la base"
echo "6) Ajouter 1 produit"
echo "0) Quitter"
read -p "Choix : " C
case $C in
  1) bash ~/aitif-base.sh ;;
  2) bash ~/aitif-ajouter-savoir.sh ;;
  3) bash ~/aitif-ajouter-prix.sh ;;
  4) bash ~/aitif-partager-savoir.sh ;;
  5) bash ~/aitif-evolue.sh ;;
  6) bash ~/aitif-ajouter-produit.sh ;;
  0) echo "Aitif dort. Base sauvee." ;;
  *) echo "Choix 0-6" ;;
esac
