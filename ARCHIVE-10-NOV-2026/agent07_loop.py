import time, pathlib
props = [
 "V7.16 : Metier Aitif - portfolio ajoute 7 agents en arriere-plan",
 "V7.17 : Metier Aitif - cv ajoute competences 4eme tour",
 "V7.18 : Metier Aitif - catalogue ajoute preuve 4eme tour",
 "V7.19 : Metier Aitif - journal ajoute 4eme tour termine",
 "V7.20 : Metier Aitif - README met a jour version V7.20",
]
for pr in props:
    pathlib.Path("AGENT-07-REPONSE.txt").write_text(f"[{time.strftime(chr(37)+chr(89)+chr(45)+chr(37)+chr(109)+chr(45)+chr(37)+chr(100)+chr(32)+chr(37)+chr(72)+chr(58)+chr(37)+chr(77))}] Agent 07 propose : {pr}\n")
    time.sleep(3600)
print("Agent 07 loop pret")
