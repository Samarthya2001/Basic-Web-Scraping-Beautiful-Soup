import requests

def fetchAndSaveFile(url, path):
    r = requests.get(url)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(r.text)


url = "https://timesofindia.indiatimes.com/city/delhi"

fetchAndSaveFile(url,"data/times.html")