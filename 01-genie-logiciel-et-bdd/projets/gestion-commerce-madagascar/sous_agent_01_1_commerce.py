# Sous-Agent 01.1 - Commerce - Employe du Maitre 01
# Projet : gestion-commerce-madagascar
# Travail : simulations, verifications, ordres
# Le projet n'est pas encore au point, c'est un labo : il peut faire des actions.
import time, pathlib, datetime, subprocess, sys

def log(msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("AGENT-01-REPONSE.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] Sous-Agent 01.1 Commerce : {msg}\n")
    print(f"[{now}] {msg}", flush=True)

def simulation():
    try:
        r = subprocess.run([sys.executable, "-c", "from main import tout_en_1_commande; tout_en_1_commande()"], capture_output=True, text=True, timeout=20)
        if r.returncode == 0 and "FIN TOUT EN 1 COMMANDE" in r.stdout:
            return "Simulation OK - tout en 1 commande marche"
        return f"Simulation ECHEC - code {r.returncode} - {r.stderr[:200]}"
    except Exception as e:
        return f"Simulation ECHEC - {e}"

def action_simulation():
    # A1.2 : ACTIONS, pas juste lecture - en labo sur copie
    try:
        import shutil, csv
        shutil.copy("stock.csv", "stock_test.csv")
        rows = list(csv.DictReader(open("stock_test.csv", encoding="utf-8")))
        # Action : simule vente 1 Riz
        for r in rows:
            if r['produit'] == 'Riz':
                avant = int(r['quantite'])
                r['quantite'] = str(max(0, avant - 1))
                apres = r['quantite']
        with open("stock_test.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=rows[0].keys())
            w.writeheader()
            w.writerows(rows)
        # Verifie : le fichier test existe et Riz a bien diminue
        check = list(csv.DictReader(open("stock_test.csv", encoding="utf-8")))
        ok = any(r['produit'] == 'Riz' and int(r['quantite']) == max(0, avant - 1) for r in check)
        pathlib.Path("stock_test.csv").unlink()
        return f"Action OK - vente simulee 1 Riz : {avant} -> {apres}, nettoyage fait" if ok else "Action ECHEC - stock test ne correspond pas"
    except Exception as e:
        try:
            pathlib.Path("stock_test.csv").unlink()
        except Exception:
            pass
        return f"Action ECHEC - {e}"

def verification():
    msgs = []
    try:
        import csv
        with open("stock.csv", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
            msgs.append(f"Stock fichier OK : {len(rows)} ligne(s)")
            d = {r['produit']: r['quantite'] for r in rows}
            if d.get('Cafe', '0') == '0':
                msgs.append("Alerte : Cafe stock 0")
            if d.get('Miel', '0') == '0':
                msgs.append("Alerte : Miel stock 0")
    except Exception as e:
        msgs.append(f"Stock fichier INTROUVABLE - {e}")
    r = subprocess.run([sys.executable, "-m", "compileall", "-q", "main.py", "produits_aitif.py"], capture_output=True, text=True)
    msgs.append("Compile OK" if r.returncode == 0 else f"Compile ECHEC - {r.stderr[:200]}")
    return " | ".join(msgs)

while True:
    # 1. ORDRE : si Miantsa a laisse un ordre, le sous-agent travaille
    ordre_f = pathlib.Path("ORDRE-AGENT-01.txt")
    if ordre_f.exists():
        ordre = ordre_f.read_text(encoding="utf-8").strip()
        log(f"Ordre recu : {ordre}")
        sim = simulation()
        act = action_simulation()
        ver = verification()
        res = pathlib.Path("RESULTAT-AGENT-01.txt")
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        res.write_text(f"[{now}] Ordre : {ordre}\n[{now}] {sim}\n[{now}] {ver}\n", encoding="utf-8")
        log(f"Ordre termine : {sim} | {act} | {ver}")
        try:
            ordre_f.unlink()
        except Exception:
            pass
    else:
        # 2. Sinon : simulation + verification de routine
        sim = simulation()
        act = action_simulation()
        ver = verification()
        log(f"Routine : {sim} | {act} | {ver}")
    time.sleep(3600)
