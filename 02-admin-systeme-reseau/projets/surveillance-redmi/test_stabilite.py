# Test de stabilite Surveillance Aitif - V2.6
# Pas de nouvelle fonction, juste la preuve que tout tient.
# Lance : python3 test_stabilite.py
import sys
print("=== TEST STABILITE - SURVEILLANCE AITIF V2.6 ===")
ok = True
try:
    import main, rapport, alerte, nettoyage, sauvegarde
    print("OK : imports main + rapport + alerte + nettoyage + sauvegarde")
except Exception as e:
    print("ECHEC imports :", e)
    ok = False
try:
    main.check_stockage()
    print("OK : check_stockage tourne")
except Exception as e:
    print("ECHEC stockage :", e)
    ok = False
print("RESULTAT :", "STABLE ✅" if ok else "A REPARER ❌")
sys.exit(0 if ok else 1)
