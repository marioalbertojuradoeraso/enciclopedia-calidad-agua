// QA real con Edge por CDP: todas las páginas, dos anchos, todos los componentes (incluidos labs y calculadoras).
import { spawn } from "node:child_process";
import { readdirSync, writeFileSync } from "node:fs";

const RAIZ = "C:/Users/majur/Downloads/MQAT/Enciclopedia/";
const paginas = ["index.html", "calculadoras.html"];
for (const d of readdirSync(RAIZ + "secciones")) for (const f of readdirSync(RAIZ + "secciones/" + d)) if (f.endsWith(".html")) paginas.push(`secciones/${d}/${f}`);

const EDGE = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe";
const PUERTO = 9444;
const edge = spawn(EDGE, ["--headless=new", `--remote-debugging-port=${PUERTO}`, `--user-data-dir=${process.env.TEMP}\\edge-qa-${Date.now()}`,
  "--autoplay-policy=no-user-gesture-required", "about:blank"], { stdio: "ignore" });
const esperar = (ms) => new Promise((r) => setTimeout(r, ms));
let destinos;
for (let i = 0; i < 40; i++) { try { destinos = await (await fetch(`http://127.0.0.1:${PUERTO}/json`)).json(); break; } catch { await esperar(250); } }
const ws = new WebSocket(destinos.find((d) => d.type === "page").webSocketDebuggerUrl);
await new Promise((r) => ws.addEventListener("open", r));
let id = 0; const pend = new Map(); const errores = [];
ws.addEventListener("message", (m) => {
  const d = JSON.parse(m.data);
  if (d.method === "Runtime.exceptionThrown") errores.push(d.params.exceptionDetails.exception?.description?.split("\n")[0] || d.params.exceptionDetails.text);
  if (d.method === "Log.entryAdded" && d.params.entry.level === "error" && !/favicon/.test(d.params.entry.text)) errores.push(d.params.entry.text + " " + (d.params.entry.url || ""));
  if (d.id && pend.has(d.id)) { pend.get(d.id)(d); pend.delete(d.id); }
});
const cdp = (method, params = {}) => new Promise((r) => { const n = ++id; pend.set(n, r); ws.send(JSON.stringify({ id: n, method, params })); });
const evaluar = async (e) => { const r = await cdp("Runtime.evaluate", { expression: e, awaitPromise: true, returnByValue: true }); return r.result?.result?.value ?? { error: r.result?.exceptionDetails?.text }; };
await cdp("Page.enable"); await cdp("Runtime.enable"); await cdp("Log.enable");

