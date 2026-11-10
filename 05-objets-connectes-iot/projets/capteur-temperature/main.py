# Capteur Temperature Aitif - V5.12 - 3eme tour
# AITIF. - IoT Aitif.
# Simule un capteur ESP32 a Fianarantsoa, sans materiel
import random, csv, os
from datetime import datetime

FICHIER = "mesures-temperature.csv"

def mesurer():
    print("=== CAPTEUR TEMPERATURE AITIF. - V5.12 - FIANARANTSOA ===")
    # Fianarantsoa : entre 12 et 26 degres en general
    # On simule comme un vrai capteur avec un peu de bruit
    heure = datetime.now().hour
    if 0 <= heure < 6:
        base = 14  # nuit froide
    elif 6 <= heure < 12:
        base = 19  # matin
    elif 12 <= heure < 18:
        base = 24  # apres-midi chaud
    else:
        base = 18  # soir
    temp = round(base + random.uniform(-2, 2), 1)
    humidite = round(random.uniform(55, 85), 1)
    print(f"Heure : {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Temperature : {temp} C")
    print(f"Humidite : {humidite} %")
    if temp < 15:
        print("Etat : FROID - couvre ton stock, surtout les legumes.")
    elif temp <= 25:
        print("Etat : NORMAL - bon pour le stockage du riz.")
    else:
        print("Etat : CHAUD - aere ton stock, risque de moisissure.")
    # Sauvegarde
    existe = os.path.exists(FICHIER)
    with open(FICHIER, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if not existe:
            w.writerow(["Date", "Heure", "Temperature (C)", "Humidite (%)"])
        w.writerow([datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M"), temp, humidite])
    print(f"\nMesure sauvegardee dans : {FICHIER}")
    from seuils_aitif import seuil_pour
    print("\n[Par produit - seuils Aitif]")
    for prod in ["Riz", "Cafe", "Miel"]:
        s = seuil_pour(prod)
        ok_t = s["t_min"] <= temp <= s["t_max"]
        ok_h = humidite <= s["h_max"]
        if ok_t and ok_h:
            print(f" - {prod} : OK ({temp} C, {humidite} %)")
        else:
            print(f" - {prod} : DANGER ({temp} C, {humidite} %) - seuil {s['t_min']}-{s['t_max']} C, humidite max {s['h_max']} %")
    print("Un vrai capteur ESP32 ferait exactement la meme chose.")

if __name__ == "__main__":
    mesurer()
    print("\n--- ALERTE AITIF. ---")
    try:
        from alerte import alerte
        alerte()
    except Exception as e:
        print(f"Alerte non lisible ici : {e}")
    print("\n--- CONSEIL STOCKAGE AITIF. ---")
    try:
        from conseil_stock_aitif import conseil_stock
        conseil_stock()
    except Exception as e:
        print(f"Conseil non lisible ici : {e}")
