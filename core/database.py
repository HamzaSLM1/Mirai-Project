import sqlite3

DB_PATH = "data/patients.db"

def init():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS doses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            supplement TEXT,
            date TEXT,
            time TEXT
        )
    """)
    conn.commit()
    conn.close()

def record(name, supplement, time):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO doses (name, supplement, date, time) VALUES (?, ?, date('now'), ?)",
        (name, supplement, time)
    )
    conn.commit()
    conn.close()

def history(name, limit=10):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(
        "SELECT date, time, supplement FROM doses WHERE name = ? ORDER BY id DESC LIMIT ?",
        (name, limit)
        )
        rows = c.fetchall()
        conn.close()
        return rows


    

    
