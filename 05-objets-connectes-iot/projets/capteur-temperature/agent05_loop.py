# Maitre 05 v3 - IoT Capteur - Maitre, pas conseiller
# Toi tu parles seulement au Maitre via MESSAGE-AGENT-05.txt
# Le Maitre discute avec son Sous-Agent via DISCUSSION-AGENT-05.txt
import time, pathlib, datetime, subprocess, sys, os
# A5.5 : REGLE AITIF - Agent ne pousse JAMAIS seul. Il travaille, Miantsa pousse.
# A5.5 : Anti-doublon - 1 seul Maitre, 1 seul Sous-Agent
_pid_f = pathlib.Path("AGENT-05.pid")
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
    with open("DISCUSSION-AGENT-05.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now()}] {qui} : {msg}\n")
def ecrire_reponse(msg):
    with open("AGENT-05-REPONSE.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now()}] Maitre 05 : {msg}\n")
ecrire_discussion("Maitre 05", "Sous-Agent 05.1, tu es cree pour le projet Capteur. Ton travail : simulations, verifications, actions, ordres.")
ecrire_reponse("Maitre v3 lance. Sous-Agent 05.1 Capteur cree. Discussion ouverte.")
sous_proc = subprocess.Popen([sys.executable, "sous_agent_05_1_capteur.py"], stdout=open("sous_agent_05_1.log", "a"), stderr=subprocess.STDOUT)
ecrire_discussion("Maitre 05", f"Sous-Agent 05.1 lance, PID {sous_proc.pid}. Travaille, je supervise.")
while True:
    msg_f = pathlib.Path("MESSAGE-AGENT-05.txt")
    if msg_f.exists():
        msg = msg_f.read_text(encoding="utf-8").strip()
        ecrire_discussion("Maitre 05", f"Sous-Agent 05.1, Miantsa dit : {msg}")
        ecrire_discussion("Maitre 05", "Transmets cet ordre dans ORDRE-AGENT-05.txt et travaille.")
        pathlib.Path("ORDRE-AGENT-05.txt").write_text(msg, encoding="utf-8")
        ecrire_reponse(f"Message de Miantsa transmis au Sous-Agent : {msg}")
        try:
            msg_f.unlink()
        except Exception:
            pass
    if sous_proc.poll() is not None:
        ecrire_discussion("Maitre 05", "Sous-Agent 05.1 s'est arrete. Je le relance.")
        sous_proc = subprocess.Popen([sys.executable, "sous_agent_05_1_capteur.py"], stdout=open("sous_agent_05_1.log", "a"), stderr=subprocess.STDOUT)
        ecrire_discussion("Maitre 05", f"Sous-Agent 05.1 relance, PID {sous_proc.pid}.")
    else:
        ecrire_discussion("Maitre 05", "Sous-Agent 05.1, tout va bien ? Continue.")
    pathlib.Path("STATUS-AGENT-05.txt").write_text(f"Agent 05 Capteur - {now()} - VIVANT - Maitre + Sous-Agent 05.1 travaillent - Voir AGENT-05-REPONSE.txt pour le detail\n", encoding="utf-8")
    time.sleep(300)
