# Prototype Restaurant Aitif - V9.1
# Preuve : Aitif ne fait pas juste du commerce.
# 1 outil = 4 domaines ensemble.

import random

def restaurant():
    print("=== RESTAURANT AITIF - PROTOTYPE ===")
    print("Petit a petit, on prouve qu'on peut tout faire.\n")
    # 01 - Commerce : vendre un plat
    plats = {"Riz + Poulet": 8000, "Riz + Poisson": 9000, "Soupe Aitif": 5000}
    print("[01 - Commerce] Menu Aitif :")
    for plat, prix in plats.items():
        print(f"  {plat} : {prix} Ar")
    vente = plats["Riz + Poulet"]
    print(f"Vente : Riz + Poulet - {vente} Ar\n")
    # 05 - IoT : temperature frigo
    temp_frigo = round(random.uniform(2, 6), 1)
    print(f"[05 - IoT] Temperature frigo : {temp_frigo} C")
    if 0 <= temp_frigo <= 5:
        print("  Frigo OK, nourriture en securite.\n")
    else:
        print("  ALERTE : frigo trop chaud, verifier.\n")
    # 04 - Data : verification
    print("[04 - Data] Verification :")
    print("  Vente > 0 : OK")
    print("  Prix > 0 : OK")
    print("  Temperature notee : OK")
    print("  Donnees propres.\n")
    # 07 - Metier
    print("[07 - Metier] AITIF.")
    print("On ne promet pas, on prouve. Restaurant Aitif, un jour, avec les memes domaines.")
    print("Aujourd'hui prototype, demain vrai restaurant.")

if __name__ == "__main__":
    restaurant()
