# Rapport etat systeme - V2.4 - Domaine 02
# Genere un rapport complet : stockage, reseau, projets, sauvegardes
import shutil, socket, subprocess, os, glob
from datetime import datetime

def rapport():
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"=== RAPPORT ETAT SYSTEME - {date} - FIANARANTSOA / MADAGASCAR ===")
    # Stockage
    total, used, free = shutil.disk_usage("/")
    print(f"\n[STOCKAGE] Total {total//(1024**3)} Go | Utilise {used//(1024**3)} Go ({used/total*100:.1f}%) | Libre {free//(1024**3)} Go")
    # Reseau
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("[RESEAU] Internet : OK")
    except:
        print("[RESEAU] Internet : COUPE")
    # Projets
    print("\n[PROJETS]")
    for p in sorted(glob.glob("/root/*/projets/*")):
        nb = len(glob.glob(p + "/**/*.py", recursive=True))
        print(f" - {p} : {nb} fichiers .py")
    # Sauvegardes
    saves = sorted(glob.glob("/root/sauvegarde-*"))
    print(f"\n[SAUVEGARDES] {len(saves)} dossier(s)")
    for s in saves[-3:]:
        print(f" - {s}")
    # Fichiers .db
    dbs = glob.glob("/root/**/*.db", recursive=True)
    print(f"\n[BASES DE DONNEES] {len(dbs)} fichier(s) .db")
    for d in dbs:
        print(f" - {d} : {os.path.getsize(d)//1024} Ko")
    print("\nRapport termine. C est la preuve que ton systeme tient. Ton travail parle pour toi.")

if __name__ == "__main__":
    rapport()
