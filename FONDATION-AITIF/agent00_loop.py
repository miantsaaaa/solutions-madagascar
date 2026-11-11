# Agent 00 Guide v3 - A0.1 - AITIF - A la tete des 7 Agents
# Travaille 1 fois par jour : tout_en_1 Fondation + TERMINE
# Pas toutes les 5 min : il guide, il ne surveille pas.
import time, subprocess, pathlib
from datetime import datetime
LOG = pathlib.Path("/root/FONDATION-AITIF/MESSAGE-AGENT-00.txt")
while True:
    try:
        r = subprocess.run(["python3", "-c", "from main import tout_en_1_fondation; tout_en_1_fondation()"], capture_output=True, text=True, timeout=60, cwd="/root/FONDATION-AITIF")
        out = r.stdout[-800:] if r.stdout else "pas de sortie"
        LOG.write_text(f"Agent 00 Guide - {datetime.now().strftime('%Y-%m-%d %H:%M')} - VIVANT\n{out}\n=== TERMINE - Agent 00 a travaille, Miantsa peut verifier ===\n", encoding="utf-8")
        print(f"Agent 00 : tour fini {datetime.now().strftime('%H:%M')} - TERMINE - prochain tour demain")
    except Exception as e:
        print(f"Agent 00 erreur : {e}")
    time.sleep(86400)
