# Portfolio Aitif - V7.20 - 3eme tour - tout_en_1
# AITIF. - Metier Digital, pour faire evoluer Madagascar
import pathlib
def tout_en_1_commande():
    """V7.20 : Verifie Portfolio en 1 commande + TERMINE."""
    print("=== TOUT EN 1 - PORTFOLIO AITIF V7.20 - MADAGASCAR ===")
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
    print("\n=== TERMINE - Portfolio V7.20 fini, Miantsa peut verifier ===")
if __name__ == "__main__":
    pass  # V7.20 : voir tout_en_1_complet ci-dessous


def tout_en_1_complet():
    """V7.20 : Check Agents + Verif Portfolio + Rapport Semaine + TERMINE."""
    print("=== TOUT EN 1 COMPLET - PORTFOLIO V7.20 ===")
    print("\n--- CHECK AGENTS AITIF. ---")
    try:
        from check_agents import check_agents
        check_agents()
    except Exception as e:
        print(f"Check Agents non lisible ici : {e}")
    print("\n--- VERIF PORTFOLIO AITIF. ---")
    try:
        tout_en_1_commande()
    except Exception as e:
        print(f"Verif Portfolio non lisible ici : {e}")
    print("\n--- RAPPORT SEMAINE AITIF. ---")
    try:
        from rapport_semaine import rapport_semaine
        rapport_semaine()
    except Exception as e:
        print(f"Rapport Semaine non lisible ici : {e}")
    print("\n=== TERMINE - Tout en 1 Portfolio V7.20 fini, Miantsa peut verifier ===")

if __name__ == "__main__":
    tout_en_1_complet()
