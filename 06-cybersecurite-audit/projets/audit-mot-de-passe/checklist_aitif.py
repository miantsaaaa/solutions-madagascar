# Checklist securite Aitif - V6.7
# 5 checks rapides chaque jour, avant de pousser.
# Si 1 check est rouge, tu corriges avant de pousser.
import os, glob, socket, re

def checklist():
    print("=== CHECKLIST SECURITE AITIF. - V6.7 ===")
    ok = 0
    total = 5
    # 1. .gitignore protege .db / .csv / .env
    print("\n[1/5] .gitignore protege tes donnees ?")
    if os.path.exists("/root/.gitignore"):
        g = open("/root/.gitignore").read()
        manq = [m for m in [".db", ".csv", ".env", "venv"] if m not in g]
        if not manq:
            print(" OK : .db, .csv, .env, venv ignores")
            ok += 1
        else:
            print(f" ROUGE : manquant {manq} - ajoute-les avant de pousser")
    else:
        print(" ROUGE : pas de .gitignore a /root")
    # 2. Pas de fichier sensible
    print("\n[2/5] Pas de fichier sensible ?")
    sens = []
    for pat in [".env", "password.txt", "motdepasse.txt", "id_rsa", ".pem"]:
        for f in glob.glob(f"/root/**/{pat}", recursive=True):
            if ".git/" not in f and "venv" not in f:
                sens.append(f)
    if not sens:
        print(" OK : aucun fichier sensible trouve")
        ok += 1
    else:
        print(f" ROUGE : {sens} - ne pousse JAMAIS ca")
    # 3. Pas de secret en dur dans les .py Aitif
    print("\n[3/5] Pas de secret en dur dans tes .py ?")
    trouves = 0
    for f in glob.glob("/root/**/*.py", recursive=True):
        if "venv" in f or ".git" in f:
            continue
        try:
            txt = open(f, encoding="utf-8", errors="ignore").read()
            if re.search(r"password\s*=\s*['\"][^'\"]+['\"]", txt, re.IGNORECASE):
                print(f" ATTENTION : possible secret dans {f}")
                trouves += 1
        except:
            pass
    if trouves == 0:
        print(" OK : aucun secret en dur trouve")
        ok += 1
    else:
        print(f" ROUGE : {trouves} fichier(s) a verifier")
    # 4. Ports sensibles fermes
    print("\n[4/5] Ports sensibles fermes ?")
    ouverts = []
    for port in [3306, 5432, 6379]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex(("127.0.0.1", port)) == 0:
            ouverts.append(port)
        s.close()
    if not ouverts:
        print(" OK : MySQL / Postgres / Redis fermes")
        ok += 1
    else:
        print(f" ROUGE : ports ouverts {ouverts} - ferme si tu n'en as pas besoin")
    # 5. Sauvegarde recente
    print("\n[5/5] Sauvegarde Aitif ?")
    saves = glob.glob("/root/sauvegarde-*")
    if saves:
        print(f" OK : {len(saves)} sauvegarde(s), derniere : {sorted(saves)[-1]}")
        ok += 1
    else:
        print(" ROUGE : aucune sauvegarde - lance sauvegarde.py (Domaine 02)")
    print(f"\n[SCORE CHECKLIST] {ok} / {total}")
    if ok == 5:
        print("VERT : tu peux pousser tranquille.")
    elif ok >= 3:
        print("ORANGE : corrige les rouges avant de pousser.")
    else:
        print("ROUGE : ne pousse pas, corrige d'abord.")
    print("\nAitif ne pousse jamais avec un rouge.")

if __name__ == "__main__":
    checklist()
