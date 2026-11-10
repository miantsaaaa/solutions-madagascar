# Vraie marge Aitif - V8.7
# Marge brute - frais = vraie marge
# Frais a verifier au marche, ici ce sont des exemples pour comprendre.

def marge_reelle(nom, achat, vente, transport, emballage):
    frais = transport + emballage
    benef = vente - achat - frais
    pct = (benef / (achat + frais) * 100) if (achat + frais) else 0
    print(f"{nom} : vente {vente} - achat {achat} - frais {frais} (transport {transport} + emballage {emballage}) = benef {benef} Ar ({pct:.1f}%)")
    if benef <= 0:
        print("  -> PERTE. Ne vends pas a ce prix.")
    elif pct < 10:
        print("  -> Marge trop petite.")
    else:
        print("  -> Marge reelle OK, a verifier au marche.")

print("=== VRAIE MARGE AITIF - 09 Nov 2026 ===")
print("Frais = exemples, a remplacer par les vrais frais du marche.\n")
marge_reelle("Riz 1kg", 1500, 2500, 200, 100)
marge_reelle("Cafe 1kg", 15467, 25000, 1000, 500)
marge_reelle("Miel 1L", 10000, 23000, 1000, 1000)
print("\nRegle Aitif : sans frais, la marge ment. Avec frais, on sait vraiment.")
