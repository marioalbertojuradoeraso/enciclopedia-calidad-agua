"""Página central de calculadoras y enlace del menú en todas las páginas."""
import re
from pathlib import Path

RAIZ = Path("C:/Users/majur/Downloads/MQAT/Enciclopedia")
S = "secciones/"
GRUPOS = [
    ("Cantidad de agua", [("🪣", "Caudal con el método del balde", S + "03-cantidad-calidad/index.html#calc-caudal", "Volumen ÷ tiempo, en L/s, L/día y m³/día.")]),
    ("pH y conductividad", [("🧪", "De [H⁺] a pH", S + "04-parametros/ph-conductividad.html#calc-ph", "pH = −log[H⁺] paso a paso.")]),
    ("Color y turbiedad", [("🎨", "Color con curva de calibración", S + "04-parametros/color.html#calc-color", "Absorbancia ÷ pendiente × dilución."),
                            ("🌫️", "Turbiedad de una dilución", S + "04-parametros/turbiedad.html#calc-turb", "Lectura × factor de dilución.")]),
    ("Titulaciones", [("🛡️", "Alcalinidad total", S + "04-parametros/alcalinidad-acidez.html#calc-alc", "(V × N × 50 000) ÷ Vm."),
                      ("⚔️", "Acidez total", S + "04-parametros/alcalinidad-acidez.html#calc-acid", "(V × N × 50 000) ÷ Vm."),
                      ("🧼", "Dureza total o cálcica", S + "04-parametros/dureza.html#calc-dureza", "(V × M × 100 090) ÷ Vm."),
                      ("➖", "Dureza magnésica", S + "04-parametros/dureza.html#calc-magnesica", "Total − cálcica."),
                      ("🐟", "Oxígeno disuelto (Winkler)", S + "05-otros-parametros/oxigeno-disuelto.html#calc-od", "(V × N × 8000) ÷ Vm."),
                      ("🧂", "Cloruros (Mohr)", S + "05-otros-parametros/iones.html#calc-cloruros", "(A − B) × N × 35 450 ÷ V.")]),
    ("Sólidos y materia orgánica", [("⚖️", "Sólidos totales", S + "04-parametros/solidos.html#calc-st", "(B − A) × 1 000 000 ÷ V."),
                                    ("🔥", "Sólidos volátiles", S + "04-parametros/solidos.html#calc-sv", "(B − C) × 1 000 000 ÷ V."),
                                    ("🦠", "DBO₅ con dilución", S + "05-otros-parametros/index.html#calc-dbo", "(OD₀ − OD₅) ÷ P."),
                                    ("⚗️", "DQO por titulación", S + "05-otros-parametros/index.html#calc-dqo", "(A − B) × M × 8000 ÷ V."),
                                    ("♻️", "Índice de biodegradabilidad", S + "05-otros-parametros/index.html#calc-bio", "DBO₅ ÷ DQO.")]),
    ("Otros parámetros de la norma", [("🧴", "Cloro para un tanque", S + "05-otros-parametros/cloro-residual.html#calc-cloro", "Dosis × volumen."),
                                      ("🔬", "Colonias a UFC/100 mL", S + "05-otros-parametros/microbiologicos.html#calc-ufc", "Colonias × 100 ÷ volumen filtrado."),
                                      ("🧲", "Hierro con curva de calibración", S + "05-otros-parametros/iones.html#calc-hierro", "Absorbancia ÷ pendiente.")]),
    ("Indicadores de calidad", [("📊", "IRCA: riesgo del agua para beber", S + "06-normatividad/index.html#calc-irca", "Puntajes de la Resolución 2115 y nivel de riesgo."),
                                ("🏞️", "ICA: calidad de un río (IDEAM)", S + "06-normatividad/index.html#calc-ica", "Subíndices de OD, SST, DQO, CE, pH y NT/PT."),
                                ("🏭", "Carga contaminante de un vertimiento", S + "05-otros-parametros/index.html#calc-carga", "C × Q × 0,0864 = kg/día.")]),
]

tarjetas = ""
for grupo, items in GRUPOS:
    tarjetas += f'\n        <h2 style="margin-top:32px">{grupo}</h2>\n        <div class="enlaces">'
    for icono, titulo, href, desc in items:
        tarjetas += f'\n          <a class="enlace" href="{href}"><span class="icono" aria-hidden="true">{icono}</span><strong>{titulo}</strong><span>{desc}</span></a>'
    tarjetas += "\n        </div>"

portada = (RAIZ / "index.html").read_text(encoding="utf-8")
cabeza = portada[:portada.index("<main>")]
cabeza = re.sub(r"<title>.*?</title>", "<title>Calculadoras del agua</title>", cabeza)
cabeza = re.sub(r"\s*<style>.*?</style>", "", cabeza, flags=re.S)
html = cabeza + f"""<main>
    <section class="portada">
      <div class="contenedor">
        <span class="etiqueta">Herramientas</span>
        <h1>Calculadoras del agua</h1>
        <p>Cada calculadora muestra la fórmula, la sustitución de los datos y el resultado, paso a paso.</p>
      </div>
    </section>

    <section class="bloque" id="lista">
      <div class="contenedor">
        <div class="parrafo">
          <p>Para empezar, cada calculadora parte de datos de laboratorio, como los mililitros gastados en una titulación o los gramos que pesa una cápsula. Además, junto a cada una está el laboratorio virtual que explica de dónde salen esos datos. Por eso, conviene recorrer primero la página del parámetro y luego usar la calculadora con datos propios.</p>
        </div>{tarjetas}
      </div>
    </section>
  </main>

</body>
</html>
"""
(RAIZ / "calculadoras.html").write_text(html, encoding="utf-8")
print("OK calculadoras.html:", sum(len(i) for _, i in GRUPOS), "calculadoras")

# Enlace «Calculadoras» en el menú de todas las páginas.
n = 0
for f in [RAIZ / "index.html", RAIZ / "calculadoras.html", *RAIZ.glob("secciones/*/*.html")]:
    s = f.read_text(encoding="utf-8")
    if "calculadoras.html\"" in s and "🧮 Calculadoras</a></li>" in s:
        continue
    rel = "" if f.parent == RAIZ else "../../"
    m = re.search(r'(<li><a href="[^"]*06-normatividad/index\.html"[^>]*>6\. Normatividad</a></li>)', s)
    if not m:
        print("SIN MENÚ:", f)
        continue
    s = s.replace(m.group(1), m.group(1) + f'\n          <li><a href="{rel}calculadoras.html">🧮 Calculadoras</a></li>', 1)
    f.write_text(s, encoding="utf-8")
    n += 1
print("menús actualizados:", n)
