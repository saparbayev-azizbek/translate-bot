import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

def tarjima(source, target, text):
    payload = {
        "q": text,
        "target": target,
        "source": source
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "cbd5965ed2mshb18c69891676784p1913f4jsn4085fa3d3037",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    res = response.json()
    return res['data']['translations'][0]['translatedText']

