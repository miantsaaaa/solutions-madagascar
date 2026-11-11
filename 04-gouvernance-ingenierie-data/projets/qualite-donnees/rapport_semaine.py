# V4.19 : Rapport Semaine Qualite - Qualite Donnees
# AITIF. - Data Aitif, pour faire evoluer Madagascar
import sqlite3, glob, os
DBS = glob.glob("/root/*/projets/**/commerce.db", recursive=True)
DB = DBS[0] if DBS else ""
def rapport_semaine():
    print("=== RAPPORT SEMAINE QUALITE - V4.19 ===")
    if not DB or not os.path.exists(DB):
        print("Pas de base trouvee.")
        return
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    checks = []
    cur.execute("SELECT COUNT(*) FROM ventes WHERE montant <= 0")
    checks.append(("Ventes montant <= 0", cur.fetchone()[0]))
    cur.execute("SELECT COUNT(*) FROM ventes WHERE produit IS NULL OR produit = ''")
    checks.append(("Ventes sans produit", cur.fetchone()[0]))
    cur.execute("SELECT COUNT(*) FROM stock WHERE quantite < 0")
    checks.append(("Stock quantite negative", cur.fetchone()[0]))
    cur.execute("SELECT COUNT(*) FROM stock WHERE prix <= 0")
    checks.append(("Stock prix <= 0", cur.fetchone()[0]))
    cur.execute("SELECT COUNT(*) FROM depenses WHERE montant <= 0")
    checks.append(("Depenses montant <= 0", cur.fetchone()[0]))
    cur.execute("SELECT COUNT(*) FROM ventes")
    nb_v = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM stock")
    nb_s = cur.fetchone()[0]
    conn.close()
    erreurs = sum(c[1] for c in checks)
    total = len(checks)
    score = int((total - sum(1 for _, v in checks if v > 0)) / total * 100) if total else 0
    print(f"\n[Semaine] {nb_v} vente(s), {nb_s} produit(s) en stock")
    for nom, val in checks:
        print(f" - {nom} : {val} {'ERREUR' if val > 0 else 'OK'}")
    print(f"\n[SCORE QUALITE SEMAINE] {score} / 100")
    if score == 100:
        print("Semaine propre. Tu peux decider, tes donnees sont propres.")
    else:
        print(f"Semaine avec {erreurs} erreur(s). Corrige avant de decider.")
    print("\n=== TERMINE - Rapport Semaine Qualite V4.19 fini ===")
if __name__ == "__main__":
    rapport_semaine()
