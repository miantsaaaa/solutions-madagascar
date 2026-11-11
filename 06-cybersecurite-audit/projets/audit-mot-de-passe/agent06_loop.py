# Agent 06 Cyber v3 - A6.1 - AITIF.
# Travaille toutes les 5 min : tout_en_1 Cyber + TERMINE
import time, subprocess, pathlib
from datetime import datetime
LOG = pathlib.Path("MESSAGE-AGENT-06.txt")
while True:
    try:
        r = subprocess.run(["python3", "-c", "from main import tout_en_1_commande; tout_en_1_commande()"], capture_output=True, text=True, timeout=60)
        out = r.stdout[-800:] if r.stdout else "pas de sortie"
        LOG.write_text(f"Agent 06 Cyber - {datetime.now().strftime('%Y-%m-%d %H:%M')} - VIVANT\n{out}\n=== TERMINE - Agent 06 a travaille, Miantsa peut verifier ===\n", encoding="utf-8")
        print(f"Agent 06 : tour fini {datetime.now().strftime('%H:%M')} - TERMINE")
    except Exception as e:
        print(f"Agent 06 erreur : {e}")
    time.sleep(300)
