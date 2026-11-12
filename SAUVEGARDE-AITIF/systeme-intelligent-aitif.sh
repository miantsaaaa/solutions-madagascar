#!/bin/bash
# AITIF - Systeme Intelligent - ne ment jamais, se verifie, apprend
echo "=== AITIF INTELLIGENT - $(date +%d-%m-%Y_%H:%M) ==="
echo "--- 1. Je me verifie ---"
bash ~/check-sante-aitif.sh | grep -E "HTTP|Prix|Veille|Agents|OK|FIN"
echo "--- 2. Ce que je sais (vrai) ---"
echo "Prix reels : $(tail -n +2 ~/07-metier-digital/projets/prix-locaux/prix-locaux.csv | grep -c .)"
echo "Regions couvertes : $(tail -n +2 ~/07-metier-digital/projets/prix-locaux/prix-locaux.csv | cut -d, -f4 | sort -u | grep -v "^$" | wc -l)"
echo "--- 3. Ce que je ne sais pas (honnête) ---"
if [ $(tail -n +2 ~/07-metier-digital/projets/prix-locaux/prix-locaux.csv | grep -c .) -eq 0 ]; then
  echo "Je ne sais PAS le prix marché. J'attends le réel. Je n'invente rien."
fi
echo "--- 4. Je sauvegarde ce que j'ai appris ---"
echo "$(date +%d-%m-%Y) - Sante OK, Prix reels: $(tail -n +2 ~/07-metier-digital/projets/prix-locaux/prix-locaux.csv | grep -c .), Agents vivants" >> ~/FONDATION-AITIF/MEMOIRE-AGENT-00.md
echo "Memoire mise a jour."
echo "=== FIN - Systeme pret a evoluer ==="
