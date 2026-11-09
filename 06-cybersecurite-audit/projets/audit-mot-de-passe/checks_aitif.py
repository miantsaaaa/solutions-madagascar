# Checks securite Aitif - V6.9
# Un seul endroit pour les checks, pour ne pas les dupliquer.
# checklist_aitif.py et rapport_audit.py utilisent ce fichier.
import os, glob, socket

def check_gitignore():
    if not os.path.exists("/root/.gitignore"):
        return False, "pas de .gitignore a /root"
    g = open("/root/.gitignore").read()
    manq = [m for m in [".db", ".csv", ".env", "venv"] if m not in g]
    if manq:
        return False, f"manquant {manq}"
    return True, ".db, .csv, .env, venv ignores"

def check_fichiers_sensibles():
    sens = []
    for pat in [".env", "password.txt", "motdepasse.txt", "id_rsa", ".pem"]:
        for f in glob.glob(f"/root/**/{pat}", recursive=True):
            if ".git/" not in f and "venv" not in f:
                sens.append(f)
    if sens:
        return False, f"{sens}"
    return True, "aucun fichier sensible trouve"

def check_ports_sensibles():
    ouverts = []
    for port in [3306, 5432, 6379]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex(("127.0.0.1", port)) == 0:
            ouverts.append(port)
        s.close()
    if ouverts:
        return False, f"ports ouverts {ouverts}"
    return True, "MySQL / Postgres / Redis fermes"

def check_sauvegarde():
    saves = glob.glob("/root/sauvegarde-*")
    if not saves:
        return False, "aucune sauvegarde"
    return True, f"{len(saves)} sauvegarde(s), derniere : {sorted(saves)[-1]}"
