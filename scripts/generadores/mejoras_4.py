"""Mejoras de la sección 4. Se ejecuta DESPUÉS de gen_sec4.py (que regenera las páginas base)."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from componentes import lab, paso, calc, ejemplo, tabla, comparacion, flujo
from comic_curva import COMIC_CURVA

DIR = Path("C:/Users/majur/Downloads/MQAT/Enciclopedia/secciones/04-parametros")
AUD = "../../assets/audio/04-parametros/"

def parrafo(texto, audio):
    return f"""<div class="parrafo">
            <p>{texto}</p>
            <button class="btn-audio" type="button" data-audio="{AUD}{audio}.mp3" hidden>🔊 Escuchar</button>
          </div>"""

def bloque(ident, titulo, contenido, instruccion=""):
    ins = f'<p class="instruccion">{instruccion}</p>\n        ' if instruccion else ""
    return f"""
    <section class="bloque" id="{ident}">
      <div class="contenedor">
        <h2>{titulo}</h2>
        {ins}{contenido}
      </div>
    </section>
"""

def reto(pregunta, opciones):
    botones = "\n".join(
        f'            <button class="opcion" type="button" data-correcta="{"true" if ok else "false"}" data-retro="{r}">{t}</button>'
        for t, ok, r in opciones)
    return f"""<div class="reto">
          <p class="pregunta">{pregunta}</p>
          <div class="opciones">
{botones}
          </div>
          <p class="retro" aria-live="polite"></p>
        </div>"""

def seccion_reto(retos):
    return bloque("reto", "Mini-reto", "\n        ".join(retos), "Todas las respuestas se encuentran en esta página.")

def editar(archivo, antes_de=None, reemplazar=None, nuevo=""):
    p = DIR / archivo
    s = p.read_text(encoding="utf-8")
    if reemplazar:
        s2, n = re.subn(reemplazar, lambda m: nuevo, s, count=1, flags=re.S)
        if n != 1:
            raise SystemExit(f"{archivo}: no se encontró {reemplazar[:60]}")
        s = s2
    else:
        marca = f'    <section class="bloque" id="{antes_de}">'
        if marca not in s:
            raise SystemExit(f"{archivo}: no existe la sección {antes_de}")
        s = s.replace(marca, nuevo.rstrip("\n") + "\n\n" + marca, 1)
    p.write_text(s, encoding="utf-8")

SECCION = lambda ident: rf'\n    <section class="bloque" id="{ident}">.*?</section>\n'
enjuagar = lambda t="Enjuagar": paso("Enjuagar el electrodo", "Se enjuaga el electrodo con agua destilada de la piseta y se seca con toques suaves de papel, sin frotar.", t, vaso=["Agua destilada"], liquido="#eef9fd", pantalla="—")

# ============================================================ pH y conductividad
TRES = comparacion([
    ("🧪", "pH", {"Pregunta que responde": "¿Qué tan ácida o básica está el agua en este momento?",
                  "Cómo se mide": "Lectura directa con pHmetro.",
                  "Unidad": "Ninguna: escala de 0 a 14.",
                  "Ejemplo": "Agua de la llave: pH 7,4.",
                  "En el cómic": "La fuerza de los villanos."}),
    ("⚔️", "Acidez", {"Pregunta que responde": "¿Cuánta sustancia ácida hay en total?",
                     "Cómo se mide": "Titulación con NaOH 0,02 N y fenolftaleína.",
                     "Unidad": "mg CaCO₃/L",
                     "Ejemplo": "50 mg CaCO₃/L.",
                     "En el cómic": "Contar a todos los villanos."}),
    ("🛡️", "Alcalinidad", {"Pregunta que responde": "¿Cuánto ácido puede resistir el agua sin que su pH se desplome?",
                          "Cómo se mide": "Titulación con HCl 0,02 N, fenolftaleína y anaranjado de metilo.",
                          "Unidad": "mg CaCO₃/L",
                          "Ejemplo": "168 mg CaCO₃/L.",
                          "En el cómic": "El tamaño del escudo."}),
])
editar("ph-conductividad.html", antes_de="medir-ph", nuevo=bloque("tres-preguntas", "pH, acidez y alcalinidad: tres preguntas distintas",
    parrafo("Además, pH, acidez y alcalinidad suelen confundirse, pero cada uno responde una pregunta distinta. "
            "Por ejemplo, en un partido de fútbol, el pH sería qué tan fuerte ataca el equipo contrario en este momento; la acidez, cuántos jugadores atacantes tiene en total; "
            "y la alcalinidad, qué tan grande es la defensa propia. Así, dos aguas pueden tener el mismo pH y, sin embargo, una puede resistir mucho más ácido que la otra.", "p1b-tres-preguntas")
    + f'\n        <div style="margin-top:24px">{TRES}</div>\n        <div style="margin-top:24px">'
    + ejemplo("mismo pH, distinta defensa",
              "Dos aguas tienen pH 7,0. El agua A tiene alcalinidad de 20 mg CaCO₃/L y el agua B, de 200 mg CaCO₃/L. A las dos les llega la misma cantidad de ácido.",
              ["El escudo de B es <span class='cuenta'>200 ÷ 20 = 10 veces</span> más grande que el de A.",
               "El agua A gasta rápido su escudo y su pH puede caer varios puntos, por ejemplo hasta cerca de 5.",
               "El agua B neutraliza el ácido y su pH casi no cambia."],
              "Por eso, el pH solo no basta: también hay que medir la alcalinidad y la acidez.") + "</div>"))

CALC_PH = """<div class="calc-ph">
          <label for="ph-ceros" style="font-weight:800;display:block">Elige un pH y mira cuántos iones H⁺ hay en un litro</label>
          <input id="ph-ceros" type="range" min="0" max="14" step="1" value="7">
          <p style="margin:12px 0 4px">pH <strong class="ph-valor" style="font-size:1.6rem">7</strong> → [H⁺] = <span class="h-decimal"></span> mol/L</p>
          <p class="ph-ceros" style="margin:0;font-weight:700"></p>
          <p class="ph-comparar" style="margin:4px 0 0"></p>
        </div>"""
editar("ph-conductividad.html", antes_de="medir-ph", nuevo=bloque("calcular-ph", "¿Cómo se calcula el pH?",
    parrafo("Por otra parte, el pH se calcula a partir de la cantidad de iones hidrógeno (H⁺), que son las partículas que hacen ácida al agua. "
            "Esa cantidad se escribe en moles por litro, una forma de contar partículas, y es un número decimal muy pequeño: en el agua neutra es 0,0000001. "
            "Entonces, el pH es la posición donde aparece el 1 después de la coma; en ese ejemplo es la séptima, así que el pH es 7.", "p1c-calcular-ph")
    + f"\n        <div style=\"margin-top:24px\">{CALC_PH}</div>\n        <div class=\"duo\" style=\"margin-top:24px;align-items:start\">"
    + ejemplo("la fórmula exacta",
              "Cuando el número no es exacto, se usa la fórmula pH = −log[H⁺], donde log es una tecla de la calculadora científica.",
              ["[H⁺] = 0,001 mol/L es lo mismo que 10⁻³.",
               "pH = −log(10⁻³) = −(−3) = <span class='cuenta'>3</span>.",
               "Si [H⁺] = 0,00004 mol/L: pH = −log(0,00004) ≈ <span class='cuenta'>4,4</span>."])
    + calc("calc-ph", "De [H⁺] a pH", [("H", "Concentración de iones H⁺", "mol/L", 0.00004, "any")],
           ["pH = −log[H⁺]", "pH = −log({H})", "pH = {=-Math.log10(H)}"], "-Math.log10(H)", "pH", "", 2,
           [(6.4999, "Es un agua ácida: queda por debajo del rango de 6,5 a 9,0 para beber."),
            (9.0, "Está dentro del rango de 6,5 a 9,0 de la Resolución 2115."),
            (None, "Es un agua básica: queda por encima del rango de 6,5 a 9,0 para beber.")])
    + "</div>"))

LAB_PH = lab("lab-ph", "medidor", "pHmetro", [
    paso("Encender", "Se enciende el pHmetro y se espera a que se estabilice.", "Encender", pantalla="---", vaso=["Vaso vacío"], liquido="#ffffff"),
    enjuagar(),
    paso("Calibrar con buffer 7", "Se sumerge el electrodo en el buffer de pH 7,00, un líquido de pH conocido, y se oprime «Calibrar».", "Calibrar con pH 7,00",
         vaso=["Buffer pH 7,00"], liquido="#f7e46b", animar={"de": 6.2, "a": 7.0, "decimales": 2}, registro=["Calibración 1", "Buffer pH 7,00 ✔"]),
    enjuagar(),
    paso("Calibrar con buffer 4", "Luego, se usa el buffer de pH 4,00. Con dos puntos conocidos, el equipo traza su propia regla, como una recta entre dos marcas.", "Calibrar con pH 4,00",
         vaso=["Buffer pH 4,00"], liquido="#f08a7a", animar={"de": 6.9, "a": 4.0, "decimales": 2}, registro=["Calibración 2", "Buffer pH 4,00 ✔ (pendiente 98 %)"]),
    enjuagar(),
    paso("Medir la muestra", "Se sumerge unos 3 cm del electrodo en la muestra, sin tocar el fondo, y se espera hasta que el número deje de moverse.", "Sumergir en la muestra",
         vaso=["Muestra M1", "agua de la llave"], liquido="#d6f0fa", animar={"de": 5.6, "a": 7.4, "decimales": 1}),
    paso("Anotar", "Se anota el valor con un decimal y se compara con la norma.", "Anotar el resultado",
         registro=["pH de M1", "7,4"], resultado="El pH de M1 es <strong>7,4</strong>. Como está entre 6,5 y 9,0, cumple el rango de la Resolución 2115 de 2007 para agua de consumo."),
], "Práctica terminada. Al final, el electrodo se enjuaga y se guarda en su solución de almacenamiento, nunca seco.", unidad="unidades de pH", vaso=["Vaso vacío"])

LAB_COND = lab("lab-cond", "medidor", "Conductímetro", [
    paso("Encender", "Se enciende el conductímetro y se espera a que se estabilice.", "Encender", pantalla="---", vaso=["Vaso vacío"], liquido="#ffffff"),
    paso("Revisar el agua destilada", "Se enjuaga la celda con agua destilada; su lectura debe ser menor a 5 µS/cm, señal de que está limpia.", "Medir agua destilada",
         vaso=["Agua destilada"], liquido="#eef9fd", animar={"de": 0, "a": 2, "decimales": 0}, registro=["Agua destilada", "2 µS/cm ✔ (menor a 5)"]),
    paso("Calibrar", "Se mide el patrón de cloruro de potasio 0,01 M, que a 25 °C tiene 1413 µS/cm, y se ajusta el equipo a ese valor.", "Calibrar con el patrón",
         vaso=["Patrón KCl 0,01 M", "1413 µS/cm"], liquido="#e3e8ff", animar={"de": 1300, "a": 1413, "decimales": 0}, registro=["Calibración", "1413 µS/cm ✔"]),
    paso("Medir M1", "Se enjuaga la celda y se mide el agua de la llave.", "Medir M1",
         vaso=["M1: agua de la llave"], liquido="#d6f0fa", animar={"de": 0, "a": 210, "decimales": 0}, registro=["M1: agua de la llave", "210 µS/cm"]),
    paso("Medir M2", "Se enjuaga otra vez y se mide el agua de la quebrada.", "Medir M2",
         vaso=["M2: agua de quebrada"], liquido="#e2f3e6", animar={"de": 0, "a": 85, "decimales": 0}, registro=["M2: agua de quebrada", "85 µS/cm"]),
    paso("Comparar", "Se restan los dos valores y se interpretan.", "Comparar resultados",
         resultado="Diferencia: 210 − 85 = <strong>125 µS/cm</strong>. El agua de la llave lleva más sales disueltas. Las dos están muy por debajo del máximo de 1000 µS/cm de la Resolución 2115."),
], "Práctica terminada: la celda se enjuaga y se guarda limpia.", unidad="µS/cm", vaso=["Vaso vacío"])

editar("ph-conductividad.html", antes_de="conductividad", nuevo=bloque("laboratorio-ph", "Laboratorio virtual: medir el pH",
    LAB_PH, "Sigue los pasos en orden con el botón azul; cada dato queda en el cuaderno de laboratorio."))
editar("ph-conductividad.html", antes_de="reto", nuevo=bloque("laboratorio-cond", "Laboratorio virtual: medir la conductividad", LAB_COND))
editar("ph-conductividad.html", reemplazar=SECCION("reto"), nuevo="\n" + seccion_reto([
    reto("La Resolución 2115 exige un pH entre 6,5 y 9,0 para el agua de beber. Una muestra marca 5,5. ¿Cumple?", [
        ("Sí, porque está cerca de 7.", False, "No del todo. Aunque parece cercano, 5,5 queda por debajo del mínimo de 6,5."),
        ("No, porque está por debajo del mínimo de 6,5.", True, "¡Correcto! Es más ácida de lo permitido."),
        ("Sí, porque está entre 0 y 14.", False, "No del todo. Todas las aguas están entre 0 y 14; la norma pide el rango de 6,5 a 9,0.")]),
    reto("Según el calculador de esta página, ¿cuántas veces más iones H⁺ tiene un agua de pH 5 que una de pH 7?", [
        ("2 veces", False, "No del todo. Cada punto multiplica por 10, así que son dos multiplicaciones: 10 × 10."),
        ("100 veces", True, "¡Correcto! Son dos puntos de diferencia: 10 × 10 = 100."),
        ("20 veces", False, "No del todo. Los puntos de pH multiplican, no suman: 10 × 10 = 100.")]),
    reto("Dos aguas tienen pH 7,0; la A tiene alcalinidad de 20 mg CaCO₃/L y la B, de 200. Les llega el mismo ácido. ¿Cuál cambia menos su pH?", [
        ("La A.", False, "No del todo. Su escudo es diez veces más pequeño y se agota rápido."),
        ("La B.", True, "¡Correcto! Su alcalinidad, es decir, su escudo, es diez veces mayor."),
        ("Las dos igual, porque tienen el mismo pH.", False, "No del todo. El mismo pH no significa la misma defensa.")]),
    reto("En el laboratorio virtual, M1 marcó 210 µS/cm y M2, 85 µS/cm. ¿Cuál lleva más sales disueltas?", [
        ("M1, el agua de la llave.", True, "¡Correcto! A mayor conductividad, más iones."),
        ("M2, el agua de quebrada.", False, "No del todo. Un número menor indica menos sales.")]),
]))

# ============================================================ Color
editar("color.html", antes_de="pasos", nuevo=bloque("comic-curva", "La curva de calibración, contada como cuento", COMIC_CURVA, "Mira las viñetas en orden."))
editar("color.html", antes_de="interpolar", nuevo=bloque("datos-curva", "La curva con datos reales de laboratorio",
    tabla(["Estándar", "Color (UC)", "Absorbancia a 455 nm"],
          [["Blanco (agua destilada)", "0", "0,000"], ["2 mL de madre en 100 mL", "10", "0,010"], ["4 mL", "20", "0,020"],
           ["6 mL", "30", "0,030"], ["8 mL", "40", "0,040"], ["10 mL", "50", "0,050"]],
          "Datos del ejemplo de la guía de laboratorio N.° 2 (estándares preparados con una solución madre de 500 UC).")
    + '\n        <div style="margin-top:24px">'
    + ejemplo("de la tabla al resultado",
              "Con esos datos se calcula la pendiente de la recta, es decir, cuánta absorbancia aporta cada unidad de color.",
              ["Pendiente = (0,050 − 0,000) ÷ (50 − 0) = <span class='cuenta'>0,0010 por UC</span>.",
               "Ecuación de la recta: Absorbancia = 0,0010 × Color. Despejando: Color = Absorbancia ÷ 0,0010.",
               "Muestra con absorbancia 0,027: <span class='cuenta'>0,027 ÷ 0,0010 = 27 UC</span>.",
               "Muestra con absorbancia 0,068: supera 0,050, así que está fuera de la curva. Se diluye a la mitad (25 mL de muestra en 50 mL) y da 0,031.",
               "Color de la muestra diluida: <span class='cuenta'>0,031 ÷ 0,0010 = 31 UC</span>; color original: <span class='cuenta'>31 × 2 = 62 UC</span>."])
    + "</div>"))

LAB_COLOR = lab("lab-color", "caja", "Espectrofotómetro · 455 nm", [
    paso("Encender", "Se enciende el espectrofotómetro y se espera 10 minutos a que la lámpara se estabilice.", "Encender", pantalla="---"),
    paso("Elegir la luz", "Se ajusta la longitud de onda en 455 nm, el tono de luz que más absorbe el color amarillo del agua.", "Ajustar 455 nm", pantalla="455 nm"),
    paso("Hacer el blanco", "Se llena la cubeta con agua destilada y se ajusta el cero: sin color, no hay absorbancia.", "Ajustar el cero",
         vaso=["Blanco:", "agua destilada"], liquido="#f4fbfd", pantalla="0,000", registro=["Blanco", "0,000"]),
    paso("Leer estándares", "Se leen los estándares de 10 a 50 UC, del más claro al más oscuro.", "Leer los estándares",
         vaso=["Estándares", "10 a 50 UC"], liquido="#f1dc7a", animar={"de": 0.01, "a": 0.05, "decimales": 3}, registro=["Estándares", "0,010 · 0,020 · 0,030 · 0,040 · 0,050"]),
    paso("Muestra sin filtrar", "Se lee la muestra tal como llegó, con sus partículas: esa lectura corresponde al color aparente.", "Leer sin filtrar",
         vaso=["M1 sin filtrar"], liquido="#d9c778", animar={"de": 0, "a": 0.041, "decimales": 3}, registro=["M1 sin filtrar (aparente)", "0,041 → 41 UC"]),
    paso("Muestra filtrada", "Se filtra otra porción por una membrana de 0,45 µm para quitar las partículas y se lee: esa lectura corresponde al color real.", "Filtrar y leer",
         vaso=["M1 filtrada", "(0,45 µm)"], liquido="#efe39a", animar={"de": 0, "a": 0.027, "decimales": 3}, registro=["M1 filtrada (real)", "0,027 → 27 UC"]),
    paso("Calcular", "Se divide cada absorbancia entre la pendiente, 0,0010.", "Calcular",
         resultado="Color aparente = 0,041 ÷ 0,0010 = <strong>41 UC</strong>. Color real = 0,027 ÷ 0,0010 = <strong>27 UC</strong>. La diferencia, 14 UC, se debía a las partículas. El color aparente supera el máximo de 15 UC de la Resolución 2115: el agua necesita tratamiento."),
], "Práctica terminada: las cubetas se lavan con agua destilada.", unidad="absorbancia", vaso=["Cubeta vacía"])

editar("color.html", antes_de="reto", nuevo=bloque("calculadora-color", "Calculadora de color",
    calc("calc-color", "De absorbancia a unidades de color",
         [("A", "Absorbancia de la muestra", "", 0.027, 0.001), ("m", "Pendiente de la curva", "por UC", 0.001, 0.0001), ("F", "Factor de dilución (1 si no se diluyó)", "", 1, 1)],
         ["Color = (Absorbancia ÷ pendiente) × factor", "Color = ({A} ÷ {m}) × {F}", "Color = {=A/m} × {F} = {=A/m*F} UC"],
         "A/m*F", "Color", "UC", 0,
         [(15, "Si se midió el color aparente, cumple el máximo de 15 UC de la Resolución 2115."),
          (None, "Si se midió el color aparente, supera el máximo de 15 UC: el agua necesita tratamiento.")]))
    + bloque("laboratorio-color", "Laboratorio virtual: color aparente y color real", LAB_COLOR, "Sigue los pasos con el botón azul."))
editar("color.html", reemplazar=SECCION("reto"), nuevo="\n" + seccion_reto([
    reto("Con la curva de esta página (pendiente 0,0010 por UC), una muestra da absorbancia 0,035. ¿Cuál es su color?", [
        ("3,5 UC", False, "No del todo. Se divide entre la pendiente: 0,035 ÷ 0,0010 = 35."),
        ("35 UC", True, "¡Correcto! Además, cae dentro de la curva, entre 30 y 40 UC."),
        ("350 UC", False, "No del todo. Esa cifra quedaría muy fuera de la curva, que llega hasta 50.")]),
    reto("En el laboratorio virtual, ¿qué lectura corresponde al color real?", [
        ("La de la muestra sin filtrar.", False, "No del todo. Esa incluye partículas: es el color aparente."),
        ("La de la muestra filtrada por 0,45 µm.", True, "¡Correcto! Sin partículas, solo queda el color de lo disuelto.")]),
]))

# ============================================================ Turbiedad
LAB_TURB = lab("lab-turb", "caja", "Turbidímetro", [
    paso("Encender", "Se enciende el turbidímetro y se espera de 5 a 10 minutos.", "Encender", pantalla="---"),
    paso("Ajustar el cero", "Se inserta una cubeta con agua de turbiedad cero (menos de 0,02 NTU) y se oprime «Zero».", "Ajustar el cero",
         vaso=["Agua de", "turbiedad cero"], liquido="#f4fbfd", pantalla="0,00"),
    paso("Calibrar", "Se inserta el estándar de formazina de 20 NTU y se confirma su valor.", "Calibrar con 20 NTU",
         vaso=["Formazina", "20 NTU"], liquido="#eef0f0", animar={"de": 0, "a": 20, "decimales": 1}, registro=["Calibración", "Formazina 20 NTU ✔"]),
    paso("Verificar", "Se mide un estándar de 10 NTU que no se usó para calibrar: debe leer dentro de ±5 %, es decir, entre 9,5 y 10,5.", "Verificar con 10 NTU",
         vaso=["Formazina", "10 NTU"], liquido="#f1f3f3", animar={"de": 0, "a": 10.2, "decimales": 1}, registro=["Verificación", "10,2 NTU ✔ (±5 %)"]),
    paso("Preparar M1", "Se agita suavemente la muestra, sin hacer burbujas; se llena la cubeta, se seca por fuera y se alinea en el equipo.", "Insertar M1",
         vaso=["M1: agua", "de la llave"], liquido="#e6f1f3"),
    paso("Leer M1", "Se espera de 10 a 30 segundos a que la lectura se estabilice.", "Leer M1",
         animar={"de": 0, "a": 3.8, "decimales": 1}, registro=["M1: agua de la llave", "3,8 NTU"]),
    paso("Diluir M2", "M2 es agua de río muy turbia: se diluye 1:10 (10 mL de muestra en 100 mL de agua de turbiedad cero) y se lee.", "Leer M2 diluida",
         vaso=["M2 diluida 1:10"], liquido="#d8cdb8", animar={"de": 0, "a": 25, "decimales": 1}, registro=["M2 diluida 1:10", "25 NTU → 250 NTU"]),
    paso("Interpretar", "Se comparan los resultados con el máximo de 2 NTU de la Resolución 2115.", "Interpretar",
         resultado="M1 = <strong>3,8 NTU</strong>: supera el máximo de 2 NTU, así que no cumple. M2 = 25 × 10 = <strong>250 NTU</strong>: es agua cruda de río que necesita tratamiento completo."),
], "Práctica terminada: las cubetas se lavan y se secan con un paño suave.", unidad="NTU", vaso=["Cubeta vacía"])
editar("turbiedad.html", antes_de="reto", nuevo=bloque("laboratorio-turb", "Laboratorio virtual: el turbidímetro", LAB_TURB, "Sigue los pasos con el botón azul.")
    + bloque("calculadora-turb", "Calculadora de dilución",
             calc("calc-turb", "Turbiedad de una muestra diluida",
                  [("L", "Lectura de la dilución", "NTU", 25, 0.1), ("Vm", "Volumen de muestra", "mL", 10, 1), ("Vt", "Volumen total de la dilución", "mL", 100, 1)],
                  ["Factor de dilución = volumen total ÷ volumen de muestra = {Vt} ÷ {Vm} = {=Vt/Vm}", "Turbiedad = lectura × factor", "Turbiedad = {L} × {=Vt/Vm} = {=L*Vt/Vm} NTU"],
                  "L*Vt/Vm", "Turbiedad de la muestra original", "NTU", 1,
                  [(2, "Cumple el máximo de 2 NTU de la Resolución 2115 para agua de consumo."), (None, "Supera el máximo de 2 NTU para agua de consumo.")])))
editar("turbiedad.html", reemplazar=SECCION("reto"), nuevo="\n" + seccion_reto([
    reto("Dos muestras marcan 3 NTU y 40 NTU. ¿Cuál es más turbia?", [
        ("La de 3 NTU.", False, "No del todo. Un número menor indica menos partículas."),
        ("La de 40 NTU.", True, "¡Correcto! A más NTU, más partículas desvían la luz.")]),
    reto("Una muestra diluida 1:10 marca 12 NTU. ¿Cuál es su turbiedad real?", [
        ("12 NTU", False, "No del todo. Como se diluyó diez veces, se multiplica por 10."),
        ("1,2 NTU", False, "No del todo. Al diluir se multiplica, no se divide."),
        ("120 NTU", True, "¡Correcto! 12 × 10 = 120 NTU.")]),
    reto("En el laboratorio virtual, M1 marcó 3,8 NTU. Si el máximo es 2 NTU, ¿cumple?", [
        ("Sí.", False, "No del todo. 3,8 es mayor que 2."),
        ("No.", True, "¡Correcto! Supera el máximo de la Resolución 2115.")]),
]))

# ============================================================ Alcalinidad y acidez
LAB_ALC = lab("lab-alc", "titulacion", "Titulación de alcalinidad", [
    paso("Llenar la bureta", "Se enjuaga la bureta con un poco de HCl 0,02 N, se llena y se enrasa en 0,00 mL, leyendo la parte baja de la curva del líquido.", "Llenar y enrasar", volumen=0),
    paso("Medir la muestra", "Con una pipeta volumétrica se miden 50,0 mL de muestra y se vierten en el erlenmeyer.", "Medir 50 mL",
         vaso=["Erlenmeyer:", "50,0 mL de muestra"], liquido="#eef6fa", registro=["Volumen de muestra (Vm)", "50,0 mL"]),
    paso("Fenolftaleína", "Se agregan 3 gotas de fenolftaleína. Si la muestra se pusiera rosada, habría alcalinidad fuerte; aquí sigue incolora, así que su pH es menor de 8,3.", "Agregar fenolftaleína",
         vaso=["50,0 mL de muestra", "+ fenolftaleína"], registro=["Con fenolftaleína", "Incolora: alcalinidad P = 0"]),
    paso("Anaranjado de metilo", "Se agregan 3 gotas de anaranjado de metilo: la muestra se vuelve amarilla.", "Agregar anaranjado de metilo",
         vaso=["50,0 mL de muestra", "+ fenolftaleína", "+ anaranjado de metilo"], liquido="#f5d130"),
    paso("Titular", "Se abre la llave y se deja caer el HCl gota a gota, agitando, hasta que el color cambie de amarillo a naranja salmón (pH 4,5).", "Titular con HCl",
         titular={"hasta": 8.4, "colorCerca": "#f5b041", "colorFinal": "#f08a5d"}),
    paso("Leer la bureta", "Se lee el volumen gastado con un decimal, a la altura de los ojos.", "Leer el volumen", registro=["HCl gastado (V)", "8,4 mL"]),
    paso("Calcular", "Se aplica la fórmula de la guía.", "Calcular",
         resultado="Alcalinidad total = (V × N × 50 000) ÷ Vm = (8,4 × 0,02 × 50 000) ÷ 50 = <strong>168 mg CaCO₃/L</strong>. Es una alcalinidad media: el agua resiste bien una descarga ácida y cumple el máximo de 200 mg CaCO₃/L de la Resolución 2115."),
], "Práctica terminada: la bureta se vacía y se enjuaga con agua destilada.", titulante="HCl 0,02 N", indicadores=["Fenolftaleína 0,5 %", "Anaranjado de metilo 0,1 %"], vaso=["Erlenmeyer vacío"], liquido="#f3f6f8")

LAB_ACID = lab("lab-acid", "titulacion", "Titulación de acidez", [
    paso("Llenar la bureta", "Se enjuaga la bureta con NaOH 0,02 N, se llena y se enrasa en 0,00 mL.", "Llenar y enrasar", volumen=0),
    paso("Medir la muestra", "Se miden 50,0 mL de muestra con pipeta volumétrica.", "Medir 50 mL",
         vaso=["Erlenmeyer:", "50,0 mL de muestra"], liquido="#eef6fa", registro=["Volumen de muestra (Vm)", "50,0 mL"]),
    paso("Fenolftaleína", "Se agregan 3 gotas de fenolftaleína: la muestra queda incolora.", "Agregar fenolftaleína",
         vaso=["50,0 mL de muestra", "+ fenolftaleína"]),
    paso("Titular", "Se agrega NaOH gota a gota, agitando, hasta que aparezca un rosado tenue que dure 30 segundos.", "Titular con NaOH",
         titular={"hasta": 2.5, "colorCerca": "#fbe3ee", "colorFinal": "#f5b3cf"}),
    paso("Leer la bureta", "Se lee el volumen gastado con un decimal.", "Leer el volumen", registro=["NaOH gastado (V)", "2,5 mL"]),
    paso("Calcular", "Se aplica la misma fórmula, ahora con el volumen de NaOH.", "Calcular",
         resultado="Acidez total = (V × N × 50 000) ÷ Vm = (2,5 × 0,02 × 50 000) ÷ 50 = <strong>50 mg CaCO₃/L</strong>. Es una acidez baja: el agua tiene poca sustancia ácida."),
], "Práctica terminada: la bureta se vacía y se enjuaga.", titulante="NaOH 0,02 N", indicadores=["Fenolftaleína 0,5 %"], vaso=["Erlenmeyer vacío"], liquido="#f3f6f8")

def calc_titulacion(ident, titulo, reactivo, v, etiqueta, reglas):
    return calc(ident, titulo, [("V", f"Volumen de {reactivo} gastado", "mL", v, 0.1), ("N", f"Normalidad del {reactivo}", "N", 0.02, 0.001), ("Vm", "Volumen de muestra", "mL", 50, 1)],
                [f"{etiqueta} = (V × N × 50 000) ÷ Vm", f"{etiqueta} = ({{V}} × {{N}} × 50 000) ÷ {{Vm}}", "= {=V*N*50000} ÷ {Vm}", "= {=V*N*50000/Vm} mg CaCO₃/L",
                 "Nota: 50 000 sale de 50 g de CaCO₃ por equivalente × 1000 mg por gramo."],
                "V*N*50000/Vm", etiqueta, "mg CaCO₃/L", 0, reglas)

editar("alcalinidad-acidez.html", reemplazar=SECCION("laboratorio"), nuevo="\n"
    + bloque("laboratorio-alc", "Laboratorio virtual: alcalinidad", LAB_ALC, "La bureta y el erlenmeyer muestran los reactivos que se usan en cada paso.")
    + bloque("calculadora-alc", "Calculadoras de alcalinidad y acidez",
             '<div class="duo" style="align-items:start">'
             + calc_titulacion("calc-alc", "Alcalinidad total", "HCl", 8.4, "Alcalinidad",
                               [(20, "Alcalinidad baja: el escudo contra los ácidos es débil."), (200, "Cumple el máximo de 200 mg CaCO₃/L de la Resolución 2115."), (None, "Supera el máximo de 200 mg CaCO₃/L de la Resolución 2115.")])
             + calc_titulacion("calc-acid", "Acidez total", "NaOH", 2.5, "Acidez",
                               [(50, "Acidez baja: poca sustancia ácida."), (None, "Acidez alta: puede corroer tuberías y afectar a los peces.")])
             + "</div>")
    + bloque("laboratorio-acid", "Laboratorio virtual: acidez", LAB_ACID))
editar("alcalinidad-acidez.html", reemplazar=SECCION("reto"), nuevo="\n" + seccion_reto([
    reto("Llega la misma descarga ácida a dos ríos con pH 7,0. El río A tiene alcalinidad de 20 mg CaCO₃/L y el B, de 180. ¿Cuál cambia menos su pH?", [
        ("El río A.", False, "No del todo. Su escudo es pequeño y se agota rápido."),
        ("El río B.", True, "¡Correcto! Su alcalinidad, es decir, su escudo, es mucho mayor."),
        ("Los dos cambian igual.", False, "No del todo. El mismo pH no significa la misma alcalinidad.")]),
    reto("En una titulación de alcalinidad se gastaron 5,0 mL de HCl 0,02 N con 50 mL de muestra. ¿Cuál es el resultado?", [
        ("100 mg CaCO₃/L", True, "¡Correcto! (5,0 × 0,02 × 50 000) ÷ 50 = 100."),
        ("5 mg CaCO₃/L", False, "No del todo. Falta aplicar la fórmula: (V × N × 50 000) ÷ Vm."),
        ("1000 mg CaCO₃/L", False, "No del todo. Revisa la división final entre 50 mL.")]),
    reto("¿Qué indicador marca el final de la titulación de acidez?", [
        ("El anaranjado de metilo, al volverse naranja salmón.", False, "No del todo. Ese es el final de la alcalinidad."),
        ("La fenolftaleína, al aparecer un rosado tenue.", True, "¡Correcto! El rosado debe durar 30 segundos.")]),
]))

# ============================================================ Dureza
LAB_DT = lab("lab-dureza", "titulacion", "Dureza total", [
    paso("Llenar la bureta", "Se enjuaga y se llena la bureta con EDTA 0,01 M, y se enrasa en 0,00 mL.", "Llenar y enrasar", volumen=0),
    paso("Medir la muestra", "Se miden 50,0 mL de muestra con pipeta volumétrica.", "Medir 50 mL",
         vaso=["Erlenmeyer:", "50,0 mL de muestra"], liquido="#eef6fa", registro=["Volumen de muestra (Vm)", "50,0 mL"]),
    paso("Buffer pH 10", "Se agregan 2 mL de buffer amoniacal de pH 10, que mantiene el pH donde el EDTA atrapa bien al calcio y al magnesio.", "Agregar buffer",
         vaso=["50,0 mL de muestra", "+ 2 mL buffer pH 10"]),
    paso("Indicador", "Se agregan 3 gotas de negro de eriocromo T: se une a los minerales y tiñe la muestra de rojo vino.", "Agregar indicador",
         vaso=["50,0 mL de muestra", "+ buffer pH 10", "+ negro de eriocromo T"], liquido="#8e1b3a"),
    paso("Titular", "Se agrega EDTA gota a gota, agitando: pasa de rojo vino a morado y, al final, a azul puro que dura 30 segundos.", "Titular con EDTA",
         titular={"hasta": 12.0, "colorCerca": "#6a3d9a", "colorFinal": "#2a6fdb"}),
    paso("Leer la bureta", "Se lee el volumen gastado.", "Leer el volumen", registro=["EDTA gastado (V)", "12,0 mL"]),
    paso("Calcular", "Se aplica la fórmula de la guía.", "Calcular",
         resultado="Dureza total = (V × M × 100 090) ÷ Vm = (12,0 × 0,01 × 100 090) ÷ 50 = <strong>240,2 mg CaCO₃/L</strong>: agua dura. Cumple el máximo de 300 mg CaCO₃/L de la Resolución 2115."),
], "Práctica terminada.", titulante="EDTA 0,01 M", indicadores=["Buffer pH 10 (amoniacal)", "Negro de eriocromo T"], vaso=["Erlenmeyer vacío"], liquido="#f3f6f8")

LAB_DC = lab("lab-calcica", "titulacion", "Dureza cálcica", [
    paso("Llenar la bureta", "Se llena la bureta con EDTA 0,01 M y se enrasa en 0,00 mL.", "Llenar y enrasar", volumen=0),
    paso("Medir la muestra", "Se miden otros 50,0 mL de la misma muestra.", "Medir 50 mL",
         vaso=["Erlenmeyer:", "50,0 mL de muestra"], liquido="#eef6fa"),
    paso("Subir el pH", "Se agregan 2 mL de NaOH 1 N para llevar el pH a 12 o 13: el magnesio forma un sólido y queda fuera del conteo.", "Agregar NaOH",
         vaso=["50,0 mL de muestra", "+ NaOH 1 N (pH 12-13)"], liquido="#f1f3f4"),
    paso("Indicador", "Se agrega una pizca de murexida, que tiñe la muestra de rosado mientras hay calcio libre.", "Agregar murexida",
         vaso=["50,0 mL de muestra", "+ NaOH 1 N", "+ murexida"], liquido="#e9669a"),
    paso("Titular", "Se agrega EDTA gota a gota hasta que el rosado cambie a violeta.", "Titular con EDTA",
         titular={"hasta": 8.0, "colorCerca": "#b56bb0", "colorFinal": "#7b3fa0"}),
    paso("Leer la bureta", "Se lee el volumen gastado.", "Leer el volumen", registro=["EDTA gastado (V)", "8,0 mL"]),
    paso("Calcular", "Se usa la misma fórmula y luego se resta.", "Calcular",
         resultado="Dureza cálcica = (8,0 × 0,01 × 100 090) ÷ 50 = <strong>160,1 mg CaCO₃/L</strong>. Dureza magnésica = 240,2 − 160,1 = <strong>80,1 mg CaCO₃/L</strong>."),
], "Práctica terminada.", titulante="EDTA 0,01 M", indicadores=["NaOH 1 N (pH 12 a 13)", "Murexida"], vaso=["Erlenmeyer vacío"], liquido="#f3f6f8")

p = DIR / "dureza.html"
s = p.read_text(encoding="utf-8")
s, n = re.subn(r'<div style="margin-top:24px">\s*<div class="titulacion".*?</svg>.*?</div>\s*</div>\s*</div>', "", s, count=1, flags=re.S)
if n != 1:
    raise SystemExit("dureza.html: no se encontró la titulación simple")
p.write_text(s, encoding="utf-8")
editar("dureza.html", antes_de="clases", nuevo=
    bloque("laboratorio-dt", "Laboratorio virtual: dureza total", LAB_DT, "Sigue los pasos con el botón azul.")
    + bloque("laboratorio-dc", "Laboratorio virtual: dureza cálcica", LAB_DC)
    + bloque("calculadora-dureza", "Calculadoras de dureza",
             '<div class="duo" style="align-items:start">'
             + calc("calc-dureza", "Dureza total o cálcica",
                    [("V", "Volumen de EDTA gastado", "mL", 12.0, 0.1), ("M", "Molaridad del EDTA", "M", 0.01, 0.001), ("Vm", "Volumen de muestra", "mL", 50, 1)],
                    ["Dureza = (V × M × 100 090) ÷ Vm", "Dureza = ({V} × {M} × 100 090) ÷ {Vm}", "= {=V*M*100090} ÷ {Vm}", "= {=V*M*100090/Vm} mg CaCO₃/L",
                     "Nota: 100 090 es la masa del carbonato de calcio, 100,09 g/mol, escrita en mg/mol."],
                    "V*M*100090/Vm", "Dureza", "mg CaCO₃/L", 1,
                    [(75, "Agua blanda."), (150, "Agua moderadamente dura."), (300, "Agua dura; cumple el máximo de 300 de la Resolución 2115."), (None, "Agua muy dura; supera el máximo de 300 mg CaCO₃/L.")])
             + calc("calc-magnesica", "Dureza magnésica",
                    [("DT", "Dureza total", "mg CaCO₃/L", 240.2, 0.1), ("DC", "Dureza cálcica", "mg CaCO₃/L", 160.1, 0.1)],
                    ["Dureza magnésica = dureza total − dureza cálcica", "= {DT} − {DC}", "= {=DT-DC} mg CaCO₃/L"],
                    "DT-DC", "Dureza magnésica", "mg CaCO₃/L", 1)
             + "</div>"))

# ============================================================ Sólidos
LAB_SOL = lab("lab-solidos", "caja", "Balanza analítica", [
    paso("Preparar la cápsula", "Se calienta la cápsula vacía en la mufla a 550 °C, para quemar cualquier resto, y se enfría en un desecador, un recipiente que la protege de la humedad.", "Preparar la cápsula",
         vaso=["Cápsula de", "porcelana vacía"], liquido="#f7f7f7", pantalla="0,0000"),
    paso("Pesar vacía (A)", "Se pesa la cápsula vacía.", "Pesar",
         animar={"de": 0, "a": 42.531, "decimales": 4}, registro=["A: cápsula vacía", "42,5310 g"]),
    paso("Secar la muestra", "Se agregan 100 mL de muestra bien mezclada y se secan en el horno a 103-105 °C hasta que no quede agua.", "Secar a 105 °C",
         vaso=["Cápsula + 100 mL", "secada a 105 °C"], liquido="#e3d6bf", pantalla="en horno"),
    paso("Pesar seca (B)", "Se enfría en el desecador y se pesa: el aumento de peso es todo el residuo.", "Pesar",
         animar={"de": 42.5, "a": 42.556, "decimales": 4}, registro=["B: cápsula + residuo seco", "42,5560 g"]),
    paso("Calcinar", "Se lleva la cápsula a la mufla a 550 °C: la materia orgánica se quema y queda ceniza.", "Calcinar a 550 °C",
         vaso=["Cápsula en la mufla", "550 °C"], liquido="#cfcfcf", pantalla="en mufla"),
    paso("Pesar con ceniza (C)", "Se enfría en el desecador y se pesa de nuevo.", "Pesar",
         animar={"de": 42.5, "a": 42.546, "decimales": 4}, registro=["C: cápsula + ceniza", "42,5460 g"]),
    paso("Calcular", "Se restan los pesos y se pasa a mg/L.", "Calcular",
         resultado="Sólidos totales = (B − A) × 1 000 000 ÷ V = (42,5560 − 42,5310) × 1 000 000 ÷ 100 = <strong>250 mg/L</strong>. Sólidos volátiles = (B − C) × 1 000 000 ÷ V = 0,0100 × 1 000 000 ÷ 100 = <strong>100 mg/L</strong>. Sólidos fijos = 250 − 100 = <strong>150 mg/L</strong>."),
], "Práctica terminada: la cápsula se lava y se guarda en el desecador.", unidad="gramos", vaso=["Cápsula vacía"], liquido="#f7f7f7")
editar("solidos.html", antes_de="reto", nuevo=
    bloque("laboratorio-sol", "Laboratorio virtual: pesar los sólidos", LAB_SOL, "Sigue los pasos con el botón azul.")
    + bloque("calculadora-sol", "Calculadoras de sólidos",
             '<div class="duo" style="align-items:start">'
             + calc("calc-st", "Sólidos totales",
                    [("A", "Peso de la cápsula vacía (A)", "g", 42.531, 0.0001), ("B", "Peso con residuo seco (B)", "g", 42.556, 0.0001), ("V", "Volumen de muestra", "mL", 100, 1)],
                    ["Sólidos totales = (B − A) × 1 000 000 ÷ V", "= ({B} − {A}) × 1 000 000 ÷ {V}", "= {=B-A} g × 1 000 000 ÷ {V}", "= {=(B-A)*1000000/V} mg/L",
                     "Nota: × 1 000 000 pasa de gramos a miligramos (× 1000) y de mililitros a litros (× 1000)."],
                    "(B-A)*1000000/V", "Sólidos totales", "mg/L", 0)
             + calc("calc-sv", "Sólidos volátiles",
                    [("B", "Peso con residuo seco (B)", "g", 42.556, 0.0001), ("C", "Peso con ceniza (C)", "g", 42.546, 0.0001), ("V", "Volumen de muestra", "mL", 100, 1)],
                    ["Sólidos volátiles = (B − C) × 1 000 000 ÷ V", "= ({B} − {C}) × 1 000 000 ÷ {V}", "= {=(B-C)*1000000/V} mg/L"],
                    "(B-C)*1000000/V", "Sólidos volátiles", "mg/L", 0)
             + "</div>"))
print("OK sección 4")
