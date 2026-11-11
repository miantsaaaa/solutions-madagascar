# V3.17 : Check Agents - Prediction Ventes sait si les Agents travaillent
# AITIF. - IA Aitif, pour faire evoluer Madagascar
import subprocess, pathlib

def check_agents():
    print("=== CHECK AGENTS - PREDICTION VENTES V3.17 ===")
    agents = [
        ("Agent 01 Commerce", "agent01_loop.py"),
        ("Agent 02 Surveillance", "agent02_loop.py"),
        ("Agent 03 Prediction", "agent03_loop.py"),
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
    print("=== TERMINE - Check Agents V3.17 fini ===")

if __name__ == "__main__":
    check_agents()
