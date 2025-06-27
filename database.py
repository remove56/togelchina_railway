import sqlite3

# Fungsi untuk mengambil hasil terbaru dari tabel 'hasill'
def get_hasil():
    connection = sqlite3.connect('chinapools.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hasill ORDER BY tanggal DESC LIMIT 1")
    hasil = cursor.fetchall()
    connection.close()
    return hasil

# Fungsi untuk memasukkan hasil baru ke tabel 'hasill'
def insert_hasil(angka, tanggal):
    connection = sqlite3.connect('chinapools.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO hasill (angka, tanggal) VALUES (?, ?)", (angka, tanggal))
    connection.commit()
    connection.close()

# Fungsi untuk mengambil prediksi terbaru
def get_prediksi():
    con = sqlite3.connect('china.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM prediksi ORDER BY tanggal DESC LIMIT 1")
    data = cur.fetchone()
    con.close()
    return data

# Membuat tabel 'hasill' jika belum ada
def create_hasil_table():
    connection = sqlite3.connect('chinapools.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hasill (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            angka INTEGER,
            tanggal TEXT
        )
    """)
    connection.commit()
    connection.close()

# Panggil fungsi untuk membuat tabel 'hasill'
create_hasil_table()
