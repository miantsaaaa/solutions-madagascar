# Audit fichiers sensibles Aitif - V6.6
# AITIF. - Cyber Aitif.
# Verifie que tu n'as pas de .env, cles, mots de passe dans ton depot
import os, glob, re

DANGEREUX = [".env", "id_rsa", "id_ed25519", ".pem", "credentials.json", "password.txt", "motdepasse.txt"]
MOTS = [r"password\s*=", r"api[_-]?key\s*=", r"secret\s*=", r"token\s*=", r"AKIA[0-9A-Z]{16}"]

def audit():
    print("=== AUDIT FICHIERS SENSIBLES AITIF. - V6.6 - MADAGASCAR ===")
    print("On cherche les fichiers qu'il ne faut JAMAIS pousser sur GitHub.\n")
    problemes = 0
    # 1. Noms de fichiers dangereux
    for pat in DANGEREUX:
        for f in glob.glob(f"/root/**/{pat}", recursive=True):
            if ".git/" not in f and "venv" not in f:
                print(f"DANGER : fichier sensible trouve : {f}")
                print("   Ne le pousse JAMAIS. Mets-le dans .gitignore.")
                problemes += 1
    if problemes == 0:
        print("OK : aucun fichier sensible avec nom dangereux trouve.")
    # 2. Mots de passe en dur dans les .py (hors venv)
    print("\n[Recherche de secrets dans les .py]")
    trouves = 0
    for f in glob.glob("/root/**/*.py", recursive=True):
        if "venv" in f or ".git" in f:
            continue
        try:
            with open(f, encoding="utf-8", errors="ignore") as fh:
                txt = fh.read()
            for motif in MOTS:
                if re.search(motif, txt, re.IGNORECASE):
                    print(f"Attention : motif {motif} dans {f} - verifie que ce n'est pas un vrai secret.")
                    trouves += 1
                    break
        except:
            pass
    if trouves == 0:
        print("OK : aucun secret en dur trouve dans tes .py.")
    # 3. .gitignore
    print("\n[.gitignore]")
    if os.path.exists("/root/.gitignore"):
        with open("/root/.gitignore") as fh:
            gitig = fh.read()
        for mot in ["*.db", "*.csv", "*.log", "venv", ".env"]:
            if mot in gitig:
                print(f" OK : {mot} est ignore")
            else:
                print(f" MANQUANT : {mot} devrait etre dans .gitignore")
    print("\nAudit termine. Ton depot est-il propre ? Si oui, tu peux dormir tranquille.")

if __name__ == "__main__":
    audit()
