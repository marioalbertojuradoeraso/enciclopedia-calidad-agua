"""HTML de laboratorios virtuales, calculadoras, ejemplos resueltos y casos (lo interpreta js/laboratorio.js)."""
import json

def _json(d):
    return json.dumps(d, ensure_ascii=False).replace("</", "<\\/")

def paso(titulo, texto, boton, **efectos):
    return {"titulo": titulo, "texto": texto, "boton": boton, **efectos}

def lab(ident, escena, equipo, pasos, final, **extra):
    datos = {"escena": escena, "equipo": equipo, "pasos": pasos, "final": final, **extra}
    return f'<div class="lab" id="{ident}"><script type="application/json">{_json(datos)}</script></div>'

def calc(ident, titulo, entradas, pasos, expr, etiqueta, unidad, decimales=1, interpretar=None):
    datos = {"titulo": titulo,
             "entradas": [dict(zip(("id", "etiqueta", "unidad", "valor", "paso"), e)) for e in entradas],
             "pasos": pasos,
             "resultado": {"expr": expr, "etiqueta": etiqueta, "unidad": unidad, "decimales": decimales},
             "interpretar": [{"hasta": h, "texto": t} for h, t in (interpretar or [])]}
    return f'<div class="calculadora" id="{ident}"><script type="application/json">{_json(datos)}</script></div>'

def ejemplo(titulo, intro, pasos, cierre=""):
    items = "".join(f"<li>{p}</li>" for p in pasos)
    return f'<div class="ejemplo"><strong>✏️ Ejemplo resuelto: {titulo}</strong><p style="margin:0">{intro}</p><ol>{items}</ol>{f"<p style=margin-bottom:0>{cierre}</p>" if cierre else ""}</div>'

def caso(titulo, parrafos):
    cuerpo = "".join(f"<p>{p}</p>" for p in parrafos)
    return f'<div class="caso"><strong>📰 Caso real: {titulo}</strong>{cuerpo}</div>'

def tabla(encabezados, filas, pie=""):
    th = "".join(f"<th>{h}</th>" for h in encabezados)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in f) + "</tr>" for f in filas)
    nota = f'<p class="instruccion" style="margin-top:8px">{pie}</p>' if pie else ""
    return f'<div class="tabla-desplazable"><table class="tabla-datos"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>{nota}'

def comparacion(tarjetas):
    """tarjetas: [(icono, título, {rótulo: texto})]"""
    bloques = []
    for icono, titulo, filas in tarjetas:
        dl = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in filas.items())
        bloques.append(f"<div><h3>{icono} {titulo}</h3><dl>{dl}</dl></div>")
    return f'<div class="comparacion">{"".join(bloques)}</div>'

def flujo(pasos, vertical=False):
    items = "\n".join(f"            <li><strong>{t}</strong>{d}</li>" for t, d in pasos)
    clase = "flujo vertical" if vertical else "flujo"
    return f'<ol class="{clase}">\n{items}\n          </ol>'
