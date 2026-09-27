"""Imágenes sin personaje (flux-pro-1.1, 1024x1024) para escenas con muchos objetos.
Uso: python bfl_pro.py <carpeta-salida> <archivo.json con {nombre: prompt}>"""
import json, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

CLAVE = open(r"C:\Users\majur\Downloads\MQAT\api_bfl.txt", encoding="utf-8").read().strip()
SALIDA = sys.argv[1].rstrip("/") + "/"
PEDIDOS = json.load(open(sys.argv[2], encoding="utf-8"))
ESTILO = (" Friendly children's educational mini-comic illustration, polished hand-painted cartoon, clean outlines, "
          "bright but harmonious turquoise, orange and green colors, soft daylight, simple and cheerful. "
          "No text, no letters, no numbers, no labels, no speech bubbles, no watermark.")

def pedir(url, datos=None):
    req = urllib.request.Request(url, data=json.dumps(datos).encode() if datos else None,
                                 headers={"x-key": CLAVE, "accept": "application/json", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)

def generar(nombre, prompt):
    try:
        tarea = pedir("https://api.bfl.ai/v1/flux-pro-1.1",
                      {"prompt": prompt + ESTILO, "width": 1024, "height": 1024, "output_format": "png"})
        sondeo = tarea.get("polling_url") or f"https://api.bfl.ai/v1/get_result?id={tarea['id']}"
        for _ in range(200):
            time.sleep(1.5)
            res = pedir(sondeo)
            if res.get("status") == "Ready":
                urllib.request.urlretrieve(res["result"]["sample"], SALIDA + nombre)
                return f"OK {nombre}"
            if res.get("status") not in ("Pending", "Processing", "Queued"):
                return f"ERROR {nombre}: {json.dumps(res)[:300]}"
        return f"ERROR {nombre}: tiempo agotado"
    except Exception as e:
        return f"ERROR {nombre}: {e}"

with ThreadPoolExecutor(6) as ex:
    for r in ex.map(lambda kv: generar(*kv), PEDIDOS.items()):
        print(r, flush=True)
