"""Crea un panel local de revisión; no envía archivos ni usa APIs."""
from pathlib import Path
from html.parser import HTMLParser
import hashlib
import html
import json
import os

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'revision'
OUT.mkdir(exist_ok=True)

class Narrations(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_p = False
        self.parts = []
        self.last_p = ''
        self.entries = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'p':
            self.in_p = True
            self.parts = []
        if 'data-audio' in attrs:
            self.entries.append((attrs['data-audio'], self.last_p))

    def handle_data(self, data):
        if self.in_p:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if tag == 'p':
            self.in_p = False
            self.last_p = ' '.join(''.join(self.parts).split())

entries, seen = [], set()
for page in sorted((ROOT / 'secciones').rglob('*.html')):
    parser = Narrations()
    parser.feed(page.read_text(encoding='utf-8'))
    for reference, text in parser.entries:
        audio = (page.parent / reference).resolve()
        if audio in seen:
            continue
        seen.add(audio)
        if not audio.is_file():
            continue
        fingerprint = hashlib.sha256(audio.read_bytes() + text.encode('utf-8')).hexdigest()
        entries.append({'id': audio.relative_to(ROOT).as_posix(),
                        'src': Path(os.path.relpath(audio, OUT)).as_posix(),
                        'page': page.relative_to(ROOT).as_posix(),
                        'page_url': Path(os.path.relpath(page, OUT)).as_posix(),
                        'text': text, 'fingerprint': fingerprint})

cards = []
for i, entry in enumerate(entries):
    esc = html.escape
    cards.append(f'''<article data-index="{i}">
<h2>{esc(Path(entry['id']).name)}</h2>
<p class="ruta">{esc(entry['page'])} · <a href="{esc(entry['page_url'])}">Abrir página fuente</a></p>
<audio controls preload="none" src="{esc(entry['src'])}">El navegador no admite audio.</audio>
<p class="guion">{esc(entry['text'])}</p>
<label for="estado-{i}">Resultado de la escucha</label>
<select id="estado-{i}"><option value="pendiente">Pendiente de escuchar</option><option value="aprobado">Escuchado: conforme</option><option value="corregir">Escuchado: requiere corrección</option></select>
<label for="notas-{i}">Observaciones (palabra, problema y segundo aproximado)</label>
<textarea id="notas-{i}" rows="3"></textarea>
</article>''')

page = '''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Revisión de narraciones</title>
<style>*{box-sizing:border-box}body{margin:0;background:#eff6fa;color:#16324f;font:16px/1.6 system-ui,sans-serif}main{max-width:900px;margin:auto;padding:24px}h1{line-height:1.2}h2{font-size:1.15rem;overflow-wrap:anywhere}article{background:white;border:1px solid #cbd5e1;border-radius:14px;padding:22px;margin:20px 0}audio{width:100%}label{display:block;font-weight:600;margin-top:12px}select,textarea,input,button{font:inherit;padding:10px;max-width:100%}textarea,input{width:100%}textarea{resize:vertical}button{border:0;background:#075985;color:white;border-radius:8px;cursor:pointer;min-height:44px}.ruta{font-size:.9rem;overflow-wrap:anywhere}.guion{border-left:4px solid #0284c7;padding-left:16px}a{color:#075985}:focus-visible{outline:3px solid #b45309;outline-offset:3px}[hidden]{display:none!important}.aviso{font-weight:600}#resumen{font-weight:700}</style></head>
<body><main><h1>Revisión de narraciones</h1>
<p>Escuchar cada archivo y compararlo con el texto de su página. Revisar pronunciación, omisiones, pausas, volumen y posibles cortes. Los símbolos pueden estar expresados con palabras en la narración.</p>
<p>Ningún resultado se aprueba automáticamente. Las notas se guardan en este navegador cuando está disponible el almacenamiento local; el botón de exportación permite entregar el informe al equipo.</p>
<p id="aviso" class="aviso" role="status"></p>
<p id="resumen" role="status"></p>
<button id="exportar" type="button">Exportar revisión JSON</button>
<label for="buscar">Filtrar por archivo, sección o texto</label><input id="buscar" type="search">
<label for="filtro">Mostrar</label><select id="filtro"><option value="todos">Todos</option><option value="pendiente">Pendientes</option><option value="corregir">Requieren corrección</option><option value="aprobado">Conformes</option></select>
__CARDS__
<noscript><p>Los audios y los textos están disponibles. Para guardar resultados y exportarlos se necesita JavaScript.</p></noscript>
</main><script>
const entries=__DATA__;
const storageKey='mqat-revision-audio-v1';
let stored={};
try{stored=JSON.parse(localStorage.getItem(storageKey)||'{}');if(!stored||typeof stored!=='object')stored={};}
catch(e){document.getElementById('aviso').textContent='No se pudo leer el almacenamiento local. Exportar la revisión antes de cerrar.';}
const reviews={};
for(const e of entries){const prior=stored[e.id];reviews[e.id]=prior&&prior.fingerprint===e.fingerprint&&['pendiente','aprobado','corregir'].includes(prior.status)?prior:{status:'pendiente',notes:'',fingerprint:e.fingerprint};}
function save(){try{localStorage.setItem(storageKey,JSON.stringify(reviews));}catch(e){document.getElementById('aviso').textContent='No se pudo guardar en este navegador. Exportar la revisión antes de cerrar.';}}
function refresh(){
 const query=document.getElementById('buscar').value.toLocaleLowerCase('es'),filter=document.getElementById('filtro').value;
 const counts={pendiente:0,aprobado:0,corregir:0};
 entries.forEach((e,i)=>{const status=reviews[e.id].status;counts[status]++;document.querySelector(`[data-index="${i}"]`).hidden=!(e.id+' '+e.page+' '+e.text).toLocaleLowerCase('es').includes(query)||(filter!=='todos'&&status!==filter);});
 document.getElementById('resumen').textContent=`${entries.length} audios: ${counts.pendiente} pendientes, ${counts.aprobado} conformes y ${counts.corregir} para corregir.`;
}
entries.forEach((e,i)=>{
 const status=document.getElementById('estado-'+i),notes=document.getElementById('notas-'+i);
 status.value=reviews[e.id].status;notes.value=reviews[e.id].notes;
 status.addEventListener('change',()=>{reviews[e.id].status=status.value;reviews[e.id].updated_at=new Date().toISOString();save();refresh();});
 notes.addEventListener('input',()=>{reviews[e.id].notes=notes.value;reviews[e.id].updated_at=new Date().toISOString();save();});
});
document.querySelectorAll('audio').forEach(a=>a.addEventListener('play',()=>document.querySelectorAll('audio').forEach(other=>{if(other!==a)other.pause();})));
document.getElementById('buscar').addEventListener('input',refresh);document.getElementById('filtro').addEventListener('change',refresh);
document.getElementById('exportar').addEventListener('click',()=>{
 const report={exported_at:new Date().toISOString(),scope:'Resultados declarados por quien realiza la escucha; no aprobación automática.',entries:entries.map(e=>({file:e.id,page:e.page,...reviews[e.id]}))};
 const url=URL.createObjectURL(new Blob([JSON.stringify(report,null,2)],{type:'application/json'}));const a=document.createElement('a');a.href=url;a.download='revision-auditiva.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
});
refresh();
</script></body></html>'''
page = page.replace('__CARDS__','\n'.join(cards)).replace('__DATA__', json.dumps(entries,ensure_ascii=False).replace('<','\\u003c'))
(OUT / 'audio.html').write_text(page,encoding='utf-8')
(OUT / 'audio-inventario.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Panel generado: {len(entries)} narraciones, todas pendientes salvo revisiones locales previas de la misma versión.')
