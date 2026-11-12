#!/bin/bash
bash ~/generer-api-base-v6.sh
python3 << 'PY'
import json, csv, pathlib
api_path = pathlib.Path("/root/docs/aitif-api.json")
api = json.loads(api_path.read_text())
def lire(nom):
    p = pathlib.Path(f"/root/BASE/{nom}")
    return list(csv.DictReader(open(p))) if p.exists() else []
api["projets_par_domaine"] = lire("projets-par-domaine.csv")
api["agents_evolution"] = lire("agents-evolution.csv")
api["systeme"] = "Vision + Agents + Base + Projets par domaine + Regles anti-faillite + Preuves - Tout evolue ensemble, jamais 1 seul."
api_path.write_text(json.dumps(api, ensure_ascii=False, indent=2))
print(f"API v7 : Projets par domaine {len(api['projets_par_domaine'])} - Agents evolution {len(api['agents_evolution'])} - Systeme OK")
PY
