import sqlite3
import matplotlib.pyplot as plt

def buat_grafik_tren():
    conn = sqlite3.connect('chinapools.db')
    cursor = conn.cursor()
    cursor.execute("SELECT angka FROM hasill")
    data = cursor.fetchall()
    conn.close()

    digit_freq = [0] * 10
    for (angka,) in data:
        for digit in str(angka):
            digit_freq[int(digit)] += 1

    plt.figure(figsize=(6,4))
    plt.bar(range(10), digit_freq)
    plt.xlabel("Digit (0-9)")
    plt.ylabel("Frekuensi")
    plt.title("Statistik Frekuensi Angka")
    plt.savefig("static/grafik.png", dpi=100)
