# Generateur mot de passe fort - V6.2 - Domaine 06
# Genere un mot de passe fort, hors-ligne, que tu copies une fois
import secrets, string

def generer(longueur=16):
    print("=== GENERATEUR MOT DE PASSE FORT - MADAGASCAR ===")
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    # On s'assure qu'il y a au moins 1 de chaque type
    mdp = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*"),
    ]
    for _ in range(longueur - 4):
        mdp.append(secrets.choice(alphabet))
    secrets.SystemRandom().shuffle(mdp)
    mot = "".join(mdp)
    print(f"\nMot de passe genere ({longueur} caracteres) : {mot}")
    print("\nCopie-le maintenant dans ton gestionnaire ou ton carnet secret.")
    print("Ne l'envoie JAMAIS par SMS, WhatsApp ou Facebook.")
    print("Ne le mets JAMAIS dans un fichier .txt sur ton Redmi.")
    print("\nConseil : 1 mot de passe different par compte (Facebook != Gmail != Mobile Money).")
    print("Si 1 compte est pirate, les autres restent en securite.")

if __name__ == "__main__":
    generer(16)
