#!/bin/bash
bash ~/generer-api-base-v3.sh
python3 << 'PY'
import json, csv, pathlib
api_path = pathlib.Path("/root/docs/aitif-api.json")
api = json.loads(api_path.read_text())
def lire(nom):
    p = pathlib.Path(f"/root/BASE/{nom}")
    return list(csv.DictReader(open(p))) if p.exists() else []
api["partages"] = lire("partages.csv")
api_path.write_text(json.dumps(api, ensure_ascii=False, indent=2))
print(f"API v4 : Partages {len(api['partages'])} - Savoirs {len(api['savoirs'])} - Preuves {len(api['preuves_a_apporter'])}")
PY
