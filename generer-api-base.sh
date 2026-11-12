#!/bin/bash
# BASE AITIF - API simple : 1 fichier JSON = toute la base, pour l'application de demain
python3 << 'PY'
import csv, json, pathlib
base = pathlib.Path("/root/BASE")
def lire(nom):
    p = base / nom
    if not p.exists():
        return []
    return list(csv.DictReader(open(p, encoding="utf-8")))
# Prix reels - depuis le vrai fichier, jamais simulation
prix_path = pathlib.Path("/root/07-metier-digital/projets/prix-locaux/prix-locaux.csv")
prix = list(csv.DictReader(open(prix_path))) if prix_path.exists() else []
api = {
  "entreprise": "AITIF",
  "pays": "Madagascar",
  "villes": ["Fianarantsoa", "Toamasina"],
  "principe": "On ne promet pas, on prouve. Petit a petit, toujours bien organise.",
  "regle": "REEL = vu. SIMULATION = entraine. IDEE = a verifier.",
  "produits": lire("produits.csv"),
  "prix_reels": prix,
  "stock": lire("stock.csv"),
  "ventes": lire("ventes.csv"),
  "savoirs": lire("savoirs.csv"),
  "domaines": lire("domaines.csv"),
  "agents": [{"id": f"{i:02d}", "etat": "VIVANT"} for i in range(8)],
}
out = pathlib.Path("/root/docs/aitif-api.json")
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(api, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"API generee : {out} - Produits {len(api['produits'])} - Prix reels {len(prix)} - Stock {len(api['stock'])} - Savoirs {len(api['savoirs'])} - Domaines {len(api['domaines'])}")
PY
cat ~/docs/aitif-api.json | head -30
