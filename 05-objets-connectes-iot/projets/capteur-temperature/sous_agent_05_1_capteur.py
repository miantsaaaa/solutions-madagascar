# Sous-Agent 05.1 - Capteur - Employe du Maitre 05
# Projet : capteur-temperature
# Travail : simulations, verifications, actions, ordres + TERMINE
import time, pathlib, datetime, subprocess, sys, glob, csv, os
def log(msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("AGENT-05-REPONSE.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] Sous-Agent 05.1 Capteur : {msg}\n")
    print(f"[{now}] {msg}", flush=True)
def simulation():
    try:
        r = subprocess.run([sys.executable, "-c", "from main import tout_en_1_commande; tout_en_1_commande()"], capture_output=True, text=True, timeout=30)
        if r.returncode == 0 and "TERMINE" in r.stdout:
            return "Simulation OK - tout en 1 commande capteur marche"
        return f"Simulation ECHEC - code {r.returncode} - {r.stderr[:200]}"
    except Exception as e:
        return f"Simulation ECHEC - {e}"
def action_simulation():
    # A5.2 prevu : action en labo - compter mesures sans modifier fichier
    try:
        if not os.path.exists("mesures-temperature.csv"):
            return "Action OK - pas de mesures, rien a compter, en simulation"
        with open("mesures-temperature.csv", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        return f"Action OK - compte {len(rows)} mesure(s) capteur, sans modifier, en simulation"
    except Exception as e:
        return f"Action ECHEC - {e}"
def verification():
    msgs = []
    r = subprocess.run([sys.executable, "-m", "compileall", "-q", "main.py", "alerte.py", "conseil_stock_aitif.py", "historique.py", "tableau_bord.py", "rapport_semaine.py", "check_agents.py"], capture_output=True, text=True)
    msgs.append("Compile OK" if r.returncode == 0 else f"Compile ECHEC - {r.stderr[:200]}")
    return " | ".join(msgs)
def proposition_action():
    try:
        if not os.path.exists("mesures-temperature.csv"):
            return "Proposition : Pas de mesures - lance main.py 3 fois par jour pour un vrai historique"
        with open("mesures-temperature.csv", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        d = rows[-1]
        hum = float(d["Humidite (%)"])
        if hum > 80:
            return f"Proposition : Humidite {hum} % trop haute - aere ton stock, protege Cafe et Miel"
        return "Proposition : Mesures OK - continue 3 fois par jour"
    except Exception as e:
        return f"Proposition ECHEC - {e}"
while True:
    ordre_f = pathlib.Path("ORDRE-AGENT-05.txt")
    if ordre_f.exists():
        ordre = ordre_f.read_text(encoding="utf-8").strip()
        log(f"Ordre recu : {ordre}")
        sim = simulation()
        act = action_simulation()
        ver = verification()
        prop = proposition_action()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        pathlib.Path("RESULTAT-AGENT-05.txt").write_text(f"[{now}] Ordre : {ordre}\n[{now}] {sim}\n[{now}] {act}\n[{now}] {ver}\n[{now}] {prop}\n[{now}] === TERMINE - Mission finie, Miantsa peut verifier ===\n", encoding="utf-8")
        with open("DISCUSSION-AGENT-05.txt", "a", encoding="utf-8") as _df:
            _df.write(f"[{now}] Sous-Agent 05.1 : Maitre, mission finie === TERMINE ===\n")
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
