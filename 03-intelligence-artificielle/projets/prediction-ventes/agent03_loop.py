import time, pathlib, datetime
fichier = pathlib.Path("AGENT-03-REPONSE.txt")
propositions = [
    "V3.16 : Prediction - moyenne mobile 7 jours, pas seulement moyenne generale",
    "V3.17 : Prediction - alerte si prediction < 5000 Ar",
    "V3.18 : Conseil - trier par benefice, pas par stock",
    "V3.19 : Graphique - courbe benefice, pas seulement ventes",
    "V3.20 : main.py integre tout en 1 commande",
]
i = 0
while True:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(fichier, "a") as f:
        f.write(f"[{now}] Agent 03 - Proposition : {propositions[i % len(propositions)]}\n")
    i += 1
    time.sleep(3600)
