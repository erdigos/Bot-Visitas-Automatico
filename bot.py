import urllib.request
import random
import time

# ⚠️ PEGA AQUÍ TU ENLACE REAL:
ENLACE = "https://nintendoproject.com/redir/?ref=erdigos"

navegadores = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"
]

def simular_visita():
    user_agent = random.choice(navegadores)
    req = urllib.request.Request(
        ENLACE, 
        headers={
            'User-Agent': user_agent,
            'Accept-Language': 'es-ES,es;q=0.9'
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            print(f"[Éxito] Visita enviada.")
    except Exception as e:
        print(f"[Error]: {e}")

if __name__ == "__main__":
    for i in range(2):
        print(f"Enviando usuario ficticio #{i+1}...")
        simular_visita()
        if i == 0:
            time.sleep(5)
