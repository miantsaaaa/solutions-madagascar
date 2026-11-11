# Alerte Aitif - V2.19
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
    # V2.19 : combien on peut liberer, sans rien supprimer
    import glob
    caches = glob.glob("/root/*/projets/**/__pycache__", recursive=True)  # V2.19 fix : seulement projets, pas tout /root
    logs = glob.glob("/root/*/projets/**/*.log", recursive=True)  # V2.19 fix : seulement projets
    print(f"\n[NETTOYAGE POSSIBLE] {len(caches)} cache(s) + {len(logs)} log(s) a nettoyer en simulation")
    print("Pour voir sans supprimer : python3 simuler_nettoyage.py")
    print("\n[BATTERIE] Dans Ubuntu proot, on ne peut pas lire la batterie.")
    print("Regle simple pour Madagascar :")
    print(" - Si tu es a moins de 20% : branche ton Redmi, ne lance pas de gros travail")
    print(" - Si coupure JIRAMA : sauvegarde d'abord avec python3 sauvegarde.py")
    print("\nConseil : lance python3 alerte.py chaque matin avant de travailler.")

if __name__ == "__main__":
    alerte()
