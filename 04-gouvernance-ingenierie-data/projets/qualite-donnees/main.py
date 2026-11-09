# Qualite Donnees - V4.1 - Domaine 04 Gouvernance Data
# Controle tes donnees commerce et donne un score / 100
import sqlite3, glob, os

DBS = glob.glob("/root/**/commerce.db", recursive=True)
DB = DBS[0] if DBS else ""

def controle():
    print("=== QUALITE DONNEES - MADAGASCAR ===")
    if not DB or not os.path.exists(DB):
        print("Pas de base trouvee.")
        return
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    erreurs = 0
    total_checks = 0
    print("\n[VENTES]")
    cur.execute("SELECT COUNT(*) FROM ventes")
    nb_v = cur.fetchone()[0]
    print(f" - Nombre de ventes : {nb_v}")
    cur.execute("SELECT COUNT(*) FROM ventes WHERE montant <= 0")
    bad = cur.fetchone()[0]
    total_checks += 1
    if bad > 0:
        print(f"   ERREUR : {bad} vente(s) avec montant <= 0")
        erreurs += 1
    else:
        print("   OK : aucun montant a 0 ou negatif")
    cur.execute("SELECT COUNT(*) FROM ventes WHERE produit IS NULL OR produit = ''")
    bad = cur.fetchone()[0]
    total_checks += 1
    if bad > 0:
        print(f"   ERREUR : {bad} vente(s) sans nom de produit")
        erreurs += 1
    else:
        print("   OK : tous les produits ont un nom")
    print("\n[STOCK]")
    cur.execute("SELECT COUNT(*) FROM stock")
    nb_s = cur.fetchone()[0]
    print(f" - Nombre de produits en stock : {nb_s}")
    cur.execute("SELECT COUNT(*) FROM stock WHERE quantite < 0")
    bad = cur.fetchone()[0]
    total_checks += 1
    if bad > 0:
        print(f"   ERREUR : {bad} produit(s) avec quantite negative")
        erreurs += 1
    else:
        print("   OK : aucune quantite negative")
    cur.execute("SELECT COUNT(*) FROM stock WHERE prix <= 0")
    bad = cur.fetchone()[0]
    total_checks += 1
    if bad > 0:
        print(f"   ERREUR : {bad} produit(s) avec prix <= 0")
        erreurs += 1
    else:
        print("   OK : tous les prix > 0")
    print("\n[DEPENSES]")
    cur.execute("SELECT COUNT(*) FROM depenses")
    nb_d = cur.fetchone()[0]
    print(f" - Nombre de depenses : {nb_d}")
    cur.execute("SELECT COUNT(*) FROM depenses WHERE montant <= 0")
    bad = cur.fetchone()[0]
    total_checks += 1
    if bad > 0:
        print(f"   ERREUR : {bad} depense(s) avec montant <= 0")
        erreurs += 1
    else:
        print("   OK : aucune depense a 0")
    conn.close()
    score = int((total_checks - erreurs) / total_checks * 100) if total_checks else 0
    print(f"\n[SCORE QUALITE] {score} / 100")
    if score == 100:
        print("Tes donnees sont PROPRES. Tu peux leur faire confiance.")
    elif score >= 80:
        print("Tes donnees sont bonnes, corrige les petites erreurs.")
    else:
        print("Tes donnees sont sales. Il faut nettoyer avant de decider.")
    print("\nLa gouvernance, c'est ca : ne pas decider sur de fausses donnees.")

if __name__ == "__main__":
    controle()
