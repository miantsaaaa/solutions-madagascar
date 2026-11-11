# Sous-Agent 02.1 - Surveillance - Employe du Maitre 02
# Projet : surveillance-redmi
# Travail : simulations, verifications, actions, ordres + TERMINE
import time, pathlib, datetime, subprocess, sys, glob
def log(msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("AGENT-02-REPONSE.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] Sous-Agent 02.1 Surveillance : {msg}\n")
    print(f"[{now}] {msg}", flush=True)
def simulation():
    try:
        r = subprocess.run([sys.executable, "-c", "from main import tout_en_1_commande; tout_en_1_commande()"], capture_output=True, text=True, timeout=30)
        if r.returncode == 0 and "TERMINE" in r.stdout:
            return "Simulation OK - tout en 1 commande surveillance marche"
        return f"Simulation ECHEC - code {r.returncode} - {r.stderr[:200]}"
    except Exception as e:
        return f"Simulation ECHEC - {e}"
def action_simulation():
    # A2.2 prevu : action en labo - compter cache/log sans supprimer
    try:
        caches = glob.glob("/root/*/projets/**/__pycache__", recursive=True)
        logs = glob.glob("/root/*/projets/**/*.log", recursive=True)
        return f"Action OK - compte {len(caches)} cache(s) + {len(logs)} log(s) sans supprimer, nettoyage en simulation"
    except Exception as e:
        return f"Action ECHEC - {e}"
def verification():
    msgs = []
    import shutil
    total, used, free = shutil.disk_usage("/")
    pct = used/total*100
    msgs.append(f"Stockage {pct:.1f}% Libre {free//(1024**3)} Go")
    if pct > 90:
        msgs.append("ALERTE ROUGE stockage")
    elif pct > 80:
        msgs.append("ALERTE ORANGE stockage")
    r = subprocess.run([sys.executable, "-m", "compileall", "-q", "main.py", "rapport.py", "alerte.py"], capture_output=True, text=True)
    msgs.append("Compile OK" if r.returncode == 0 else f"Compile ECHEC - {r.stderr[:200]}")
    return " | ".join(msgs)
def proposition_action():
    try:
        import shutil
        total, used, free = shutil.disk_usage("/")
        pct = used/total*100
        if pct > 90:
            return "Proposition : Lancer simuler_nettoyage.py - stockage ROUGE, ne pas pousser gros fichiers"
        if pct > 80:
            return "Proposition : Lancer simuler_nettoyage.py - stockage ORANGE, nettoyer cache/log en simulation"
        return "Proposition : Stockage OK - tu peux pousser"
    except Exception as e:
        return f"Proposition ECHEC - {e}"
while True:
    ordre_f = pathlib.Path("ORDRE-AGENT-02.txt")
    if ordre_f.exists():
        ordre = ordre_f.read_text(encoding="utf-8").strip()
        log(f"Ordre recu : {ordre}")
        sim = simulation()
        act = action_simulation()
        ver = verification()
        prop = proposition_action()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        pathlib.Path("RESULTAT-AGENT-02.txt").write_text(f"[{now}] Ordre : {ordre}\n[{now}] {sim}\n[{now}] {act}\n[{now}] {ver}\n[{now}] {prop}\n[{now}] === TERMINE - Mission finie, Miantsa peut verifier ===\n", encoding="utf-8")
        with open("DISCUSSION-AGENT-02.txt", "a", encoding="utf-8") as _df:
            _df.write(f"[{now}] Sous-Agent 02.1 : Maitre, mission finie === TERMINE ===\n")
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
