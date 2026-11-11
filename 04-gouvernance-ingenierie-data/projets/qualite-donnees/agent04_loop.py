# Maitre 04 v3 - Gouvernance Data - Maitre, pas conseiller
# Toi tu parles seulement au Maitre via MESSAGE-AGENT-04.txt
# Le Maitre discute avec son Sous-Agent via DISCUSSION-AGENT-04.txt
import time, pathlib, datetime, subprocess, sys, os
# A4.5 : REGLE AITIF - Agent ne pousse JAMAIS seul. Il travaille, Miantsa pousse.
# A4.5 : Anti-doublon - 1 seul Maitre, 1 seul Sous-Agent
_pid_f = pathlib.Path("AGENT-04.pid")
if _pid_f.exists():
    try:
        _old = int(_pid_f.read_text().strip())
        os.kill(_old, 0)
        print(f"Maitre deja en cours PID {_old} - je m'arrete, pas de doublon.")
        raise SystemExit(0)
    except (ProcessLookupError, ValueError):
        pass
_pid_f.write_text(str(os.getpid()))
def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
def ecrire_discussion(qui, msg):
    with open("DISCUSSION-AGENT-04.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now()}] {qui} : {msg}\n")
def ecrire_reponse(msg):
    with open("AGENT-04-REPONSE.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now()}] Maitre 04 : {msg}\n")
ecrire_discussion("Maitre 04", "Sous-Agent 04.1, tu es cree pour le projet Qualite. Ton travail : simulations, verifications, actions, ordres.")
ecrire_reponse("Maitre v3 lance. Sous-Agent 04.1 Qualite cree. Discussion ouverte.")
sous_proc = subprocess.Popen([sys.executable, "sous_agent_04_1_qualite.py"], stdout=open("sous_agent_04_1.log", "a"), stderr=subprocess.STDOUT)
ecrire_discussion("Maitre 04", f"Sous-Agent 04.1 lance, PID {sous_proc.pid}. Travaille, je supervise.")
while True:
    msg_f = pathlib.Path("MESSAGE-AGENT-04.txt")
    if msg_f.exists():
        msg = msg_f.read_text(encoding="utf-8").strip()
        ecrire_discussion("Maitre 04", f"Sous-Agent 04.1, Miantsa dit : {msg}")
        ecrire_discussion("Maitre 04", "Transmets cet ordre dans ORDRE-AGENT-04.txt et travaille.")
        pathlib.Path("ORDRE-AGENT-04.txt").write_text(msg, encoding="utf-8")
        ecrire_reponse(f"Message de Miantsa transmis au Sous-Agent : {msg}")
        try:
            msg_f.unlink()
        except Exception:
            pass
    if sous_proc.poll() is not None:
        ecrire_discussion("Maitre 04", "Sous-Agent 04.1 s'est arrete. Je le relance.")
        sous_proc = subprocess.Popen([sys.executable, "sous_agent_04_1_qualite.py"], stdout=open("sous_agent_04_1.log", "a"), stderr=subprocess.STDOUT)
        ecrire_discussion("Maitre 04", f"Sous-Agent 04.1 relance, PID {sous_proc.pid}.")
    else:
        ecrire_discussion("Maitre 04", "Sous-Agent 04.1, tout va bien ? Continue.")
    time.sleep(300)
