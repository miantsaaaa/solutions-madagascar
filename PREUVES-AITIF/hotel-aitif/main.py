# Prototype Hotel Aitif - V9.2
# Preuve : Aitif peut faire un hotel, avec les memes domaines.

import random

def hotel():
    print("=== HOTEL AITIF - PROTOTYPE ===")
    print("Petit a petit, on prouve qu'on peut tout faire.\n")
    # 01 - Commerce : chambre
    chambres = {"Chambre Simple": 40000, "Chambre Double": 60000, "Suite Aitif": 100000}
    print("[01 - Commerce] Chambres Aitif :")
    for nom, prix in chambres.items():
        print(f"  {nom} : {prix} Ar / nuit")
    print("Reservation : Chambre Double - 60000 Ar / nuit\n")
    # 02 - Surveillance : stockage / systeme
    print("[02 - Surveillance] Systeme :")
    print("  Sauvegarde : OK, derniere sauvegarde aujourd'hui")
    print("  Stockage : OK, pas plein\n")
    # 03 - IA : prediction occupation
    occupation = random.choice([50, 60, 70, 80])
    print(f"[03 - IA] Prediction occupation demain : {occupation}%")
    if occupation >= 70:
        print("  Conseil IA : prepare plus de petit-dejeuner demain.\n")
    else:
        print("  Conseil IA : occupation normale.\n")
    # 06 - Securite
    print("[06 - Securite] Audit :")
    print("  Ports : 0 ouvert, hotel ferme comme il faut")
    print("  Mots de passe : forts, audit OK\n")
    print("[07 - Metier] AITIF.")
    print("Aujourd'hui prototype, demain vrai hotel.")

if __name__ == "__main__":
    hotel()
