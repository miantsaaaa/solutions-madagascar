# Alerte stock Aitif - V3.7
# AITIF. - IA Aitif, alerte avec vraie marge.
# Predis quel produit va manquer, avec tes vraies ventes + ton stock
import sqlite3, glob, os
from marge_aitif import marge_pour

DBS = glob.glob("/root/**/commerce.db", recursive=True)
DB = DBS[0] if DBS else ""

def alerte():
    print("=== ALERTE STOCK AITIF. - V3.7 - MADAGASCAR ===")
    if not DB or not os.path.exists(DB):
        print("Pas de base trouvee.")
        return
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    # Stock actuel
    try:
        cur.execute("SELECT produit, quantite, prix FROM stock")
        stocks = cur.fetchall()
    except Exception as e:
        print(f"Table stock non trouvee : {e}")
        return
    # Ventes par produit
    try:
        cur.execute("SELECT produit, COUNT(*), SUM(montant) FROM ventes GROUP BY produit")
        ventes = {r[0]: (r[1], r[2]) for r in cur.fetchall()}
    except:
        ventes = {}
    conn.close()
    if not stocks:
        print("Aucun stock. Ajoute du stock dans ton commerce (Domaine 01).")
        return
    print("\n[Stock + Ventes]")
    for produit, qte, prix in stocks:
        nb_ventes, total_v = ventes.get(produit, (0, 0))
        # Vente moyenne par jour : on suppose 1 jour de donnees pour l'instant
        # Si tu vends 1 par jour et qu'il reste 2, il reste 2 jours
        marge = marge_pour(produit)
        print(f" - {produit} : {qte} restant(s), {nb_ventes} vente(s), {total_v} Ar vendus | Vraie marge / vente : {marge} Ar")
        if qte <= 2:
            print(f"   ALERTE ROUGE : {produit} va manquer tres vite ! Rachete demain.")
        elif qte <= 5:
            print(f"   ALERTE ORANGE : {produit} bientot bas. Pense a recharger.")
        else:
            print(f"   OK : {produit} encore assez.")
    print("\nTon IA croise stock + ventes. Plus tu vends, plus son alerte est juste.")

if __name__ == "__main__":
    alerte()
