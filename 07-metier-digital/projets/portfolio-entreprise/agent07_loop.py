# Agent 07 Portfolio v3 - A7.1 - AITIF.
# Travaille toutes les 5 min : tout_en_1 complet Portfolio + TERMINE
import time, subprocess, pathlib
from datetime import datetime
LOG = pathlib.Path("MESSAGE-AGENT-07.txt")
while True:
    try:
        r = subprocess.run(["python3", "-c", "from main import tout_en_1_complet; tout_en_1_complet()"], capture_output=True, text=True, timeout=60)
        out = r.stdout[-800:] if r.stdout else "pas de sortie"
        LOG.write_text(f"Agent 07 Portfolio - {datetime.now().strftime('%Y-%m-%d %H:%M')} - VIVANT\n{out}\n=== TERMINE - Agent 07 a travaille, Miantsa peut verifier ===\n", encoding="utf-8")
        print(f"Agent 07 : tour fini {datetime.now().strftime('%H:%M')} - TERMINE")
    except Exception as e:
        print(f"Agent 07 erreur : {e}")
    time.sleep(300)
