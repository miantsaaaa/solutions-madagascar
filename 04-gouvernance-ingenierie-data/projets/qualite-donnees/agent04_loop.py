import time, pathlib, datetime
fichier = pathlib.Path("AGENT-04-REPONSE.txt")
propositions = [
    "V4.16 : Qualite - verifier date vente manquante",
    "V4.17 : Qualite - alerte si stock > 1000 suspect",
    "V4.18 : Export - nom fichier avec heure, pas seulement date",
    "V4.19 : Rapport - courbe ventes mois par mois",
    "V4.20 : main.py integre tout en 1 commande",
]
i = 0
while True:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(fichier, "a") as f:
        f.write(f"[{now}] Agent 04 - Proposition : {propositions[i % len(propositions)]}\n")
    i += 1
    time.sleep(3600)
