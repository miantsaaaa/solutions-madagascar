#!/bin/bash
echo "=== AITIF - AJOUTER 1 SAVOIR ==="
echo "Domaines : Agriculture Education Sante Energie/Eau Environnement Numerique Commerce"
read -p "Titre : " TITRE
read -p "Domaine : " DOMAINE
read -p "En malgache : " MG
read -p "En francais : " FR
DATE=$(date +%d-%m-%Y)
echo "$TITRE,$DOMAINE,$MG,$FR,$DATE" >> ~/BASE/savoirs.csv
echo "Savoir ajoute : $TITRE - $DOMAINE - $DATE"
bash ~/generer-api-base-v4.sh | tail -1
echo "12-11-2026,Miantsa + Meta AI,Savoir ajoute,$TITRE - $DOMAINE" >> ~/BASE/historique.csv
bash ~/generer-api-base-v4.sh | tail -1
echo "=== FIN - Savoir dans la base, API a jour ==="
