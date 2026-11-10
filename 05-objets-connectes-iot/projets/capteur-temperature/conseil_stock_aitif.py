# Conseil stockage Aitif - V5.15 - 3eme tour - bilan 1 phrase
# Seuils dans seuils_aitif.py, 1 seul endroit.
# Dit si le stock Aitif est en securite, selon la derniere mesure.
# Riz : 15-25 C, humidite < 80 %
# Cafe : 15-25 C, humidite < 70 % (sinon moisissure, perte de gout)
# Miel : < 25 C, humidite < 70 % (sinon fermentation)
import csv, os
from seuils_aitif import SEUILS

def conseil_stock():
    print("=== CONSEIL STOCKAGE AITIF. - V5.15 ===")
    if not os.path.exists("mesures-temperature.csv"):
        print("Aucune mesure. Lance d'abord : python3 main.py")
        return
    with open("mesures-temperature.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    d = rows[-1]
    temp = float(d["Temperature (C)"])
    hum = float(d["Humidite (%)"])
    print(f"Derniere mesure : {d['Date']} {d['Heure']} - {temp} C, {hum} %\n")
    def ok(t_min, t_max, h_max):
        return t_min <= temp <= t_max and hum <= h_max
    ACTIONS = {"Riz": "Aere si humide, couvre si froid.", "Cafe": "Garde au sec, loin du soleil, sinon perte de gout.", "Miel": "Garde au frais, pot bien ferme, sinon fermentation."}
    for produit, s in SEUILS.items():
        t_min, t_max, h_max = s["t_min"], s["t_max"], s["h_max"]
        action = ACTIONS[produit]
        etat = "OK - en securite" if ok(t_min, t_max, h_max) else "ATTENTION - agis"
        print(f"[{produit}] {etat} | {action}")
    ok_n = sum(1 for s in SEUILS.values() if s["t_min"] <= temp <= s["t_max"] and hum <= s["h_max"])
    danger_n = 3 - ok_n
    print(f"\nBilan Capteur : {ok_n}/3 en securite, {danger_n} en danger - {'stock protege.' if danger_n == 0 else 'protege-les, humidite ou temperature menace.'}")
    print("Ton capteur protege tes 3 produits Aitif, pas seulement le riz.")

if __name__ == "__main__":
    conseil_stock()
