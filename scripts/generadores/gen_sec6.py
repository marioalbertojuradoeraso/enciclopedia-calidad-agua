"""Genera secciones/06-normatividad/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0].rsplit("\\", 1)[0])
from plantilla import *

C = "06-normatividad"
p = Pagina(C)
P4 = "../04-parametros/"

html = cabecera(C, "Normatividad del agua en Colombia", "Sección 6", "Normatividad en Colombia",
                "Las reglas que protegen el agua del país.")

html += bloque("norma", f"""<div class="duo">
          {p.parrafo("Para empezar, una norma es una regla escrita que el Estado establece para proteger algo importante, en este caso el agua. "
                     "Por ejemplo, funciona como el reglamento de un partido de fútbol: dice qué está permitido, qué no y quién vigila que se cumpla. "
                     "Además, en Colombia las normas del agua fijan límites, es decir, valores máximos o mínimos que los parámetros medidos en el laboratorio no deben pasar.", "p1-norma")}
          {p.imagen("norma-arbitro.webp", "Gotita sostiene un libro verde de reglas junto a un río limpio.")}
        </div>""", "¿Qué es una norma?")

html += bloque("tres", f"""<div class="tarjetas">
          {tarjeta("🚰", "Agua para beber", "Decreto 1575 y Resolución 2115 de 2007", "Por ejemplo, fijan cómo debe ser el agua que llega a las casas y cada cuánto se analiza.")}
          {tarjeta("🏭", "Vertimientos", "Resolución 631 de 2015", "Además, fija cuánta contaminación pueden devolver al río las fábricas y las ciudades.")}
          {tarjeta("🏞️", "Ríos y cuencas", "Decreto 1076 de 2015", "Finalmente, reúne en un solo texto las reglas para usar, ordenar y cuidar ríos, lagos y cuencas.")}
        </div>""", "Tres grandes reglas", "Toca cada tarjeta.")

html += bloque("potable", f"""{p.parrafo("En primer lugar, la Resolución 2115 de 2007 dice cómo debe ser el agua potable, es decir, el agua segura para beber. "
                   "Para ello, fija valores máximos para varios parámetros de las secciones anteriores. "
                   "Por ejemplo, el pH debe estar entre 6,5 y 9,0, la turbiedad no debe pasar de 2 NTU y el agua no debe tener bacterias Escherichia coli, que indican contaminación con heces. "
                   "Así, cada resultado de laboratorio se compara con estos límites.", "p2-potable")}
        <div class="enlaces" style="margin-top:24px">
          <a class="enlace" href="{P4}ph-conductividad.html"><span class="icono" aria-hidden="true">🧪</span><strong>pH: 6,5 a 9,0</strong><span>Ni muy ácida ni muy básica.</span></a>
          <a class="enlace" href="{P4}turbiedad.html"><span class="icono" aria-hidden="true">🌫️</span><strong>Turbiedad: máximo 2 NTU</strong><span>Casi sin partículas.</span></a>
          <a class="enlace" href="{P4}color.html"><span class="icono" aria-hidden="true">🎨</span><strong>Color aparente: máximo 15 UC</strong><span>Unidades platino-cobalto, también escritas UPC.</span></a>
          <a class="enlace" href="{P4}dureza.html"><span class="icono" aria-hidden="true">🧼</span><strong>Dureza: máximo 300 mg CaCO₃/L</strong><span>Evita el exceso de sarro.</span></a>
          <a class="enlace" href="{P4}alcalinidad-acidez.html"><span class="icono" aria-hidden="true">🛡️</span><strong>Alcalinidad: máximo 200 mg CaCO₃/L</strong><span>Un escudo sin exagerar.</span></a>
          <a class="enlace" href="{P4}ph-conductividad.html"><span class="icono" aria-hidden="true">⚡</span><strong>Conductividad: máximo 1000 µS/cm</strong><span>Sales disueltas bajo control.</span></a>
          <div class="enlace"><span class="icono" aria-hidden="true">🧴</span><strong>Cloro residual: 0,3 a 2,0 mg/L</strong><span>Suficiente para desinfectar hasta la llave.</span></div>
          <div class="enlace"><span class="icono" aria-hidden="true">🦠</span><strong>E. coli: 0 en 100 mL</strong><span>Ni una sola bacteria de origen fecal.</span></div>
        </div>
        <p class="instruccion" style="margin-top:14px">Valores de la Resolución 2115 de 2007 para agua de consumo humano. Toca una tarjeta con enlace para repasar el parámetro.</p>""",
    "El agua para beber")

html += bloque("cumple", clasificar(
    [("cumple", "Cumple"), ("no", "No cumple")],
    [("Agua de la llave con pH 7,2.", "cumple", "Correcto: 7,2 está dentro del rango de 6,5 a 9,0."),
     ("Agua de la llave con turbiedad de 5 NTU.", "no", "Correcto: supera el máximo de 2 NTU."),
     ("Agua de la llave con dureza de 180 mg CaCO₃/L.", "cumple", "Correcto: está por debajo de 300 mg CaCO₃/L."),
     ("Agua de la llave con 3 E. coli en 100 mL.", "no", "Correcto: debe haber 0; cualquier E. coli indica contaminación fecal."),
     ("Agua de la llave con color aparente de 10 UC.", "cumple", "Correcto: está por debajo de 15 UC."),
     ("Agua de la llave con pH 9,6.", "no", "Correcto: pasa del máximo de 9,0."),],
    "Todavía no. Compara el valor con el límite de las tarjetas de arriba.",
    "¡Excelente! Así se revisan los resultados, igual que lo hace una autoridad sanitaria."), "¿Cumple la norma?", "Clasifica cada resultado de laboratorio.")

html += bloque("irca", f"""<div class="duo">
          {p.imagen("norma-acueducto.webp", "En el laboratorio de una planta de tratamiento, un técnico y Gotita analizan una muestra de agua de la llave.")}
          {p.parrafo("Además, con los resultados se calcula el IRCA, el Índice de Riesgo de la Calidad del Agua para consumo humano. "
                     "Este índice funciona como una nota de 0 a 100, pero al revés: 0 significa sin riesgo y 100, riesgo muy alto. "
                     "Por otra parte, las empresas de acueducto deben analizar su agua, mientras que las secretarías de salud, con apoyo del Instituto Nacional de Salud, vigilan que los resultados sean confiables.", "p3-irca")}
        </div>
        <div class="barra-clases cinco" style="margin-top:24px">
          <div><strong>Sin riesgo</strong>0 a 5</div>
          <div><strong>Bajo</strong>5,1 a 14</div>
          <div><strong>Medio</strong>14,1 a 35</div>
          <div><strong>Alto</strong>35,1 a 80</div>
          <div><strong>Inviable</strong>80,1 a 100</div>
        </div>
        <p class="instruccion" style="margin-top:14px">Niveles de riesgo del IRCA según la Resolución 2115 de 2007.</p>""", "El IRCA: una nota para el agua")

html += bloque("vertimientos", f"""<div class="duo">
          {p.parrafo("Por otro lado, un vertimiento es el agua residual que una fábrica, una granja o una ciudad descarga en un río o en el alcantarillado. "
                     "Por eso, la Resolución 631 de 2015 fija, para cada tipo de actividad, cuánta DBO₅, DQO, sólidos, grasas y otras sustancias puede llevar esa descarga. "
                     "Por ejemplo, el vertimiento no puede salir a más de 40 °C, para no calentar el río. "
                     "Así, antes de descargar, las aguas residuales deben tratarse.", "p4-vertimientos")}
          {p.imagen("norma-vertimiento.webp", "Una pequeña fábrica con una planta de tratamiento descarga agua limpia al río, mientras Gotita mide la temperatura del agua.")}
        </div>
        <div class="descubrir" style="margin-top:24px">
          {descubrir("dato-permiso", "¿Quién da permiso para verter?", "Por ejemplo, la autoridad ambiental de cada región, como la Corporación Autónoma Regional, otorga el permiso de vertimiento. Además, revisa con análisis de laboratorio que la descarga cumpla los límites.")}
          {descubrir("dato-persona", "¿Qué puede hacer cada persona?", "De hecho, cada casa también vierte agua. Por eso, ayuda no arrojar aceite ni basura al desagüe, usar detergentes con moderación y avisar a la autoridad ambiental si se ve una descarga extraña en un río.")}
        </div>""", "Lo que se devuelve al río")

html += bloque("historia", flujo([
    ("1984", "Decreto 1594: primeras reglas sobre usos del agua y vertimientos."),
    ("2007", "Decreto 1575 y Resolución 2115: el agua para beber."),
    ("2010", "Decreto 3930: usos del agua y control de vertimientos."),
    ("2015", "Decreto 1076 reúne las normas; Resolución 631 fija límites de vertimientos."),
    ("2021", "Resolución 699: vertimientos de aguas tratadas al suelo."),
]), "Las reglas a lo largo del tiempo")

html += bloque("reto", reto("El agua de un acueducto tiene turbiedad de 4 NTU. ¿Cumple la Resolución 2115?", [
    ("Sí, porque 4 es un número pequeño.", False, "No del todo. El límite es 2 NTU, y 4 lo duplica."),
    ("No, porque supera el máximo de 2 NTU.", True, "¡Correcto! El acueducto debe mejorar su tratamiento."),
]) + reto("¿Qué significa un IRCA de 0?", [
    ("Que el agua no tiene riesgo para beber.", True, "¡Correcto! En el IRCA, 0 es la mejor nota posible."),
    ("Que el agua tiene el riesgo más alto.", False, "No del todo. Al revés: el riesgo más alto está cerca de 100."),
    ("Que no se hicieron análisis.", False, "No del todo. En realidad, el IRCA se calcula precisamente con los análisis."),
]), "Mini-reto")

html += pie("../../index.html", "Volver a la portada →")
escribir(C, html)
