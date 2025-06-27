
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from database import simpan_hasil

def scrape_hasil():
    url = 'https://chinapools.asia/'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    result = soup.find('h4').text.strip()
    angka = result.split(':')[-1].strip()
    tanggal = datetime.now().strftime('%Y-%m-%d')
    simpan_hasil(tanggal, angka)
    print(f"Hasil disimpan: {tanggal} - {angka}")

if __name__ == "__main__":
    scrape_hasil()
