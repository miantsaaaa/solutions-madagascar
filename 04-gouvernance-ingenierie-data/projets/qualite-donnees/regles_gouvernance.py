# Regles de gouvernance Aitif - V4.6
# AITIF. - Data Aitif, regles qui protegent.
# Qui peut modifier quoi : les regles qui protegent tes donnees
import os

REGLES = [
    ("1. Sauvegarde avant modification", "Avant de modifier la base, lance : python3 sauvegarde.py (Domaine 02)"),
    ("2. Ne jamais supprimer une vente", "Une vente est une preuve. Si erreur, on corrige avec une nouvelle ligne, on ne supprime pas."),
    ("3. Prix > 0 toujours", "Aucun produit avec prix 0 ou negatif. Verifie avec V4.1."),
    ("4. Stock jamais negatif", "Si stock = 0, on dit 'rupture', on ne met pas -1."),
    ("5. Export = lecture seule", "Les CSV exportes ne modifient jamais la base. La base reste la verite."),
    ("6. 1 seul fichier verite", "commerce.db est la verite. Les CSV sont des copies, pas l'original."),
    ("7. Verifie avant de decider", "Avant chaque decision, lance : python3 main.py (V4.1) pour le score qualite."),
    ("8. Vraie marge, avec frais", "Sans frais, la marge ment. Avec frais, on sait vraiment. Riz 700 Ar, Cafe 8033 Ar, Miel 11000 Ar."),
]

def afficher():
    print("=== REGLES DE GOUVERNANCE AITIF. - V4.6 - MADAGASCAR ===")
    print("Ces regles protegent ton entreprise, meme quand tu es fatigue ou presse.\n")
    for titre, texte in REGLES:
        print(f"{titre}")
        print(f"   {texte}\n")
    print("Si tu respectes ces 8 regles, tes donnees restent propres.")
    print("Et si quelqu'un te trouve plus tard, il verra que tu travailles comme un pro.")

if __name__ == "__main__":
    afficher()
