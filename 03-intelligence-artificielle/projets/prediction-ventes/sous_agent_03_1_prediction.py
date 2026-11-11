# Sous-Agent 03.1 - Prediction - Employe du Maitre 03
# Projet : prediction-ventes
# Travail : simulations, verifications, actions, ordres + TERMINE
import time, pathlib, datetime, subprocess, sys, glob
def log(msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("AGENT-03-REPONSE.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] Sous-Agent 03.1 Prediction : {msg}\n")
    print(f"[{now}] {msg}", flush=True)
def simulation():
    try:
        r = subprocess.run([sys.executable, "-c", "from main import tout_en_1_commande; tout_en_1_commande()"], capture_output=True, text=True, timeout=30)
        if r.returncode == 0 and "TERMINE" in r.stdout:
            return "Simulation OK - tout en 1 commande prediction marche"
        return f"Simulation ECHEC - code {r.returncode} - {r.stderr[:200]}"
    except Exception as e:
        return f"Simulation ECHEC - {e}"
def action_simulation():
    # A3.2 prevu : action en labo - compter predictions possibles sans modifier base
    try:
        import sqlite3
        dbs = glob.glob("/root/*/projets/**/commerce.db", recursive=True)
        if not dbs:
            return "Action OK - pas de base, rien a compter, en simulation"
        conn = sqlite3.connect(dbs[0])
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM ventes")
        nb = cur.fetchone()[0]
        conn.close()
        return f"Action OK - compte {nb} vente(s) pour prediction, sans modifier, en simulation"
    except Exception as e:
        return f"Action ECHEC - {e}"
def verification():
    msgs = []
    r = subprocess.run([sys.executable, "-m", "compileall", "-q", "main.py", "conseil_achat.py", "alerte_stock.py", "rapport_semaine.py", "check_agents.py"], capture_output=True, text=True)
    msgs.append("Compile OK" if r.returncode == 0 else f"Compile ECHEC - {r.stderr[:200]}")
    return " | ".join(msgs)
def proposition_action():
    try:
        import sqlite3
        dbs = glob.glob("/root/*/projets/**/commerce.db", recursive=True)
        if not dbs:
            return "Proposition : Pas de base - ajoute une vente dans Commerce pour entrainer ton IA"
        conn = sqlite3.connect(dbs[0])
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM ventes")
        nb = cur.fetchone()[0]
        conn.close()
        if nb < 7:
            return f"Proposition : Seulement {nb} vente(s) - ajoute 1 vente par jour pour que ton IA connaisse chaque jour de semaine"
        return "Proposition : Assez de ventes - ton IA peut predire par jour de semaine"
    except Exception as e:
        return f"Proposition ECHEC - {e}"
while True:
    ordre_f = pathlib.Path("ORDRE-AGENT-03.txt")
    if ordre_f.exists():
        ordre = ordre_f.read_text(encoding="utf-8").strip()
        log(f"Ordre recu : {ordre}")
        sim = simulation()
        act = action_simulation()
        ver = verification()
        prop = proposition_action()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        pathlib.Path("RESULTAT-AGENT-03.txt").write_text(f"[{now}] Ordre : {ordre}\n[{now}] {sim}\n[{now}] {act}\n[{now}] {ver}\n[{now}] {prop}\n[{now}] === TERMINE - Mission finie, Miantsa peut verifier ===\n", encoding="utf-8")
        with open("DISCUSSION-AGENT-03.txt", "a", encoding="utf-8") as _df:
            _df.write(f"[{now}] Sous-Agent 03.1 : Maitre, mission finie === TERMINE ===\n")
        log(f"Ordre termine : {sim} | {act} | {ver} | {prop} | === TERMINE ===")
        try:
            ordre_f.unlink()
        except Exception:
            pass
    else:
        sim = simulation()
        act = action_simulation()
        ver = verification()
        prop = proposition_action()
        log(f"Routine : {sim} | {act} | {ver} | {prop}")
    time.sleep(300)
