# Scan ports ouverts - V6.4 - Domaine 06
# Scan TON propre Redmi / localhost, jamais celui des autres sans autorisation
import socket

def scan():
    print("=== SCAN PORTS OUVERTS - AUDIT - MADAGASCAR ===")
    print("On scanne uniquement localhost (ton propre Redmi).")
    print("Ne scanne JAMAIS le reseau de quelqu'un d'autre sans son accord.\n")
    ports = {
        22: "SSH",
        80: "HTTP (site web)",
        443: "HTTPS (site securise)",
        3306: "MySQL",
        5432: "PostgreSQL",
        6379: "Redis",
        8000: "Dev / FastAPI",
        8080: "Dev / Proxy",
        1883: "MQTT (IoT)",
        1884: "MQTT securise",
    }
    ouverts = []
    for port, nom in ports.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            res = s.connect_ex(("127.0.0.1", port))
            if res == 0:
                print(f"Port {port} ({nom}) : OUVERT")
                ouverts.append(port)
            else:
                print(f"Port {port} ({nom}) : ferme")
        except Exception as e:
            print(f"Port {port} : erreur {e}")
        s.close()
    print(f"\n[Resume] {len(ouverts)} port(s) ouvert(s) sur {len(ports)} testes.")
    if 22 in ouverts:
        print("SSH ouvert : verifie que ton mot de passe SSH est fort (V6.1).")
    if 3306 in ouverts or 5432 in ouverts:
        print("Base de donnees ouverte : ne l'expose jamais sur Internet sans mot de passe fort.")
    if not ouverts:
        print("Aucun port ouvert : ton Redmi est ferme, c'est bien pour la securite.")
    print("\nAudit termine. Un port ouvert n'est pas un danger en soi,")
    print("c'est un port ouvert SANS mot de passe fort qui est dangereux.")

if __name__ == "__main__":
    scan()
