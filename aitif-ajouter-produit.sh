#!/bin/bash
echo "=== AITIF - AJOUTER 1 PRODUIT ==="
read -p "Nom produit (ex: Gingembre) : " NOM
read -p "Categorie (Alimentation / Epice / Autre) : " CAT
read -p "Unite (kg / L / piece) : " UNITE
read -p "Saison (Toute annee / Saison seche / Saison recolte) : " SAISON
read -p "Note (ex: Produit local) : " NOTE
echo "$NOM,$CAT,$UNITE,$SAISON,$NOTE" >> ~/BASE/produits.csv
echo "Produit ajoute : $NOM - $CAT - $UNITE - $SAISON"
echo "12-11-2026,Miantsa + Meta AI,Produit ajoute,$NOM - $CAT" >> ~/BASE/historique.csv
bash ~/generer-api-base-v7.sh | tail -1
echo "=== FIN - Produit dans la base ==="
