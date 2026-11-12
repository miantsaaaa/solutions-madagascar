#!/bin/bash
echo "=== AITIF - AJOUTER 1 VRAI PRIX - VU AU MARCHE ==="
echo "Regle : REEL = vu. Pas vu = pas de prix."
read -p "Produit (ex: Riz) : " PRODUIT
read -p "Prix en Ar (ex: 5000) : " PRIX
read -p "Unite (kg / L / piece) : " UNITE
read -p "Region (ex: Haute Matsiatra) : " REGION
read -p "Ville (ex: Fianarantsoa) : " VILLE
read -p "Lieu exact (ex: Marche Anjoma) : " LIEU
read -p "Source (ex: Vendeuse Anjoma) : " SOURCE
read -p "Vu par (ex: Miantsa) : " VU
DATE=$(date +%d-%m-%Y)
FICHIER=~/07-metier-digital/projets/prix-locaux/prix-locaux.csv
echo "$DATE,$REGION,$VILLE,$LIEU,$PRODUIT,$PRIX,$UNITE,$SOURCE,$VU" >> $FICHIER
echo "Prix REEL ajoute : $PRODUIT $PRIX Ar / $UNITE - $VILLE - $LIEU - $DATE - vu par $VU"
bash ~/generer-api-base-v4.sh | tail -1
bash ~/verifier-base-aitif.sh | tail -3
echo "=== FIN - Prix reel dans la base ==="
