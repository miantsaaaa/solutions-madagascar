# Capteur Temperature - V5.1
## Probleme Madagascar
A Fianarantsoa, il fait froid la nuit, chaud le jour.
Un commercant qui stocke du riz, des legumes, des medicaments, doit savoir s'il fait trop chaud ou trop froid.
Sans capteur, il le decouvre trop tard.

## Solution
Un capteur IoT simule qui mesure la temperature, comme un vrai capteur ESP32.
100% sur Redmi, sans acheter de materiel pour commencer.

## Comment lancer
python3 main.py

## Fonctions V5.1
- Simule une mesure de temperature a Fianarantsoa
- Dit si c'est froid, normal, ou trop chaud pour le stockage
- Sauvegarde la mesure dans un fichier

## Prochaines versions
- V5.2 : mesures toutes les heures + historique
- V5.3 : alerte si trop chaud / trop froid
- V5.4 : envoi MQTT (comme un vrai objet connecte)
- V5.5 : tableau de bord temperature du jour
