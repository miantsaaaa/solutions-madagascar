# Conseil stockage Aitif - V5.7
# Dit si le stock Aitif est en securite, selon la derniere mesure.
# Riz : 15-25 C, humidite < 80 %
# Cafe : 15-25 C, humidite < 70 % (sinon moisissure, perte de gout)
# Miel : < 25 C, humidite < 70 % (sinon fermentation)
import csv, os

def conseil_stock():
    print("=== CONSEIL STOCKAGE AITIF. - V5.7 ===")
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
    for produit, t_min, t_max, h_max, action in [
        ("Riz", 15, 25, 80, "Aere si humide, couvre si froid."),
        ("Cafe", 15, 25, 70, "Garde au sec, loin du soleil, sinon perte de gout."),
        ("Miel", 0, 25, 70, "Garde au frais, pot bien ferme, sinon fermentation."),
    ]:
        etat = "OK - en securite" if ok(t_min, t_max, h_max) else "ATTENTION - agis"
        print(f"[{produit}] {etat} | {action}")
    print("\nTon capteur protege tes 3 produits Aitif, pas seulement le riz.")

if __name__ == "__main__":
    conseil_stock()