const PRUEBA = `(async () => {
  const f = []; const n = {};
  const ok = (k, c, d) => { n[k] = (n[k] || 0) + 1; if (!c) f.push(k + (d ? ': ' + d : '')); };
  const pausa = (ms) => new Promise(r => setTimeout(r, ms));
  document.querySelectorAll('img').forEach(i => ok('imagen', i.complete && i.naturalWidth > 0, i.getAttribute('src')));
  document.querySelectorAll('a[href]').forEach(a => { const h = a.getAttribute('href'); if (!/^(https?:|#|mailto)/.test(h)) ok('enlace a archivo', /\\.html(#.*)?$|\\.(png|jpg|svg|mp3)$/.test(h) || h.startsWith('../../assets'), h); });
  document.querySelectorAll('.btn-audio').forEach(b => ok('audio visible', !b.hidden));
  document.querySelectorAll('.tarjeta').forEach(t => { t.click(); ok('tarjeta', t.getAttribute('aria-pressed') === 'true'); });
  document.querySelectorAll('.btn-descubrir').forEach(b => { b.click(); ok('descubrir', !document.getElementById(b.getAttribute('aria-controls')).hidden); });
  document.querySelectorAll('.reto').forEach(r => { const o = r.querySelector('.opcion[data-correcta="true"]'); ok('reto', !!o); if (o) { o.click(); ok('reto responde', r.querySelector('.retro').textContent.length > 3); } });
  document.querySelectorAll('[role=tablist] [role=tab]').forEach(t => { t.click(); ok('pestaña', !document.getElementById(t.getAttribute('aria-controls')).hidden); });
  document.querySelectorAll('.ordenar').forEach(a => { [...a.querySelectorAll('.etapa')].sort((x, y) => x.dataset.orden - y.dataset.orden).forEach(x => x.click()); ok('ordenar', a.querySelector('.retro').textContent === a.dataset.exito); });
  document.querySelectorAll('.clasificar').forEach(a => { a.querySelectorAll('.item').forEach(i => i.querySelector('[data-opcion="' + i.dataset.respuesta + '"]').click()); ok('clasificar', a.querySelector('.marcador').textContent === a.dataset.exito); });
  document.querySelectorAll('.simulador, .curva, .escala-ph, .calc-ph').forEach(s => { const c = s.querySelector('input[type=range]'); const antes = s.textContent; c.value = Number(c.max) > 1 ? c.max - 1 : c.max; c.dispatchEvent(new Event('input')); ok('deslizador', s.textContent !== antes); });
  document.querySelectorAll('.comparador').forEach(c => { const x = () => [...c.querySelectorAll('.cifra')].map(e => e.textContent).join(); const b = c.querySelectorAll('[data-tipo]'); b[0].click(); const a = x(); b[b.length - 1].click(); ok('comparador', a !== x()); });
  document.querySelectorAll('.calculadora').forEach(c => { const t = c.querySelector('.calc-resultado').textContent + c.querySelector('.calc-pasos').textContent; ok('calculadora ' + c.id, /\\d/.test(t) && !/[{}]|NaN|undefined|Infinity/.test(t), t.slice(0, 80)); });
  document.querySelectorAll('.irca').forEach(c => { const t = c.querySelector('.calc-resultado').textContent; ok('irca', /IRCA: \\d/.test(t) && t.includes('medio'), t); });
  for (const lab of document.querySelectorAll('.lab')) {
    const b = lab.querySelector('.lab-boton');
    for (let i = 0; i < 20 && !b.hidden; i++) { b.click(); await pausa(60); for (let k = 0; k < 100 && b.disabled; k++) await pausa(60); }
    const r = lab.querySelector('.lab-resultado').textContent;
    ok('laboratorio ' + lab.id, b.hidden && r.length > 20 && !/[{}]|NaN|undefined/.test(r + lab.querySelector('svg').textContent), r.slice(0, 60));
  }
  ok('sin desplazamiento horizontal', document.documentElement.scrollWidth <= innerWidth + 1, document.documentElement.scrollWidth + ' > ' + innerWidth);
  return { f, total: Object.values(n).reduce((a, b) => a + b, 0), labs: n['laboratorio'] ? Object.keys(n).filter(k => k.startsWith('laboratorio')).length : 0 };
})()`;

const informe = {};
let fallas = 0;
for (const ancho of [1280, 390]) {
  await cdp("Emulation.setDeviceMetricsOverride", { width: ancho, height: 900, deviceScaleFactor: 1, mobile: ancho < 600 });
  for (const p of paginas) {
    errores.length = 0;
    await cdp("Page.navigate", { url: "file:///" + RAIZ + p });
    await esperar(1200);
    const r = await evaluar(PRUEBA);
    const e = [...errores];
    const mal = (r.f || [r.error]).length + e.length;
    fallas += mal;
    informe[`${p}@${ancho}`] = { ...r, erroresJS: e };
    console.log(`${mal ? "FALLA" : "OK   "} ${ancho} ${p.padEnd(48)} ${r.total ?? "?"} pruebas ${mal ? JSON.stringify([...(r.f || [r.error]), ...e]).slice(0, 300) : ""}`);
  }
}
writeFileSync(process.argv[2] || "qa_cdp.json", JSON.stringify(informe, null, 1));
console.log("FALLAS TOTALES:", fallas);
ws.close(); edge.kill(); process.exit(0);
