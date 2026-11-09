# Alerte temperature Aitif - V5.6
# AITIF. - IoT Aitif.
# Lit la derniere mesure et te dit si tu dois agir maintenant
import csv, os

def alerte():
    print("=== ALERTE TEMPERATURE AITIF. - V5.6 - FIANARANTSOA ===")
    if not os.path.exists("mesures-temperature.csv"):
        print("Aucune mesure. Lance d'abord : python3 main.py")
        return
    with open("mesures-temperature.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    derniere = rows[-1]
    temp = float(derniere["Temperature (C)"])
    hum = float(derniere["Humidite (%)"])
    print(f"Derniere mesure : {derniere['Date']} {derniere['Heure']} - {temp} C, {hum} %")
    if temp < 12:
        print("\nALERTE ROUGE FROID : il fait tres froid !")
        print("Action : couvre ton stock, ferme les fenetres, protege les legumes et medicaments.")
    elif temp < 15:
        print("\nALERTE ORANGE FROID : il fait froid.")
        print("Action : couvre ton stock ce soir.")
    elif temp > 28:
        print("\nALERTE ROUGE CHAUD : il fait tres chaud !")
        print("Action : aere tout de suite, ouvre, deplace ton stock a l'ombre, risque de moisissure.")
    elif temp > 25:
        print("\nALERTE ORANGE CHAUD : il fait chaud.")
        print("Action : aere ton stock, verifie qu'il n'est pas au soleil.")
    else:
        print("\nOK : temperature normale, pas d'action. Ton stock est en securite.")
    if hum > 85:
        print("Humidite tres haute : risque de moisissure sur le riz. Aere.")
    elif hum > 80:
        print("Humidite haute : surveille ton riz.")
    print("\nTon capteur te previent avant que ce soit trop tard.")

if __name__ == "__main__":
    alerte()
