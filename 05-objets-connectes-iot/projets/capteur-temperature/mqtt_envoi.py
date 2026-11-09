# Envoi MQTT Aitif - V5.6
# AITIF. - IoT Aitif.
# Envoie la mesure comme un vrai capteur ESP32, via MQTT
# Sans serveur, on simule l'envoi et on l'ecrit dans un fichier mqtt.log
import csv, os, json
from datetime import datetime

def envoyer():
    print("=== ENVOI MQTT AITIF. - V5.6 - FIANARANTSOA ===")
    if not os.path.exists("mesures-temperature.csv"):
        print("Aucune mesure. Lance d'abord : python3 main.py")
        return
    with open("mesures-temperature.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    derniere = rows[-1]
    message = {
        "capteur": "capteur-temperature-fianarantsoa-01",
        "date": derniere["Date"],
        "heure": derniere["Heure"],
        "temperature": float(derniere["Temperature (C)"]),
        "humidite": float(derniere["Humidite (%)"]),
        "lieu": "Fianarantsoa / Madagascar"
    }
    topic = "madagascar/fianarantsoa/capteur-temperature-01"
    print(f"Topic MQTT : {topic}")
    print(f"Message JSON : {json.dumps(message, ensure_ascii=False)}")
    # Simulation : on ecrit dans mqtt.log comme si on l'avait envoye
    with open("mqtt.log", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {topic} | {json.dumps(message, ensure_ascii=False)}\n")
    print("\nEnvoye ! (simule dans mqtt.log, comme un vrai ESP32 vers Mosquitto)")
    print("Quand tu auras un vrai ESP32, tu remplaceras ce fichier par paho-mqtt.")
    print("La logique reste la meme : topic + JSON.")

if __name__ == "__main__":
    envoyer()
