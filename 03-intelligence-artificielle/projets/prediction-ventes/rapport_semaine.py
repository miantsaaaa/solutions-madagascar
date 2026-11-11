# V3.19 : Rapport Semaine Ventes - Prediction Ventes
# AITIF. - IA Aitif, pour faire evoluer Madagascar
import sqlite3, glob, os
from datetime import datetime, timedelta
DBS = glob.glob("/root/*/projets/**/commerce.db", recursive=True)
DB = DBS[0] if DBS else ""
JOURS = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
def rapport_semaine():
    print("=== RAPPORT SEMAINE VENTES - V3.19 ===")
    if not DB or not os.path.exists(DB):
        print("Pas de base trouvee.")
        return
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT date, SUM(montant) FROM ventes GROUP BY date ORDER BY date")
    rows = cur.fetchall()
    cur.execute("SELECT produit, COUNT(*), SUM(montant) FROM ventes GROUP BY produit")
    par_produit = cur.fetchall()
    conn.close()
    if not rows:
        print("Pas encore de ventes cette semaine.")
        return
    total = sum(m for _, m in rows)
    print(f"\n[Semaine] {len(rows)} jour(s) de ventes, total {total} Ar, moyenne {total/len(rows):.0f} Ar / jour")
    meilleur_jour = max(rows, key=lambda x: x[1])
    print(f" - Meilleur jour : {meilleur_jour[0]} ({JOURS[datetime.strptime(meilleur_jour[0], '%Y-%m-%d').weekday()]}) : {meilleur_jour[1]} Ar")
    print("\n[Par produit]")
    for prod, nb, tot in par_produit:
        print(f" - {prod} : {nb} vente(s), {tot} Ar")
    print("\n=== TERMINE - Rapport Semaine V3.19 fini ===")
if __name__ == "__main__":
    rapport_semaine()
