# Portfolio Aitif - V7.16 - 3eme tour - tout_en_1
# AITIF. - Metier Digital, pour faire evoluer Madagascar
import pathlib
def tout_en_1_commande():
    """V7.16 : Verifie Portfolio en 1 commande + TERMINE."""
    print("=== TOUT EN 1 - PORTFOLIO AITIF V7.16 - MADAGASCAR ===")
    base = pathlib.Path(".")
    fichiers = ["index.html", "cv.html", "catalogue.html", "journal.html", "style.css"]
    ok = 0
    for nom in fichiers:
        f = base / nom
        if f.exists() and f.stat().st_size > 100:
            txt = f.read_text(encoding="utf-8", errors="ignore")
            print(f" OK : {nom} present ({f.stat().st_size} octets)")
            ok += 1
        else:
            print(f" ROUGE : {nom} manquant ou trop petit")
    # Liens internes
    print("\n[LIENS]")
    index = (base / "index.html").read_text(encoding="utf-8", errors="ignore")
    for lien in ["cv.html", "catalogue.html", "journal.html", "style.css"]:
        if lien in index:
            print(f" OK : lien {lien} dans index.html")
        else:
            print(f" ROUGE : lien {lien} manquant dans index.html")
    # Produits reels
    print("\n[PRODUITS REELS]")
    cat = (base / "catalogue.html").read_text(encoding="utf-8", errors="ignore")
    for prod in ["Riz", "Cafe", "Miel", "2 500 Ar", "25 000 Ar", "23 000 Ar"]:
        print(f" {'OK' if prod in cat else 'ROUGE'} : {prod} {'present' if prod in cat else 'manquant'} dans catalogue.html")
    print(f"\n[SCORE PORTFOLIO] {ok} / {len(fichiers)} fichiers OK")
    print("\n=== TERMINE - Portfolio V7.16 fini, Miantsa peut verifier ===")
if __name__ == "__main__":
    tout_en_1_commande()
