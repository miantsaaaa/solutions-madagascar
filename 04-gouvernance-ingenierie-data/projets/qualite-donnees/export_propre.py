# Export propre Aitif - V4.19 CALME
# Regle Aitif V2 : 1 chose = 1 fichier. BASE/stock.csv et BASE/ventes.csv sont la verite.
# On ne cree plus ventes-propres-DATE.csv ni stock-propre-DATE.csv.
# On lit BASE, on compte, on ne cree rien.
import pathlib, csv
def export():
    print("=== EXPORT PROPRE AITIF - V4.19 CALME ===")
    base = pathlib.Path("/root/BASE")
    for nom in ["stock.csv", "ventes.csv"]:
        p = base / nom
        if p.exists():
            lignes = list(csv.DictReader(open(p, encoding="utf-8")))
            print(f"{nom} : {len(lignes)} lignes dans BASE - pas de copie creee")
        else:
            print(f"{nom} : pas encore dans BASE")
    print("BASE est la verite. Aucun fichier par jour cree.")
    print("=== TERMINE - Export Propre V4.19 calme, Miantsa peut verifier ===")
if __name__ == "__main__":
    export()
