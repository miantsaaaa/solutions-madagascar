#!/bin/bash
echo "=== AITIF - PARTAGER 1 SAVOIR A 1 PERSONNE ==="
echo "--- Savoirs dans la base ---"
cat ~/BASE/savoirs.csv | tail -n +2 | cut -d, -f1,2 | nl
read -p "Numero du savoir partage (ex: 10) : " NUM
read -p "A qui tu l'as partage ? (prenom) : " QUI
read -p "Ou / Comment ? (ex: Marche, bouche a oreille) : " OU
DATE=$(date +%d-%m-%Y)
SAVOIR=$(sed -n "$((NUM+1))p" ~/BASE/savoirs.csv | cut -d, -f1)
echo "$DATE,$QUI,$SAVOIR,$OU" >> ~/BASE/partages.csv 2>/dev/null || echo "date,qui,savoir,ou
$DATE,$QUI,$SAVOIR,$OU" > ~/BASE/partages.csv
echo "Partage enregistre : $DATE - $SAVOIR -> $QUI - $OU"
echo "12-11-2026,Miantsa + Meta AI,Savoir partage,$SAVOIR -> $QUI" >> ~/BASE/historique.csv
bash ~/generer-api-aitif.sh | tail -1
echo "=== FIN - Savoir partage, base a jour ==="
