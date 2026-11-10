# Generateur mot de passe fort Aitif - V6.13 - 3eme tour
# AITIF. - Cyber Aitif.
# Genere un mot de passe fort, hors-ligne, que tu copies une fois
import secrets, string, re

def generer(longueur=16):
    print("=== GENERATEUR MOT DE PASSE FORT AITIF. - V6.13 - MADAGASCAR ===")
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
    # V6.13 : jamais de repetition / suite, sinon on regenere (comme audit V6.12)
    essais = 1
    while re.search(r"(.)\1\1", mot) or any(s in mot.lower() for s in ["123", "abc", "qwerty", "000", "111"]):
        essais += 1
        mdp = [secrets.choice(string.ascii_uppercase), secrets.choice(string.ascii_lowercase), secrets.choice(string.digits), secrets.choice("!@#$%^&*")]
        for _ in range(longueur - 4):
            mdp.append(secrets.choice(alphabet))
        secrets.SystemRandom().shuffle(mdp)
        mot = "".join(mdp)
        if essais > 20:
            break
    print(f"Verifie : pas de repetition / suite (essais : {essais}) - passe l'audit V6.12.")
    print(f"\nMot de passe genere ({longueur} caracteres) : {mot}")
    print("\nCopie-le maintenant dans ton gestionnaire ou ton carnet secret.")
    print("Ne l'envoie JAMAIS par SMS, WhatsApp ou Facebook.")
    print("Ne le mets JAMAIS dans un fichier .txt sur ton Redmi.")
    print("\nConseil : 1 mot de passe different par compte (Facebook != Gmail != Mobile Money).")
    print("Si 1 compte est pirate, les autres restent en securite.")

if __name__ == "__main__":
    generer(16)
