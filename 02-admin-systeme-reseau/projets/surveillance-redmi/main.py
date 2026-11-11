# Surveillance Aitif - V2.20 - 4eme tour
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
    print(f"Estimation Aitif : Libre {free//(1024**3)} Go = environ {free//(1024**3)} jours si 1 Go par jour")
    if pct > 90:
        print("ALERTE : stockage presque plein !")
        print("Conseil Aitif : Lance : python3 simuler_nettoyage.py - ne supprime jamais sans simuler")
    elif pct > 80:
        print("Attention : stockage bientot plein")
        print("Conseil Aitif : Lance : python3 simuler_nettoyage.py pour voir ce que tu peux liberer")
    else:
        print("OK stockage")

def check_agents():
    print("\n--- AGENTS AITIF ---")
    from datetime import datetime
    print(f"Derniere verification : {datetime.now().strftime('%d %b %Y %H:%M')}")
    # Agent 01 : Maitre + Sous-Agent - on verifie via PID file et ps
    import pathlib
    pid_f = pathlib.Path("/root/01-genie-logiciel-et-bdd/projets/gestion-commerce-madagascar/AGENT-01.pid")
    if pid_f.exists():
        try:
            pid = int(pid_f.read_text().strip())
            os.kill(pid, 0)
            print(f"Agent 01 Maitre : VIVANT (PID {pid})")
        except Exception:
            print("Agent 01 Maitre : ARRETE - relance avec nohup python3 agent01_loop.py")
    else:
        print("Agent 01 Maitre : PAS DE PID - arrete ou jamais lance")
    # Sous-Agent : on cherche via ps
    try:
        r = subprocess.run(["ps", "aux"], capture_output=True, text=True, timeout=5)
        if "sous_agent_01_1_commerce.py" in r.stdout:
            print("Agent 01 Sous-Agent 01.1 Commerce : VIVANT")
        else:
            print("Agent 01 Sous-Agent 01.1 Commerce : ARRETE")
    except Exception as e:
        print(f"Agent 01 Sous-Agent : non verifiable ({e})")

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
                    try:
                        ms = float(line.strip().split('time=')[-1].replace(' ms',''))
                        if ms > 200:
                            print("Conseil Aitif : 4G faible, travaille hors-ligne, pousse plus tard")
                        else:
                            print("Conseil Aitif : Bon pour pousser sur GitHub")
                    except:
                        pass
        else:
            print("Ping : echec")
    except Exception as e:
        print(f"Ping : {e}")

def tout_en_1_commande():
    print("=== TOUT EN 1 COMMANDE - SURVEILLANCE AITIF V2.20 ===")
    check_stockage()
    check_batterie()
    check_agents()
    check_reseau()
    print("\n--- ALERTE AITIF. ---")
    try:
        from alerte import alerte
        alerte()
    except Exception as e:
        print(f"Alerte non lisible ici : {e}")
    print("\nBILAN AITIF EN 1 PHRASE : Stockage a surveiller, Reseau a verifier avant push, Batterie a verifier sur Redmi - Action : simuler nettoyage si ORANGE")
    print("=== FIN TOUT EN 1 COMMANDE ===")
    print("=== TERMINE - Surveillance finie, Miantsa peut verifier ===")

if __name__ == "__main__":
        tout_en_1_commande()
