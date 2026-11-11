import pathlib, datetime, glob
base = pathlib.Path(__file__).parent
# Dernier fichier TENDANCE
fichiers = sorted(glob.glob(str(base / "TENDANCE-INTERNET-*.md")))
if not fichiers:
    print("VEILLE A FAIRE - Aucune tendance. Lancer les 4 requetes.")
else:
    dernier = pathlib.Path(fichiers[-1])
    age = (datetime.datetime.now() - datetime.datetime.fromtimestamp(dernier.stat().st_mtime)).days
    print(f"Dernier : {dernier.name} - il y a {age} jour(s)")
    if age >= 1:
        print("VEILLE A FAIRE - Tendance vieille de 1 jour ou plus.")
    else:
        print("OK - Tendance a jour, pas de veille a refaire aujourd'hui.")
print("")
print("Requetes a lancer avec Meta AI si VEILLE A FAIRE :")
print("1. prix riz Madagascar aujourd'hui ariary marche")
print("2. prix cafe Madagascar 2026 producteurs export")
print("3. prix miel 1 litre Madagascar ariary")
print("4. prix vanille Madagascar 2026 nouvelles")
print("")
print("Regle : mettre a jour TENDANCE-INTERNET-*.md, JAMAIS prix-locaux.csv avec Internet.")
