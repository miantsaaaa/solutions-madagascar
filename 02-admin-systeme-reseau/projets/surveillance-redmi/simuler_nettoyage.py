# Simuler nettoyage Aitif - V2.7
# Vraie amelioration : voir avant de supprimer.
# Lance : python3 simuler_nettoyage.py
import glob
print("=== SIMULATION NETTOYAGE AITIF. - V2.7 ===")
print("Ce qui serait supprime, sans rien supprimer :")
for p in glob.glob("/root/**/__pycache__", recursive=True):
    print(" - cache :", p)
for p in glob.glob("/root/**/*.log", recursive=True):
    print(" - log :", p)
print("Tes .db, .csv, .md et projets ne sont JAMAIS touches.")
print("Pour vraiment nettoyer : python3 nettoyage.py")
