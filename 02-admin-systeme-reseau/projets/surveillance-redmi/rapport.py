# Rapport etat systeme - V2.18 Aitif - Domaine 02
# Genere un rapport complet : stockage, reseau, projets, sauvegardes
import shutil, socket, subprocess, os, glob, pathlib
from datetime import datetime

def rapport():
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"=== RAPPORT ETAT SYSTEME AITIF. - {date} - FIANARANTSOA / MADAGASCAR ===")
    # Stockage
    total, used, free = shutil.disk_usage("/")
    print(f"\n[STOCKAGE] Total {total//(1024**3)} Go | Utilise {used//(1024**3)} Go ({used/total*100:.1f}%) | Libre {free//(1024**3)} Go")
    # Reseau
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("[RESEAU] Internet : OK")
    except:
        print("[RESEAU] Internet : COUPE")
    # Agents - V2.17
    print("\n[AGENTS]")
    pid_f = pathlib.Path("/root/01-genie-logiciel-et-bdd/projets/gestion-commerce-madagascar/AGENT-01.pid")
    if pid_f.exists():
        try:
            _pid = int(pid_f.read_text().strip())
            os.kill(_pid, 0)
            print(f" - Agent 01 Maitre : VIVANT (PID {_pid})")
        except Exception:
            print(" - Agent 01 Maitre : ARRETE")
    else:
        print(" - Agent 01 Maitre : PAS DE PID - arrete")
    try:
        _r = subprocess.run(["ps", "aux"], capture_output=True, text=True, timeout=5)
        if "sous_agent_01_1_commerce.py" in _r.stdout:
            print(" - Agent 01 Sous-Agent 01.1 Commerce : VIVANT")
        else:
            print(" - Agent 01 Sous-Agent 01.1 Commerce : ARRETE")
    except Exception as e:
        print(f" - Agent 01 Sous-Agent : non verifiable ({e})")
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
    # V2.18 : ne scanne plus tout /root, trop long - seulement projets/
    dbs = glob.glob("/root/*/projets/**/*.db", recursive=True)
    print(f"\n[BASES DE DONNEES] {len(dbs)} fichier(s) .db")
    for d in dbs:
        print(f" - {d} : {os.path.getsize(d)//1024} Ko")
    print("\nRapport termine. C est la preuve que ton systeme tient. Ton travail parle pour toi.")

if __name__ == "__main__":
    rapport()
