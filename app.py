from flask import Flask
import sqlite3
from typing import Any

app = Flask(__name__)

DATABASE = 'membership.db'

def init_db() -> None:
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS members (
                iid INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                phone TEXT,
                birthdate TEXT
            )
        ''')
        c.execute('''
            INSERT OR IGNORE INTO members (username, email, password, phone, birthdate)
            VALUES (?, ?, ?, ?, ?)''', 
            ('admin', 'admin@example.com', 'admin123', '0912345678', '1990-01-01'))
        conn.commit()


init_db()
