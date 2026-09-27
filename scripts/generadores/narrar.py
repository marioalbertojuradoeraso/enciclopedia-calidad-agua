"""Genera las narraciones de una sección a partir de los .parrafo con botón de audio.
Uso: python narrar.py <carpeta-seccion>   (omite los MP3 que ya existen)."""
import html, json, re, sys, urllib.request
from pathlib import Path

BASE = Path("C:/Users/majur/Downloads/MQAT/Enciclopedia")
CLAVE = (BASE.parent / "api_ElevenLabs.txt").read_text(encoding="utf-8").strip()
VOZ = "YFz1BE3aN7fQBZrEgdBE"
PAUSA = '<break time="0.4s" />'

ruta = BASE / "secciones" / sys.argv[1]
pagina = ruta if ruta.suffix == ".html" else ruta / "index.html"
t = pagina.read_text(encoding="utf-8")
for m in re.finditer(r'<div class="parrafo"[^>]*>\s*<p>(.*?)</p>\s*<button class="btn-audio"[^>]*data-audio="([^"]+)"', t, re.S):
    texto = html.unescape(re.sub(r"<[^>]+>", "", m.group(1)))
    # Símbolos que la voz leería mal: se escriben con palabras solo para la narración.
    for simbolo, palabras in [(" (mg CaCO₃/L)", ""), ("mg CaCO₃/L", "miligramos de carbonato de calcio por litro"),
                              (" (UC)", ""), (" UC", " unidades de color"), (" °C", " grados Celsius"),
                              (", o NTU", ""), (" NTU", " unidades N T U"), ("µS/cm", "microsiemens por centímetro"), ("DBO₅", "DBO cinco"), ("mg/L", "miligramos por litro"), ("CaCO₃", "carbonato de calcio"),
                              (" (H⁺)", ""), ("H⁺", "hidrógeno"), ("E. coli", "E coli"), ("0,0000001", "cero coma seis ceros y un uno")]:
        texto = texto.replace(simbolo, palabras)
    destino = (pagina.parent / m.group(2)).resolve()
    if destino.exists():
        print("Existe", destino.name); continue
    # Pausa después del conector que abre cada oración (primera coma dentro de las 4 primeras palabras).
    oraciones = re.split(r"(?<=[.!?])\s+", texto)
    def pausar(o):
        i = o.find(",")
        return o[:i+1] + " " + PAUSA + o[i+1:] if 0 < i and len(o[:i].split()) <= 4 else o
    guion = " ".join(pausar(o) for o in oraciones)
    req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{VOZ}?output_format=mp3_44100_128",
        data=json.dumps({"text": guion, "model_id": "eleven_multilingual_v2", "language_code": "es",
                         "voice_settings": {"stability": 0.55, "similarity_boost": 0.75, "style": 0.2, "speed": 0.95}}).encode(),
        headers={"xi-api-key": CLAVE, "Content-Type": "application/json", "accept": "audio/mpeg"})
    try:
        datos = urllib.request.urlopen(req, timeout=120).read()
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_bytes(datos)
        print("OK", destino.name, round(len(datos) * 8 / 128000, 1), "s aprox")
    except urllib.error.HTTPError as e:
        print("ERROR", destino.name, e.code, e.read()[:200])
