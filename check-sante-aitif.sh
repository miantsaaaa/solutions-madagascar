#!/bin/bash
echo "=== SANTE AITIF - $(date +%d-%m-%Y_%H:%M) ==="
echo "--- 1. Site en ligne ---"
curl -s -o /dev/null -w "Portfolio : HTTP %{http_code}\n" https://miantsaaaa.github.io/solutions-madagascar/
curl -s -o /dev/null -w "Prix : HTTP %{http_code}\n" https://miantsaaaa.github.io/solutions-madagascar/prix.html
curl -s -o /dev/null -w "Ajouter prix : HTTP %{http_code}\n" https://miantsaaaa.github.io/solutions-madagascar/ajouter-prix.html
echo "--- 2. Prix Locaux - donnees ---"
wc -l ~/07-metier-digital/projets/prix-locaux/prix-locaux.csv
head -1 ~/07-metier-digital/projets/prix-locaux/prix-locaux.csv
echo "--- 3. Veille ---"
python3 ~/07-metier-digital/projets/prix-locaux/veille-auto.py | head -2
echo "--- 4. Agents 01-07 ---"
ps aux | grep -c "[a]gent0"
echo "--- 5. Git propre ? ---"
git -C ~ status --short | grep -v "MESSAGE-AGENT\|DISCUSSION\|STATUS-AGENT\|__pycache__\|.bash_history\|agent0.*\.bak" | head -5 || echo "Propre (hors logs agents)"
echo "--- 6. Poids pages (4G faible) ---"
ls -lh ~/docs/*.html | awk '{print $9, $5}'
echo "=== FIN SANTE ==="
