"""Piezas compartidas para generar páginas de sección (secciones 5 y 6)."""
from pathlib import Path

BASE = Path("C:/Users/majur/Downloads/MQAT/Enciclopedia")
SECCIONES = [
    ("01-introduccion", "1. Introducción"),
    ("02-hidrosfera-ciclos", "2. Hidrosfera y ciclos"),
    ("03-cantidad-calidad", "3. Cantidad y calidad"),
    ("04-parametros", "4. Parámetros"),
    ("05-otros-parametros", "5. Otros parámetros"),
    ("06-normatividad", "6. Normatividad"),
]

def cabecera(carpeta, titulo, etiqueta, h1, subtitulo):
    menu = "\n".join(
        f'          <li><a href="{"index.html" if c == carpeta else f"../{c}/index.html"}"{" aria-current=\"page\"" if c == carpeta else ""}>{n}</a></li>'
        for c, n in SECCIONES) + "\n" + '          <li><a href="../../calculadoras.html">🧮 Calculadoras</a></li>'
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{titulo}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../css/estilos.css">
  <script src="../../js/enciclopedia.js" defer></script>
  <script src="../../js/laboratorio.js" defer></script>
</head>
<body>

  <header class="barra">
    <div class="contenedor">
      <a class="marca" href="../../index.html">💧 Enciclopedia del Agua</a>
      <nav aria-label="Secciones">
        <ul class="menu">
{menu}
        </ul>
      </nav>
    </div>
    <div class="progreso" aria-hidden="true"><span></span></div>
  </header>

  <main>
    <section class="portada">
      <div class="contenedor">
        <span class="etiqueta">{etiqueta}</span>
        <h1>{h1}</h1>
        <p>{subtitulo}</p>
      </div>
    </section>
"""

def pie(href, texto):
    return f"""
    <div class="contenedor siguiente">
      <a class="btn-siguiente" href="{href}">{texto}</a>
    </div>
  </main>

</body>
</html>
"""

class Pagina:
    def __init__(self, carpeta):
        self.img = f"../../assets/images/{carpeta}/"
        self.aud = f"../../assets/audio/{carpeta}/"

    def parrafo(self, texto, audio):
        return f"""<div class="parrafo">
            <p>{texto}</p>
            <button class="btn-audio" type="button" data-audio="{self.aud}{audio}.mp3" hidden>🔊 Escuchar</button>
          </div>"""

    def imagen(self, archivo, alt, pie=None):
        fig = f'<div class="imagen" data-pendiente="Imagen pendiente"><img src="{self.img}{archivo}" alt="{alt}"></div>'
        return f'<figure class="ilustracion-explicada">{fig}<figcaption>{pie}</figcaption></figure>' if pie else fig

    def vineta(self, archivo, alt, texto):
        return f"""<figure class="vineta">
            <div class="imagen" data-pendiente="Viñeta pendiente"><img src="{self.img}{archivo}" alt="{alt}"></div>
            <figcaption>{texto}</figcaption>
          </figure>"""

def descubrir(ident, pregunta, respuesta):
    return f"""<div>
            <button class="btn-descubrir" type="button" aria-expanded="false" aria-controls="{ident}">{pregunta}</button>
            <div class="revelado" id="{ident}" hidden><p>{respuesta}</p></div>
          </div>"""

def reto(pregunta, opciones):
    botones = "\n".join(
        f'            <button class="opcion" type="button" data-correcta="{"true" if ok else "false"}" data-retro="{retro}">{texto}</button>'
        for texto, ok, retro in opciones)
    return f"""<div class="reto">
          <p class="pregunta">{pregunta}</p>
          <div class="opciones">
{botones}
          </div>
          <p class="retro" aria-live="polite"></p>
        </div>"""

def tarjeta(icono, titulo, sub, reverso):
    return f"""<button class="tarjeta" type="button" aria-pressed="false">
            <span class="tarjeta-interior">
              <span class="cara frente"><span class="icono" aria-hidden="true">{icono}</span><strong>{titulo}</strong><small>{sub}</small></span>
              <span class="cara reverso">{reverso}</span>
            </span>
          </button>"""

def clasificar(opciones, items, pista, exito):
    botones = "".join(f'<button type="button" data-opcion="{v}">{t}</button>' for v, t in opciones)
    filas = "\n".join(f"""            <div class="item" data-respuesta="{r}" data-explica="{e}">
              <p>{f}</p>
              <div class="botones">{botones}</div>
              <p class="retro-item" aria-live="polite"></p>
            </div>""" for f, r, e in items)
    return f"""<div class="clasificar" data-pista="{pista}" data-exito="{exito}">
          <div class="items">
{filas}
          </div>
          <p class="marcador" aria-live="polite"></p>
        </div>"""

def flujo(pasos):
    items = "\n".join(f"            <li><strong>{t}</strong>{d}</li>" for t, d in pasos)
    return f'<ol class="flujo">\n{items}\n          </ol>'

def bloque(ident, contenido, titulo=None, instruccion=None):
    h2 = f"<h2>{titulo}</h2>\n        " if titulo else ""
    ins = f'<p class="instruccion">{instruccion}</p>\n        ' if instruccion else ""
    return f"""
    <section class="bloque" id="{ident}">
      <div class="contenedor">
        {h2}{ins}{contenido}
      </div>
    </section>
"""

def escribir(carpeta, html):
    destino = BASE / "secciones" / carpeta / "index.html"
    destino.write_text(html, encoding="utf-8")
    gitkeep = destino.parent / ".gitkeep"
    if gitkeep.exists():
        gitkeep.unlink()
    print("OK", destino)
