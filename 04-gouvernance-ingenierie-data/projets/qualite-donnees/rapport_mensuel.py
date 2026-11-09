# Rapport data mensuel - V4.3 - Domaine 04
# Bilan du mois : ventes, depenses, benefice, meilleur produit
import sqlite3, glob, os
from datetime import datetime

DBS = glob.glob("/root/**/commerce.db", recursive=True)
DB = DBS[0] if DBS else ""

def rapport():
    print("=== RAPPORT DATA MENSUEL - MADAGASCAR ===")
    if not DB or not os.path.exists(DB):
        print("Pas de base trouvee.")
        return
    mois = datetime.now().strftime("%Y-%m")
    print(f"Mois : {mois}")
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*), COALESCE(SUM(montant),0) FROM ventes WHERE date LIKE ?", (mois+"%",))
    nb_v, total_v = cur.fetchone()
    cur.execute("SELECT COUNT(*), COALESCE(SUM(montant),0) FROM depenses WHERE date LIKE ?", (mois+"%",))
    nb_d, total_d = cur.fetchone()
    cur.execute("SELECT produit, COUNT(*), SUM(montant) FROM ventes WHERE date LIKE ? GROUP BY produit ORDER BY SUM(montant) DESC LIMIT 1", (mois+"%",))
    top = cur.fetchone()
    cur.execute("SELECT produit, quantite FROM stock ORDER BY quantite ASC LIMIT 1")
    stock_bas = cur.fetchone()
    conn.close()
    print(f"\n[VENTES] {nb_v} vente(s) : {total_v} Ar")
    print(f"[DEPENSES] {nb_d} depense(s) : {total_d} Ar")
    print(f"[BENEFICE] {total_v - total_d} Ar (ventes - depenses)")
    if top:
        print(f"\n[MEILLEUR PRODUIT] {top[0]} : {top[1]} vente(s), {top[2]} Ar")
    else:
        print("\n[MEILLEUR PRODUIT] Aucune vente ce mois.")
    if stock_bas:
        print(f"[STOCK LE PLUS BAS] {stock_bas[0]} : {stock_bas[1]} restant(s)")
    print("\nCe rapport est propre : il vient de donnees verifiees (V4.1 + V4.2).")
    print("Tu peux le garder chaque mois pour voir ton evolution.")

if __name__ == "__main__":
    rapport()
