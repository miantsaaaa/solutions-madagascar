# Graphique evolution ventes - V3.4 - Domaine 03 IA
# Genere une image PNG que tu peux ouvrir sur ton Redmi
import sqlite3, glob, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DBS = glob.glob("/root/**/commerce.db", recursive=True)
DB = DBS[0] if DBS else ""

def graphique():
    print("=== GRAPHIQUE VENTES - IA - MADAGASCAR ===")
    if not DB or not os.path.exists(DB):
        print("Pas de base trouvee.")
        return
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT date, SUM(montant) FROM ventes GROUP BY date ORDER BY date")
    rows = cur.fetchall()
    conn.close()
    if not rows:
        print("Pas encore de ventes.")
        return
    dates = [r[0] for r in rows]
    montants = [r[1] for r in rows]
    plt.figure(figsize=(8, 4))
    plt.plot(dates, montants, marker="o", linewidth=2)
    plt.title("Evolution des ventes - Madagascar (Ar)")
    plt.xlabel("Date")
    plt.ylabel("Ventes (Ar)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("evolution-ventes.png")
    print(f"Ventes : {list(zip(dates, montants))}")
    print("Graphique sauvegarde : evolution-ventes.png")
    print("Ouvre-le dans ta Galerie pour voir la courbe.")

if __name__ == "__main__":
    graphique()
