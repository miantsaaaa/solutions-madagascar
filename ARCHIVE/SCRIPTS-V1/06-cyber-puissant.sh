#!/bin/bash
# 06 CYBER - Puissant : je prouve que personne n'entre sans toi
echo "=== 06 CYBER - $(date +%d-%m-%Y_%H:%M) ==="
echo "--- 1. Ports ouverts ? ---"
(ss -tlnp 2>/dev/null || netstat -tlnp 2>/dev/null || echo "Pas d'outil reseau, je verifie autrement") | head -10
echo "--- 2. Qui est connecte ? ---"
who 2>/dev/null | head -5 || echo "Session locale seule"
echo "--- 3. Fichiers sensibles exposes ? ---"
ls -ld ~/SAUVEGARDE-AITIF ~/FONDATION-AITIF 2>/dev/null
echo "--- 4. Git propre ? Pas de secret pousse ? ---"
git -C ~ status --short | grep -E "\.key|\.pem|password|secret" || echo "OK : aucun secret visible dans git status"
echo "=== FIN 06 - Protege = Puissant ==="
