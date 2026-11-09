# Export propre Aitif - V4.7
# AITIF. - Data Aitif.
# Exporte seulement les donnees verifiees, avec en-tetes claires
import sqlite3, glob, os, csv
from datetime import datetime

DBS = glob.glob("/root/**/commerce.db", recursive=True)
DB = DBS[0] if DBS else ""

def export():
    print("=== EXPORT PROPRE AITIF. - V4.7 - MADAGASCAR ===")
    if not DB or not os.path.exists(DB):
        print("Pas de base trouvee.")
        return
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d")
    # Ventes propres : montant > 0, produit non vide
    cur.execute("SELECT date, produit, montant FROM ventes WHERE montant > 0 AND produit != '' ORDER BY date")
    ventes = cur.fetchall()
    with open(f"ventes-propres-{date}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Date", "Produit", "Montant (Ar)"])
        w.writerows(ventes)
    print(f"Ventes propres -> ventes-propres-{date}.csv ({len(ventes)} lignes)")
    # Stock propre
    cur.execute("SELECT produit, quantite, prix FROM stock WHERE quantite >= 0 AND prix > 0 ORDER BY produit")
    stocks = cur.fetchall()
    with open(f"stock-propre-{date}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Produit", "Quantite", "Prix (Ar)"])
        w.writerows(stocks)
    print(f"Stock propre -> stock-propre-{date}.csv ({len(stocks)} lignes)")
    conn.close()
    print("\nExport propre : pas de lignes sales, pas de doublons fusionnes.")
    print("Tu peux ouvrir dans Excel sans nettoyer a la main.")

if __name__ == "__main__":
    export()
