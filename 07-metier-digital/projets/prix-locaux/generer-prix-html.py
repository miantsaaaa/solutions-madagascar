import csv, pathlib, html
base = pathlib.Path(__file__).parent
csv_path = base / "prix-locaux.csv"
out = pathlib.Path("/root/docs/prix.html")
rows = list(csv.DictReader(open(csv_path, encoding="utf-8")))
lignes = ""
for r in rows:
    lignes += f"<tr><td>{html.escape(r['date'])}</td><td>{html.escape(r['produit'])}</td><td>{html.escape(r['categorie'])}</td><td>{html.escape(r['region'])}</td><td>{html.escape(r['ville'])}</td><td>{html.escape(r['lieu'])}</td><td>{html.escape(r['prix_ar'])} Ar</td><td>{html.escape(r['source'])}</td></tr>\n"
if not lignes:
    lignes = "<tr><td colspan='8'><i>0 prix pour l'instant. Squelette pret. On ajoute les vrais prix petit a petit.</i></td></tr>"
out.write_text(f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Prix Locaux - Madagascar entier - Aitif</title><link rel="stylesheet" href="style.css"></head><body><h1>Prix Locaux - Madagascar entier 🇲🇬</h1><p>Pas de prix invente. Chaque prix : date + region + ville + lieu + source.</p><p><b>{len(rows)} prix reels</b> - Riz / Cafe / Miel = exemples seulement, tous produits bienvenus.</p><table border="1" cellpadding="6"><tr><th>Date</th><th>Produit</th><th>Categorie</th><th>Region</th><th>Ville</th><th>Lieu</th><th>Prix</th><th>Source</th></tr>{lignes}</table><p><a href="ajouter-prix.html">+ Ajouter un prix</a> | <a href="index.html">← Portfolio</a></p><footer>Internet = tendance, Marche = vrai prix.</footer></body></html>""", encoding="utf-8")
print(f"OK - {len(rows)} prix - {out}")
