from flask import Flask, render_template_string, send_file
from database import get_hasil, get_prediksi
import os
from grafik import buat_grafik_tren

app = Flask(__name__)

@app.route('/')
def index():
    hasil = get_hasil()
    prediksi = get_prediksi()
    buat_grafik_tren()

    template = """
    <h1>📊 Keluaran dan Prediksi</h1>
    <p><strong>Hasil Terbaru:</strong> {{ hasil[0][1] if hasil else '-' }} ({{ hasil[0][2] if hasil else '-' }})</p>
    <p><strong>Prediksi Hari Ini:</strong> {{ prediksi[1] if prediksi else '-' }} ({{ prediksi[2] if prediksi else '-' }})</p>
    <img src='/grafik' width='400px' alt='Grafik Frekuensi Angka'/>
    """
    return render_template_string(template, hasil=hasil, prediksi=prediksi)

@app.route('/grafik')
def grafik():
    return send_file('static/grafik.png', mimetype='image/png')

if __name__ == '__main__':
    app.run()
