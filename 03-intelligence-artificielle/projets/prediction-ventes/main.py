# Prediction Ventes Aitif - V3.10
# AITIF. - IA Aitif, pour faire evoluer Madagascar
# Prediction avec jour de semaine : samedi != lundi
import sqlite3, glob, os
from datetime import datetime, timedelta

DBS = glob.glob("/root/**/commerce.db", recursive=True)
DB = DBS[0] if DBS else ""

JOURS = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]

def prediction():
    print("=== PREDICTION VENTES AITIF. - V3.6 - MADAGASCAR ===")
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
    print("\n[Ventes passees]")
    total = 0
    par_jour = {}
    for date, montant in rows:
        try:
            d = datetime.strptime(date, "%Y-%m-%d")
            jour = JOURS[d.weekday()]
        except:
            jour = "?"
        print(f" - {date} ({jour}) : {montant} Ar")
        total += montant
        par_jour.setdefault(jour, []).append(montant)
    moyenne = total / len(rows)
    demain = datetime.now() + timedelta(days=1)
    jour_demain = JOURS[demain.weekday()]
    print(f"\n[Moyenne generale] {moyenne:.0f} Ar")
    print(f"[Moyenne par jour de semaine]")
    for j, vals in par_jour.items():
        print(f" - {j} : {sum(vals)/len(vals):.0f} Ar ({len(vals)} jour(s))")
    if jour_demain in par_jour:
        pred = sum(par_jour[jour_demain]) / len(par_jour[jour_demain])
        print(f"\n[IA] Demain c'est {jour_demain} ({demain.strftime('%Y-%m-%d')})")
        print(f"[IA] Prediction basee sur les {jour_demain}s : {pred:.0f} Ar")
    else:
        print(f"\n[IA] Demain c'est {jour_demain}, pas encore de {jour_demain} dans tes ventes.")
        print(f"[IA] Prediction avec moyenne generale : {moyenne:.0f} Ar")
    print("\nPlus tu vends chaque jour, plus ton IA connait chaque jour de semaine.")

if __name__ == "__main__":
    prediction()
    print("\n--- CONSEIL AITIF. ---")
    try:
        from conseil_achat import conseil
        conseil()
    except Exception as e:
        print(f"Conseil non lisible ici : {e}")
    print("\n--- ALERTE AITIF. ---")
    try:
        from alerte_stock import alerte
        alerte()
    except Exception as e:
        print(f"Alerte non lisible ici : {e}")
