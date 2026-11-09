# Gestion Commerce Madagascar - V1
# Outil pour petits commerces partout a Madagascar
# 100% sur Redmi, hors-ligne, en Ariary, base SQLite
# Par Miantsa - solutions-madagascar

import sqlite3
from config import get_ville
VILLE = get_ville()
from datetime import datetime

DB = "commerce.db"

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ventes (id INTEGER PRIMARY KEY, produit TEXT, montant INTEGER, date TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS depenses (id INTEGER PRIMARY KEY, raison TEXT, montant INTEGER, date TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS stock (id INTEGER PRIMARY KEY, produit TEXT UNIQUE, quantite INTEGER, prix INTEGER)")
    conn.commit()
    conn.close()

def aujourd_hui():
    return datetime.now().strftime("%Y-%m-%d")

def ajouter_vente():
    produit = input("Produit vendu : ")
    try:
        montant = int(input("Montant en Ariary : "))
    except:
        print("Montant invalide, mets un nombre.")
        return
    conn = sqlite3.connect(DB)
    conn.execute("INSERT INTO ventes (produit, montant, date) VALUES (?, ?, ?)", (produit, montant, aujourd_hui()))
    conn.commit()
    conn.close()
    print(f"✅ Vente enregistree : {produit} - {montant} Ar")

def ajouter_depense():
    raison = input("Raison de la depense : ")
    try:
        montant = int(input("Montant en Ariary : "))
    except:
        print("Montant invalide.")
        return
    conn = sqlite3.connect(DB)
    conn.execute("INSERT INTO depenses (raison, montant, date) VALUES (?, ?, ?)", (raison, montant, aujourd_hui()))
    conn.commit()
    conn.close()
    print(f"✅ Depense enregistree : {raison} - {montant} Ar")

def ajouter_stock():
    produit = input("Produit : ")
    try:
        quantite = int(input("Quantite : "))
        prix = int(input("Prix de vente en Ariary : "))
    except:
        print("Nombre invalide.")
        return
    conn = sqlite3.connect(DB)
    conn.execute("INSERT INTO stock (produit, quantite, prix) VALUES (?, ?, ?) ON CONFLICT(produit) DO UPDATE SET quantite=quantite+excluded.quantite, prix=excluded.prix", (produit, quantite, prix))
    conn.commit()
    conn.close()
    print(f"✅ Stock mis a jour : {produit} - {quantite} pieces")

def bilan_jour():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT COALESCE(SUM(montant),0) FROM ventes WHERE date=?", (aujourd_hui(),))
    ventes = cur.fetchone()[0]
    cur.execute("SELECT COALESCE(SUM(montant),0) FROM depenses WHERE date=?", (aujourd_hui(),))
    depenses = cur.fetchone()[0]
    print(f"\n--- BILAN DU JOUR - {VILLE} / MADAGASCAR ---")
    print(f"Date : {aujourd_hui()}")
    print(f"Ventes : {ventes} Ar")
    print(f"Depenses : {depenses} Ar")
    print(f"Benefice : {ventes - depenses} Ar")
    print("----------------------------------")
    cur.execute("SELECT produit, quantite, prix FROM stock")
    print("\nSTOCK :")
    for p, q, pr in cur.fetchall():
        print(f"- {p} : {q} pieces x {pr} Ar")
    conn.close()

def menu():
    init_db()
    while True:
        print(f"\n=== GESTION COMMERCE - {VILLE.upper()} / MADAGASCAR ===")
        print("1. Ajouter une vente")
        print("2. Ajouter une depense")
        print("3. Ajouter / Mettre a jour stock")
        print("4. Voir bilan du jour + stock")
        print("5. Quitter")
        choix = input("Ton choix (1-5) : ")
        if choix == "1":
            ajouter_vente()
        elif choix == "2":
            ajouter_depense()
        elif choix == "3":
            ajouter_stock()
        elif choix == "4":
            bilan_jour()
        elif choix == "5":
            print("Misaotra ! A demain. Donnees sauvegardees.")
            break
        else:
            print("Choix invalide, mets 1 a 5.")

if __name__ == "__main__":
    menu()
