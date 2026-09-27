"""Sección 6: IRCA, ICA, escalera normativa, línea de tiempo ampliada y guía de uso.
Se ejecuta DESPUÉS de gen_sec6.py."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from componentes import ejemplo, tabla

P = Path("C:/Users/majur/Downloads/MQAT/Enciclopedia/secciones/06-normatividad/index.html")
AUD = "../../assets/audio/06-normatividad/"
s = P.read_text(encoding="utf-8")

def parrafo(texto, audio):
    return f"""<div class="parrafo">
            <p>{texto}</p>
            <button class="btn-audio" type="button" data-audio="{AUD}{audio}.mp3" hidden>🔊 Escuchar</button>
          </div>"""

def seccion(ident, titulo, contenido, instruccion=""):
    ins = f'<p class="instruccion">{instruccion}</p>\n        ' if instruccion else ""
    return f"""
    <section class="bloque" id="{ident}">
      <div class="contenedor">
        <h2>{titulo}</h2>
        {ins}{contenido}
      </div>
    </section>
"""

def antes_de(ident, nuevo):
    global s
    marca = f'    <section class="bloque" id="{ident}">'
    assert marca in s, ident
    s = s.replace(marca, nuevo.strip("\n") + "\n\n" + marca, 1)

# ============================================================ IRCA
PARAM = [
    ("pH", "unidades", 1.5, 6.5, 9.0, 7.2), ("Color aparente", "UC", 6, None, 15, 20), ("Turbiedad", "NTU", 15, None, 2, 1.5),
    ("Cloro residual libre", "mg/L", 15, 0.3, 2.0, 0.2), ("Alcalinidad total", "mg CaCO₃/L", 1, None, 200, 120),
    ("Dureza total", "mg CaCO₃/L", 1, None, 300, 180), ("Hierro total", "mg/L", 1.5, None, 0.3, 0.1), ("Cloruros", "mg/L", 1, None, 250, 45),
    ("Sulfatos", "mg/L", 1, None, 250, 60), ("Nitratos", "mg/L", 1, None, 10, 3), ("Nitritos", "mg/L", 3, None, 0.1, 0.02),
    ("Aluminio", "mg/L", 3, None, 0.2, 0.05), ("Fluoruros", "mg/L", 1, None, 1.0, 0.4),
    ("Coliformes totales", "UFC/100 mL", 15, None, 0, 0), ("E. coli", "UFC/100 mL", 25, None, 0, 0),
]
datos = {"parametros": [dict({"nombre": n, "unidad": u, "puntaje": pt, "max": mx, "valor": v}, **({"min": mn} if mn is not None else {})) for n, u, pt, mn, mx, v in PARAM]}
IRCA = f'<div class="irca" id="calc-irca"><script type="application/json">{json.dumps(datos, ensure_ascii=False)}</script></div>'
EJ_IRCA = ejemplo("el IRCA de una muestra",
    "Un acueducto analiza los 15 parámetros de la tabla. Todos cumplen, menos dos: el color aparente (20 UC, cuando el máximo es 15) y el cloro residual (0,2 mg/L, cuando el mínimo es 0,3).",
    ["Puntajes de los parámetros analizados: <span class='cuenta'>1,5 + 6 + 15 + 15 + 1 + 1 + 1,5 + 1 + 1 + 1 + 3 + 3 + 1 + 15 + 25 = 91</span>.",
     "Puntajes de los que no cumplen: color (6) + cloro (15) = <span class='cuenta'>21</span>.",
     "IRCA = <span class='cuenta'>21 ÷ 91 × 100 ≈ 23,1 %</span>.",
     "Como 23,1 está entre 14,1 y 35, el nivel de riesgo es <strong>medio</strong>."],
    "Así, fallar en un parámetro de puntaje alto, como el cloro o E. coli, sube mucho el riesgo.")
antes_de("vertimientos", seccion("calculadora-irca", "Calculadora del IRCA", f"""{EJ_IRCA}
        <div style="margin-top:24px">{IRCA}</div>
        <p class="instruccion" style="margin-top:12px">Fórmula de la Resolución 2115: IRCA = (suma de puntajes de los parámetros que no cumplen ÷ suma de puntajes de todos los analizados) × 100. La tabla muestra 15 de sus 22 parámetros.</p>""",
    "Cambia los resultados o desmarca los parámetros que no se analizaron; el IRCA se recalcula solo."))

# ============================================================ ICA
EJ_ICA = ejemplo("el ICA de un río con 5 variables",
    "En un punto de monitoreo se midió: oxígeno disuelto 6,0 mg/L (el de saturación allí es 7,5 mg/L), SST 50 mg/L, DQO 30 mg/L, conductividad 120 µS/cm y pH 7,5.",
    ["Oxígeno: saturación = <span class='cuenta'>6,0 ÷ 7,5 × 100 = 80 %</span>; como es menor de 100 %, subíndice = <span class='cuenta'>1 − (1 − 0,01 × 80) = 0,80</span>.",
     "SST: <span class='cuenta'>1 − (−0,02 + 0,003 × 50) = 1 − 0,13 = 0,87</span>.",
     "DQO: 30 mg/L está entre 25 y 40, así que el subíndice es <span class='cuenta'>0,51</span>.",
     "Conductividad: <span class='cuenta'>1 − 10^(−3,26 + 1,34 × log 120) = 1 − 10^(−0,474) = 1 − 0,336 = 0,664</span>.",
     "pH: 7,5 está entre 7 y 8, así que el subíndice es <span class='cuenta'>1</span>.",
     "ICA = <span class='cuenta'>0,2 × (0,80 + 0,87 + 0,51 + 0,664 + 1) = 0,2 × 3,844 ≈ 0,77</span>, es decir, calidad <strong>aceptable</strong>."],
    "Así, la DQO y la conductividad son las que más bajan la nota de este río.")
ICA_HTML = f"""{parrafo("Por otra parte, el ICA, o Índice de Calidad del Agua, evalúa la salud de un río y no la del agua de la llave. "
                        "Lo calcula el IDEAM con seis datos del río: oxígeno disuelto, sólidos suspendidos, DQO, conductividad, pH y la relación entre nitrógeno y fósforo. "
                        "Además, cada dato se convierte en una nota de 0 a 1, llamada subíndice, y las notas se suman con pesos. "
                        "Así, un ICA cercano a 1 indica un río en buen estado.", "p6-ica")}
        <div style="margin-top:24px">{tabla(["", "IRCA", "ICA"], [
            ["¿Qué evalúa?", "El riesgo del agua para beber", "La calidad de un río o una quebrada"],
            ["¿Dónde se mide?", "En la red del acueducto y en la llave", "En puntos de monitoreo sobre el río"],
            ["Escala", "De 0 a 100 %: mientras más alto, más riesgo", "De 0 a 1: mientras más alto, mejor calidad"],
            ["¿Quién lo calcula?", "Acueductos y autoridades de salud (Resolución 2115 de 2007)", "IDEAM y autoridades ambientales"],
            ["Mejor valor", "0", "1"]])}</div>
        <div style="margin-top:24px">{EJ_ICA}</div>
        <div class="ica" id="calc-ica" style="margin-top:24px"></div>
        <p class="instruccion" style="margin-top:12px">Fórmulas de la hoja metodológica del ICA del IDEAM (GCI-OE-F002, versión 03, 2025). El oxígeno de saturación depende de la temperatura y de la altitud: por ejemplo, es de unos 9,1 mg/L a 20 °C al nivel del mar, y menor en ciudades altas.</p>"""
antes_de("vertimientos", seccion("ica", "El ICA: la nota de salud de un río", ICA_HTML))

# ============================================================ Escalera y línea de tiempo
ESCALERA = """<div class="escalera" role="img" aria-label="Escalera normativa: Constitución, leyes, decretos y resoluciones.">
          <div>Constitución Política<small>Artículos 79 y 80: ambiente sano</small></div>
          <div>Leyes<small>Las aprueba el Congreso</small></div>
          <div>Decretos<small>Los expide el Gobierno para aplicar las leyes</small></div>
          <div>Resoluciones<small>Los ministerios fijan los números técnicos: límites y métodos</small></div>
        </div>"""

N = [  # (año, tipo, nombre, qué regula, cuándo se usa, ejemplo, verificar)
    ("1974", "Decreto-Ley", "Decreto-Ley 2811: Código Nacional de Recursos Naturales", "Declara que el agua es un bien de uso público y fija las reglas generales para usar los recursos naturales.", "Es la base de todas las demás normas del agua.", "Un río no tiene dueño: para usarlo se necesita permiso del Estado.", False),
    ("1978", "Decreto", "Decreto 1541: concesiones de agua", "Regula el permiso, llamado concesión, para tomar agua de ríos, lagos y pozos.", "Cuando alguien quiere captar agua para riego, industria o un acueducto.", "Una finca pide a la corporación autónoma regional una concesión para regar con agua de una quebrada.", False),
    ("1984", "Decreto", "Decreto 1594: usos del agua y vertimientos", "Fijó criterios de calidad para cada uso del agua y los primeros límites a los vertimientos.", "Sus criterios por uso rigieron de forma transitoria hasta que la Resolución 0565 de 2026 los reemplazó.", "Comparar un río con los criterios para consumo humano o para la vida acuática.", False),
    ("1991", "Constitución", "Constitución Política, artículos 79 y 80", "Reconoce el derecho a un ambiente sano y obliga al Estado a protegerlo.", "Cuando se defiende un río ante un juez con una acción popular o una tutela.", "Una comunidad pide a un juez que se detenga una descarga que daña su quebrada.", False),
    ("1993", "Ley", "Ley 99: Sistema Nacional Ambiental", "Crea el Ministerio de Ambiente y las corporaciones autónomas regionales, y las tasas por usar y contaminar el agua.", "Para saber quién vigila en cada región y quién cobra las tasas.", "La corporación autónoma regional de un departamento revisa una fábrica y le cobra la tasa retributiva.", False),
    ("1997", "Ley", "Ley 373: uso eficiente y ahorro del agua", "Obliga a acueductos y usuarios a tener un programa de ahorro y uso eficiente del agua.", "Cuando un acueducto o una empresa con concesión planea cómo reducir pérdidas y consumo.", "Un acueducto repara fugas y promueve aparatos ahorradores.", False),
    ("2007", "Decreto y resolución", "Decreto 1575 y Resolución 2115: agua para beber", "Definen cómo debe ser el agua potable, cada cuánto se analiza y el IRCA.", "Cuando se revisa el agua que llega a las casas.", "La secretaría de salud toma muestras en un barrio y calcula el IRCA.", False),
    ("2009", "Ley", "Ley 1333: procedimiento sancionatorio ambiental", "Define cómo se investiga y se sanciona a quien daña el ambiente.", "Cuando alguien incumple: multas, cierre temporal o decomiso.", "Una empresa que vierte sin permiso recibe una multa.", False),
    ("2010", "Decreto", "Decreto 3930: ordenamiento del recurso hídrico y vertimientos", "Ordena los usos de cada río y reglamenta el permiso de vertimiento.", "Cuando la autoridad planea un río por tramos o estudia un permiso de vertimiento.", "Se define que un tramo del río se reserva para abastecer un acueducto.", False),
    ("2012", "Decreto", "Decreto 1640: planes de ordenación de cuencas (POMCA)", "Regula los planes que deciden cómo usar y proteger toda una cuenca.", "Cuando se decide dónde se puede construir, cultivar o se debe conservar un páramo.", "Un POMCA protege la zona alta de la cuenca que abastece a una ciudad.", False),
    ("2012", "Decreto", "Decreto 2667: tasa retributiva", "Fija cómo se cobra por verter DBO₅ y sólidos suspendidos a los ríos.", "Cuando la autoridad calcula el cobro según la carga contaminante.", "Una industria que reduce su carga de DBO₅ paga menos tasa.", False),
    ("2015", "Decreto", "Decreto 1076: Decreto Único Reglamentario", "Reúne en un solo texto los decretos ambientales, entre ellos los de concesiones, vertimientos y cuencas.", "Es el punto de partida para consultar cualquier trámite ambiental.", "Para pedir una concesión o un permiso de vertimiento se consultan sus artículos.", False),
    ("2015", "Resolución", "Resolución 631: la norma de vertimientos", "Fija los límites de lo que se puede verter a ríos y alcantarillados, según cada sector productivo.", "Cuando una fábrica, un hospital o una planta de tratamiento descarga agua residual.", "Una curtiembre debe tratar su agua hasta cumplir los límites de DBO₅, DQO y cromo de su sector.", False),
    ("2018", "Decreto", "Decreto 50: ajustes al Decreto 1076", "Modifica reglas de ordenamiento del recurso hídrico, vertimientos y los consejos de macrocuencas.", "Cuando se tramita hoy un permiso de vertimiento o un plan de ordenamiento.", "Una empresa actualiza su trámite de permiso con las nuevas reglas.", False),
    ("2018", "Resolución", "Resolución 883: vertimientos al mar", "Fija los límites para descargas a aguas marinas.", "En ciudades costeras e industrias junto al mar.", "Un emisario submarino de una ciudad costera debe cumplirla.", False),
    ("2019", "Ley", "Ley 1955: Plan Nacional de Desarrollo", "Precisa que el permiso de vertimiento se exige para descargas al agua superficial, al mar o al suelo.", "Para saber si un vertimiento necesita permiso ambiental.", "Una descarga al alcantarillado la controla la empresa de alcantarillado.", False),
    ("2021", "Resolución", "Resolución 699: aguas residuales domésticas tratadas al suelo", "Fija límites para las aguas de casas que, ya tratadas, se infiltran en el suelo.", "En viviendas rurales o conjuntos con sistemas de infiltración.", "Una casa de campo con pozo séptico y campo de infiltración.", False),
    ("2021", "Resolución", "Resolución 1256: reúso de aguas residuales tratadas", "Regula el uso de agua residual tratada, por ejemplo en agricultura.", "Cuando se quiere regar con agua tratada en lugar de agua limpia.", "Una planta de tratamiento vende agua tratada para regar pastos.", False),
    ("2025", "Decreto", "Decreto 774: biosólidos (Ministerio de Vivienda)", "Modifica el Decreto 1077 de 2015 para regular el uso de los lodos tratados de las plantas de aguas residuales, llamados biosólidos, en categorías A y B.", "Cuando una planta de tratamiento quiere aprovechar sus lodos, por ejemplo como abono.", "Un lote de biosólido de categoría A se analiza y se aplica en un cultivo a más de 30 m de una toma de agua superficial.", False),
    ("2026", "Resolución", "Resolución 0565: criterios de calidad por uso (Ministerio de Ambiente)", "Define cómo debe ser el agua superficial, subterránea y marina para cada uso: consumo humano, vida acuática, riego, animales, recreación, estético, pesca y acuicultura, y navegación. Reemplaza los criterios transitorios del Decreto 1594.", "Cuando se evalúa si un río, un acuífero o el mar sirven para el uso que se les quiere dar.", "Para preservar los peces, un río debe tener al menos 5 mg/L de oxígeno disuelto y un pH entre 5,0 y 9,0.", False),
]
items = ""
for anio, tipo, nombre, que, cuando, ej, verif in N:
    nota = '<p class="verificar">⚠ Norma reciente citada en los documentos de la carpeta Normatividad Agua: conviene verificar su texto oficial.</p>' if verif else ""
    items += f"""
          <li data-anio="{anio}"><span class="tipo">{tipo}</span><h3>{nombre}</h3>
            <dl><dt>Qué regula</dt><dd>{que}</dd><dt>¿Cuándo se usa?</dt><dd>{cuando}</dd><dt>Ejemplo</dt><dd>{ej}</dd></dl>{nota}
          </li>"""
LINEA = f'<div class="linea-tiempo-envoltura"><ol class="linea-tiempo">{items}\n        </ol></div>'

GUIA = tabla(["Si la pregunta es…", "Se usa…", "Quién la aplica"], [
    ["¿Puedo tomar agua de este río o pozo?", "Concesión de aguas (Decreto 1541, hoy en el Decreto 1076)", "Corporación autónoma regional"],
    ["¿El agua de la llave es segura para beber?", "Decreto 1575 y Resolución 2115 de 2007 (IRCA)", "Acueducto y secretaría de salud"],
    ["¿Qué puedo devolver al río o al alcantarillado?", "Resolución 631 de 2015 (y la 883 si es al mar)", "Autoridad ambiental y empresa de alcantarillado"],
    ["¿Puedo infiltrar al suelo el agua tratada de mi casa?", "Resolución 699 de 2021", "Autoridad ambiental"],
    ["¿Cuánto pago por contaminar?", "Tasa retributiva (Decreto 2667 de 2012)", "Autoridad ambiental"],
    ["¿Qué calidad debe tener el río para su uso?", "Resolución 0565 de 2026 (criterios por uso) e ICA", "Autoridad ambiental e IDEAM"],
    ["¿Puedo usar como abono los lodos de una planta de tratamiento?", "Decreto 774 de 2025 (biosólidos)", "Ministerio de Vivienda y autoridades ambientales"],
    ["¿Qué pasa si alguien incumple?", "Ley 1333 de 2009", "Autoridad ambiental"]])

CLAS_ITEMS = [
    ("Un acueducto municipal revisa si el agua de la llave es segura.", "potable", "Correcto: es agua para beber, así que aplica la Resolución 2115."),
    ("Una curtiembre quiere descargar su agua tratada al río.", "vertimiento", "Correcto: es un vertimiento a un río; aplica la Resolución 631."),
    ("Una finca quiere tomar agua de una quebrada para regar.", "concesion", "Correcto: para usar agua de un río se necesita una concesión."),
    ("Una casa rural infiltra al suelo el agua tratada de su pozo séptico.", "suelo", "Correcto: es un vertimiento al suelo; aplica la Resolución 699."),
    ("La secretaría de salud calcula el IRCA de un barrio.", "potable", "Correcto: el IRCA está en la Resolución 2115."),
    ("Una fábrica de gaseosas descarga al alcantarillado.", "vertimiento", "Correcto: la Resolución 631 también fija límites para el alcantarillado."),
]
botones = "".join(f'<button type="button" data-opcion="{v}">{t}</button>' for v, t in [("potable", "Agua potable"), ("vertimiento", "Vertimientos"), ("concesion", "Concesión"), ("suelo", "Al suelo")])
CLAS = '<div class="clasificar" data-pista="Todavía no. Pregunta clave: ¿el agua se va a beber, a tomar de la fuente o a devolver al ambiente?" data-exito="¡Excelente! Ya se sabe qué norma usar en cada caso."><div class="items">' + "".join(
    f'<div class="item" data-respuesta="{r}" data-explica="{e}"><p>{f}</p><div class="botones" style="flex-wrap:wrap">{botones}</div><p class="retro-item" aria-live="polite"></p></div>' for f, r, e in CLAS_ITEMS) + '</div><p class="marcador" aria-live="polite"></p></div>'

NUEVO_HISTORIA = seccion("historia", "Cómo se ordenan las normas", f"""<div class="duo">
          {parrafo("Para empezar a ordenarlas, las normas forman una escalera. En la cima está la Constitución, que ordena proteger el ambiente. "
                   "Debajo están las leyes, que aprueba el Congreso; luego, los decretos, que expide el Gobierno para explicar cómo cumplir las leyes; "
                   "y finalmente, las resoluciones, que fijan los números técnicos, como los límites de cada parámetro. "
                   "Por eso, una resolución nunca puede contradecir a una ley ni a la Constitución.", "p5-escalera")}
          {ESCALERA}
        </div>""") + seccion("linea-tiempo", "Las reglas del agua a lo largo del tiempo", LINEA,
    "Cada tarjeta dice qué regula la norma, cuándo se usa y un ejemplo real de su aplicación.") + seccion("guia", "¿Qué norma se usa en cada caso?",
    GUIA + '<div style="margin-top:24px">' + CLAS + "</div>", "Primero se identifica la pregunta; luego, la norma.")
s, n = re.subn(r'\n    <section class="bloque" id="historia">.*?</section>\n', lambda m: "\n" + NUEVO_HISTORIA, s, count=1, flags=re.S)
assert n == 1, "historia"

# Mini-reto ampliado.
RETO_EXTRA = """<div class="reto">
          <p class="pregunta">Según la escalera de las normas, ¿quién fija los números técnicos, como el límite de 2 NTU de turbiedad?</p>
          <div class="opciones">
            <button class="opcion" type="button" data-correcta="false" data-retro="No del todo. La Constitución da los principios, no los números.">La Constitución.</button>
            <button class="opcion" type="button" data-correcta="true" data-retro="¡Correcto! La Resolución 2115 es la que fija ese límite.">Una resolución de un ministerio.</button>
            <button class="opcion" type="button" data-correcta="false" data-retro="No del todo. Las leyes definen el marco general; los límites técnicos van en resoluciones.">Una ley del Congreso.</button>
          </div>
          <p class="retro" aria-live="polite"></p>
        </div>
        <div class="reto">
          <p class="pregunta">Un río tiene un ICA de 0,45. Según la tabla del IDEAM (0,26 a 0,50 = malo), ¿cómo está su calidad?</p>
          <div class="opciones">
            <button class="opcion" type="button" data-correcta="true" data-retro="¡Correcto! 0,45 cae en la categoría malo.">Mala.</button>
            <button class="opcion" type="button" data-correcta="false" data-retro="No del todo. Aceptable empieza en 0,71.">Aceptable.</button>
          </div>
          <p class="retro" aria-live="polite"></p>
        </div>"""
marca_reto = '<h2>Mini-reto</h2>'
i = s.index(marca_reto) + len(marca_reto)
s = s[:i] + "\n        " + RETO_EXTRA + s[i:]

# ============================================================ Resolución 0565 y Decreto 774
USOS = tabla(["Uso del agua", "Qué se vigila más", "Ejemplos de criterios"], [
    ["Consumo humano y doméstico (antes de tratarla)", "Microbios y metales", "Coliformes y metales pesados por debajo de su límite"],
    ["Preservación de la flora y la fauna acuática", "Oxígeno, pH y nutrientes", "Oxígeno disuelto de al menos 5 mg/L; pH de 5,0 a 9,0"],
    ["Agrícola (riego)", "Sales y sodio", "Conductividad y RAS: con una RAS mayor que 20 no se permite regar"],
    ["Pecuario (animales)", "Sales y microbios", "Cambia según la especie: las aves toleran menos sales que las ovejas"],
    ["Recreación", "Enterococos, bacterias de origen fecal", "Hasta 200 NMP/100 mL"],
    ["Estético", "Aspecto, olor y grasas", "pH de 5,0 a 9,0; grasas y aceites hasta 10 mg/L"],
    ["Pesca, maricultura y acuicultura", "Metales y amoníaco", "Cadmio en cantidades de milésimas de mg/L"],
    ["Navegación", "Condiciones generales", "pH de 5,0 a 9,0 y oxígeno disuelto mayor de 5 mg/L"]],
    "Valores de ejemplo tomados del documento de síntesis de la carpeta Normatividad Agua. La resolución no fija criterios para el uso industrial; allí siguen rigiendo los límites de vertimiento de la Resolución 631 de 2015.")
BIO = tabla(["Regla del Decreto 774 de 2025", "Qué significa"], [
    ["Dos categorías", "Categoría A: la de mejor calidad, para uso agrícola como abono o para mejorar suelos. Categoría B: para usos menos exigentes."],
    ["Análisis por lote", "Cada lote, medido en toneladas de base seca, se caracteriza por separado."],
    ["Distancia a tomas de agua", "No se aplica a menos de 100 m de una toma de agua subterránea ni a menos de 30 m de una toma superficial."],
    ["Lugares prohibidos", "Humedales, zonas inundables, acuíferos superficiales y áreas protegidas."],
    ["Distancia a las viviendas", "El biosólido de categoría B debe aplicarse a más de 300 m de un asentamiento humano."],
    ["Premio al buen desempeño", "Si una planta grande logra siete lotes seguidos dentro de los límites, puede pedir analizar una sola vez al año."]])
antes_de("reto", seccion("criterios-uso", "¿Cómo debe estar el agua para cada uso?",
    parrafo("Además, la Resolución 0565 de 2026 define cómo debe estar el agua de ríos, acuíferos y mar según el uso que se le quiera dar. "
            "Por ejemplo, el agua para que vivan los peces necesita mucho oxígeno, mientras que el agua para regar debe tener pocas sales y poco sodio. "
            "Así, un mismo río puede servir para navegar y, sin embargo, no servir para bañarse. "
            "Por eso, sus análisis deben hacerlos laboratorios acreditados por el IDEAM.", "p7-criterios-uso")
    + '<div style="margin-top:24px">' + USOS + "</div>")
    + seccion("biosolidos", "Los biosólidos: cuando el lodo se vuelve abono",
    parrafo("Por último, las plantas de tratamiento de aguas residuales producen lodos, que son los sólidos que se separan del agua. "
            "Cuando esos lodos se estabilizan, es decir, se tratan para eliminar microbios y malos olores, se llaman biosólidos y pueden servir como abono. "
            "Sin embargo, deben usarse con cuidado para no contaminar el agua. Por eso, el Decreto 774 de 2025 fija categorías, análisis y distancias mínimas.", "p8-biosolidos")
    + '<div style="margin-top:24px">' + BIO + "</div>"))
RETO_774 = """<div class="reto">
          <p class="pregunta">Según el Decreto 774 de 2025, ¿se puede aplicar biosólido a 50 m de una toma de agua subterránea?</p>
          <div class="opciones">
            <button class="opcion" type="button" data-correcta="false" data-retro="No del todo. La distancia mínima a una toma subterránea es de 100 m.">Sí, porque está a más de 30 m.</button>
            <button class="opcion" type="button" data-correcta="true" data-retro="¡Correcto! Se necesitan al menos 100 m de una toma de agua subterránea.">No, porque debe estar a más de 100 m.</button>
          </div>
          <p class="retro" aria-live="polite"></p>
        </div>"""
k = s.index('<h2>Mini-reto</h2>') + len('<h2>Mini-reto</h2>')
s = s[:k] + "\n        " + RETO_774 + s[k:]

# Enlace a la calculadora de carga contaminante (sección 5) desde vertimientos.
ancla = '<div class="descubrir" style="margin-top:24px">'
j = s.index(ancla, s.index('id="vertimientos"'))
s = s[:j] + '<p style="margin-top:20px"><a href="../05-otros-parametros/index.html#calc-carga" style="font-weight:800;color:var(--agua-700)">🧮 Calcular la carga contaminante de un vertimiento →</a></p>\n        ' + s[j:]
P.write_text(s, encoding="utf-8")
print("OK sección 6")
