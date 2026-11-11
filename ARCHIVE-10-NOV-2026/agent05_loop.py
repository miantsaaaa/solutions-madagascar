import time, datetime, pathlib
propositions = [
    "V5.16 : IoT Aitif - historique ajoute combien de fois en danger par produit",
    "V5.17 : IoT Aitif - mqtt_envoi ajoute produits en danger dans le message",
    "V5.18 : IoT Aitif - alerte ajoute conseil action par produit en danger",
    "V5.19 : IoT Aitif - tableau ajoute pire heure humidite de la journee",
    "V5.20 : IoT Aitif - bilan capteur ajoute benefice protege en Ar",
]
i = 0
base = pathlib.Path('/root') / '05-objets-connectes-iot' / 'projets' / 'capteur-temperature'
while True:
    out = base / 'AGENT-05-REPONSE.txt'
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    out.write_text(f'[{now}] Agent 05 propose : {propositions[i % len(propositions)]}\n', encoding='utf-8')
    print(f'Agent 05 : {propositions[i % len(propositions)]}')
    i += 1
    time.sleep(3600)
