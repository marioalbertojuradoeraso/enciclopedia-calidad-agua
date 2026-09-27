"""Sección 5: laboratorios y calculadoras en el índice + cuatro subpáginas de parámetros de la norma.
Se ejecuta DESPUÉS de gen_sec5.py."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from plantilla import cabecera, pie, Pagina, descubrir, bloque as bloque_base
from componentes import lab, paso, calc, ejemplo, tabla, flujo

C = "05-otros-parametros"
DIR = Path("C:/Users/majur/Downloads/MQAT/Enciclopedia/secciones") / C
p = Pagina(C)

def bloque(ident, titulo, contenido, instruccion=None):
    return bloque_base(ident, contenido, titulo, instruccion)

def reto(pregunta, opciones):
    botones = "\n".join(f'            <button class="opcion" type="button" data-correcta="{"true" if ok else "false"}" data-retro="{r}">{t}</button>' for t, ok, r in opciones)
    return f"""<div class="reto">
          <p class="pregunta">{pregunta}</p>
          <div class="opciones">
{botones}
          </div>
          <p class="retro" aria-live="polite"></p>
        </div>"""

def ficha(unidad, metodo, norma):
    return tabla(["Unidad", "Método estándar", "Qué dice la norma"], [[unidad, metodo, norma]])

def subpagina(archivo, titulo, sub, cuerpo, anterior, siguiente):
    html = cabecera(C, titulo, "Sección 5 · Parámetro de la norma", titulo, sub)
    html = html.replace('<span class="etiqueta">', '<a class="volver" href="index.html">← Otros parámetros</a><br><span class="etiqueta">', 1)
    html += cuerpo
    html += f"""
    <div class="contenedor entre-parametros">
      <a class="btn-siguiente" href="{anterior[0]}">← {anterior[1]}</a>
      <a class="btn-siguiente" href="{siguiente[0]}">{siguiente[1]} →</a>
    </div>
  </main>

