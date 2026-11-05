import os
import random
import threading
import time
import requests
from flask import Flask

# Servidor Web mínimo para mantener Render contento
app = Flask(__name__)


@app.route("/")
def home():
    return "Bot de visitas ejecutándose en Render 24/7"


def ejecutar_bot():
    URL = "https://nintendoproject.com/redir/?ref=erdigos"
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.82 Mobile Safari/537.36",
    ]

    visitas = 0
    print("=== Bot iniciado en Render ===")

    while True:
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept-Language": "es-ES,es;q=0.9",
        }
        try:
            r = requests.get(URL, headers=headers, timeout=10)
            if r.status_code == 200:
                visitas += 1
                print(
                    f"[{time.strftime('%H:%M:%S')}] Visita #{visitas} enviada correctamente desde Render."
                )
        except Exception as e:
            print(f"Error en la petición: {e}")

        # Pausa aleatoria entre visitas (10 a 25 segundos)
        time.sleep(random.randint(10, 25))


# Iniciar el bucle de visitas en un hilo secundario
hilo_bot = threading.Thread(target=ejecutar_bot, daemon=True)
hilo_bot.start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
