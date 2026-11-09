# Nettoyage auto - V2.3 - Domaine 02
# Nettoie les fichiers temporaires sans toucher a tes donnees
import os, shutil, glob

def taille_dossier(path):
    total = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except:
                pass
    return total

def nettoyer():
    print("=== NETTOYAGE AUTO - REDMI ===")
    libere = 0
    # 1. __pycache__
    for p in glob.glob("/root/**/__pycache__", recursive=True):
        try:
            s = taille_dossier(p)
            shutil.rmtree(p)
            libere += s
            print(f"Supprime : {p} ({s//1024} Ko)")
        except Exception as e:
            print(f"Erreur {p} : {e}")
    # 2. *.log
    for p in glob.glob("/root/**/*.log", recursive=True):
        try:
            s = os.path.getsize(p)
            os.remove(p)
            libere += s
            print(f"Supprime : {p} ({s//1024} Ko)")
        except:
            pass
    # 3. *.pyc
    for p in glob.glob("/root/**/*.pyc", recursive=True):
        try:
            s = os.path.getsize(p)
            os.remove(p)
            libere += s
            print(f"Supprime : {p}")
        except:
            pass
    print(f"\nTotal libere : {libere//1024} Ko ({libere//(1024*1024)} Mo)")
    print("Tes .db, .csv, .md et projets sont TOUJOURS la. On ne touche pas a tes donnees.")

if __name__ == "__main__":
    nettoyer()
