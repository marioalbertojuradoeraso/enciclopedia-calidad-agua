# Bloque del cómic de la curva de calibración (se importa desde mejoras_4.py).
IMG = "../../assets/images/04-parametros/"

def _vineta(src, alt, texto):
    return f"""<figure class="vineta">
            <div class="imagen" data-pendiente="Viñeta pendiente"><img src="{IMG}{src}" alt="{alt}"></div>
            <figcaption>{texto}</figcaption>
          </figure>"""

PANEL4 = """<figure class="vineta">
            <div class="imagen"><svg viewBox="0 0 300 300" role="img" aria-label="Gráfica: desde una absorbancia en el eje vertical, una línea punteada avanza hasta la recta y baja al eje del color." style="width:100%;height:100%;background:#fff8ec">
              <g stroke="#e3f5fb" stroke-width="2">""" + "".join(f'<line x1="50" x2="280" y1="{250 - 40 * k}" y2="{250 - 40 * k}"/>' for k in range(1, 6)) + """</g>
              <line x1="50" y1="250" x2="280" y2="250" stroke="#0b3954" stroke-width="3"/>
              <line x1="50" y1="30" x2="50" y2="250" stroke="#0b3954" stroke-width="3"/>
              <line x1="50" y1="250" x2="270" y2="60" stroke="#087e8b" stroke-width="5"/>
              """ + "".join(f'<circle cx="{50 + 44 * i}" cy="{250 - 38 * i}" r="6" fill="#0b3954"/>' for i in range(6)) + """
              <path d="M50 158 L157 158" stroke="#ff6f59" stroke-width="4" stroke-dasharray="9 6"/>
              <path d="M157 158 L157 250" stroke="#ff6f59" stroke-width="4" stroke-dasharray="9 6"/>
              <circle cx="157" cy="158" r="9" fill="#ff6f59" stroke="#fff" stroke-width="3"/>
              <g font-family="Nunito, Segoe UI, sans-serif" font-weight="800" font-size="15" fill="#0b3954">
                <text x="58" y="148">1. absorbancia</text>
                <text x="165" y="215">2. la recta</text>
                <text x="120" y="280">3. el color</text>
              </g>
              <path d="M235 40 Q245 20 255 40 Q258 55 245 58 Q232 55 235 40 Z" fill="#1fa2c4"/>
            </svg></div>
            <figcaption>Finalmente, se mide la muestra y, desde su absorbancia, se sigue la recta para leer su color.</figcaption>
          </figure>"""

COMIC_CURVA = f"""<div class="comic">
          {_vineta("curva-1.webp", "Gotita ordena en una gradilla seis tubos con líquido de transparente a amarillo oscuro.", "Primero, se preparan estándares de color conocido, de 0 a 50 UC, como las marcas de una regla.")}
          {_vineta("curva-2.webp", "Gotita coloca una cubeta con líquido amarillo en un espectrofotómetro; al lado está la gradilla de tubos.", "Después, el espectrofotómetro mide cuánta luz absorbe cada estándar.")}
          {_vineta("curva-3.webp", "Gotita traza con una regla una recta que une seis puntos en una hoja de papel milimetrado.", "Luego, los puntos se dibujan en una gráfica y se unen con una sola recta que pasa por el cero.")}
          {PANEL4}
        </div>"""
