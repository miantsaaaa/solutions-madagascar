import time, pathlib, datetime
fichier = pathlib.Path("AGENT-01-REPONSE.txt")
propositions = [
    "V1.16 : Produits - ajouter date de mise a jour des prix",
    "V1.17 : Produits - ajouter stock restant Riz Cafe Miel",
    "V1.18 : Bilan jour - benefice avec vraie marge",
    "V1.19 : Menu - option 9 total semaine avec vraie marge",
    "V1.20 : main.py integre tout en 1 commande",
]
i = 0
while True:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(fichier, "a") as f:
        f.write(f"[{now}] Agent 01 - Proposition : {propositions[i % len(propositions)]}\n")
    i += 1
    time.sleep(3600)
