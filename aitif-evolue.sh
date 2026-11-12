#!/bin/bash
# AITIF - J'evolue : CSV -> site -> memoire, sans recoder
echo "=== AITIF EVOLUE - $(date +%d-%m-%Y_%H:%M) ==="
echo "--- 1. Je regenere le site depuis le reel ---"
python3 ~/07-metier-digital/projets/prix-locaux/generer-prix-html.py 2>/dev/null || echo "Generateur prix.html : deja a jour / a verifier"
echo "--- 2. Je recalcule les marges depuis le reel ---"
python3 ~/07-metier-digital/projets/prix-locaux/calculer-marge.py 2>/dev/null || echo "Marge : pas de prix reel, j'attends, je n'invente rien"
echo "--- 3. Je regenere les donnees jeu / site ---"
bash ~/generer-jeu-data.sh 2>/dev/null | head -1 || echo "Jeu-data : script absent, on le recreera si besoin"
echo "--- 4. Je verifie que je suis toujours vivant ---"
bash ~/systeme-intelligent-aitif.sh | grep -E "Prix reels|Je ne sais|Memoire"
echo "=== FIN EVOLUTION - Pret pour le prochain reel ==="
bash ~/generer-api-base-v2.sh 2>/dev/null | head -1
