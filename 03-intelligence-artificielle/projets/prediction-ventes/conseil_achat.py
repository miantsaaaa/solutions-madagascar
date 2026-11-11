# Conseil achat Aitif - V3.12 - 3eme tour
# AITIF. - IA Aitif, conseille avec la vraie marge.
# Ton IA te dit quoi acheter, combien, et combien ca va couter
import sqlite3, glob, os
from marge_aitif import marge_pour

DBS = glob.glob("/root/*/projets/**/commerce.db", recursive=True)  # V3.18 : scan projets seulement
DB = DBS[0] if DBS else ""

def conseil():
    print("=== CONSEIL ACHAT AITIF. - V3.12 - MADAGASCAR ===")
    if not DB or not os.path.exists(DB):
        print("Pas de base trouvee.")
        return
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT produit, quantite, prix FROM stock")
    stocks = cur.fetchall()
    cur.execute("SELECT produit, COUNT(*) FROM ventes GROUP BY produit")
    ventes = dict(cur.fetchall())
    conn.close()
    if not stocks:
        print("Aucun stock.")
        return
    print("\n[Conseil de ton IA pour demain]")
    total_achat = 0
    total_benef = 0
    for produit, qte, prix in stocks:
        nb = ventes.get(produit, 0)
        # Regle simple : si tu as vendu et qu'il reste peu, rachete pour 7 jours
        # Exemple : tu vends 1 par jour, il reste 2 -> rachete 5 pour tenir 7 jours
        besoin = 7 - qte  # viser 7 jours de stock
        if nb > 0 and qte < 7:
            if besoin > 0:
                cout = besoin * prix
                total_achat += cout
                marge = marge_pour(produit)
                total_benef += besoin * marge
                print(f" - {produit} : il reste {qte}, tu vends ~{nb} / jour. Rachete {besoin} x {prix} Ar = {cout} Ar | Vraie marge / vente : {marge} Ar")
            else:
                print(f" - {produit} : stock OK ({qte}), pas besoin d'acheter.")
        elif qte >= 7:
            print(f" - {produit} : stock OK ({qte}), pas besoin d'acheter.")
        else:
            print(f" - {produit} : pas encore de vente, garde ton stock ({qte}).")
    print(f"\n[Budget achat total prevu] : {total_achat} Ar")
    print(f"[Benefice total attendu avec cet achat] : {total_benef} Ar")
    if total_achat == 0:
        print("Conseil IA : n'achete rien demain, ton stock tient.")
    else:
        print("Conseil IA : achete juste ce qu'il faut, pas plus. Ton argent reste dans ta poche.")
    print("\nTon IA devient ton conseiller. C'est ca, l'IA pour Madagascar.")

if __name__ == "__main__":
    conseil()
