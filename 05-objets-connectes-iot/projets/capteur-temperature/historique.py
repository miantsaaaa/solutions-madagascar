# Historique temperature Aitif - V5.6
# AITIF. - IoT Aitif.
# Lit toutes les mesures et montre l'evolution de la journee
import csv, os, glob

def historique():
    print("=== HISTORIQUE TEMPERATURE AITIF. - V5.6 - FIANARANTSOA ===")
    fichiers = glob.glob("mesures-temperature.csv")
    if not fichiers or not os.path.exists(fichiers[0]):
        print("Aucune mesure. Lance d'abord : python3 main.py")
        return
    with open(fichiers[0], encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    print(f"\nNombre de mesures : {len(rows)}")
    temps = [float(r["Temperature (C)"]) for r in rows]
    hums = [float(r["Humidite (%)"]) for r in rows]
    print("\n[Mesures]")
    for r in rows:
        print(f" - {r['Date']} {r['Heure']} : {r['Temperature (C)']} C, {r['Humidite (%)']} %")
    print(f"\n[Resume]")
    print(f"Temperature min : {min(temps)} C")
    print(f"Temperature max : {max(temps)} C")
    print(f"Temperature moyenne : {sum(temps)/len(temps):.1f} C")
    print(f"Humidite moyenne : {sum(hums)/len(hums):.1f} %")
    if max(temps) > 25:
        print("Alerte : il a fait trop chaud a un moment. Aeration necessaire.")
    elif min(temps) < 15:
        print("Alerte : il a fait froid. Couvre ton stock la nuit.")
    else:
        print("Journee stable, bon pour le stockage.")
    print("\nAstuce : lance main.py 3 fois par jour (matin, midi, soir) pour un vrai historique.")

if __name__ == "__main__":
    historique()
