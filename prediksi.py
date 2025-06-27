
from database import get_hasil, simpan_prediksi
from datetime import datetime
import random

def prediksi_ai():
    data = get_hasil(10)
    all_angka = ''.join([d[2] for d in data])
    frekuensi = {str(i): all_angka.count(str(i)) for i in range(10)}
    sorted_freq = sorted(frekuensi.items(), key=lambda x: -x[1])
    prediksi = ''.join([x[0] for x in sorted_freq[:4]])
    syair = "Analisa angka tertinggi dari 10 histori terakhir."
    tgl = datetime.now().strftime('%Y-%m-%d')
    simpan_prediksi(tgl, prediksi, syair)
    print(f"Prediksi disimpan: {prediksi}")

if __name__ == "__main__":
    prediksi_ai()
