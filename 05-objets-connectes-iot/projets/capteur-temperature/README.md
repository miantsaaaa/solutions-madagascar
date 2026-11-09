# IoT Aitif - Capteur Temperature - V5.8

## Probleme Madagascar
A Fianarantsoa, il fait froid la nuit, chaud le jour.
Un commercant qui stocke du riz, du cafe, du miel, doit savoir s'il fait trop chaud ou trop froid.
Sans capteur, il le decouvre trop tard.

## Solution Aitif
Un capteur IoT simule qui mesure la temperature, comme un vrai capteur ESP32.
100% sur Redmi, sans acheter de materiel pour commencer.
Petit a petit, toujours bien organise. On ne promet pas, on prouve.

## Comment lancer
python3 main.py
python3 alerte.py
python3 historique.py
python3 tableau_bord.py
python3 mqtt_envoi.py
python3 conseil_stock_aitif.py

## Structure - plusieurs fichiers, pas trop de code dans un fichier
- `main.py` - simule une mesure, sauvegarde dans mesures-temperature.csv
- `alerte.py` - lit la derniere mesure, dit si tu dois agir maintenant
- `historique.py` - montre l'evolution de la journee, min / max / moyenne
- `tableau_bord.py` - 1 ecran : derniere mesure, moyenne, alerte, historique
- `mqtt_envoi.py` - envoie la mesure comme un vrai ESP32, via MQTT (simule dans mqtt.log)
- `conseil_stock_aitif.py` - dit si Riz + Cafe + Miel sont en securite, selon temperature + humidite

## Fonctions
- Simule une mesure de temperature a Fianarantsoa
- Dit si c'est froid, normal, ou trop chaud pour le stockage
- Conseil stockage pour les 3 produits Aitif
- Sauvegarde chaque mesure

## Regles Aitif
Verification ne compte pas comme version, seule une amelioration compte comme Vx.x.
Sans frais, la marge ment. Avec frais, on sait vraiment.

## Pour qui
Pour tout commercant a Madagascar qui veut proteger son stock avant qu'il soit trop tard.
