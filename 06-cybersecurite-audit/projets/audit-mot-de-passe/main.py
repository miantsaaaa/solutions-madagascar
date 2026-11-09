# Audit Mot de Passe Aitif - V6.6
# AITIF. - Cyber Aitif.
# Teste la force, 100% hors-ligne, ne sauvegarde JAMAIS le mot de passe
import getpass, re

FAIBLES = ["123456", "12345678", "password", "motdepasse", "madagascar", "fianarantsoa", "1234", "azerty", "000000", "admin"]

def audit():
    print("=== AUDIT MOT DE PASSE AITIF. - V6.6 - MADAGASCAR ===")
    print("Ton mot de passe ne sera JAMAIS sauvegarde, ni envoye.")
    print("Il reste dans ta tete et dans ce test, c'est tout.")
    mdp = getpass.getpass("Tape un mot de passe a tester (il sera cache) : ")
    if not mdp:
        print("Aucun mot de passe tape.")
        return
    score = 0
    conseils = []
    # Longueur
    if len(mdp) >= 12:
        score += 30
        print("Longueur >= 12 : +30 (tres bien)")
    elif len(mdp) >= 8:
        score += 15
        print("Longueur 8-11 : +15 (correct, vise 12)")
        conseils.append("Allonge a 12 caracteres ou plus.")
    else:
        print("Longueur < 8 : +0 (trop court, dangereux)")
        conseils.append("Mets au moins 12 caracteres.")
    # Majuscule
    if re.search(r"[A-Z]", mdp):
        score += 15
        print("Majuscule : +15")
    else:
        conseils.append("Ajoute une majuscule (A-Z).")
    # Minuscule
    if re.search(r"[a-z]", mdp):
        score += 10
        print("Minuscule : +10")
    else:
        conseils.append("Ajoute une minuscule (a-z).")
    # Chiffre
    if re.search(r"[0-9]", mdp):
        score += 15
        print("Chiffre : +15")
    else:
        conseils.append("Ajoute un chiffre (0-9).")
    # Special
    if re.search(r"[^A-Za-z0-9]", mdp):
        score += 15
        print("Caractere special : +15")
    else:
        conseils.append("Ajoute un caractere special (! @ # ...).")
    # Mots faibles
    bas = mdp.lower()
    if bas in FAIBLES or any(m in bas for m in FAIBLES):
        print("\nDANGER : mot de passe connu / trop simple ! Score divise.")
        score = min(score, 20)
        conseils.append("Ne mets jamais 123456, madagascar, ta ville ou ta date de naissance.")
    print(f"\n[SCORE] {score} / 85+")
    if score >= 80:
        print("FORT : bon mot de passe. Garde-le secret, ne le partage jamais.")
    elif score >= 50:
        print("MOYEN : ameliorable. Suis les conseils ci-dessous.")
    else:
        print("FAIBLE : change-le tout de suite, surtout pour Mobile Money, Gmail, Facebook.")
    if conseils:
        print("\n[Conseils]")
        for c in conseils:
            print(f" - {c}")
    print("\nRappel : ne tape jamais ton VRAI mot de passe Mobile Money ici pour tester.")
    print("Teste avec un mot de passe similaire, pas le vrai.")

if __name__ == "__main__":
    audit()
