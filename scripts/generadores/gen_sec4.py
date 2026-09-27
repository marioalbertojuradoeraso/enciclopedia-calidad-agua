"""Genera las páginas estáticas de la sección 4 (índice + seis parámetros)."""
from pathlib import Path

DIR = Path("C:/Users/majur/Downloads/MQAT/Enciclopedia/secciones/04-parametros")
IMG = "../../assets/images/04-parametros/"
AUD = "../../assets/audio/04-parametros/"

CABECERA = """<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 100 100%27%3E%3Ctext y=%27.9em%27 font-size=%2790%27%3E%F0%9F%92%A7%3C/text%3E%3C/svg%3E">
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
          <li><a href="../01-introduccion/index.html">1. Introducción</a></li>
          <li><a href="../02-hidrosfera-ciclos/index.html">2. Hidrosfera y ciclos</a></li>
          <li><a href="../03-cantidad-calidad/index.html">3. Cantidad y calidad</a></li>
          <li><a href="index.html" aria-current="page">4. Parámetros</a></li>
          <li><a href="../05-otros-parametros/index.html">5. Otros parámetros</a></li>
          <li><a href="../06-normatividad/index.html">6. Normatividad</a></li>
          <li><a href="../../calculadoras.html">🧮 Calculadoras</a></li>
        </ul>
      </nav>
    </div>
    <div class="progreso" aria-hidden="true"><span></span></div>
  </header>

  <main>
    <section class="portada">
      <div class="contenedor">
        {volver}<span class="etiqueta">{etiqueta}</span>
        <h1>{h1}</h1>
        <p>{subtitulo}</p>
      </div>
    </section>
"""

PIE = """
    {navegacion}
  </main>

</body>
</html>
"""

def parrafo(texto, audio):
    return f"""<div class="parrafo">
            <p>{texto}</p>
            <button class="btn-audio" type="button" data-audio="{AUD}{audio}.mp3" hidden>🔊 Escuchar</button>
          </div>"""

def imagen(archivo, alt, pie=None):
    fig = f'<div class="imagen" data-pendiente="Imagen pendiente"><img src="{IMG}{archivo}" alt="{alt}"></div>'
    if pie:
        return f'<figure class="ilustracion-explicada">{fig}<figcaption>{pie}</figcaption></figure>'
    return fig

def comic_completo(archivo, alt, pie):
    return f"""<figure class="comic-completo">
          <a href="{IMG}{archivo}" target="_blank" rel="noopener"><img src="{IMG}{archivo}" alt="{alt}" loading="lazy"></a>
          <figcaption>{pie} Toca la imagen para verla en grande.</figcaption>
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

def flujo(pasos):
    items = "\n".join(f"            <li><strong>{t}</strong>{d}</li>" for t, d in pasos)
    return f'<ol class="flujo">\n{items}\n          </ol>'

def bloque(ident, contenido, titulo=None, instruccion=None, clase_contenedor="contenedor"):
    h2 = f"<h2>{titulo}</h2>\n        " if titulo else ""
    ins = f'<p class="instruccion">{instruccion}</p>\n        ' if instruccion else ""
    return f"""
    <section class="bloque" id="{ident}">
      <div class="{clase_contenedor}">
        {h2}{ins}{contenido}
      </div>
    </section>
