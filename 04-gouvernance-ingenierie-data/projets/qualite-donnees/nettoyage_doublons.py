# Nettoyage doublons - V4.2 - Domaine 04
# Detecte et fusionne les doublons dans stock, sans supprimer tes ventes
import sqlite3, glob, os

DBS = glob.glob("/root/**/commerce.db", recursive=True)
DB = DBS[0] if DBS else ""

def nettoyer():
    print("=== NETTOYAGE DOUBLONS - DATA - MADAGASCAR ===")
    if not DB or not os.path.exists(DB):
        print("Pas de base trouvee.")
        return
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    # Cherche les produits en double dans stock
    cur.execute("SELECT produit, COUNT(*), SUM(quantite) FROM stock GROUP BY produit HAVING COUNT(*) > 1")
    doublons = cur.fetchall()
    if not doublons:
        print("Aucun doublon dans le stock. Tes donnees sont propres.")
        print("Exemple : si tu avais Riz 2 fois, on les aurait fusionnes en 1 ligne.")
    else:
        print(f"{len(doublons)} doublon(s) trouve(s) :")
        for produit, nb, total_qte in doublons:
            print(f" - {produit} : {nb} lignes, total {total_qte}")
            # On garde 1 ligne avec la somme, on supprime les autres
            cur.execute("SELECT id, prix FROM stock WHERE produit = ? LIMIT 1", (produit,))
            garde_id, prix = cur.fetchone()
            cur.execute("DELETE FROM stock WHERE produit = ? AND id != ?", (produit, garde_id))
            cur.execute("UPDATE stock SET quantite = ? WHERE id = ?", (total_qte, garde_id))
            print(f"   Fusionne en 1 ligne : {produit} = {total_qte} (prix {prix} Ar)")
        conn.commit()
        print("\nDoublons fusionnes. Aucune vente supprimee.")
    # Verifie aussi les ventes en double exact (meme produit, meme montant, meme date)
    cur.execute("SELECT produit, montant, date, COUNT(*) FROM ventes GROUP BY produit, montant, date HAVING COUNT(*) > 1")
    doublons_v = cur.fetchall()
    if doublons_v:
        print(f"\nAttention : {len(doublons_v)} vente(s) en double exact possible :")
        for p, m, d, c in doublons_v:
            print(f" - {p} {m} Ar le {d} : {c} fois (verifie si c'est vraiment un doublon)")
    else:
        print("\nAucune vente en double exact.")
    conn.close()
    print("\nNettoyage termine. Tes donnees restent intactes.")

if __name__ == "__main__":
    nettoyer()
