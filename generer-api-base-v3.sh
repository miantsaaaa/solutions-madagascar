#!/bin/bash
bash ~/generer-api-base-v2.sh
python3 << 'PY'
import json, csv, pathlib
api_path = pathlib.Path("/root/docs/aitif-api.json")
api = json.loads(api_path.read_text())
api["preuves_a_apporter"] = list(csv.DictReader(open("/root/BASE/preuves.csv")))
api_path.write_text(json.dumps(api, ensure_ascii=False, indent=2))
print(f"API v3 : Preuves {len(api['preuves_a_apporter'])} - dont EN ATTENTE : {sum(1 for p in api['preuves_a_apporter'] if p['statut']=='EN ATTENTE')}")
PY
