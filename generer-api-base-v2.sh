#!/bin/bash
bash ~/generer-api-base.sh
python3 << 'PY'
import json, csv, pathlib
api_path = pathlib.Path("/root/docs/aitif-api.json")
api = json.loads(api_path.read_text())
api["regions"] = list(csv.DictReader(open("/root/BASE/regions.csv")))
api["historique"] = list(csv.DictReader(open("/root/BASE/historique.csv")))
api_path.write_text(json.dumps(api, ensure_ascii=False, indent=2))
print(f"API v2 : Regions {len(api['regions'])} - Historique {len(api['historique'])} lignes")
PY
