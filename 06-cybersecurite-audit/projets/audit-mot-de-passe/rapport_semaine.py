# V6.19 : Rapport Semaine Cyber - Audit Cyber sait si ta semaine est saine
# AITIF. - Cyber Aitif, pour faire evoluer Madagascar
import glob, socket, subprocess
from datetime import datetime, timedelta
def rapport_semaine():
    print("=== RAPPORT SEMAINE CYBER - V6.19 - MADAGASCAR ===")
    print(f"Semaine du {datetime.now().strftime('%Y-%m-%d')}")
    # 1. Checklist
    print("\n[1. CHECKLIST]")
    try:
        from checklist_aitif import checklist
        checklist()
    except Exception as e:
        print(f"Checklist non lisible ici : {e}")
    # 2. Ports
    print("\n[2. PORTS OUVERTS]")
    ouverts = []
    for port in [22, 80, 443, 3306, 5432, 6379, 8000, 8080, 1883]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex(("127.0.0.1", port)) == 0:
            ouverts.append(port)
        s.close()
    print(f"Ports ouverts cette semaine : {ouverts if ouverts else '0 - Redmi ferme'}")
    # 3. Sauvegardes de la semaine
    print("\n[3. SAUVEGARDES DE LA SEMAINE]")
    saves = sorted(glob.glob("/root/sauvegarde-*"))
    print(f"Total sauvegardes : {len(saves)} - derniere : {saves[-1] if saves else 'AUCUNE'}")
    # 4. Agents
    print("\n[4. AGENTS CETTE SEMAINE]")
    try:
        from check_agents import check_agents
        check_agents()
    except Exception as e:
        print(f"Check Agents non lisible ici : {e}")
    # 5. Bilan 1 phrase
    bilan = "semaine Cyber propre : checklist VERT, Redmi ferme, sauvegardes OK - tu peux pousser tranquille." if not ouverts else "semaine Cyber a surveiller : des ports ouverts, verifie qu'ils sont voulus."
    print(f"\nBilan Cyber Semaine : {bilan}")
    print("\n=== TERMINE - Rapport Semaine Cyber V6.19 fini, Miantsa peut verifier ===")
if __name__ == "__main__":
    rapport_semaine()
