import time, datetime, pathlib
propositions = [
    "V6.16 : Cyber Aitif - checklist ajoute check tokens ghp sk- dans les .py",
    "V6.17 : Cyber Aitif - rapport ajoute fichiers .key .kdbx dans score",
    "V6.18 : Cyber Aitif - audit mot de passe ajoute duree casse estimee",
    "V6.19 : Cyber Aitif - scan ports ajoute alerte si port base ouverte",
    "V6.20 : Cyber Aitif - bilan cyber ajoute benefice protege en Ar",
]
i = 0
base = pathlib.Path('/root') / '06-cybersecurite-audit' / 'projets' / 'audit-mot-de-passe'
while True:
    out = base / 'AGENT-06-REPONSE.txt'
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    out.write_text(f'[{now}] Agent 06 propose : {propositions[i % len(propositions)]}\n', encoding='utf-8')
    print(f'Agent 06 : {propositions[i % len(propositions)]}')
    i += 1
    time.sleep(3600)
