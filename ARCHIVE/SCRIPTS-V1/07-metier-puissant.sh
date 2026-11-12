#!/bin/bash
# 07 METIER - Puissant : visible partout, leger partout, meme avec 100 prix
echo "=== 07 METIER - $(date +%d-%m-%Y_%H:%M) ==="
echo "--- 1. Site en ligne ? ---"
curl -s -o /dev/null -w "Portfolio : %{http_code}\n" https://miantsaaaa.github.io/solutions-madagascar/
curl -s -o /dev/null -w "Prix : %{http_code}\n" https://miantsaaaa.github.io/solutions-madagascar/prix.html
echo "--- 2. Poids : leger = puissant sur 4G faible ---"
ls -lh ~/docs/*.html | awk '{print $9, $5}'
TOTAL=$(du -sb ~/docs | cut -f1)
echo "Total docs : $TOTAL octets"
if [ "$TOTAL" -lt 50000 ]; then echo "OK : < 50 Ko total, ultra-leger, 4G faible OK"; else echo "ALERTE : trop lourd, a alleger"; fi
echo "--- 3. Prix sur le site = prix dans le CSV ? ---"
echo "CSV : $(tail -n +2 ~/07-metier-digital/projets/prix-locaux/prix-locaux.csv | grep -c .) prix reels"
grep -o "0 prix" ~/docs/prix.html | head -1 || echo "prix.html : a regenerer"
echo "=== FIN 07 - Visible + Leger = Puissant ==="
