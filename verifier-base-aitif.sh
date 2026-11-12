#!/bin/bash
echo "=== VERIFIER BASE AITIF - $(date +%d-%m-%Y_%H:%M) ==="
echo "Produits : $(tail -n +2 ~/BASE/produits.csv | wc -l)"
echo "Savoirs : $(tail -n +2 ~/BASE/savoirs.csv | wc -l)"
echo "Domaines : $(tail -n +2 ~/BASE/domaines.csv | wc -l)"
echo "Regions : $(tail -n +2 ~/BASE/regions.csv | wc -l)"
echo "Historique : $(tail -n +2 ~/BASE/historique.csv | wc -l)"
echo "Stock : $(cat ~/BASE/stock.csv)"
echo "Prix reels : $(tail -n +2 ~/07-metier-digital/projets/prix-locaux/prix-locaux.csv 2>/dev/null | wc -l)"
# Regle d'or : pas de prix sans source
if grep -q "TEST\|FAKE\|SIMULATION" ~/07-metier-digital/projets/prix-locaux/prix-locaux.csv 2>/dev/null; then
  echo "ALERTE : faux prix detecte dans prix-locaux.csv - a nettoyer"
else
  echo "OK : 0 faux prix - base propre"
fi
# API en ligne ?
curl -s https://miantsaaaa.github.io/solutions-madagascar/aitif-api.json | grep -q '"entreprise": "AITIF"' && echo "OK : API en ligne" || echo "VEILLE : API pas encore en ligne"
echo "=== FIN VERIFICATION ==="
