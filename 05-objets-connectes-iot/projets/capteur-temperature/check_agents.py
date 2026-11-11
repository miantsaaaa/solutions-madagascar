# V5.17 : Check Agents - Capteur sait si les Agents travaillent
# AITIF. - IoT Aitif, pour faire evoluer Madagascar
import subprocess
def check_agents():
    print("=== CHECK AGENTS - CAPTEUR V5.17 ===")
    agents = [
        ("Agent 01 Commerce", "agent01_loop.py"),
        ("Agent 02 Surveillance", "agent02_loop.py"),
        ("Agent 03 Prediction", "agent03_loop.py"),
        ("Agent 04 Qualite", "agent04_loop.py"),
        ("Agent 05 Capteur", "agent05_loop.py"),
    ]
    for nom, proc in agents:
        try:
            r = subprocess.run(["pgrep", "-f", proc], capture_output=True, text=True, timeout=5)
            if r.stdout.strip():
                print(f" - {nom} : VIVANT PID {r.stdout.strip().split()[0]}")
            else:
                print(f" - {nom} : ARRETE - a relancer")
        except Exception as e:
            print(f" - {nom} : CHECK ECHEC - {e}")
    print("=== TERMINE - Check Agents V5.17 fini ===")
if __name__ == "__main__":
    check_agents()
