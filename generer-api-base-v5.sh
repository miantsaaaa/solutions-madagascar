#!/bin/bash
bash ~/generer-api-base-v4.sh
python3 << 'PY'
import json, csv, pathlib
api_path = pathlib.Path("/root/docs/aitif-api.json")
api = json.loads(api_path.read_text())
def lire(nom):
    p = pathlib.Path(f"/root/BASE/{nom}")
    return list(csv.DictReader(open(p))) if p.exists() else []
api["projets_futurs"] = lire("projets-futurs.csv")
api["regles_anti_faillite"] = lire("regles-anti-faillite.csv")
api["vision"] = "Creer l'entreprise petit a petit, pour qu'apres le lancement - peut-etre pret banque - elle n'entre JAMAIS en faillite et fasse vraiment evoluer Madagascar. Restaurants, Hopitaux, Laboratoires, Usines, Batisseurs routes, Ecoles, Energie."
api["but"] = "Preparer, pas vendre. Prouver, pas promettre."
api_path.write_text(json.dumps(api, ensure_ascii=False, indent=2))
print(f"API v5 : Projets {len(api['projets_futurs'])} - Regles anti-faillite {len(api['regles_anti_faillite'])} - Vision OK")
PY