</body>
</html>
"""
    (DIR / archivo).write_text(html, encoding="utf-8")
    print("OK", archivo)

PAGINAS = [("oxigeno-disuelto.html", "Oxígeno disuelto"), ("cloro-residual.html", "Cloro residual"),
           ("microbiologicos.html", "Coliformes y E. coli"), ("iones.html", "Cloruros, hierro y otros iones")]
def vecinos(i):
    ant = PAGINAS[i - 1] if i > 0 else ("index.html", "Otros parámetros")
    sig = PAGINAS[i + 1] if i < len(PAGINAS) - 1 else ("../06-normatividad/index.html", "Normatividad")
    return ant, sig

# ============================================================ Oxígeno disuelto
LAB_OD = lab("lab-od", "titulacion", "Método de Winkler", [
    paso("Tomar la muestra", "Se llena una botella de 300 mL hasta rebosar y se tapa sin dejar burbujas, para que no entre oxígeno del aire.", "Llenar la botella",
         vaso=["Botella de 300 mL", "con la muestra"], liquido="#e3f3f9"),
    paso("Fijar el oxígeno", "Se agregan 1 mL de sulfato de manganeso y 1 mL de álcali-yoduro-azida, se tapa y se invierte: el oxígeno queda atrapado en un sólido café.", "Agregar reactivos",
         vaso=["+ sulfato de manganeso", "+ álcali-yoduro-azida"], liquido="#b8864b"),
    paso("Liberar el yodo", "Se agrega 1 mL de ácido sulfúrico concentrado: el sólido se disuelve y el agua queda amarilla por el yodo liberado.", "Agregar ácido",
         vaso=["+ ácido sulfúrico", "(yodo liberado)"], liquido="#f2c94c"),
    paso("Medir 200 mL", "Se pasan 200 mL al erlenmeyer y se llena la bureta con tiosulfato de sodio 0,025 N.", "Medir y llenar la bureta",
         vaso=["Erlenmeyer:", "200 mL de la botella"], volumen=0, registro=["Volumen titulado (Vm)", "200 mL"]),
    paso("Titular hasta amarillo pálido", "Se agrega tiosulfato hasta que el amarillo casi desaparezca.", "Titular",
         titular={"hasta": 5.4, "colorFinal": "#f7eaa8"}),
    paso("Agregar almidón", "Se agregan unas gotas de almidón: el poco yodo que queda tiñe la muestra de azul.", "Agregar almidón",
         vaso=["200 mL", "+ almidón"], liquido="#2b3d8f"),
    paso("Titular hasta incoloro", "Se sigue titulando gota a gota hasta que el azul desaparezca.", "Terminar de titular",
         titular={"desde": 5.4, "hasta": 7.2, "colorCerca": "#9aa6d6", "colorFinal": "#f3f6f8"}),
    paso("Calcular", "Con 200 mL de muestra y tiosulfato 0,025 N, cada mililitro gastado equivale a 1 mg/L de oxígeno.", "Calcular",
         registro=["Tiosulfato gastado (V)", "7,2 mL"],
         resultado="OD = (V × N × 8000) ÷ Vm = (7,2 × 0,025 × 8000) ÷ 200 = <strong>7,2 mg/L</strong>. Es un agua bien oxigenada, buena para los peces."),
], "Práctica terminada.", titulante="Tiosulfato de sodio 0,025 N", indicadores=["Sulfato de manganeso", "Álcali-yoduro-azida", "Ácido sulfúrico", "Almidón"],
   vaso=["Botella vacía"], liquido="#f3f6f8")

subpagina("oxigeno-disuelto.html", "Oxígeno disuelto", "El aire que respiran los peces.",
    bloque("que-es", "¿Qué es el oxígeno disuelto?", f"""<div class="duo">
          {p.parrafo("Para empezar, el oxígeno disuelto es el oxígeno del aire que queda mezclado dentro del agua, en forma de moléculas invisibles. "
                     "Los peces lo toman con sus branquias, igual que las personas lo toman del aire con los pulmones. "
                     "Por eso, un río sano suele tener entre 7 y 10 miligramos por litro, mientras que con menos de 4 muchos peces sufren. "
                     "Además, el agua fría guarda más oxígeno que el agua caliente.", "od-p1")}
          {p.imagen("oxigeno-peces.webp", "Bajo el agua de un río limpio, peces nadan entre burbujas de oxígeno mientras Gotita mide con una sonda.", "Gotita mide el oxígeno con una sonda, un sensor que se sumerge en el agua.")}
        </div>
        <div style="margin-top:20px">{ficha("mg O₂/L", "Winkler (SM 4500-O C) o electrodo de oxígeno (SM 4500-O G)", "Para preservar la flora y la fauna acuática, la Resolución 0565 de 2026 pide al menos 5 mg/L.")}</div>""")
    + bloque("winkler", "El método de Winkler", p.parrafo(
        "Por otra parte, el método de Winkler mide el oxígeno con reactivos. Primero, se agregan sulfato de manganeso y una mezcla alcalina de yoduro, que atrapan el oxígeno y forman un sólido café. "
        "Luego, el ácido sulfúrico disuelve ese sólido y libera yodo, que tiñe el agua de amarillo. "
        "Finalmente, se titula con tiosulfato de sodio usando almidón, que se pone azul y se vuelve incoloro cuando se acaba el yodo.", "od-p2")
        + f'<div style="margin-top:24px">{LAB_OD}</div>', "Sigue los pasos con el botón azul.")
    + bloque("calculadora", "Calculadora de oxígeno disuelto", calc("calc-od", "Oxígeno disuelto por Winkler",
        [("V", "Tiosulfato gastado", "mL", 7.2, 0.1), ("N", "Normalidad del tiosulfato", "N", 0.025, 0.001), ("Vm", "Volumen titulado", "mL", 200, 1)],
        ["OD = (V × N × 8000) ÷ Vm", "OD = ({V} × {N} × 8000) ÷ {Vm}", "= {=V*N*8000} ÷ {Vm} = {=V*N*8000/Vm} mg/L", "Nota: 8000 sale de 8 g de oxígeno por equivalente × 1000 mg por gramo."],
        "V*N*8000/Vm", "Oxígeno disuelto", "mg/L", 1,
        [(3.9999, "Muy poco oxígeno: muchos peces no sobreviven."), (4.9999, "Por debajo del mínimo de 5 mg/L de la Resolución 0565 para la vida acuática."), (None, "Cumple el mínimo de 5 mg/L para la vida acuática.")]))
    + bloque("reto", "Mini-reto", reto("Un río tiene 3 mg/L de oxígeno disuelto. La Resolución 0565 pide al menos 5 mg/L para la vida acuática. ¿Es suficiente para los peces?", [
        ("Sí.", False, "No del todo. 3 es menor que el mínimo de 5 mg/L."),
        ("No.", True, "¡Correcto! Con tan poco oxígeno, muchos peces sufren.")])
        + reto("En la titulación de Winkler con 200 mL y tiosulfato 0,025 N se gastan 5,0 mL. ¿Cuál es el oxígeno disuelto?", [
        ("5,0 mg/L", True, "¡Correcto! (5,0 × 0,025 × 8000) ÷ 200 = 5,0."),
        ("0,5 mg/L", False, "No del todo. Revisa la fórmula: (V × N × 8000) ÷ Vm.")])),
    *vecinos(0))

# ============================================================ Cloro residual
LAB_CL = lab("lab-cloro", "caja", "Colorímetro de cloro (DPD)", [
    paso("Tomar la muestra", "Se deja correr el agua de la llave durante un minuto y se llena un vial de 10 mL.", "Llenar el vial", vaso=["Vial: 10 mL de", "agua de la llave"], liquido="#eef8fc", pantalla="---"),
    paso("Ajustar el cero", "Se coloca el vial sin reactivo en el colorímetro y se oprime «Zero».", "Ajustar el cero", pantalla="0,00"),
    paso("Agregar DPD", "Se agrega un sobre de reactivo DPD y se agita 20 segundos: si hay cloro, el agua se vuelve rosada.", "Agregar DPD",
         vaso=["10 mL", "+ reactivo DPD"], liquido="#f6b3cc"),
    paso("Leer", "Se lee antes de un minuto, porque con el tiempo el color cambia.", "Leer",
         animar={"de": 0, "a": 0.8, "decimales": 2}, registro=["Cloro residual libre", "0,80 mg/L"]),
    paso("Interpretar", "Se compara con el rango de la Resolución 2115.", "Interpretar",
         resultado="0,80 mg/L está entre 0,3 y 2,0: <strong>cumple</strong>. El agua llega a la llave con suficiente cloro para seguir protegida contra los microbios."),
], "Práctica terminada.", unidad="mg/L de cloro", vaso=["Vial vacío"])

subpagina("cloro-residual.html", "Cloro residual libre", "El guardián que viaja con el agua.",
    bloque("que-es", "¿Qué es el cloro residual?", f"""<div class="duo">
          {p.parrafo("Para empezar, el cloro se agrega en las plantas de tratamiento para matar los microbios del agua, igual que el jabón elimina los gérmenes de las manos. "
                     "Sin embargo, no basta con agregarlo en la planta: debe quedar un poco de cloro en el agua hasta que llega a la llave, porque el camino por las tuberías es largo. "
                     "Ese sobrante se llama cloro residual libre y funciona como un guardián que viaja con el agua.", "cl-p1")}
          {p.imagen("cloro-dpd.webp", "Junto a una llave, dos viales: uno con agua clara y otro rosado tras agregar un reactivo; al lado, un colorímetro.", "Con el reactivo DPD, el agua con cloro se vuelve rosada.")}
        </div>
        <div style="margin-top:20px">{p.parrafo("Por eso, la Resolución 2115 de 2007 pide que el agua de la llave tenga entre 0,3 y 2,0 miligramos de cloro residual libre por litro. "
                     "Con menos de 0,3, los microbios podrían sobrevivir; con más de 2,0, el agua tendría un sabor y un olor fuertes. "
                     "Además, se mide fácilmente con el método DPD: un reactivo que tiñe el agua de rosado, más intenso cuanto más cloro hay.", "cl-p2")}</div>
        <div style="margin-top:20px">{ficha("mg Cl₂/L", "Colorimétrico DPD (SM 4500-Cl G)", "Resolución 2115 de 2007: entre 0,3 y 2,0 mg/L en cualquier punto de la red.")}</div>""")
    + bloque("laboratorio", "Laboratorio virtual: medir el cloro", LAB_CL, "Sigue los pasos con el botón azul.")
    + bloque("calculadora", "Calculadora de cloro para un tanque", calc("calc-cloro", "¿Cuánto cloro puro necesita un tanque?",
        [("D", "Dosis deseada", "mg/L", 2, 0.1), ("V", "Volumen del tanque", "L", 1000, 10)],
        ["Cloro = dosis × volumen", "Cloro = {D} mg/L × {V} L = {=D*V} mg", "En gramos: {=D*V} mg ÷ 1000 = {=D*V/1000} g de cloro puro"],
        "D*V/1000", "Cloro puro necesario", "g", 2)
        + '<p class="instruccion" style="margin-top:10px">Los productos comerciales traen cloro diluido; por eso, la cantidad real del producto depende de su concentración y de la etiqueta.</p>')
    + bloque("reto", "Mini-reto", reto("En la llave se mide 0,1 mg/L de cloro residual. El rango de la norma es de 0,3 a 2,0. ¿Cumple?", [
        ("Sí.", False, "No del todo. 0,1 es menor que el mínimo de 0,3."),
        ("No: tiene muy poco cloro para proteger el agua.", True, "¡Correcto! Los microbios podrían sobrevivir en la tubería.")])),
    *vecinos(1))

# ============================================================ Coliformes y E. coli
LAB_MB = lab("lab-micro", "filtracion", "Placa con medio cromogénico", [
    paso("Preparar el embudo", "Se desinfecta el embudo y, con pinzas estériles, se coloca una membrana de poros de 0,45 µm.", "Colocar la membrana", pantalla="Placa vacía", colonias=0),
    paso("Filtrar", "Se filtran 100 mL de muestra: las bacterias, más grandes que los poros, quedan atrapadas en la membrana.", "Filtrar 100 mL", registro=["Volumen filtrado", "100 mL"]),
    paso("Sembrar", "Con las pinzas se pasa la membrana a una placa con medio de cultivo, el alimento donde crecerán las bacterias.", "Pasar a la placa", pantalla="Sembrada"),
    paso("Incubar", "Se incuba la placa 24 horas a unos 35 °C: cada bacteria se multiplica hasta formar un puntito visible llamado colonia.", "Incubar 24 h",
         pantalla="24 h · 35 °C", colonias=23),
    paso("Contar", "Se cuentan las colonias: en este medio, las rojizas son coliformes y las azul oscuro son E. coli.", "Contar colonias",
         pantalla="23 colonias", registro=["Coliformes totales", "23 UFC/100 mL"]),
    paso("Contar E. coli", "Se cuentan aparte las colonias azul oscuro.", "Contar E. coli", pantalla="5 azules",
         registro=["E. coli", "5 UFC/100 mL"],
         resultado="La norma exige <strong>0 UFC/100 mL</strong> de coliformes totales y de E. coli. Esta agua <strong>no cumple</strong>: tuvo contacto con heces y no debe beberse sin desinfectarla."),
], "Práctica terminada: las placas se esterilizan antes de desecharlas.", liquido="#f3e6c4", vaso=["Membrana sobre el medio de cultivo"])

subpagina("microbiologicos.html", "Coliformes y E. coli", "Buscar microbios que no se ven.",
    bloque("que-son", "¿Qué son los coliformes?", f"""<div class="duo">
          {p.parrafo("Para empezar, los coliformes son un grupo de bacterias que viven en el suelo, en las plantas y en el intestino de las personas y los animales. "
                     "Entre ellos está Escherichia coli, o E. coli, que vive casi solo en el intestino; por eso, encontrarla en el agua prueba que el agua tuvo contacto con heces. "
                     "Además, donde hay E. coli pueden estar microbios que causan diarrea. Por esta razón, la norma exige que no haya ni una en 100 mL.", "mb-p1")}
          {p.imagen("colonias.webp", "Una placa de Petri con una membrana blanca y varias colonias; al lado, un embudo de filtración; Gotita las cuenta con su lupa.", "Cada puntito es una colonia que creció a partir de una sola bacteria.")}
        </div>
        <div style="margin-top:20px">{p.parrafo("Por otra parte, se miden con el método de filtración por membrana. Se hacen pasar 100 mL de agua por un filtro con poros tan pequeños, de 0,45 micrómetros, que las bacterias quedan atrapadas. "
                     "Luego, el filtro se coloca sobre un alimento especial, llamado medio de cultivo, y se incuba 24 horas a unos 35 °C. "
                     "Así, cada bacteria se multiplica hasta formar un puntito visible, llamado colonia, que se puede contar.", "mb-p2")}</div>
        <div style="margin-top:20px">{ficha("UFC/100 mL (unidades formadoras de colonias)", "Filtración por membrana (SM 9222)", "Resolución 2115 de 2007: 0 UFC/100 mL de coliformes totales y 0 de E. coli.")}</div>""")
    + bloque("laboratorio", "Laboratorio virtual: filtración por membrana", LAB_MB, "Sigue los pasos con el botón azul.")
    + bloque("calculadora", "Calculadora de colonias", calc("calc-ufc", "Pasar colonias a UFC/100 mL",
        [("n", "Colonias contadas", "", 23, 1), ("V", "Volumen filtrado", "mL", 100, 1)],
        ["UFC/100 mL = colonias × 100 ÷ volumen filtrado", "= {n} × 100 ÷ {V}", "= {=n*100/V} UFC/100 mL"],
        "n*100/V", "Resultado", "UFC/100 mL", 0,
        [(0, "Cumple: no se encontraron colonias."), (None, "No cumple la Resolución 2115, que exige 0 UFC/100 mL.")])
        + '<div style="margin-top:20px">' + ejemplo("filtrar menos agua", "Si el agua está muy sucia, se filtran solo 10 mL para poder contar las colonias.",
                  ["Se cuentan 12 colonias en 10 mL.", "UFC/100 mL = <span class='cuenta'>12 × 100 ÷ 10 = 120</span>."]) + "</div>")
    + bloque("reto", "Mini-reto", reto("Al filtrar 100 mL de agua de la llave aparecen 2 colonias de E. coli. ¿Se puede beber sin tratarla?", [
        ("Sí, porque son muy pocas.", False, "No del todo. La norma exige 0: una sola indica contaminación fecal."),
        ("No, porque la norma exige 0 UFC/100 mL.", True, "¡Correcto! Hay que desinfectarla antes de beberla.")])),
    *vecinos(2))

# ============================================================ Iones
LAB_CLORUROS = lab("lab-cloruros", "titulacion", "Cloruros por el método de Mohr", [
    paso("Llenar la bureta", "Se llena la bureta con nitrato de plata 0,0141 N y se enrasa en 0,00 mL.", "Llenar y enrasar", volumen=0),
    paso("Medir la muestra", "Se miden 100 mL de muestra.", "Medir 100 mL", vaso=["Erlenmeyer:", "100 mL de muestra"], liquido="#eef6fa", registro=["Volumen de muestra (V)", "100 mL"]),
    paso("Indicador", "Se agrega 1 mL de cromato de potasio: la muestra se vuelve amarilla.", "Agregar cromato", vaso=["100 mL de muestra", "+ cromato de potasio"], liquido="#f5d130"),
    paso("Titular", "Se agrega nitrato de plata: primero forma un sólido blanco con los cloruros; cuando se acaban, aparece un color rojo ladrillo.", "Titular",
         titular={"hasta": 9.2, "colorCerca": "#e8b04a", "colorFinal": "#c0602f"}),
    paso("Blanco", "Se repite con agua destilada para saber cuánto gasta el indicador solo.", "Titular el blanco",
         registro=["Muestra (A)", "9,2 mL"]),
    paso("Calcular", "Se resta el blanco y se aplica la fórmula.", "Calcular", registro=["Blanco (B)", "0,2 mL"],
         resultado="Cloruros = (A − B) × N × 35 450 ÷ V = (9,2 − 0,2) × 0,0141 × 35 450 ÷ 100 = <strong>45 mg/L</strong>. Cumple el máximo de 250 mg/L."),
], "Práctica terminada: los residuos con plata se guardan en un recipiente especial.", titulante="Nitrato de plata 0,0141 N", indicadores=["Cromato de potasio 5 %"],
   vaso=["Erlenmeyer vacío"], liquido="#f3f6f8")

subpagina("iones.html", "Cloruros, hierro y otros iones", "Partículas pequeñas con efectos grandes.",
    bloque("que-son", "Los iones del agua", p.parrafo(
        "Para empezar, el agua lleva disueltos varios iones, que son partículas con carga eléctrica, como los cloruros, los sulfatos, el hierro, los nitritos y los nitratos. "
        "En pequeñas cantidades son normales, porque vienen de las rocas y del suelo. "
        "Sin embargo, en exceso cambian el sabor, manchan la ropa o afectan la salud. Por eso, la Resolución 2115 fija un máximo para cada uno.", "io-p1")
        + '<div style="margin-top:24px">' + tabla(["Ion", "Qué causa en exceso", "Máximo (Res. 2115)", "Método estándar", "Cómo se ve en el laboratorio"], [
            ["Cloruros (Cl⁻)", "Sabor salado y corrosión de tuberías", "250 mg/L", "Mohr (SM 4500-Cl⁻ B)", "Titulación con nitrato de plata; el cromato pasa de amarillo a rojo ladrillo"],
            ["Sulfatos (SO₄²⁻)", "Sabor amargo y efecto laxante", "250 mg/L", "Turbidimétrico (SM 4500-SO₄²⁻ E)", "Con cloruro de bario se forma una nube blanca que se lee a 420 nm"],
            ["Hierro total (Fe)", "Color rojizo, manchas en la ropa y sabor metálico", "0,3 mg/L", "Fenantrolina (SM 3500-Fe B)", "Color naranja rojizo que se lee a 510 nm"],
            ["Nitritos (NO₂⁻)", "Peligro para los bebés", "0,1 mg/L", "Colorimétrico (SM 4500-NO₂⁻ B)", "Color rosado magenta que se lee a 543 nm"],
            ["Nitratos (NO₃⁻)", "Peligro para los bebés; señal de abonos o aguas residuales", "10 mg/L", "Ultravioleta (SM 4500-NO₃⁻ B)", "Lectura de luz ultravioleta a 220 nm"]],
            "Los métodos con color usan una curva de calibración, igual que la del color del agua en la sección 4.") + "</div>")
    + bloque("laboratorio", "Laboratorio virtual: cloruros por el método de Mohr", LAB_CLORUROS, "Sigue los pasos con el botón azul.")
    + bloque("calculadoras", "Calculadoras de iones", '<div class="duo" style="align-items:start">'
        + calc("calc-cloruros", "Cloruros (método de Mohr)",
               [("A", "Nitrato de plata gastado con la muestra", "mL", 9.2, 0.1), ("B", "Gastado con el blanco", "mL", 0.2, 0.1), ("N", "Normalidad del nitrato de plata", "N", 0.0141, 0.0001), ("V", "Volumen de muestra", "mL", 100, 1)],
               ["Cloruros = (A − B) × N × 35 450 ÷ V", "= ({A} − {B}) × {N} × 35 450 ÷ {V}", "= {=(A-B)*N*35450/V} mg/L", "Nota: 35 450 es la masa del cloro, 35,45 g/mol, escrita en mg."],
               "(A-B)*N*35450/V", "Cloruros", "mg/L", 1, [(250, "Cumple el máximo de 250 mg/L."), (None, "Supera el máximo de 250 mg/L: sabor salado.")])
        + calc("calc-hierro", "Hierro con curva de calibración",
               [("Abs", "Absorbancia a 510 nm", "", 0.08, 0.001), ("m", "Pendiente de la curva", "por mg/L", 0.199, 0.001)],
               ["Hierro = absorbancia ÷ pendiente", "= {Abs} ÷ {m}", "= {=Abs/m} mg/L"],
               "Abs/m", "Hierro total", "mg/L", 2, [(0.3, "Cumple el máximo de 0,3 mg/L."), (None, "Supera 0,3 mg/L: el agua puede manchar la ropa y saber a metal.")])
        + "</div>")
    + bloque("reto", "Mini-reto", reto("Un agua tiene 0,5 mg/L de hierro. El máximo es 0,3 mg/L. ¿Qué problema puede causar?", [
        ("Manchas rojizas en la ropa y sabor metálico.", True, "¡Correcto! Además, supera el máximo de la norma."),
        ("Ninguno, porque es menos de 1 mg/L.", False, "No del todo. El máximo es 0,3, y 0,5 lo supera.")])
        + reto("En la titulación de Mohr, ¿qué color indica que se acabaron los cloruros?", [
        ("Rojo ladrillo.", True, "¡Correcto! Aparece cuando el nitrato de plata ya no encuentra cloruros."),
        ("Azul.", False, "No del todo. El azul es el final de la dureza con EDTA.")])),
    *vecinos(3))

# ============================================================ Índice de la sección 5
LAB_DBO = lab("lab-dbo", "medidor", "Oxímetro", [
    paso("Diluir la muestra", "Como el agua residual gasta mucho oxígeno, se diluye: 6 mL de muestra en una botella de 300 mL que se completa con agua de dilución aireada.", "Preparar la botella",
         vaso=["Botella DBO de 300 mL", "6 mL de muestra"], liquido="#e9f3f6", pantalla="---", registro=["Muestra en la botella", "6 mL de 300 mL (P = 0,02)"]),
    paso("Oxígeno inicial", "Se mide el oxígeno disuelto el primer día con el oxímetro.", "Medir OD inicial",
         animar={"de": 0, "a": 8.6, "decimales": 1}, registro=["OD inicial (OD₀)", "8,6 mg/L"]),
    paso("Incubar", "Se tapa sin burbujas y se guarda 5 días a 20 °C, en la oscuridad.", "Incubar 5 días", pantalla="5 días", vaso=["Botella tapada", "5 días · 20 °C · oscuridad"]),
    paso("Oxígeno final", "Se mide otra vez el oxígeno: las bacterias gastaron una parte.", "Medir OD final",
         animar={"de": 8.6, "a": 3.4, "decimales": 1}, registro=["OD a los 5 días (OD₅)", "3,4 mg/L"]),
    paso("Calcular", "Se resta y se corrige por la dilución.", "Calcular",
         resultado="DBO₅ = (OD₀ − OD₅) ÷ P = (8,6 − 3,4) ÷ 0,02 = <strong>260 mg/L</strong>, donde P = 6 ÷ 300 = 0,02. La prueba es válida porque se gastaron más de 2 mg/L y quedó más de 1 mg/L de oxígeno."),
], "Práctica terminada.", unidad="mg/L de oxígeno", vaso=["Botella vacía"])

LAB_DQO = lab("lab-dqo", "titulacion", "DQO por reflujo cerrado", [
    paso("Digerir", "Se mezclan 20 mL de muestra con dicromato de potasio y ácido sulfúrico, y se calientan 2 horas a 150 °C en tubos cerrados.", "Digerir 2 horas",
         vaso=["20 mL de muestra", "+ dicromato + ácido sulfúrico"], liquido="#e8943a", registro=["Volumen de muestra (V)", "20 mL"]),
    paso("Indicador", "Se enfría y se agregan 2 gotas de ferroína: el color queda verde azulado.", "Agregar ferroína",
         vaso=["Muestra digerida", "+ ferroína"], liquido="#3e9c8f", volumen=0),
    paso("Blanco", "Se titula primero un blanco, hecho con agua destilada, que gasta 10,0 mL de FAS.", "Titular el blanco", registro=["Blanco (A)", "10,0 mL"]),
    paso("Titular la muestra", "Se agrega FAS gota a gota hasta que el color cambie de verde azulado a café rojizo.", "Titular con FAS",
         titular={"hasta": 6.5, "colorCerca": "#6b8f5e", "colorFinal": "#a0522d"}),
    paso("Calcular", "Mientras menos FAS gasta la muestra, más dicromato consumió su materia orgánica.", "Calcular", registro=["Muestra (B)", "6,5 mL"],
         resultado="DQO = (A − B) × M × 8000 ÷ V = (10,0 − 6,5) × 0,10 × 8000 ÷ 20 = <strong>140 mg/L</strong>."),
], "Práctica terminada: los residuos de dicromato se guardan como residuo peligroso.", titulante="FAS 0,10 M (sulfato ferroso amoniacal)", indicadores=["Dicromato de potasio", "Ferroína"],
   vaso=["Tubo de digestión"], liquido="#f3f6f8")

idx = DIR / "index.html"
s = idx.read_text(encoding="utf-8")
def antes_de(ident, nuevo):
    global s
    marca = f'    <section class="bloque" id="{ident}">'
    assert marca in s, ident
    s = s.replace(marca, nuevo.rstrip("\n") + "\n\n" + marca, 1)

antes_de("dqo", bloque("lab-dbo-bloque", "Laboratorio virtual y calculadora de DBO₅", LAB_DBO
    + '<div style="margin-top:24px">' + calc("calc-dbo", "DBO₅ con dilución",
        [("OD0", "Oxígeno inicial (OD₀)", "mg/L", 8.6, 0.1), ("OD5", "Oxígeno a los 5 días (OD₅)", "mg/L", 3.4, 0.1), ("Vm", "Muestra en la botella", "mL", 6, 0.5), ("Vb", "Volumen de la botella", "mL", 300, 1)],
        ["P = muestra ÷ botella = {Vm} ÷ {Vb} = {=Vm/Vb}", "DBO₅ = (OD₀ − OD₅) ÷ P", "= ({OD0} − {OD5}) ÷ {=Vm/Vb}", "= {=OD0-OD5} ÷ {=Vm/Vb} = {=(OD0-OD5)/(Vm/Vb)} mg/L"],
        "(OD0-OD5)/(Vm/Vb)", "DBO₅", "mg/L", 0,
        [(5, "Agua limpia, como la de un río de montaña."), (50, "Agua con algo de contaminación orgánica."), (None, "Carga orgánica alta, típica de aguas residuales.")]) + "</div>",
    "Sigue los pasos con el botón azul."))
antes_de("nutrientes", bloque("lab-dqo-bloque", "Laboratorio virtual y calculadoras de DQO", LAB_DQO
    + '<div class="duo" style="margin-top:24px;align-items:start">'
    + calc("calc-dqo", "DQO por titulación",
           [("A", "FAS gastado con el blanco", "mL", 10, 0.1), ("B", "FAS gastado con la muestra", "mL", 6.5, 0.1), ("M", "Molaridad del FAS", "M", 0.1, 0.01), ("V", "Volumen de muestra", "mL", 20, 1)],
           ["DQO = (A − B) × M × 8000 ÷ V", "= ({A} − {B}) × {M} × 8000 ÷ {V}", "= {=(A-B)*M*8000} ÷ {V} = {=(A-B)*M*8000/V} mg/L"],
           "(A-B)*M*8000/V", "DQO", "mg/L", 0)
    + calc("calc-bio", "¿Se degrada fácil?",
           [("DBO", "DBO₅", "mg/L", 190, 1), ("DQO", "DQO", "mg/L", 430, 1)],
           ["Índice = DBO₅ ÷ DQO", "= {DBO} ÷ {DQO} = {=DBO/DQO}"],
           "DBO/DQO", "Índice de biodegradabilidad", "", 2,
           [(0.3, "Poco biodegradable: tiene sustancias difíciles de degradar para las bacterias."), (0.5, "Biodegradabilidad moderada."), (None, "Fácilmente biodegradable: las bacterias pueden limpiarla bien.")])
    + "</div>"))
antes_de("clasificar", bloque("carga", "¿Cuánta contaminación llega al río cada día?",
    p.parrafo("Finalmente, para saber cuánto contamina una descarga no basta con la concentración: también importa el caudal. "
              "Por ejemplo, un vaso de agua muy sucia contamina menos que un río entero un poco sucio. "
              "Por eso, se calcula la carga contaminante, es decir, los kilogramos de una sustancia que llegan al río en un día. "
              "Así, en Colombia se cobra una tasa retributiva según la carga de DBO₅ y de sólidos que cada usuario vierte.", "p8-carga")
    + '<div style="margin-top:24px">' + calc("calc-carga", "Carga contaminante",
        [("C", "Concentración", "mg/L", 190, 1), ("Q", "Caudal de la descarga", "L/s", 20, 0.5)],
        ["Carga (kg/día) = C × Q × 0,0864", "= {C} × {Q} × 0,0864", "= {=C*Q*0.0864} kg/día",
         "Nota: 0,0864 convierte mg/s en kg/día: 86 400 segundos por día ÷ 1 000 000 mg por kg."],
        "C*Q*0.0864", "Carga contaminante", "kg/día", 1) + "</div>"))
antes_de("reto", bloque("mas-parametros", "Más parámetros de la norma", """<div class="enlaces">
          <a class="enlace" href="oxigeno-disuelto.html"><span class="icono" aria-hidden="true">🐟</span><strong>Oxígeno disuelto</strong><span>El aire que respiran los peces. Método de Winkler.</span></a>
          <a class="enlace" href="cloro-residual.html"><span class="icono" aria-hidden="true">🧴</span><strong>Cloro residual</strong><span>El guardián que viaja con el agua. Método DPD.</span></a>
          <a class="enlace" href="microbiologicos.html"><span class="icono" aria-hidden="true">🦠</span><strong>Coliformes y E. coli</strong><span>Microbios que no se ven. Filtración por membrana.</span></a>
          <a class="enlace" href="iones.html"><span class="icono" aria-hidden="true">🧂</span><strong>Cloruros, hierro y otros iones</strong><span>Sabor, manchas y salud. Método de Mohr.</span></a>
        </div>""", "Cada tarjeta abre una página con explicación, laboratorio virtual y calculadora."))
idx.write_text(s, encoding="utf-8")
print("OK index.html de la sección 5")
