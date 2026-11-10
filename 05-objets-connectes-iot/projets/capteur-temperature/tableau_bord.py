# Tableau de bord temperature Aitif - V5.14 - 3eme tour
# AITIF. - IoT Aitif.
# 1 ecran : derniere mesure, moyenne, alerte, historique
import csv, os

def tableau():
    print("=== TABLEAU DE BORD TEMPERATURE AITIF. - V5.14 - FIANARANTSOA / MADAGASCAR ===")
    if not os.path.exists("mesures-temperature.csv"):
        print("Aucune mesure. Lance : python3 main.py")
        return
    with open("mesures-temperature.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    derniere = rows[-1]
    temps = [float(r["Temperature (C)"]) for r in rows]
    hums = [float(r["Humidite (%)"]) for r in rows]
    print(f"\n[DERNIERE MESURE] {derniere['Date']} {derniere['Heure']} : {derniere['Temperature (C)']} C, {derniere['Humidite (%)']} %")
    print(f"[JOURNEE] {len(rows)} mesure(s) | Min {min(temps)} C | Max {max(temps)} C | Moyenne {sum(temps)/len(temps):.1f} C")
    print(f"[HUMIDITE] Moyenne {sum(hums)/len(hums):.1f} %")
    temp = float(derniere["Temperature (C)"])
    if temp < 15:
        print("[ALERTE] FROID - couvre ton stock")
    elif temp > 25:
        print("[ALERTE] CHAUD - aere ton stock")
    else:
        print("[ETAT] NORMAL - stock en securite")
    from seuils_aitif import seuil_pour
    hum_der = float(derniere["Humidite (%)"])
    print("\n[PRODUITS - seuils Aitif]")
    for prod in ["Riz", "Cafe", "Miel"]:
        s = seuil_pour(prod)
        ok = s["t_min"] <= temp <= s["t_max"] and hum_der <= s["h_max"]
        etat = "OK" if ok else "DANGER"
        print(f" - {prod} : {etat} ({temp} C, {hum_der} %)")
    print("\n[HISTORIQUE]")
    for r in rows[-5:]:
        barre = "#" * int(float(r["Temperature (C)"]))
        print(f" {r['Heure']} {r['Temperature (C)']} C |{barre}")
    print("\nTon tableau de bord IoT est pret. C'est comme ca qu'un commercant voit son stock en 1 coup d'oeil.")

if __name__ == "__main__":
    tableau()
