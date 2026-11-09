# Surveillance Aitif - V2.10
# AITIF. - Aitif, pour faire evoluer Madagascar
# Domaine 02 - Admin Systeme + Reseau
# Par Miantsa - solutions-madagascar
import shutil, socket, subprocess, os

def check_stockage():
    total, used, free = shutil.disk_usage("/")
    print("--- STOCKAGE ---")
    print(f"Total : {total//(1024**3)} Go")
    print(f"Utilise : {used//(1024**3)} Go")
    print(f"Libre : {free//(1024**3)} Go")
    pct = used/total*100
    print(f"Utilisation : {pct:.1f}%")
    if pct > 90:
        print("ALERTE : stockage presque plein !")
    elif pct > 80:
        print("Attention : stockage bientot plein")
    else:
        print("OK stockage")

def check_batterie():
    print("\n--- BATTERIE ---")
    # Dans Ubuntu proot, la batterie n'est pas visible directement.
    # On essaie de lire le fichier systeme, sinon on explique.
    try:
        for f in os.listdir("/sys/class/power_supply"):
            if "battery" in f.lower():
                with open(f"/sys/class/power_supply/{f}/capacity") as fh:
                    print(f"Batterie : {fh.read().strip()}%")
                    return
        print("Batterie : non visible dans Ubuntu (normal en proot)")
        print("Astuce : regarde l'icone batterie en haut de ton Redmi")
    except Exception as e:
        print(f"Batterie : non lisible ici ({e})")

def check_reseau():
    print("\n--- RESEAU ---")
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("Internet : OK (connecte)")
    except:
        print("Internet : COUPE ou 4G faible")
    try:
        r = subprocess.run(["ping","-c","1","-W","2","8.8.8.8"], capture_output=True, text=True, timeout=5)
        if r.returncode == 0:
            for line in r.stdout.splitlines():
                if "time=" in line:
                    print(f"Ping : {line.strip().split('time=')[-1]}")
        else:
            print("Ping : echec")
    except Exception as e:
        print(f"Ping : {e}")

if __name__ == "__main__":
    print("=== SURVEILLANCE AITIF. - MADAGASCAR ===")
    check_stockage()
    check_batterie()
    check_reseau()
    print("\n--- ALERTE AITIF. ---")
    try:
        from alerte import alerte
        alerte()
    except Exception as e:
        print(f"Alerte non lisible ici : {e}")
    print("\nTermine. Relance quand tu veux avec : python3 main.py")
