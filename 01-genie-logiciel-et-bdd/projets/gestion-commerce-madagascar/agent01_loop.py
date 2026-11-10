# Maitre 01 v3 - Genie Logiciel + BDD - Maitre, pas conseiller
# Travail : creer son sous-agent, discuter avec lui, superviser
# Toi tu parles seulement au Maitre via MESSAGE-AGENT-01.txt
# Le Maitre discute avec son Sous-Agent via DISCUSSION-AGENT-01.txt
import time, pathlib, datetime, subprocess, sys, os
def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
def ecrire_discussion(qui, msg):
    with open("DISCUSSION-AGENT-01.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now()}] {qui} : {msg}\n")
def ecrire_reponse(msg):
    with open("AGENT-01-REPONSE.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now()}] Maitre 01 : {msg}\n")
# 1. Le Maitre cree / verifie son Sous-Agent
ecrire_discussion("Maitre 01", "Sous-Agent 01.1, tu es cree pour le projet Commerce. Ton travail : simulations, verifications, ordres.")
ecrire_reponse("Maitre v3 lance. Sous-Agent 01.1 Commerce cree. Discussion ouverte.")
# 2. Le Maitre lance son Sous-Agent en arriere-plan
sous_proc = subprocess.Popen([sys.executable, "sous_agent_01_1_commerce.py"], stdout=open("sous_agent_01_1.log", "a"), stderr=subprocess.STDOUT)
ecrire_discussion("Maitre 01", f"Sous-Agent 01.1 lance, PID {sous_proc.pid}. Travaille, je supervise.")
while True:
    # 3. Message de Miantsa au Maitre seulement
    msg_f = pathlib.Path("MESSAGE-AGENT-01.txt")
    if msg_f.exists():
        msg = msg_f.read_text(encoding="utf-8").strip()
        ecrire_discussion("Maitre 01", f"Sous-Agent 01.1, Miantsa dit : {msg}")
        ecrire_discussion("Maitre 01", "Transmets cet ordre dans ORDRE-AGENT-01.txt et travaille.")
        pathlib.Path("ORDRE-AGENT-01.txt").write_text(msg, encoding="utf-8")
        ecrire_reponse(f"Message de Miantsa transmis au Sous-Agent : {msg}")
        try:
            msg_f.unlink()
        except Exception:
            pass
    # 4. Supervision : le Sous-Agent est-il vivant ?
    if sous_proc.poll() is not None:
        ecrire_discussion("Maitre 01", "Sous-Agent 01.1 s'est arrete. Je le relance.")
        sous_proc = subprocess.Popen([sys.executable, "sous_agent_01_1_commerce.py"], stdout=open("sous_agent_01_1.log", "a"), stderr=subprocess.STDOUT)
        ecrire_discussion("Maitre 01", f"Sous-Agent 01.1 relance, PID {sous_proc.pid}.")
    else:
        ecrire_discussion("Maitre 01", "Sous-Agent 01.1, tout va bien ? Continue.")
    time.sleep(3600)
