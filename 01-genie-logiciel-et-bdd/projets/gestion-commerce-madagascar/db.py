# Base de donnees Aitif - V1.8
# Separe de main.py pour que main.py reste leger, stable, puissant.
# Si la base change demain, on touche seulement ici.

import sqlite3

DB = "commerce.db"

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ventes (id INTEGER PRIMARY KEY, produit TEXT, montant INTEGER, date TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS depenses (id INTEGER PRIMARY KEY, raison TEXT, montant INTEGER, date TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS stock (id INTEGER PRIMARY KEY, produit TEXT UNIQUE, quantite INTEGER, prix INTEGER)")
    conn.commit()
    conn.close()

def connect():
    return sqlite3.connect(DB)
