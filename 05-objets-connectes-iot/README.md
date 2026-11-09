# 05 - IoT - VERSION MOBILE / REDMI

## Mission ici
Utiliser TON 【entity-Redmi¦canonical_name=Redmi】 comme un objet connecte. Ton telephone EST un capteur.

## TYPES d'outils MOBILE a creer ici
- Utiliser les capteurs du 【entity-Redmi¦canonical_name=Redmi】 : batterie, reseau, stockage comme donnees
- Simulation de capteur : simuler temperature, humidite quand tu n'as pas le materiel
- Collecte MQTT : recevoir des donnees sur le telephone, les enregistrer
- Visualisation : voir en temps reel sur le telephone ce que tu mesures
- Alerte mobile : si batterie < 20% ou stockage > 90%, alerte

## D'abord quotidien sur Redmi
Ex : station meteo simulee, suivi batterie / reseau, alerte stockage plein.

## Ensuite pro sur Redmi
Ex : systeme IoT complet : Capteur (ou simule) -> MQTT -> BDD sur telephone -> Dashboard -> Alerte.
Ton Redmi devient la passerelle IoT.

## Regle Mobile
Commencer en simule, sans acheter de materiel.
MQTT toujours securise, jamais en ouvert.
Penser batterie : un outil IoT ne doit pas tuer la batterie.
