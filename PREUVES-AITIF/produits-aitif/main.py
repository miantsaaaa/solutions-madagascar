# Prototype Produits Aitif - V9.3
# Preuve : Aitif peut faire ses propres produits locaux.

def produit(nom, origine, achat, vente, transport, emballage):
    frais = transport + emballage
    benef = vente - achat - frais
    print(f"=== ETIQUETTE AITIF. ===")
    print(f"Produit : {nom}")
    print(f"Origine : {origine}")
    print(f"Prix vente : {vente} Ar")
    print(f"Achat {achat} + frais {frais} = cout {achat + frais} Ar")
    print(f"Benefice : {benef} Ar")
    print(f"Petit a petit, toujours bien organise.\n")

print("=== PRODUITS AITIF - PROTOTYPE ===\n")
# Prix observes 09 nov 2026
produit("Riz Aitif", "Fianarantsoa", 1500, 2500, 200, 100)
produit("Cafe Aitif", "Fianarantsoa / Toamasina", 15467, 25000, 1000, 500)
produit("Miel Aitif", "Vatovavy / Fianarantsoa", 10000, 23000, 1000, 1000)
print("Un jour, ces etiquettes seront sur de vrais produits.")
print("Aujourd'hui prototype, demain vrai produit Aitif.")
