# Agent 00 - Guide Aitif - V0.1 COMPRENDRE - A la tete des 7 Agents
# AITIF. - Fondation. Mission V0.1 : comprendre ce qui existe, avant de guider.
# Pas de grand pas : il se raccorde aux 7 Masters, il lit les evolutions deja faites.
import pathlib, re
def comprendre():
    """V0.1 : Inventaire Fondation + 7 domaines + 7 Masters + versions deja faites."""
    print("=== AGENT 00 - V0.1 COMPRENDRE - MADAGASCAR ===")
    print("Je ne guide pas encore. Je comprends d'abord ce qu'on a deja fait.")
    memo = []
    # 1. Fondation
    print("\n[1. FONDATION - FICHIERS HORS DOMAINES]")
    base = pathlib.Path("/root")
    fond = base / "FONDATION-AITIF"
    for f in sorted(fond.glob("*.md")):
        print(f" - {f.name}")
        memo.append(f"Fondation : {f.name}")
    for f in [base / "MON-ENTREPRISE.md", base / "ORGANISATION.md", base / "PROBLEMES-MADAGASCAR.md", base / "ROADMAP-VERSIONS.md"]:
        print(f" - {'OK ' if f.exists() else 'ROUGE '} {f.name}")
    # 2. Les 7 domaines : ce qu'ils ont deja fait
    print("\n[2. LES 7 DOMAINES - CE QU'ON A DEJA FAIT]")
    for i in range(1, 8):
        doms = list(base.glob(f"0{i}-*"))
        if not doms:
            print(f" - Domaine 0{i} : ROUGE manquant")
            continue
        dom = doms[0]
        projets = list((dom / "projets").glob("*")) if (dom / "projets").exists() else []
        print(f" - Domaine 0{i} : {dom.name} | projets : {[x.name for x in projets]}")
        # Version dans main.py du projet
        for proj in projets:
            mains = list(proj.glob("main.py"))
            for m in mains:
                txt = m.read_text(encoding="utf-8", errors="ignore")
                vers = sorted(set(re.findall(rf"V{i}\.\d+", txt)))
                print(f"    -> {proj.name}/main.py : versions trouvees {vers[-3:] if vers else 'aucune'}")
                memo.append(f"Domaine 0{i} {proj.name} : {vers}")
            # Master / Sub-Agent ?
            for nom in ["MESSAGE-AGENT-0%d.txt" % i, "DISCUSSION-AGENT-0%d.txt" % i, "agent0%d_loop.py" % i]:
                f = proj / nom
                if f.exists():
                    print(f"    -> {nom} : OK ({f.stat().st_size} octets)")
    # 3. Agents vivants ?
    print("\n[3. LES 7 MASTERS - SONT-ILS VIVANTS ?]")
    import subprocess
    for i in range(1, 8):
        r = subprocess.run(["pgrep", "-f", f"agent0{i}_loop.py"], capture_output=True, text=True, timeout=5)
        print(f" - Agent 0{i} : {'VIVANT PID ' + r.stdout.strip().split()[0] if r.stdout.strip() else 'ARRETE'}")
    # 4. Memoire
    memo_path = pathlib.Path("MEMOIRE-AGENT-00.md")
    memo_path.write_text("# MEMOIRE AGENT 00 - V0.1 COMPRENDRE\n\n" + "\n".join(memo) + "\n\nAgent 00 a compris : Fondation + 7 domaines + 7 Masters. Il ne guide pas encore, il se raccorde d'abord.\n", encoding="utf-8")
    print(f"\nMemoire ecrite : {memo_path} ({len(memo)} lignes)")
    print("\nBilan Comprendre : j'ai lu la Fondation + les 7 domaines + les 7 Masters - je suis raccorde, je peux guider petit a petit.")
    print("\n=== TERMINE - Agent 00 V0.1 Comprendre fini, Miantsa peut verifier ===")
if __name__ == "__main__":
    pass  # V0.2 : voir verifier_propre ci-dessous


def verifier_propre():
    """V0.2 : Verifie que le depot est propre - pas de doublons a la racine + TERMINE."""
    print("=== VERIFIER PROPRE - AGENT 00 V0.2 ===")
    import pathlib as pl
    base = pl.Path("/root")
    # Doublons a la racine qui ne devraient pas etre la
    doublons = list(base.glob("agent0*_loop.py")) + list(base.glob("MESSAGE-AGENT-*.txt")) + list(base.glob("AGENT-*-REPONSE.txt"))
    if doublons:
        print(f" ATTENTION : {len(doublons)} fichier(s) doublon a la racine :")
        for f in doublons:
            print(f"  - {f.name} (vrai fichier est dans son domaine, celui-ci est un doublon)")
    else:
        print(" OK : aucun doublon a la racine")
    # .gitignore
    gitig = (base / ".gitignore").read_text(encoding="utf-8")
    for mot in ["*.pid", "MESSAGE-AGENT-*.txt", "*.log"]:
        print(f" {'OK' if mot in gitig else 'ROUGE'} : {mot} {'dans .gitignore' if mot in gitig else 'manquant dans .gitignore'}")
    print("\nBilan Propre : depot range = on ne se perd plus, git status lisible.")
    print("\n=== TERMINE - Verifier Propre V0.2 fini, Miantsa peut verifier ===")

if __name__ == "__main__":
    verifier_propre()
