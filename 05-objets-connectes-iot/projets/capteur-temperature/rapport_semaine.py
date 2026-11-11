# V5.19 : Rapport Semaine Capteur - Capteur Temperature
# AITIF. - IoT Aitif, pour faire evoluer Madagascar
import csv, os
def rapport_semaine():
    print("=== RAPPORT SEMAINE CAPTEUR - V5.19 ===")
    if not os.path.exists("mesures-temperature.csv"):
        print("Aucune mesure. Lance d'abord : python3 main.py")
        return
    with open("mesures-temperature.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    temps = [float(r["Temperature (C)"]) for r in rows]
    hums = [float(r["Humidite (%)"]) for r in rows]
    print(f"\n[Semaine] {len(rows)} mesure(s)")
    print(f" - Temperature : min {min(temps)} C, max {max(temps)} C, moyenne {sum(temps)/len(temps):.1f} C")
    print(f" - Humidite : moyenne {sum(hums)/len(hums):.1f} %, max {max(hums)} %")
    chaud = sum(1 for t in temps if t > 25)
    froid = sum(1 for t in temps if t < 15)
    humide = sum(1 for h in hums if h > 80)
    print(f" - Mesures CHAUD >25 C : {chaud}")
    print(f" - Mesures FROID <15 C : {froid}")
    print(f" - Mesures HUMIDE >80 % : {humide}")
    if chaud == 0 and froid == 0 and humide == 0:
        print("\nSemaine stable. Ton stock est reste en securite.")
    else:
        print("\nSemaine avec alertes. Verifie ton stockage, surtout Cafe et Miel.")
    print("\n=== TERMINE - Rapport Semaine Capteur V5.19 fini ===")
if __name__ == "__main__":
    rapport_semaine()
