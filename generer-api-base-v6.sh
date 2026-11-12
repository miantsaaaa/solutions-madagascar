#!/bin/bash
bash ~/generer-api-base-v5.sh
python3 << 'PY'
import json, csv, pathlib
api_path = pathlib.Path("/root/docs/aitif-api.json")
api = json.loads(api_path.read_text())
def lire(nom):
    p = pathlib.Path(f"/root/BASE/{nom}")
    return list(csv.DictReader(open(p))) if p.exists() else []
api["agents"] = lire("agents.csv")
api_path.write_text(json.dumps(api, ensure_ascii=False, indent=2))
print(f"API v6 : Agents {len(api['agents'])} - Projets {len(api['projets_futurs'])} - Regles {len(api['regles_anti_faillite'])}")
PY
