# data/db.py

import sqlite3
from datetime import datetime
import os

DB_PATH = "data/db.sqlite"

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            comment TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_expense(user_id: int, category: str, amount: float, comment: str = None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    date = datetime.now().isoformat(sep=' ', timespec='seconds')
    cursor.execute("""
        INSERT INTO expenses (user_id, date, category, amount, comment)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, date, category, amount, comment))
    conn.commit()
    conn.close()
