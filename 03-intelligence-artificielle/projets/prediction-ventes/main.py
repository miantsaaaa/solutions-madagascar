# Prediction Ventes - V3.1 - Domaine 03 IA
# Lit commerce.db du Domaine 01 et predit demain
import sqlite3, os
from datetime import datetime, timedelta

import glob
DB = glob.glob("/root/**/commerce.db", recursive=True)[0] if glob.glob("/root/**/commerce.db", recursive=True) else ""

def prediction():
    print("=== PREDICTION VENTES - IA - MADAGASCAR ===")
    if not os.path.exists(DB):
        print("Pas de base trouvee. Lance d'abord ton commerce (Domaine 01).")
        return
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    # Ventes des 7 derniers jours
    cur.execute("SELECT date, SUM(montant) FROM ventes GROUP BY date ORDER BY date DESC LIMIT 7")
    rows = cur.fetchall()
    conn.close()
    if not rows:
        print("Pas encore de ventes. Ajoute des ventes dans ton commerce, puis relance.")
        print("Exemple : Riz 5000 Ar, puis relance cette IA.")
        return
    print("\n[Ventes des derniers jours]")
    total = 0
    for date, montant in reversed(rows):
        print(f" - {date} : {montant} Ar")
        total += montant
    moyenne = total / len(rows)
    demain = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    print(f"\n[IA] Moyenne sur {len(rows)} jour(s) : {moyenne:.0f} Ar")
    print(f"[IA] Prediction pour demain ({demain}) : {moyenne:.0f} Ar")
    if moyenne < 10000:
        print("Conseil IA : ventes faibles. Ne rachete pas trop de stock demain.")
    elif moyenne < 50000:
        print("Conseil IA : ventes moyennes. Garde ton stock normal.")
    else:
        print("Conseil IA : bonnes ventes ! Pense a recharger ton stock.")
    print("\nTon IA apprend de TES vraies ventes. Plus tu vends, plus elle devient juste.")

if __name__ == "__main__":
    prediction()