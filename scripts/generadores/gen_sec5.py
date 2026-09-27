"""Genera secciones/05-otros-parametros/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0].rsplit("\\", 1)[0])
from plantilla import *

C = "05-otros-parametros"
p = Pagina(C)
VALORES = ('{"natural":{"dbo":2,"dqo":10,"nt":0.5,"pt":0.02},'
           '"residual":{"dbo":190,"dqo":430,"nt":40,"pt":7}}')

html = cabecera(C, "Otros parámetros y tipos de agua", "Sección 5", "Otros parámetros y tipos de agua",
                "DBO₅, DQO, nitrógeno, fósforo y la diferencia entre aguas naturales y residuales.")

html += bloque("hambre", f"""<div class="duo">
          {p.parrafo("Para empezar, en el agua viven bacterias diminutas que se alimentan de materia orgánica, es decir, de restos de hojas, comida o desechos. "
                     "Al comer, esas bacterias respiran y gastan el oxígeno disuelto en el agua, el mismo que necesitan los peces. "
                     "Por eso, un agua con mucha materia orgánica puede quedarse sin oxígeno. "
                     "Así, para saber cuánta materia orgánica hay, el laboratorio mide cuánto oxígeno se gastaría al eliminarla.", "p1-hambre")}
          {p.imagen("dbo-bacterias.webp", "Dentro de una botella con agua, bacterias sonrientes comen migas de materia orgánica mientras las burbujas de oxígeno se hacen menos.",
                    "Las bacterias comen materia orgánica y, al respirar, gastan el oxígeno del agua.")}
        </div>""", "El hambre de oxígeno")

html += bloque("dbo", f"""{p.parrafo("En primer lugar, la DBO₅, o demanda bioquímica de oxígeno, indica cuánto oxígeno gastan las bacterias al comerse la materia orgánica de una muestra durante cinco días. "
                   "Para medirla, se llena una botella sin dejar burbujas, se mide su oxígeno y se guarda cinco días a 20 °C y en la oscuridad. "
                   "Luego, se mide otra vez el oxígeno: la diferencia es la DBO₅, en miligramos de oxígeno por litro.", "p2-dbo")}
        <div class="comic tres" style="margin-top:24px">
          {p.vineta("dbo-botella.webp", "Gotita junto al río con una botella de vidrio oscuro para tomar la muestra.", "Primero, se llena la botella con la muestra, sin dejar burbujas de aire.")}
          {p.vineta("dbo-incubadora.webp", "Una incubadora abierta con varias botellas de vidrio oscuro en sus estantes.", "Después, la botella pasa cinco días en una incubadora, a 20 °C y a oscuras.")}
          {p.vineta("dbo-bacterias.webp", "Bacterias comen restos orgánicos dentro de la botella y quedan pocas burbujas de oxígeno.", "Finalmente, se mide cuánto oxígeno gastaron las bacterias: esa es la DBO₅.")}
        </div>
        <div class="descubrir" style="margin-top:24px">
          {descubrir("dato-oscuras", "¿Por qué a oscuras?", "De hecho, si hubiera luz, las algas de la muestra producirían oxígeno con la fotosíntesis y el resultado saldría engañoso. Por eso, la botella se guarda en la oscuridad.")}
          {descubrir("dato-cinco", "¿Por qué cinco días?", "En realidad, es un acuerdo entre laboratorios: en cinco días las bacterias ya comieron buena parte de la materia orgánica. Así, todos los resultados se comparan con la misma regla.")}
        </div>""", "DBO₅: el oxígeno que gastan las bacterias")

html += bloque("dqo", f"""<div class="duo">
          {p.imagen("dqo-viales.webp", "Gotita, con guantes y gafas, saca con pinzas un tubo de un bloque calefactor lleno de tubos con líquidos de colores.",
                    "Los tubos de DQO se calientan unas dos horas; el color naranja del dicromato se vuelve verde a medida que destruye la materia orgánica.")}
          {p.parrafo("Por otra parte, la DQO, o demanda química de oxígeno, mide algo parecido pero sin esperar a las bacterias. "
                     "En lugar de ellas, se usa una sustancia química muy fuerte, el dicromato, que en caliente destruye casi toda la materia orgánica en unas dos horas. "
                     "Mientras trabaja, el líquido cambia de naranja a verde. "
                     "Por eso, la DQO siempre es igual o mayor que la DBO₅: la química también destruye lo que las bacterias no pueden comer.", "p3-dqo")}
        </div>
        <div class="tarjetas dos" style="margin-top:24px">
          {tarjeta("🦠", "DBO₅", "bacterias vivas", "Por ejemplo, usa bacterias y tarda cinco días; mide solo la materia orgánica que ellas pueden comer.")}
          {tarjeta("⚗️", "DQO", "química en caliente", "En cambio, usa dicromato caliente y tarda unas dos horas; mide casi toda la materia orgánica.")}
        </div>
        <div class="descubrir" style="margin-top:20px">
          {descubrir("dato-cociente", "¿Para qué comparar la DBO₅ con la DQO?", "Por ejemplo, si la DBO₅ es más o menos la mitad de la DQO, o más, las bacterias pueden limpiar bien esa agua. En cambio, si es mucho menor, el agua lleva sustancias difíciles de degradar.")}
        </div>""", "DQO: la prueba química", "Toca las tarjetas para comparar.")

html += bloque("nutrientes", f"""<div class="duo" style="align-items:start">
          <div>
            <h2>Nitrógeno total</h2>
            {p.parrafo("Además, el nitrógeno total suma todas las formas del nitrógeno en el agua: el que forma parte de restos orgánicos, el amonio, los nitritos y los nitratos. "
                       "Estas formas vienen de la orina, las heces, los abonos y los restos de alimentos. "
                       "Sin embargo, en exceso alimentan una explosión de algas; además, demasiados nitratos en el agua de beber son peligrosos para los bebés. "
                       "Por eso, las aguas residuales se tratan antes de volver al río.", "p4-nitrogeno")}
          </div>
          <div>
            <h2>Fósforo total</h2>
            {p.parrafo("De igual forma, el fósforo total reúne todo el fósforo del agua, que llega sobre todo de detergentes, abonos y desechos humanos. "
                       "Para medirlo, primero se calienta la muestra con un reactivo que convierte todo el fósforo en fosfato. "
                       "Luego, se agrega otro reactivo que tiñe la muestra de azul: mientras más fósforo, más intenso es el azul. "
                       "Así, igual que con el color del agua, un espectrofotómetro y una curva de calibración dan el resultado.", "p5-fosforo")}
          </div>
        </div>
        <div class="duo" style="margin-top:24px">
          {p.imagen("eutrofizacion.webp", "Un lago cubierto por una capa verde de algas, con peces que boquean en la superficie; Gotita mira preocupada desde la orilla.",
                    "Exceso de nitrógeno y fósforo: las algas cubren el lago y, al morir, gastan el oxígeno que necesitan los peces. Es la eutrofización de la sección 2.")}
          {p.imagen("fosforo-azul.webp", "Seis cubetas con líquido azul, de casi transparente a azul oscuro, junto a un espectrofotómetro.",
                    "Más fósforo, azul más intenso: la curva de calibración traduce ese azul en miligramos por litro.")}
        </div>""", "Los nutrientes")

html += bloque("tipos", f"""<div class="duo" style="align-items:start">
          <div>
            {p.imagen("rio-natural.webp", "Gotita sentada en una roca junto a una quebrada limpia de montaña con peces.")}
            <div style="margin-top:20px">{p.parrafo("Por un lado, las aguas naturales son las de ríos, lagos, quebradas y pozos antes de que las personas las usen. "
                       "Su composición depende de la naturaleza: de las rocas que tocan, del suelo y de la lluvia. "
                       "Por ejemplo, un río de montaña suele tener mucho oxígeno, poca materia orgánica y pocos nutrientes; por eso, su DBO₅ es muy baja.", "p6-natural")}</div>
          </div>
          <div>
            {p.imagen("agua-residual.webp", "Gotita señala una pequeña planta de tratamiento de aguas residuales cerca de un pueblo.")}
            <div style="margin-top:20px">{p.parrafo("Por otro lado, las aguas residuales son las que salen de casas, fábricas y granjas después de usarse, como el agua del inodoro, la ducha o el lavaplatos. "
                       "En otras palabras, es agua que ya trabajó y viene cargada de restos de comida, jabón, microbios y nutrientes. "
                       "Por eso, su DBO₅ puede ser casi cien veces mayor que la de un río limpio, y debe pasar por una planta de tratamiento antes de volver a la naturaleza.", "p7-residual")}</div>
          </div>
        </div>
        <div class="tarjetas dos" style="margin-top:24px">
          {tarjeta("🍽️", "Agua natural", "antes de usarse", "Por ejemplo, se parece a un plato limpio guardado en la alacena: lista para usarse.")}
          {tarjeta("🧽", "Agua residual", "después de usarse", "En cambio, se parece al agua con la que se lavaron los platos de la cena: lleva restos de todo lo que limpió.")}
        </div>""", "Aguas naturales y aguas residuales")

html += bloque("comparar", f"""<div class="comparador" data-valores='{VALORES}'>
          <div class="tipos">
            <button type="button" data-tipo="natural" aria-pressed="true">🏞️ Río de montaña</button>
            <button type="button" data-tipo="residual" aria-pressed="false">🏘️ Agua residual doméstica</button>
          </div>
          <div class="fila" data-param="dbo" data-max="190"><span class="nombre">DBO₅</span><span class="pista-barra"><span class="relleno"></span></span><span class="cifra"></span></div>
          <div class="fila" data-param="dqo" data-max="430"><span class="nombre">DQO</span><span class="pista-barra"><span class="relleno"></span></span><span class="cifra"></span></div>
          <div class="fila" data-param="nt" data-max="40"><span class="nombre">Nitrógeno total</span><span class="pista-barra"><span class="relleno"></span></span><span class="cifra"></span></div>
          <div class="fila" data-param="pt" data-max="7"><span class="nombre">Fósforo total</span><span class="pista-barra"><span class="relleno"></span></span><span class="cifra"></span></div>
          <p class="nota">Valores típicos aproximados. El agua residual corresponde a una concentración media según Metcalf y Eddy; cada barra se compara con el valor del agua residual.</p>
        </div>""", "Compara los dos tipos de agua", "Cambia el tipo de agua y mira cómo crecen las barras.")

html += bloque("clasificar", clasificar(
    [("natural", "Natural"), ("residual", "Residual")],
    [("El agua de una quebrada en el páramo.", "natural", "Correcto: nadie la ha usado todavía."),
     ("El agua que sale de la lavadora.", "residual", "Correcto: ya se usó y lleva jabón y mugre."),
     ("El agua de un pozo profundo en una finca.", "natural", "Correcto: viene del subsuelo sin haberse usado."),
     ("El agua que sale de un matadero.", "residual", "Correcto: lleva sangre y restos orgánicos, con una DBO₅ muy alta."),
     ("Un lago de montaña sin casas cerca.", "natural", "Correcto: su composición depende solo de la naturaleza."),
     ("El agua que baja por el desagüe de la cocina.", "residual", "Correcto: lleva restos de comida y grasa.")],
    "Todavía no. Pregunta clave: ¿esa agua ya fue usada por las personas?",
    "¡Excelente! Las seis aguas quedaron bien clasificadas."), "¿Natural o residual?")

html += bloque("reto", reto("Una muestra tiene DBO₅ de 200 mg/L y DQO de 450 mg/L. ¿Qué tipo de agua es más probable?", [
    ("Agua de un río de montaña.", False, "No del todo. Un río limpio tiene una DBO₅ de apenas unos pocos mg/L."),
    ("Agua residual doméstica.", True, "¡Correcto! Esos valores son típicos de un agua residual sin tratar."),
    ("Agua destilada.", False, "No del todo. En realidad, el agua destilada casi no tiene materia orgánica."),
]) + reto("¿Por qué la DQO es igual o mayor que la DBO₅?", [
    ("Porque se mide durante más días.", False, "No del todo. Al contrario, la DQO tarda unas dos horas y la DBO₅, cinco días."),
    ("Porque la química destruye también lo que las bacterias no pueden comer.", True, "¡Correcto! El dicromato ataca casi toda la materia orgánica."),
    ("Porque usa agua más sucia.", False, "No del todo. Las dos pruebas usan la misma muestra."),
]), "Mini-reto")

html += pie("../06-normatividad/index.html", "Siguiente: Normatividad →")
escribir(C, html)
