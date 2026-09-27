"""Construye un diagrama vectorial exacto con los datos didácticos de la guía local."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / 'assets/diagrams/04-parametros'
OUT.mkdir(parents=True, exist_ok=True)
grid = []
for uc in range(0, 51, 10):
    x, y = 120 + uc * 12, 450 - uc * 6
    grid.append(f'<path d="M{x} 150V450 M120 {y}H720" stroke="#dbe7ee"/>')
    grid.append(f'<text x="{x}" y="476" text-anchor="middle">{uc}</text>')
    grid.append(f'<text x="105" y="{y+6}" text-anchor="end">{uc/1000:.3f}</text>'.replace('.', ','))
points = ''.join(f'<circle cx="{120+uc*12}" cy="{450-uc*6}" r="7" fill="#075985" stroke="white" stroke-width="2"/>' for uc in range(0,51,10))
svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 660" role="img" aria-labelledby="titulo descripcion">
<title id="titulo">Del valor de absorbancia al color</title>
<desc id="descripcion">Ejemplo didáctico: una absorbancia de 0,027 se busca en el eje vertical. Se avanza horizontalmente hasta la recta y se baja al eje de color: 27 unidades Pt-Co. Los patrones van de 0 a 50 unidades.</desc>
<defs><marker id="punta" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#b45309"/></marker></defs>
<rect width="960" height="660" rx="24" fill="#f8fafc"/>
<g font-family="Arial, sans-serif" fill="#16324f" font-size="18">
<text x="40" y="48" font-size="29" font-weight="bold">Del valor de absorbancia al color</text>
<text x="40" y="80">Un recorrido por la recta de calibración</text>
<text x="120" y="122">Absorbancia a 455 nm (sin unidades)</text>
__GRID__
<path d="M120 142V450H736" fill="none" stroke="#16324f" stroke-width="3"/>
<path d="M120 450L720 150" fill="none" stroke="#075985" stroke-width="4"/>
__POINTS__
<path id="horizontal" d="M120 288H437" fill="none" stroke="#b45309" stroke-width="3" stroke-dasharray="9 5" marker-end="url(#punta)"/>
<path id="vertical" d="M444 288V443" fill="none" stroke="#b45309" stroke-width="3" stroke-dasharray="9 5" marker-end="url(#punta)"/>
<circle id="muestra" cx="444" cy="288" r="9" fill="#b45309" stroke="white" stroke-width="3"/>
<text id="lectura" x="130" y="274" fill="#92400e" font-weight="bold">1. Buscar 0,027</text>
<text x="750" y="195" font-size="17">2. Llegar</text><text x="750" y="218" font-size="17">a la recta</text>
<text id="resultado" x="444" y="510" text-anchor="middle" fill="#92400e" font-weight="bold">3. Leer 27 UC</text>
<text x="420" y="548" text-anchor="middle">Color: unidades Pt-Co (UC)</text>
<text x="40" y="590" font-size="17">Ejemplo: A = 0,001 × color. Para A = 0,027: color = 27 UC.</text>
<text x="40" y="620" font-size="16">Datos didácticos. En el laboratorio se usa la recta obtenida con sus propios patrones.</text>
</g></svg>'''.replace('__GRID__',''.join(grid)).replace('__POINTS__', points)
(OUT / 'color-interpolacion.svg').write_text(svg, encoding='utf-8')
page = '''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Explorar la curva de color</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#f0f7fb;color:#16324f;font:1rem/1.6 system-ui,sans-serif}main{max-width:1000px;margin:auto;padding:24px}h1{font-size:clamp(1.6rem,4vw,2.2rem);line-height:1.2}p{max-width:78ch}.grafico{overflow-x:auto;border:1px solid #cbd5e1;border-radius:20px;background:#f8fafc}.grafico svg{display:block;width:100%;min-width:640px;height:auto}.controles{padding:20px;background:white;border-radius:16px;margin-top:20px}input[type=range]{display:block;width:100%;min-height:44px;accent-color:#075985}button{min-height:44px;padding:8px 16px;background:#075985;color:white;border:0;border-radius:8px;font:inherit;cursor:pointer}button:focus-visible,input:focus-visible,summary:focus-visible,.grafico:focus-visible{outline:3px solid #b45309;outline-offset:4px}.botones{display:flex;gap:12px;flex-wrap:wrap}output{font-weight:700}.nota{font-size:.95rem}table{border-collapse:collapse;width:100%;max-width:500px}th,td{text-align:left;padding:8px;border-bottom:1px solid #cbd5e1}details{margin-top:20px}summary{cursor:pointer;padding:10px 0}
</style></head><body><main>
<h1>¿Qué color corresponde a la lectura?</h1>
<p>Para empezar, el equipo mide absorbancia, una señal relacionada con la luz absorbida por la muestra. Después, la recta permite convertir esa señal en unidades de color.</p>
<div class="grafico" tabindex="0" role="region" aria-label="Gráfico de interpolación; desplazable horizontalmente en pantallas pequeñas">__SVG__</div>
<div class="controles">
<label for="absorbancia">Absorbancia de la muestra: <output id="valor" for="absorbancia">0,027</output></label>
<input id="absorbancia" type="range" min="0" max="50" step="1" value="27" aria-describedby="ayuda">
<p id="ayuda">Primero, se elige una lectura entre 0,000 y 0,050; después, se sigue la línea punteada hasta el eje del color.</p>
<p id="respuesta" role="status">Una absorbancia de 0,027 corresponde a 27 UC en este ejemplo.</p>
<div class="botones"><button type="button" data-ejemplo="27">Ejemplo: 0,027</button><button type="button" data-ejemplo="40">Ejemplo: 0,040</button></div>
</div>
<details><summary>Ver los patrones y el cálculo</summary>
<table><caption>Datos didácticos de la guía</caption><thead><tr><th scope="col">Color (UC Pt-Co)</th><th scope="col">Absorbancia</th></tr></thead><tbody>__ROWS__</tbody></table>
<p>En este ejemplo, absorbancia = 0,001 × color; por tanto, color = absorbancia ÷ 0,001. En una recta general A = m × color + b, se calcula color = (A − b) ÷ m.</p>
</details>
<details><summary>¿Y si la lectura supera el último patrón?</summary>
<p>En ese caso, la lectura queda fuera del intervalo calibrado; por eso, no se prolonga la recta para asignar un resultado. Se diluye la muestra según el procedimiento y se vuelve a medir dentro del intervalo.</p>
<p>Por ejemplo, una muestra diluida con factor 2 da 0,031: la curva indica 31 UC. Después, se multiplica por 2 para obtener 62 UC en la muestra original.</p>
</details>
<p class="nota">Además, estos valores sirven para explorar el procedimiento; por tanto, no sustituyen una calibración experimental ni indican si el agua es potable.</p>
<noscript><p>El gráfico muestra el ejemplo de 0,027 y 27 UC. Para mover el control se necesita JavaScript; la tabla y las explicaciones siguen disponibles.</p></noscript>
</main><script>
const control=document.getElementById('absorbancia');
function actualizar(){
 const color=Number(control.value), absorbancia=(color/1000).toFixed(3).replace('.',','),x=120+color*12,y=450-color*6;
 document.getElementById('valor').textContent=absorbancia;
 control.setAttribute('aria-valuetext',absorbancia+' de absorbancia');
 const horizontal=document.getElementById('horizontal'),vertical=document.getElementById('vertical');
 horizontal.setAttribute('d',`M120 ${y}H${Math.max(120,x-7)}`);
 vertical.setAttribute('d',`M${x} ${y}V443`);
 horizontal.style.display=vertical.style.display=color===0?'none':'';
 document.getElementById('muestra').setAttribute('cx',x);document.getElementById('muestra').setAttribute('cy',y);
 const lectura=document.getElementById('lectura');lectura.setAttribute('y',y-14);lectura.textContent='1. Buscar '+absorbancia;
 const resultado=document.getElementById('resultado');resultado.setAttribute('x',x);resultado.textContent='3. Leer '+color+' UC';
 document.getElementById('respuesta').textContent=`Una absorbancia de ${absorbancia} corresponde a ${color} UC en este ejemplo.`;
 document.getElementById('descripcion').textContent=`Absorbancia ${absorbancia}: se avanza horizontalmente hasta la recta y se baja al eje de color para leer ${color} UC. Datos didácticos.`;
}
control.addEventListener('input',actualizar);
document.querySelectorAll('[data-ejemplo]').forEach(b=>b.addEventListener('click',()=>{control.value=b.dataset.ejemplo;actualizar()}));
actualizar();
</script></body></html>'''.replace('__SVG__',svg).replace('__ROWS__',''.join(f'<tr><td>{c}</td><td>{c/1000:.3f}</td></tr>'.replace('.',',') for c in range(0,51,10)))
(OUT / 'color-interpolacion.html').write_text(page, encoding='utf-8')
print('Creados: color-interpolacion.svg y color-interpolacion.html')
