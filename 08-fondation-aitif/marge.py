# Calculateur marge Aitif - V8.6
# Utilise les prix observes du 09 nov 2026
# Petit a petit : d'abord comprendre, apres vendre.

def marge(nom, achat, vente):
    benef = vente - achat
    pct = (benef / achat * 100) if achat else 0
    print(f"{nom} : achat {achat} Ar -> vente {vente} Ar = benef {benef} Ar ({pct:.1f}%)")
    if pct < 10:
        print("  -> Marge trop petite, ne vends pas a ce prix.")
    elif pct < 30:
        print("  -> Marge correcte, a verifier au marche.")
    else:
        print("  -> Bonne marge, a etudier.")

print("=== MARGE AITIF - 09 Nov 2026 ===")
print("Prix observes, a verifier au marche.\n")
# Riz : paddy 1500 -> riz marche 2500
marge("Riz 1kg", 1500, 2500)
# Cafe : marche 15467 -> producteur 25000 (exemple si tu revends)
marge("Cafe 1kg", 15467, 25000)
# Miel : gros producteur 10000 -> detail 23000
marge("Miel 1L", 10000, 23000)
print("\nRegle Aitif : Internet donne la tendance, le marche donne le vrai prix.")
print("On ne vend rien tant qu'on n'a pas verifie au marche.")
