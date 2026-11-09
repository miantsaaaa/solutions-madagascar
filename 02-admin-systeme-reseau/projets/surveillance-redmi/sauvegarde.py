# Sauvegarde auto - V2.2 - Domaine 02
# Sauvegarde les fichiers importants de l'entreprise
import shutil, os
from datetime import datetime

def sauvegarder():
    date = datetime.now().strftime("%Y-%m-%d_%H-%M")
    dest = f"/root/sauvegarde-{date}"
    os.makedirs(dest, exist_ok=True)
    # Ce qu'on sauvegarde : les .md + les projets, pas les venv
    for f in ["MON-ENTREPRISE.md","PROBLEMES-MADAGASCAR.md","ORGANISATION.md","ROADMAP-VERSIONS.md","README.md"]:
        src = f"/root/{f}"
        if os.path.exists(src):
            shutil.copy(src, dest)
            print(f"OK : {f}")
    # Projets
    for domaine in ["01-genie-logiciel-et-bdd","02-admin-systeme-reseau"]:
        src = f"/root/{domaine}/projets"
        if os.path.exists(src):
            shutil.copytree(src, f"{dest}/{domaine}-projets", dirs_exist_ok=True, ignore=shutil.ignore_patterns("*.db","__pycache__","*.csv","venv"))
            print(f"OK : {domaine}/projets")
    print(f"\nSauvegarde terminee dans : {dest}")
    print("Ne pas oublier de copier ce dossier ailleurs (Google Drive, cle USB)")

if __name__ == "__main__":
    sauvegarder()
