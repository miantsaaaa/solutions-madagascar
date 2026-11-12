#!/bin/bash
echo "=== BASE AITIF - $(date +%d-%m-%Y_%H:%M) ==="
echo "Produits : 12 - Savoirs : 9 - Domaines : 7 - Regions : 23"
echo "Stock : 1L Miel, Fianarantsoa, en main"
echo "Prix reels : 0 - Ventes : 0 - Faux : 0"
echo "--- Preuves a apporter ---"
tail -n +2 ~/BASE/preuves.csv | cut -d, -f2,3
echo "--- API ---"
curl -s https://miantsaaaa.github.io/solutions-madagascar/aitif-api.json | grep -q '"entreprise"' && echo "API en ligne : OK" || echo "API : a verifier"
echo "=== FIN BASE ==="
