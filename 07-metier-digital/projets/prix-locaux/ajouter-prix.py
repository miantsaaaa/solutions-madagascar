import argparse, csv, datetime, pathlib
p = argparse.ArgumentParser()
p.add_argument("--produit", required=True)
p.add_argument("--lieu", required=True)
p.add_argument("--prix", required=True, type=int)
p.add_argument("--source", required=True)
p.add_argument("--vu-par", default="Miantsa")
p.add_argument("--note", default="")
a = p.parse_args()
f = pathlib.Path(__file__).parent / "prix-locaux.csv"
with open(f, "a", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow([datetime.date.today().isoformat(), a.produit, a.lieu, a.prix, a.source, a.vu_par, a.note])
print(f"OK - {a.produit} - {a.prix} Ar - {a.lieu} - {a.source}")
