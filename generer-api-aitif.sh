#!/bin/bash
# AITIF V2 - 1 seul generateur API. Lit BASE/*.csv -> docs/aitif-api.json. N'appelle personne. Pas de chaine.
python3 << 'PY'
import json, csv, pathlib
base = pathlib.Path("/root/BASE")
out = pathlib.Path("/root/docs/aitif-api.json")
def lire(nom):
    p = base / nom
    return list(csv.DictReader(open(p, encoding="utf-8"))) if p.exists() else []
api = {
  "entreprise": "AITIF",
  "pays": "Madagascar",
  "villes": ["Fianarantsoa", "Toamasina"],
  "principe": "On ne promet pas, on prouve. Petit a petit, toujours bien organise.",
  "regle": "REEL = vu. SIMULATION = entraine. IDEE = a verifier.",
  "architecture": "V2 - 1 chose = 1 fichier, 1 appel = 1 sens, verifier avant de faire",
  "produits": lire("produits.csv"),
  "prix_reels": lire("prix-reels.csv"),
  "stock": lire("stock.csv"),
  "ventes": lire("ventes.csv"),
  "savoirs": lire("savoirs.csv"),
  "domaines": lire("domaines.csv"),
  "regions": lire("regions.csv"),
  "historique": lire("historique.csv"),
  "preuves": lire("preuves.csv"),
  "partages": lire("partages.csv"),
  "agents": lire("agents.csv"),
  "agents_evolution": lire("agents-evolution.csv"),
  "projets_par_domaine": lire("projets-par-domaine.csv"),
  "regles_anti_faillite": lire("regles-anti-faillite.csv"),
  "systeme": "Vision + Agents + Base + Projets par domaine + Regles anti-faillite + Preuves - Tout evolue ensemble",
}
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(api, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"API V2 propre : Produits {len(api['produits'])} - Savoirs {len(api['savoirs'])} - Regions {len(api['regions'])} - Projets par domaine {len(api["projets_par_domaine"])} - Prix reels {len(api["prix_reels"])} - Agents {len(api['agents'])} - 1 generateur, 0 chaine")
PY
