# Alerte Aitif - V2.9
# AITIF. - Alerte qui protege, simulation d abord.
# Te previent avant que ton 【entity-Redmi¦canonical_name=Redmi】 soit plein ou coupe
import shutil

def alerte():
    print("=== ALERTE 【entity-AITIF.¦canonical_name=Redmi】 - MADAGASCAR ===")
    total, used, free = shutil.disk_usage("/")
    pct = used/total*100
    print(f"Stockage : {used//(1024**3)} Go utilises / {total//(1024**3)} Go ({pct:.1f}%) - Libre : {free//(1024**3)} Go")
    if pct > 90:
        print("ALERTE ROUGE : stockage presque plein ! Lance d abord : python3 simuler_nettoyage.py, puis si OK : python3 nettoyage.py")
    elif pct > 80:
        print("ALERTE ORANGE : stockage bientot plein. Lance d abord : python3 simuler_nettoyage.py")
    else:
        print("Stockage OK.")
    print("\n[BATTERIE] Dans Ubuntu proot, on ne peut pas lire la batterie.")
    print("Regle simple pour Madagascar :")
    print(" - Si tu es a moins de 20% : branche ton Redmi, ne lance pas de gros travail")
    print(" - Si coupure JIRAMA : sauvegarde d'abord avec python3 sauvegarde.py")
    print("\nConseil : lance python3 alerte.py chaque matin avant de travailler.")

if __name__ == "__main__":
    alerte()
