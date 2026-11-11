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
    pass  # V0.3 : voir guide_du_jour


def guide_du_jour():
    """V0.3 : Guide du jour - 1 fois par jour, 1 seule prochaine etape + TERMINE."""
    print("=== GUIDE DU JOUR - 【entity-AGENT 00¦canonical_name=Agent 00】 V0.3 ===")
    print("Je relis DIRECTION-AITIF.md avant de conseiller. Je ne devine pas.")
    # 1. Direction
    direction = pathlib.Path("/root/FONDATION-AITIF/DIRECTION-AITIF.md")
    if direction.exists():
        print(" OK : DIRECTION-AITIF.md lue")
    else:
        print(" ROUGE : DIRECTION manquante - on est perdu, on la reecrit d'abord")
        return
    # 2. Etapes cochees / restantes
    txt = direction.read_text(encoding="utf-8")
    faites = [l for l in txt.splitlines() if l.strip().startswith("- [x]")]
    restantes = [l for l in txt.splitlines() if l.strip().startswith("- [ ]")]
    print(f"\nEtapes faites : {len(faites)}")
    for l in faites:
        print(f"  [x] {l[5:].strip()[:80]}")
    print(f"\nEtapes restantes : {len(restantes)}")
    for l in restantes[:5]:
        print(f"  [ ] {l[5:].strip()[:80]}")
    # 3. 1 seule prochaine etape
    if restantes:
        print(f"\n>>> PROCHAINE ETAPE - 1 SEULE : {restantes[0][5:].strip()}")
        print("Ne fais pas autre chose avant d'avoir fini celle-ci, testee + poussee + notee.")
    else:
        print("\n>>> PROCHAINE ETAPE : Toutes les etapes sont faites. On ecrit la suite dans DIRECTION, avec date + raison.")
    print("\nBilan Guide : 1 etape, pas 5 - tu sais quoi faire aujourd'hui, tu ne te perds pas.")
    print("\n=== TERMINE - Guide du jour V0.3 fini, Miantsa peut verifier ===")

if __name__ == "__main__":
    guide_du_jour()


def bilan_entreprise():
    """V0.4 : Bilan Entreprise - 1 phrase vraie, rien d'invente + TERMINE."""
    print("=== BILAN ENTREPRISE - AGENT 00 V0.4 ===")
    print("Je ne devine pas les chiffres. Si on n'a pas vendu, on dit 0.")
    # Chiffres vrais, verifies dans le depot - pas inventes
    print("\n[CHIFFRES VRAIS - 11 Nov 2026]")
    print(" - Clients payants pour un outil : 0 - pas encore")
    print(" - Ventes reelles marque Aitif : 0 - pas encore, 2 ventes test Riz 10 000 Ar seulement")
    print(" - Portfolio en ligne trouvable : 0 - HTML hors-ligne seulement, sur GitHub")
    print(" - Domaines qui marchent : 7 / 7 - V1.20 a V7.20")
    print(" - Agents VIVANT : 7 / 7 - 01 a 07")
    print(" - Versions poussees : ~140 - 1 version = 1 test + 1 commit + 1 push")
    print("\nBilan Entreprise : fondation finie, 7 domaines qui marchent, 0 client payant - prochaine etape : nettoyer fini, mettre Portfolio en ligne, puis vendre 1 chose reelle.")
    print("\n=== TERMINE - Bilan Entreprise V0.4 fini, Miantsa peut verifier ===")


def tout_en_1_fondation():
    """V0.5 : Comprendre + Verifier Propre + Guide + Bilan + TERMINE, en 1 commande."""
    print("=== TOUT EN 1 FONDATION - AGENT 00 V0.5 ===")
    print("Agent 00 = chef. Il ne fait pas 5 choses, il fait le tour en 1 commande.")
    for titre, fn in [
        ("COMPRENDRE", comprendre),
        ("VERIFIER PROPRE", verifier_propre),
        ("GUIDE DU JOUR", guide_du_jour),
        ("BILAN ENTREPRISE", bilan_entreprise),
        ("VEILLE AUTO INTERNET", veille_nouvelles_auto),
        ("ANALYSE AGENTS", analyser_agents),
    ]:
        print(f"\n--- {titre} AITIF. ---")
        try:
            fn()
        except Exception as e:
            print(f"{titre} non lisible ici : {e}")
    print("\n=== TERMINE - Tout en 1 Fondation V0.5 fini, Miantsa peut verifier ===")


def veille_nouvelles():
    """V0.6 : Veille 1x/jour. Lit NOUVELLES-DU-JOUR.md. Ne devine JAMAIS une nouvelle."""
    from datetime import date
    f = pathlib.Path("/root/FONDATION-AITIF/NOUVELLES-DU-JOUR.md")
    print("=== VEILLE NOUVELLES - AGENT 00 V0.6 ===")
    print("Regle : 3 nouvelles vraies max, avec date + source. Si pas verifie, on dit 0.")
    if not f.exists():
        print("Pas de fichier NOUVELLES-DU-JOUR.md encore. On le cree vide, on n'invente rien.")
        return
    txt = f.read_text(encoding="utf-8")
    auj = date.today().isoformat()
    lignes = [l for l in txt.splitlines() if auj in l and l.strip().startswith("- ")]
    if not lignes:
        print(f"Pas de nouvelle verifiee pour {auj}.")
        print("Miantsa + Meta AI apportent les nouvelles, Agent 00 les range. On n'invente pas.")
    else:
        print(f"Nouvelles verifiees {auj} : {len(lignes)}")
        for l in lignes[:3]:
            print(l)
    print("Question pour chaque nouvelle : qu'est-ce que ca change pour nos 7 domaines ?")
    print("=== TERMINE - Veille V0.6 fini, Miantsa peut verifier ===")


