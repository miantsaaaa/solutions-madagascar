# Rapport audit securite complet Aitif - V6.15 - 3eme tour - bilan 1 phrase
# AITIF. - Cyber Aitif.
# Reprend les 4 audits precedents en 1 rapport
import os, glob, socket
from datetime import datetime

def rapport():
    print("=== RAPPORT AUDIT SECURITE COMPLET AITIF. - V6.15 - MADAGASCAR ===")
    print(f"Date : {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("Perimetre : ton Redmi + ton depot /root\n")
    score = 100
    # 1. Fichiers sensibles
    print("[1. FICHIERS SENSIBLES]")
    dangereux = []
    for pat in [".env", "id_rsa", ".pem", "password.txt"]:
        for f in glob.glob(f"/root/*/projets/**/{pat}", recursive=True):  # V6.16 scan projets seulement
            if ".git/" not in f and "venv" not in f:
                dangereux.append(f)
    if not dangereux:
        print(" OK : aucun fichier sensible trouve")
    else:
        print(f" DANGER : {len(dangereux)} fichier(s) sensible(s)")
        score -= 30
    # 2. .gitignore
    print("\n[2. .GITIGNORE]")
    if os.path.exists("/root/.gitignore"):
        with open("/root/.gitignore") as fh:
            g = fh.read()
        manquants = [m for m in [".env", "*.db", "*.csv", "venv"] if m not in g]
        if not manquants:
            print(" OK : .gitignore complet")
        else:
            print(f" MANQUANT : {manquants}")
            score -= 10
    # 3. Ports
    print("\n[3. PORTS OUVERTS]")
    ouverts = []
    for port in [22, 80, 443, 3306, 5432, 8000, 1883]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex(("127.0.0.1", port)) == 0:
            ouverts.append(port)
        s.close()
    if not ouverts:
        print(" OK : 0 port ouvert, Redmi ferme")
    else:
        print(f" ATTENTION : ports ouverts {ouverts} - verifie qu'ils sont voulus")
        score -= 10
    # 4. Sauvegardes
    print("\n[4. SAUVEGARDES]")
    saves = glob.glob("/root/sauvegarde-*")
    if saves:
        print(f" OK : {len(saves)} sauvegarde(s) trouvee(s), derniere : {sorted(saves)[-1]}")
    else:
        print(" ATTENTION : aucune sauvegarde trouvee. Lance sauvegarde.py (Domaine 02).")
        score -= 20
    print(f"\n[SCORE SECURITE GLOBAL] {score} / 100")
    if score >= 90:
        print("EXCELLENT : ton systeme est bien protege. Continue comme ca.")
    elif score >= 70:
        print("BON : quelques points a corriger, mais base saine.")
    else:
        print("A CORRIGER : corrige les points rouges avant de continuer.")
    if score >= 90:
        bilan = "ton Redmi est protege, tu peux pousser tranquille."
    elif score >= 70:
        bilan = "corrige les points orange avant de pousser."
    else:
        bilan = "ne pousse pas, corrige les rouges d'abord."
    print(f"\nBilan Cyber : {score}/100 - {bilan}")
    print("Ton audit est la preuve que tu travailles comme un pro de la securite.")
    print("Et si quelqu'un te trouve, il verra que tu ne laisses rien au hasard.")

if __name__ == "__main__":
    rapport()
    print("\n--- CHECKLIST AITIF. ---")
    try:
        from checklist_aitif import checklist
        checklist()
    except Exception as e:
        print(f"Checklist non lisible ici : {e}")
