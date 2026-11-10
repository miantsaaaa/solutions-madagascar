import time, pathlib, datetime
fichier = pathlib.Path("AGENT-02-REPONSE.txt")
propositions = [
    "V2.16 : Surveillance - alerte si libre < 20 Go, pas seulement %",
    "V2.17 : Surveillance - historique stockage dans un fichier",
    "V2.18 : Surveillance - conseil JIRAMA si batterie faible",
    "V2.19 : Surveillance - rapport semaine stockage",
    "V2.20 : main.py integre tout en 1 commande",
]
i = 0
while True:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(fichier, "a") as f:
        f.write(f"[{now}] Agent 02 - Proposition : {propositions[i % len(propositions)]}\n")
    i += 1
    time.sleep(3600)
