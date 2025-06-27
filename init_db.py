
import sqlite3

# hasil keluaran
conn1 = sqlite3.connect('chinapools.db')
conn1.execute("""CREATE TABLE IF NOT EXISTS hasil (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tanggal TEXT UNIQUE,
    angka TEXT
)""")
conn1.commit()

# prediksi
conn2 = sqlite3.connect('china.db')
conn2.execute("""CREATE TABLE IF NOT EXISTS prediksi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tanggal TEXT UNIQUE,
    angka TEXT,
    syair TEXT
)""")
conn2.commit()
print("Database siap.")
