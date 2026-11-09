# Test de stabilite Commerce Aitif - V1.9
# Pas de nouvelle fonction, juste la preuve que tout tient.
# Lance : python3 test_stabilite.py
# Si tout est OK, Commerce Aitif est stable.

import sys
print("=== TEST STABILITE - COMMERCE AITIF V1.9 ===")
ok = True

try:
    import db, produits_aitif, main
    print("OK : imports db + produits_aitif + main")
except Exception as e:
    print("ECHEC imports :", e)
    ok = False

try:
    db.init_db()
    print("OK : base commerce.db initialisee")
except Exception as e:
    print("ECHEC base :", e)
    ok = False

try:
    produits_aitif.produits_aitif()
    print("OK : produits Aitif affichent")
except Exception as e:
    print("ECHEC produits :", e)
    ok = False

print("RESULTAT :", "STABLE ✅" if ok else "A REPARER ❌")
sys.exit(0 if ok else 1)