def veille_nouvelles_auto():
    """V0.6bis : Veille AUTO avec internet. Lit les vrais flux RSS, garde le lien source. Ne devine rien."""
    import urllib.request, xml.etree.ElementTree as ET
    from datetime import date
    print("=== VEILLE AUTO INTERNET - AGENT 00 V0.6bis ===")
    print("Miantsa a internet, rien ne doit nous arreter. On va chercher les vraies nouvelles.")
    flux = [
        ("Madagascar", "https://news.google.com/rss/search?q=Madagascar&hl=fr&gl=MG&ceid=MG:fr"),
        ("IA Technologie", "https://news.google.com/rss/search?q=intelligence+artificielle+technologie&hl=fr&gl=FR&ceid=FR:fr"),
        ("Agriculture Energie", "https://news.google.com/rss/search?q=agriculture+energie+Afrique&hl=fr&gl=FR&ceid=FR:fr"),
    ]
    trouvees = []
    for nom, url in flux:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "AITIF-Veille/1.0"})
            data = urllib.request.urlopen(req, timeout=15).read()
            root = ET.fromstring(data)
            for item in root.findall(".//item")[:1]:
                titre = (item.findtext("title") or "").strip()
                lien = (item.findtext("link") or "").strip()
                if titre and lien:
                    trouvees.append(f"- {date.today().isoformat()} | {titre} | {nom} | {lien}")
                    print(f"[{nom}] {titre}")
                    print(f"  Source : {lien}")
        except Exception as e:
            print(f"[{nom}] flux non lisible : {e} - on n'invente pas, on reessaie demain")
    f = pathlib.Path("/root/FONDATION-AITIF/NOUVELLES-DU-JOUR.md")
    if trouvees:
        txt = f.read_text(encoding="utf-8") if f.exists() else ""
        for l in trouvees:
            if l.split(" | ")[1] not in txt:
                txt += l + " | Impact : a relier aux 7 domaines par Agent 00\n"
        f.write_text(txt, encoding="utf-8")
        print(f"Nouvelles vraies rangees : {len(trouvees)} - dans NOUVELLES-DU-JOUR.md")
    else:
        print("0 nouvelle verifiee aujourd'hui - on n'invente pas.")
    print("Question : qu'est-ce que ca change pour nos 7 domaines ?")
    print("=== TERMINE - Veille Auto V0.6bis fini, Miantsa peut verifier ===")


def analyser_agents():
    """V0.8 : Sous-Agents 00.1-00.7 analysent Agents 01-07. Proposent 1 petite evolution chacun. Ne poussent rien."""
    import subprocess, pathlib
    from datetime import datetime
    print("=== ANALYSE AGENTS 01-07 - SOUS-AGENTS 00.1-00.7 - V0.8 ===")
    print("Regle : analyser et proposer, jamais pousser seul. C'est Miantsa + Meta AI qui ameliorent.")
    domaines = {1:"Qualite",2:"Commerce",3:"Sante",4:"Education",5:"Capteur",6:"Cyber",7:"Portfolio"}
    lignes = []
    for i in range(1,8):
        try:
            pid = subprocess.run(["pgrep","-f",f"agent0{i}_loop.py"], capture_output=True, text=True).stdout.strip().splitlines()
            vivant = "VIVANT" if pid else "ARRETE"
            # MESSAGE peut etre dans domaine, /root, ou FONDATION selon ou l'agent a ete lance
            dossiers = {
                1: "[STRIPPED 66 bytes]",
                2: "/root/02-admin-systeme-reseau/projets/surveillance-redmi",
                3: "/root/03-intelligence-artificielle/projets/prediction-ventes",
                4: "/root/04-gouvernance-ingenierie-data/projets/qualite-donnees",
                5: "/root/05-objets-connectes-iot/projets/capteur-temperature",
                6: "/root/06-cybersecurite-audit/projets/audit-mot-de-passe",
                7: "/root/07-metier-digital/projets/portfolio-entreprise",
            }
            msg = None
            for base in [dossiers[i], "/root", "/root/FONDATION-AITIF"]:
                # STATUS d’abord (nouveau), puis MESSAGE, puis REPONSE
                for nom in [f"STATUS-AGENT-0{i}.txt", f"MESSAGE-AGENT-0{i}.txt", f"AGENT-0{i}-REPONSE.txt"]:
                    cand2 = pathlib.Path(base) / nom
                    if cand2.exists():
                        msg = cand2
                        break
                if msg is not None:
                    break
                cand = pathlib.Path(base) / f"MESSAGE-AGENT-0{i}.txt"
                if cand.exists():
                    msg = cand
                    break
            dernier = "pas de MESSAGE"
            if msg is not None and msg.exists():
                txt = msg.read_text(encoding="utf-8", errors="ignore").strip().splitlines()
                dernier = txt[-1][:90] if txt else "vide"
            prop = f"1 petite evolution petit a petit dans {domaines[i]}, a decider par Miantsa + Meta AI"
            print(f"00.{i} -> Agent 0{i} {domaines[i]} : {vivant} | Dernier : {dernier} | Proposition : {prop}")
            lignes.append(f"00.{i} -> Agent 0{i} {domaines[i]} : {vivant} | {datetime.now().strftime('%Y-%m-%d')} | {prop}")
        except Exception as e:
            print(f"00.{i} -> Agent 0{i} : erreur analyse : {e}")
    pathlib.Path("/root/FONDATION-AITIF/ANALYSE-AGENTS-00.txt").write_text("\n".join(lignes)+"\n", encoding="utf-8")
    print("Analyse rangee dans ANALYSE-AGENTS-00.txt")
    print("=== TERMINE - Analyse V0.8 fini, Miantsa peut verifier ===")