"""

MATRAZ = """<svg viewBox="0 0 120 200" aria-hidden="true">
            <rect x="55" y="0" width="10" height="64" rx="3" fill="#e3f5fb" stroke="#0b3954" stroke-width="3"/>
            <path d="M58 64 L62 64 L61 76 L59 76 Z" fill="#0b3954"/>
            <path d="M57 82 Q60 76 63 82 Q63 86 60 86 Q57 86 57 82 Z" fill="#1fa2c4"/>
            <path class="liquido" d="M29 148 L91 148 L108 185 Q110 190 104 190 L16 190 Q10 190 12 185 Z" fill="#f5d130"/>
            <path d="M48 92 L48 122 L10 186 Q8 192 16 192 L104 192 Q112 192 110 186 L72 122 L72 92" fill="none" stroke="#0b3954" stroke-width="4" stroke-linejoin="round"/>
          </svg>"""

def titulacion(fin, paso, factor, inicio, medio, final, antes, cerca, fin_txt, nota, boton):
    return f"""<div class="titulacion" data-fin="{fin}" data-paso="{paso}" data-factor="{factor}"
             data-inicio="{inicio}" data-medio="{medio}" data-final="{final}"
             data-texto-antes="{antes}" data-texto-cerca="{cerca}" data-texto-fin="{fin_txt}">
          {MATRAZ}
          <div>
            <p class="lectura">Titulante agregado: <strong class="vol">0,0</strong> mL</p>
            <div class="botones">
              <button class="btn-gota" type="button">{boton}</button>
              <button class="btn-reiniciar" type="button">Reiniciar</button>
            </div>
            <p class="mensaje" aria-live="polite"></p>
            <p class="nota">{nota}</p>
          </div>
        </div>"""

ORDEN = [
    ("ph-conductividad.html", "pH y conductividad"),
    ("color.html", "Color"),
    ("turbiedad.html", "Turbiedad"),
    ("alcalinidad-acidez.html", "Alcalinidad y acidez"),
    ("dureza.html", "Dureza"),
    ("solidos.html", "Sólidos"),
]

def navegacion(archivo):
    i = [a for a, _ in ORDEN].index(archivo)
    ant = f'<a class="btn-siguiente" href="{ORDEN[i-1][0]}">← {ORDEN[i-1][1]}</a>' if i > 0 else '<a class="btn-siguiente" href="index.html">← Todos los parámetros</a>'
    sig = f'<a class="btn-siguiente" href="{ORDEN[i+1][0]}">{ORDEN[i+1][1]} →</a>' if i < len(ORDEN) - 1 else '<a class="btn-siguiente" href="index.html">Todos los parámetros →</a>'
    return f'<div class="contenedor entre-parametros">\n      {ant}\n      {sig}\n    </div>'

def pagina(archivo, titulo, etiqueta, h1, subtitulo, cuerpo):
    volver = '<a class="volver" href="index.html">← Todos los parámetros</a><br>' if archivo != "index.html" else ""
    nav = navegacion(archivo) if archivo != "index.html" else \
        '<div class="contenedor siguiente">\n      <a class="btn-siguiente" href="../05-otros-parametros/index.html">Siguiente: Otros parámetros →</a>\n    </div>'
    html = CABECERA.format(titulo=titulo, etiqueta=etiqueta, h1=h1, subtitulo=subtitulo, volver=volver) + cuerpo + PIE.format(navegacion=nav)
    (DIR / archivo).write_text(html, encoding="utf-8")
    print("OK", archivo)

# ---------------------------------------------------------------- índice
pagina("index.html", "Parámetros de calidad del agua", "Sección 4", "Parámetros de calidad del agua",
       "Seis pistas para conocer cómo está el agua.",
       bloque("que-es", parrafo(
           "Para empezar, un parámetro es una característica del agua que se puede medir y expresar con un número y una unidad. "
           "Por ejemplo, así como un médico revisa la temperatura y la presión de una persona, el laboratorio revisa el pH, el color o la dureza del agua. "
           "Además, cada parámetro responde una pregunta distinta, por lo que ninguno basta por sí solo. "
           "De esta manera, al juntar varios resultados se obtiene un retrato completo del agua.", "p0-parametros"),
           "¿Qué es un parámetro?")
       + bloque("parametros", """<div class="enlaces">
          <a class="enlace" href="ph-conductividad.html"><span class="icono" aria-hidden="true">🧪</span><strong>pH y conductividad</strong><span>¿Es ácida o básica? ¿Cuántas sales lleva?</span></a>
          <a class="enlace" href="color.html"><span class="icono" aria-hidden="true">🎨</span><strong>Color</strong><span>Color real, color aparente y la curva de calibración.</span></a>
          <a class="enlace" href="turbiedad.html"><span class="icono" aria-hidden="true">🌫️</span><strong>Turbiedad</strong><span>¿Qué tan difícil es ver a través del agua?</span></a>
          <a class="enlace" href="alcalinidad-acidez.html"><span class="icono" aria-hidden="true">🛡️</span><strong>Alcalinidad y acidez</strong><span>El escudo del agua frente a los ácidos.</span></a>
          <a class="enlace" href="dureza.html"><span class="icono" aria-hidden="true">🧼</span><strong>Dureza</strong><span>Calcio, magnesio y el sarro de las tuberías.</span></a>
          <a class="enlace" href="solidos.html"><span class="icono" aria-hidden="true">⚖️</span><strong>Sólidos</strong><span>Lo que queda cuando el agua se evapora.</span></a>
        </div>""", "Elige un parámetro", "Cada tarjeta abre una página con cómic, laboratorio y mini-reto."))

# ---------------------------------------------------------------- pH y conductividad
EJEMPLOS_PH = ('{"0":"Ácido de batería: muy peligroso.","1":"Jugo del estómago, que ayuda a digerir.","2":"Jugo de limón.","3":"Vinagre.",'
               '"4":"Jugo de tomate.","5":"Café negro.","6":"Leche.","7":"Agua pura: ni ácida ni básica.","8":"Agua de mar.",'
               '"9":"Jabón de tocador.","10":"Leche de magnesia, un antiácido.","11":"Amoníaco de limpieza.","12":"Agua de cal.",'
               '"13":"Blanqueador de ropa.","14":"Destapador de cañerías: muy peligroso."}')
pagina("ph-conductividad.html", "pH y conductividad", "Parámetro 1 de 6", "pH y conductividad",
       "¿El agua es ácida o básica? ¿Cuántas sales lleva disueltas?",
       bloque("ph", f"""<div class="duo">
          <div>
            <h2>El pH</h2>
            {parrafo("Para comenzar, el pH indica si el agua es ácida, neutra o básica, usando una escala que va de 0 a 14. "
                     "Por ejemplo, el jugo de limón es ácido y tiene un pH cercano a 2, mientras que el jabón es básico y pasa de 9. "
                     "En el centro, cerca de 7, está el agua pura, que es neutra. "
                     "Además, en Colombia el agua para beber debe tener un pH entre 6,5 y 9,0, según la Resolución 2115 de 2007.", "p1-ph")}
          </div>
          {imagen("ph-escala.webp", "Una barra de colores del rojo al morado con un limón en el extremo rojo, un vaso de agua en el centro verde y un jabón en el extremo morado; Gotita señala el vaso.")}
        </div>""")
       + bloque("escala", f"""<div class="escala-ph" data-ejemplos='{EJEMPLOS_PH}'>
          <label for="control-ph" style="font-weight:800;display:block;margin-bottom:10px">Mueve el control por la escala de pH</label>
          <input id="control-ph" type="range" min="0" max="14" step="1" value="7">
          <div class="extremos"><span>0 · más ácido</span><span>7 · neutro</span><span>14 · más básico</span></div>
          <div class="lectura" aria-live="polite"><span class="valor">7</span><span class="tipo">Neutro</span></div>
          <p class="ejemplo"></p>
        </div>
        <div class="descubrir" style="margin-top:20px">
          {descubrir("dato-diez", "¿Un punto de pH es mucho o poco?", "De hecho, cada punto de la escala multiplica por diez la cantidad de iones hidrógeno libres, que son las partículas que hacen ácida al agua. Por eso, un agua con pH 5 tiene diez veces más de esas partículas que una con pH 6, y cien veces más que una con pH 7.")}
        </div>""", "La escala del pH", "Explora ejemplos de la vida diaria.")
       + bloque("medir-ph", f"""<div class="duo">
          {parrafo("Por otra parte, el pH se mide con un pHmetro, un aparato con una punta de vidrio llamada electrodo que se sumerge en la muestra. "
                   "Antes de usarlo, se calibra con líquidos de pH conocido, por ejemplo 4 y 7, igual que se ajusta una balanza antes de pesar. "
                   "Luego, se espera a que el número de la pantalla deje de moverse y se anota con un decimal, como 7,4.", "p2-medir-ph")}
          {parrafo("Además, la conductividad indica qué tan fácil pasa la corriente eléctrica por el agua. "
                   "Esto ocurre porque las sales disueltas se separan en partículas con carga, llamadas iones, que transportan la electricidad. "
                   "Por eso, a más sales disueltas, mayor conductividad. "
                   "Por ejemplo, en una práctica, el agua de la llave marcó 210 microsiemens por centímetro y el agua de una quebrada marcó 85; es decir, el agua de la llave llevaba más sales.", "p3-conductividad")}
        </div>""", "¿Cómo se mide?")
       + bloque("conductividad", f"""<div class="duo">
          {imagen("conductividad.webp", "Dos vasos con electrodos conectados a bombillos: el del agua con más sales disueltas enciende su bombillo con mucha más fuerza.",
                  "En este dibujo, el bombillo brilla más en el agua con más sales: los puntos de colores representan los iones. Un conductímetro real no usa bombillo, sino que muestra un número en su pantalla.")}
          <div class="descubrir">
            {descubrir("dato-unidad", "¿Qué significa µS/cm?", "Por ejemplo, µS/cm se lee «microsiemens por centímetro» y es la unidad de la conductividad. Así, un número más alto significa que el agua lleva más sales disueltas.")}
            {descubrir("dato-destilada", "¿Y el agua destilada?", "En cambio, el agua destilada casi no tiene sales, así que su conductividad es muy baja, menor a 5 µS/cm. Por eso, se usa para enjuagar los electrodos entre una muestra y otra.")}
          </div>
        </div>""", "Más sales, más corriente")
       + bloque("reto", reto("Una muestra de agua tiene pH 5,5. ¿Cumple el rango para beber en Colombia?", [
           ("Sí, porque está cerca de 7.", False, "No del todo. Aunque parece cercano, el rango es de 6,5 a 9,0, y 5,5 queda por debajo."),
           ("No, porque está por debajo de 6,5.", True, "¡Correcto! Un pH de 5,5 es más ácido de lo permitido para agua de consumo."),
           ("No se puede saber sin medir la dureza.", False, "No del todo. En realidad, para esta pregunta basta con comparar el pH con el rango 6,5 a 9,0."),
       ]) + reto("Dos aguas marcan 210 y 85 µS/cm. ¿Cuál lleva más sales disueltas?", [
           ("La de 210 µS/cm.", True, "¡Correcto! A mayor conductividad, más iones y más sales disueltas."),
           ("La de 85 µS/cm.", False, "No del todo. Al contrario, un número menor indica menos sales disueltas."),
       ]), "Mini-reto"))

# ---------------------------------------------------------------- color
PUNTOS = "".join(f'<circle cx="{70 + 6.2 * x}" cy="{260 - 4000 * x / 1000}" r="5" fill="#0b3954"/>' for x in range(0, 51, 10))
EJES = "".join(f'<line x1="70" x2="380" y1="{260 - 40 * k}" y2="{260 - 40 * k}" stroke="#e3f5fb" stroke-width="2"/>' for k in range(1, 7))
ETQ_Y = "".join(f'<text x="64" y="{264 - 40 * k}" text-anchor="end">{k / 100:.3f}'.replace(".", ",") + "</text>" for k in range(0, 7))
ETQ_X = "".join(f'<text x="{70 + 6.2 * x}" y="280" text-anchor="middle">{x}</text>' for x in range(0, 51, 10))
GRAFICA = f"""<svg viewBox="0 0 400 320" role="img" aria-label="Curva de calibración: recta que va de absorbancia 0 con 0 UC hasta absorbancia 0,050 con 50 UC.">
            <g font-family="Nunito, Segoe UI, sans-serif" font-size="12" fill="#4f6272">
              {EJES}
              <line x1="70" y1="260" x2="380" y2="260" stroke="#0b3954" stroke-width="2"/>
              <line x1="70" y1="20" x2="70" y2="260" stroke="#0b3954" stroke-width="2"/>
              {ETQ_Y}{ETQ_X}
              <text x="225" y="306" text-anchor="middle" font-weight="800" fill="#0b3954">Color (UC)</text>
              <text x="14" y="140" text-anchor="middle" font-weight="800" fill="#0b3954" transform="rotate(-90 14 140)">Absorbancia</text>
            </g>
            <line x1="70" y1="260" x2="380" y2="60" stroke="#087e8b" stroke-width="4"/>
            {PUNTOS}
            <line class="guia-h" x1="70" y1="152" x2="228" y2="152" stroke="#ff6f59" stroke-width="3" stroke-dasharray="7 5"/>
            <line class="guia-v" x1="228" y1="152" x2="228" y2="260" stroke="#ff6f59" stroke-width="3" stroke-dasharray="7 5"/>
            <circle class="punto" cx="228" cy="152" r="8" fill="#ff6f59" stroke="#fff" stroke-width="3"/>
          </svg>"""
pagina("color.html", "Color del agua", "Parámetro 2 de 6", "Color del agua",
       "El caso de los dos colores y la regla que traduce la luz en números.",
       bloque("dos-colores", f"""{parrafo("Para empezar, el color del agua se debe a sustancias disueltas, como restos de hojas descompuestas o hierro. "
                   "Sin embargo, al mirar una muestra sin tratar, también se ven partículas que flotan y la enturbian. "
                   "Por eso, se distinguen dos colores: el color aparente, que es el que se ve en la muestra tal como llega, "
                   "y el color real, que es el que queda después de filtrarla para quitar esas partículas.", "p1-dos-colores")}
        <div style="margin-top:28px">
        {comic_completo("comic-dos-colores.jpg", "Cómic «El caso de los dos colores»: dos detectives observan agua de río amarilla y nublada, la iluminan, la filtran y comparan el color aparente con el color real.",
                        "Cómic «El caso de los dos colores»: primero se observa, luego se ilumina y al final se filtra.")}
        </div>""", "Color aparente y color real")
       + bloque("comparar", """<div class="tarjetas dos">
          <button class="tarjeta" type="button" aria-pressed="false">
            <span class="tarjeta-interior">
              <span class="cara frente"><span class="icono" aria-hidden="true">👀</span><strong>Color aparente</strong><small>antes de filtrar</small></span>
              <span class="cara reverso">Por ejemplo, incluye todo lo que se ve: el color de lo disuelto más el efecto de las partículas que flotan.</span>
            </span>
          </button>
          <button class="tarjeta" type="button" aria-pressed="false">
            <span class="tarjeta-interior">
              <span class="cara frente"><span class="icono" aria-hidden="true">🔎</span><strong>Color real</strong><small>después de filtrar</small></span>
              <span class="cara reverso">En cambio, solo muestra el color de lo disuelto, porque las partículas quedaron en el filtro.</span>
            </span>
          </button>
        </div>""", "Compara los dos colores", "Toca cada tarjeta.")
       + bloque("unidades", f"""<div class="duo">
          <div>
            {parrafo("Además, el color se expresa en unidades de color (UC), también llamadas unidades platino-cobalto. "
                     "Esto se debe a que se compara con mezclas preparadas con esos dos metales, que tienen un tono amarillo conocido. "
                     "Por ejemplo, una mezcla de 10 UC es casi transparente y una de 50 UC ya es claramente amarilla. "
                     "Así, esos tubos de referencia, llamados estándares, funcionan como las marcas de una regla.", "p2-unidades")}
          </div>
          {imagen("color-tubos.webp", "Una gradilla con tubos de ensayo que van de transparentes a color ámbar, y un tubo suelto con una muestra amarillenta para comparar.")}
        </div>""", "¿En qué se mide el color?")
       + bloque("espectro", f"""<div class="duo">
          {imagen("espectrofotometro.webp", "Gotita introduce una cubeta de vidrio en un espectrofotómetro; un haz de luz atraviesa la cubeta.")}
          <div>
            {parrafo("Por otra parte, el espectrofotómetro es un aparato que ilumina la muestra y mide cuánta luz se queda atrapada en ella; ese número se llama absorbancia. "
                     "Mientras más color tiene el agua, más luz retiene y mayor es la absorbancia. "
                     "Sin embargo, el aparato no entrega unidades de color, sino solo absorbancia. "
                     "Por eso, se necesita una curva de calibración que traduzca un número en el otro.", "p3-espectrofotometro")}
          </div>
        </div>""", "Medir con luz")
       + bloque("pasos", flujo([
           ("Preparar", "Seis estándares: 0, 10, 20, 30, 40 y 50 UC."),
           ("Medir", "La absorbancia de cada estándar."),
           ("Graficar", "Marcar los puntos y trazar una recta desde el cero."),
           ("Medir la muestra", "Leer su absorbancia en el aparato."),
           ("Interpolar", "Buscar ese valor en la recta y leer el color abajo."),
       ]), "La curva de calibración, paso a paso")
       + bloque("interpolar", f"""{parrafo("Finalmente, interpolar significa encontrar un valor desconocido que está entre dos valores conocidos. "
                   "Por ejemplo, si la muestra da una absorbancia de 0,027, se ubica ese número en el eje vertical, se avanza en línea recta hasta tocar la recta y luego se baja hasta el eje horizontal, donde se lee 27 UC. "
                   "Además, la curva solo vale entre 0 y 50 UC; por eso, si la muestra pasa ese límite, se diluye con agua destilada y el resultado se multiplica.", "p4-interpolar")}
        <div class="curva" style="margin-top:24px" data-pendiente="0.0010" data-max-x="50" data-max-y="0.060"
             data-dentro="La muestra tiene {{v}} UC. El punto cae dentro de la curva, así que el resultado es confiable."
             data-fuera="Fuera de rango: la absorbancia supera 0,050, que corresponde a 50 UC. Se diluye la muestra a la mitad, se mide otra vez y el resultado se multiplica por 2.">
          {GRAFICA}
          <div>
            <label for="absorbancia">Absorbancia de la muestra: <span class="abs">0,027</span></label>
            <input id="absorbancia" type="range" min="0" max="0.060" step="0.001" value="0.027">
            <p class="resultado">Color: <strong class="valor">27</strong> UC</p>
            <p class="mensaje" aria-live="polite"></p>
          </div>
        </div>
        <p style="margin-top:16px"><a href="../../assets/diagrams/04-parametros/color-interpolacion.html" target="_blank" rel="noopener" style="font-weight:800;color:var(--agua-700)">Ver la versión ampliada, con la tabla de estándares y el ejemplo de dilución →</a></p>""", "Interpolar: leer la curva", "Mueve el control y sigue la línea punteada.")
       + bloque("reto", reto("Una muestra da una absorbancia de 0,035. Con la curva anterior, ¿cuál es su color?", [
           ("3,5 UC", False, "No del todo. Para convertir, se divide entre 0,0010: 0,035 ÷ 0,0010 = 35."),
           ("35 UC", True, "¡Correcto! El punto cae dentro de la curva, entre 30 y 40 UC."),
           ("350 UC", False, "No del todo. Además, 350 UC quedaría muy por fuera de la curva, que llega hasta 50."),
       ]) + reto("¿Qué color se mide después de filtrar la muestra?", [
           ("El color aparente.", False, "No del todo. El color aparente es el de la muestra tal como llega, con partículas."),
           ("El color real.", True, "¡Correcto! Al quitar las partículas, queda solo el color de lo disuelto."),
       ]), "Mini-reto"))

# ---------------------------------------------------------------- turbiedad
pagina("turbiedad.html", "Turbiedad del agua", "Parámetro 3 de 6", "Turbiedad",
       "¿Qué tan difícil es ver a través del agua?",
       bloque("que-es", f"""<div class="duo">
          <div>
            {parrafo("Para empezar, la turbiedad indica qué tan difícil es ver a través del agua. "
                     "Esto ocurre porque el agua lleva partículas muy pequeñas suspendidas, como barro, arcilla o microbios, que desvían la luz. "
                     "Por ejemplo, sucede lo mismo con los faros de un carro en una noche con neblina: las gotitas de la niebla dispersan la luz y el camino se ve borroso. "
                     "Así, a más partículas, mayor turbiedad.", "p1-turbiedad")}
          </div>
          {imagen("turb-niebla.webp", "De noche y con neblina, la luz de los faros de un carro se ve borrosa; Gotita alumbra el camino con una linterna.")}
        </div>""", "¿Qué es la turbiedad?")
       + bloque("comparar", f"""<div class="duo">
          {imagen("turb-luz.webp", "Dos botellas de agua: la de la izquierda es transparente y la de la derecha se ve lechosa por las partículas que flotan.",
                  "A la izquierda, agua clara; a la derecha, agua turbia. Las partículas desvían la luz y la botella se ve lechosa. En Colombia, la unidad NTU también se escribe UNT.")}
          <div>
            {parrafo("Por eso, la turbiedad se mide con un turbidímetro, un aparato que ilumina la muestra y detecta cuánta luz sale desviada hacia un lado por las partículas. "
                     "Su resultado se expresa en unidades nefelométricas de turbiedad, o NTU. "
                     "Además, antes de medir, el equipo se ajusta con agua sin partículas, que marca 0 NTU, y con líquidos de turbiedad conocida, preparados con una sustancia llamada formazina.", "p2-turbidimetro")}
          </div>
        </div>""", "El turbidímetro")
       + bloque("pasos", f"""<div class="duo" style="align-items:start">
          {imagen("turbidimetro.webp", "Gotita coloca un frasco pequeño con agua ligeramente turbia dentro del pozo de un turbidímetro.")}
          {flujo([
              ("Encender", "Esperar de 5 a 10 minutos a que el equipo se estabilice."),
              ("Calibrar", "Con agua de 0 NTU y con estándares de formazina."),
              ("Preparar", "Agitar la muestra suavemente, sin hacer burbujas."),
              ("Medir", "Llenar la cubeta, limpiarla por fuera y leer el valor en NTU."),
          ]).replace('class="flujo"', 'class="flujo" style="grid-auto-flow:row;gap:30px"')}
        </div>
        <div class="descubrir" style="margin-top:24px">
          {descubrir("dato-burbujas", "¿Por qué sin burbujas?", "De hecho, las burbujas también desvían la luz, así que el aparato las contaría como si fueran partículas. Por eso, si se forman, se deja reposar la muestra unos minutos antes de medir.")}
          {descubrir("dato-huellas", "¿Por qué se limpia la cubeta por fuera?", "Además, una huella o una gota en el vidrio desvía la luz igual que una partícula. Así, una cubeta sucia o rayada daría una turbiedad más alta que la real.")}
          {descubrir("dato-diluir", "¿Y si el agua está muy turbia?", "En ese caso, se diluye: por ejemplo, 10 mL de muestra con 90 mL de agua sin partículas. Luego, el resultado se multiplica por 10; así, una lectura de 25 NTU equivale a 250 NTU reales.")}
        </div>""", "Medir paso a paso")
       + bloque("reto", reto("Dos muestras marcan 3 NTU y 40 NTU. ¿Cuál es más turbia?", [
           ("La de 3 NTU.", False, "No del todo. Al contrario, un número menor indica menos partículas."),
           ("La de 40 NTU.", True, "¡Correcto! A más NTU, más partículas desvían la luz."),
       ]) + reto("Una muestra diluida 1:10 marca 12 NTU. ¿Cuál es su turbiedad real?", [
           ("12 NTU", False, "No del todo. Como la muestra se diluyó diez veces, hay que multiplicar por 10."),
           ("1,2 NTU", False, "No del todo. En realidad, al diluir se multiplica, no se divide."),
           ("120 NTU", True, "¡Correcto! 12 × 10 = 120 NTU."),
       ]), "Mini-reto"))

# ---------------------------------------------------------------- alcalinidad y acidez
pagina("alcalinidad-acidez.html", "Alcalinidad y acidez", "Parámetro 4 de 6", "Alcalinidad y acidez",
       "El escudo del agua y los villanos que lo ponen a prueba.",
       bloque("comic", comic_completo("comic-ph-heroe.jpg", "Cómic «El superhéroe pH y los villanos del agua»: el héroe pH mide la fuerza de los H⁺, cuenta a los villanos para conocer la acidez y el escudo de alcalinidad protege al agua.",
                                      "Cómic «El superhéroe pH y los villanos del agua»: el pH mide la fuerza, la acidez cuenta a los villanos y la alcalinidad es el escudo."),
              "Una historia para empezar")
       + bloque("conceptos", f"""<div class="duo" style="align-items:start">
          <div>
            <h2>🛡️ Alcalinidad</h2>
            {parrafo("Para empezar, la alcalinidad es la capacidad del agua para neutralizar ácidos, es decir, para quitarles su fuerza. "
                     "Por ejemplo, funciona como un escudo: cuando llega una lluvia ácida o una descarga ácida, el agua la resiste y su pH cambia poco. "
                     "Esta defensa proviene sobre todo de sales disueltas llamadas bicarbonatos y carbonatos. "
                     "Sin embargo, el escudo tiene un límite y puede agotarse si llega demasiado ácido.", "p1-alcalinidad")}
          </div>
          <div>
            <h2>⚔️ Acidez</h2>
            {parrafo("Por otro lado, la acidez es la capacidad del agua para neutralizar bases, que son las sustancias contrarias a los ácidos, como el jabón. "
                     "Además, una acidez alta suele deberse a mucho dióxido de carbono disuelto, a aguas que salen de minas o a residuos de fábricas. "
                     "Por eso, un agua muy ácida puede corroer, es decir, desgastar las tuberías, y además dañar a los peces.", "p2-acidez")}
          </div>
        </div>
        <div class="descubrir" style="margin-top:24px">
          {descubrir("dato-ph-acidez", "¿El pH y la acidez son lo mismo?", "No exactamente. En realidad, el pH muestra qué tan fuerte es la acidez en ese momento, mientras que la acidez cuenta cuánta sustancia ácida hay en total. Así, en el cómic, el pH mide la fuerza de los villanos y la acidez los cuenta a todos.")}
        </div>""")
       + bloque("titular", f"""<div class="duo">
          {parrafo("Por ejemplo, las dos se miden por titulación: se agrega gota a gota un líquido de concentración conocida hasta que un indicador cambia de color. "
                   "Para la alcalinidad se agrega un ácido y el indicador pasa de amarillo a naranja salmón; para la acidez se agrega una base y la muestra se vuelve rosada tenue. "
                   "Finalmente, con el volumen gastado se calcula el resultado en miligramos de carbonato de calcio por litro (mg CaCO₃/L).", "p3-titulacion")}
          {imagen("alc-bureta.webp", "Una bureta deja caer una gota en un matraz cuyo líquido pasa de amarillo a naranja; Gotita observa con su lupa.")}
        </div>""", "¿Cómo se mide?")
       + bloque("laboratorio", titulacion(8.5, 0.5, 20, "#f5d130", "#f5b041", "#f08a5d",
                   "Sigue amarillo: la alcalinidad todavía resiste el ácido.",
                   "¡Atención! El color empieza a cambiar: agregar más despacio.",
                   "¡Naranja salmón! Se gastaron {v} mL de ácido. Alcalinidad = {v} × 20 = {r} mg CaCO₃/L: el agua tiene un buen escudo.",
                   "Con ácido 0,02 N y 50 mL de muestra, cada mililitro gastado equivale a 20 mg CaCO₃/L. Simulación basada en el ejemplo de la guía de laboratorio.",
                   "Agregar 0,5 mL de ácido"), "Laboratorio virtual: alcalinidad", "Agrega ácido hasta que el indicador cambie de color.")
       + bloque("reto", reto("Llega una descarga ácida a dos ríos con el mismo pH. ¿Cuál cambia menos su pH?", [
           ("El río con mayor alcalinidad.", True, "¡Correcto! Su escudo es más grande y neutraliza más ácido."),
           ("El río con menor alcalinidad.", False, "No del todo. Con poca alcalinidad, el escudo se agota rápido y el pH baja más."),
           ("Los dos cambian igual, porque tienen el mismo pH.", False, "No del todo. Aunque el pH sea igual, la alcalinidad puede ser distinta."),
       ]), "Mini-reto"))

# ---------------------------------------------------------------- dureza
pagina("dureza.html", "Dureza del agua", "Parámetro 5 de 6", "Dureza del agua",
       "Calcio, magnesio, espuma y sarro.",
       bloque("que-es", f"""{parrafo("Para empezar, la dureza indica cuánto calcio y magnesio hay disueltos en el agua. "
                   "Estos minerales llegan cuando el agua atraviesa rocas como la caliza. "
                   "Por ejemplo, un agua dura deja una costra blanca, llamada sarro, dentro de ollas, duchas y tuberías. "
                   "Además, con ella el jabón hace poca espuma, por lo que se gasta más. "
                   "Sin embargo, el agua dura no suele causar daño a la salud.", "p1-dureza")}
        <div class="duo" style="margin-top:24px">
          {imagen("dureza-sarro.webp", "Corte de una tubería con una costra blanca y dura en su interior, junto a una regadera con los orificios tapados de sarro.", "El sarro estrecha las tuberías y tapa las regaderas.")}
          {imagen("dureza-jabon.webp", "Dos lavamanos: en uno el jabón hace mucha espuma; en el otro casi no hace espuma y deja una capa gris.", "Con agua blanda hay mucha espuma; con agua dura, poca.")}
        </div>""", "¿Qué es la dureza?")
       + bloque("comic", comic_completo("comic-dureza-viaje.jpg", "Cómic «El viaje microscópico por el río»: Sara y Gotita conocen a los pasajeros calcio y magnesio, miden la dureza total con EDTA, separan el magnesio para medir la dureza cálcica y calculan la magnésica con una resta.",
                                        "Cómic «El viaje microscópico por el río»: dureza total, cálcica y magnésica."),
              "Un viaje para entender los tres tipos")
       + bloque("tipos", f"""{parrafo("Además, la dureza se divide en tres tipos. "
                   "La dureza total suma el calcio y el magnesio juntos. "
                   "En cambio, la dureza cálcica cuenta solo el calcio; para medirla, se sube mucho el pH, de modo que el magnesio se separa y no participa. "
                   "Finalmente, la dureza magnésica no se mide directamente, sino que se calcula con una resta: dureza total menos dureza cálcica.", "p2-tipos")}
        <div class="tarjetas" style="margin-top:24px">
          <button class="tarjeta" type="button" aria-pressed="false">
            <span class="tarjeta-interior">
              <span class="cara frente"><span class="icono" aria-hidden="true">🧺</span><strong>Dureza total</strong><small>calcio + magnesio</small></span>
              <span class="cara reverso">Por ejemplo, se mide con EDTA a pH 10 y el indicador cambia de rojo vino a azul.</span>
            </span>
          </button>
          <button class="tarjeta" type="button" aria-pressed="false">
            <span class="tarjeta-interior">
              <span class="cara frente"><span class="icono" aria-hidden="true">🥚</span><strong>Dureza cálcica</strong><small>solo calcio</small></span>
              <span class="cara reverso">En cambio, se mide a pH muy alto, con otro indicador llamado murexida, para que el magnesio no participe.</span>
            </span>
          </button>
          <button class="tarjeta" type="button" aria-pressed="false">
            <span class="tarjeta-interior">
              <span class="cara frente"><span class="icono" aria-hidden="true">➖</span><strong>Dureza magnésica</strong><small>total − cálcica</small></span>
              <span class="cara reverso">Así, no necesita otra prueba: basta con restar la dureza cálcica a la dureza total.</span>
            </span>
          </button>
        </div>""", "Total, cálcica y magnésica")
       + bloque("titular", f"""{parrafo("Por ejemplo, la dureza total se mide por titulación con EDTA, una sustancia que atrapa al calcio y al magnesio como una red. "
                   "Antes, se agrega un indicador llamado negro de eriocromo T, que tiñe la muestra de rojo vino mientras hay minerales libres. "
                   "Luego, cuando el EDTA ya atrapó todos los minerales, el color cambia a azul. "
                   "Así, con el volumen gastado se calcula la dureza en mg CaCO₃/L.", "p3-edta")}
        <div style="margin-top:24px">
        {titulacion(12, 1, 20, "#8e1b3a", "#6a3d9a", "#2a6fdb",
                    "Sigue rojo vino: todavía hay calcio y magnesio libres.",
                    "¡Morado! Falta poco: agregar gota a gota.",
                    "¡Azul puro! Se gastaron {v} mL de EDTA. Dureza total = {v} × 20 = {r} mg CaCO₃/L: es un agua dura.",
                    "Con EDTA 0,01 M y 50 mL de muestra, cada mililitro gastado equivale a unos 20 mg CaCO₃/L. Simulación basada en el ejemplo de la guía de laboratorio.",
                    "Agregar 1 mL de EDTA")}
        </div>""", "Laboratorio virtual: dureza total", "Agrega EDTA hasta que el color cambie a azul.")
       + bloque("clases", """<div class="barra-clases">
          <div><strong>Blanda</strong>0 a 75</div>
          <div><strong>Moderadamente dura</strong>75 a 150</div>
          <div><strong>Dura</strong>150 a 300</div>
          <div><strong>Muy dura</strong>más de 300</div>
        </div>
        <p class="instruccion" style="margin-top:14px">Valores en mg CaCO₃/L. En Colombia, el agua para beber puede tener como máximo 300 mg CaCO₃/L (Resolución 2115 de 2007).</p>""",
              "¿Qué tan dura es?")
       + bloque("reto", reto("Un agua tiene dureza total de 240 mg CaCO₃/L y dureza cálcica de 160. ¿Cuál es su dureza magnésica?", [
           ("80 mg CaCO₃/L", True, "¡Correcto! 240 − 160 = 80."),
           ("400 mg CaCO₃/L", False, "No del todo. La magnésica se obtiene restando, no sumando."),
           ("160 mg CaCO₃/L", False, "No del todo. Ese es el valor del calcio; falta restarlo de la dureza total."),
       ]) + reto("¿Por qué con agua dura se gasta más jabón?", [
           ("Porque el calcio y el magnesio impiden que el jabón haga espuma.", True, "¡Correcto! Esos minerales reaccionan con el jabón y forman una capa gris en lugar de espuma."),
           ("Porque el agua dura está más sucia.", False, "No del todo. En realidad, un agua dura puede verse muy limpia; lo que tiene son minerales disueltos."),
       ]), "Mini-reto"))

# ---------------------------------------------------------------- sólidos
pagina("solidos.html", "Sólidos en el agua", "Parámetro 6 de 6", "Sólidos totales y volátiles",
       "Lo que queda cuando el agua se va.",
       bloque("que-son", f"""<div class="duo">
          <div>
            {parrafo("Para empezar, los sólidos son todo lo que queda cuando al agua se le quita el agua misma. "
                     "Por ejemplo, si una olla con agua hierve hasta secarse, en el fondo aparece una costra: esos son los sólidos. "
                     "Algunos estaban disueltos, como la sal, y otros flotaban, como el barro. "
                     "Además, se miden en miligramos por litro, es decir, cuántos miligramos de residuo deja cada litro de agua.", "p1-solidos")}
          </div>
          {imagen("solidos-sopa.webp", "Una olla vacía y seca sobre la estufa, con una costra blanca y cuarteada en el fondo.")}
        </div>""", "¿Qué son los sólidos?")
       + bloque("totales", f"""<div class="duo">
          {imagen("solidos-horno.webp", "Gotita saca con pinzas una cápsula de porcelana de un horno de secado del laboratorio.")}
          <div>
            {parrafo("Por otra parte, en el laboratorio los sólidos totales se miden en un recipiente de porcelana llamado cápsula. "
                     "Primero, se pesa la cápsula vacía; después, se le agrega un volumen conocido de muestra y se seca en un horno a unos 105 °C hasta que el agua se evapora. "
                     "Finalmente, se pesa otra vez: la diferencia de peso corresponde a los sólidos totales.", "p2-totales")}
          </div>
        </div>""", "Sólidos totales")
       + bloque("volatiles", f"""<div class="duo">
          <div>
            {parrafo("Luego, esa misma cápsula se calienta en un horno mucho más caliente, llamado mufla, a unos 550 °C. "
                     "A esa temperatura, la materia orgánica, como restos de hojas o microbios, se quema y desaparece; por eso, a esa parte se le llama sólidos volátiles. "
                     "En cambio, lo que resiste, como la arena y los minerales, queda como ceniza y se llama sólidos fijos. "
                     "Así, se parece a una fogata: la leña se quema, pero la ceniza queda.", "p3-volatiles")}
          </div>
          {imagen("solidos-mufla.webp", "Una mufla encendida de color naranja y, sobre la mesa, una cápsula con un poco de ceniza gris; Gotita observa con un guante protector.")}
        </div>""", "Sólidos volátiles y fijos")
       + bloque("pasos", flujo([
           ("Pesar", "La cápsula vacía."),
           ("Secar a 105 °C", "Con la muestra, hasta que el agua se evapore."),
           ("Pesar", "El aumento de peso son los sólidos totales."),
           ("Calcinar a 550 °C", "En la mufla se quema la materia orgánica."),
           ("Pesar", "Lo que se perdió son los sólidos volátiles."),
       ]) + f"""
        <div class="descubrir" style="margin-top:24px">
          {descubrir("dato-calculo", "¿Cómo se pasa a mg/L?", "Por ejemplo, si 100 mL de muestra dejan 25 mg de residuo, un litro, que es diez veces más, dejaría 250 mg. Así, los sólidos totales serían 250 mg/L.")}
          {descubrir("dato-volatiles", "¿Por qué importan los volátiles?", "De hecho, los sólidos volátiles indican cuánta materia orgánica lleva el agua. Por eso, son muy altos en las aguas residuales, que llevan restos de comida y otros desechos.")}
        </div>""", "Del horno a la mufla, paso a paso")
       + bloque("reto", reto("Después de la mufla, la cápsula pesa menos que antes. ¿Qué se perdió?", [
           ("El agua de la muestra.", False, "No del todo. El agua ya se había evaporado en el horno a 105 °C."),
           ("La materia orgánica, es decir, los sólidos volátiles.", True, "¡Correcto! A 550 °C, la materia orgánica se quema y se va como gas."),
           ("La arena y los minerales.", False, "No del todo. Al contrario, esos resisten el calor y quedan como ceniza: son los sólidos fijos."),
       ]), "Mini-reto"))
