# Rapport mensuel Aitif - V4.14 - 3eme tour
# AITIF. - Data Aitif.
# Bilan du mois : ventes, depenses, benefice, meilleur produit
import sqlite3, glob, os
from datetime import datetime
from marge_aitif import marge_pour

DBS = glob.glob("/root/**/commerce.db", recursive=True)
DB = DBS[0] if DBS else ""

def rapport():
    print("=== RAPPORT MENSUEL AITIF. - V4.14 - MADAGASCAR ===")
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
    cur.execute("SELECT produit, COUNT(*) FROM ventes WHERE date LIKE ? GROUP BY produit", (mois+"%",))
    benef_vrai = 0
    for prod, nb in cur.fetchall():
        benef_vrai += nb * marge_pour(prod)
    conn.close()
    print(f"\n[VENTES] {nb_v} vente(s) : {total_v} Ar")
    print(f"[DEPENSES] {nb_d} depense(s) : {total_d} Ar")
    print(f"[BENEFICE] {total_v - total_d} Ar (ventes - depenses)")
    print(f"[BENEFICE VRAIE MARGE] {benef_vrai} Ar (avec frais, on sait vraiment)")
    if top:
        print(f"\n[MEILLEUR PRODUIT] {top[0]} : {top[1]} vente(s), {top[2]} Ar | Vraie marge / vente : {marge_pour(top[0])} Ar")
    else:
        print("\n[MEILLEUR PRODUIT] Aucune vente ce mois.")
    if stock_bas:
        print(f"[STOCK LE PLUS BAS] {stock_bas[0]} : {stock_bas[1]} restant(s)")
    print("\nCe rapport est propre : il vient de donnees verifiees (V4.1 + V4.2).")
    print("Tu peux le garder chaque mois pour voir ton evolution.")

if __name__ == "__main__":
    rapport()
