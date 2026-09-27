// Uso: node cdp_foto.mjs <ruta relativa a Enciclopedia> <selector> <salida.png> [js a ejecutar antes] [ancho]
import { spawn } from "node:child_process";
import { writeFileSync } from "node:fs";

const [ruta, selector, salida, accion = "", ancho = "1280"] = process.argv.slice(2);
const EDGE = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe";
const PUERTO = 9300 + Math.floor(Math.random() * 500);
const edge = spawn(EDGE, ["--headless=new", `--remote-debugging-port=${PUERTO}`, `--user-data-dir=${process.env.TEMP}\\edge-foto-${PUERTO}`,
  "--autoplay-policy=no-user-gesture-required", `--window-size=${ancho},1000`, "about:blank"], { stdio: "ignore" });
const esperar = (ms) => new Promise((r) => setTimeout(r, ms));
let destinos;
for (let i = 0; i < 40; i++) { try { destinos = await (await fetch(`http://127.0.0.1:${PUERTO}/json`)).json(); break; } catch { await esperar(250); } }
const ws = new WebSocket(destinos.find((d) => d.type === "page").webSocketDebuggerUrl);
await new Promise((r) => ws.addEventListener("open", r));
let id = 0; const pend = new Map();
ws.addEventListener("message", (m) => { const d = JSON.parse(m.data); if (d.id && pend.has(d.id)) { pend.get(d.id)(d); pend.delete(d.id); } });
const cdp = (method, params = {}) => new Promise((r) => { const n = ++id; pend.set(n, r); ws.send(JSON.stringify({ id: n, method, params })); });
const evaluar = async (e) => (await cdp("Runtime.evaluate", { expression: e, awaitPromise: true, returnByValue: true })).result?.result?.value;
await cdp("Page.enable");
await cdp("Emulation.setDeviceMetricsOverride", { width: Number(ancho), height: 1000, deviceScaleFactor: 1, mobile: Number(ancho) < 600 });
await cdp("Page.navigate", { url: "file:///C:/Users/majur/Downloads/MQAT/Enciclopedia/" + ruta });
await esperar(1500);
const errores = await evaluar(`window.__e = []; addEventListener('error', e => __e.push(e.message)); 0`);
if (accion) console.log("acción:", JSON.stringify(await evaluar(`(async () => { ${accion} })()`)));
const caja = await evaluar(`(() => { const el = document.querySelector(${JSON.stringify(selector)}); el.scrollIntoView(); const r = el.getBoundingClientRect(); return { x: r.x + scrollX, y: r.y + scrollY, w: r.width, h: r.height }; })()`);
const foto = await cdp("Page.captureScreenshot", { format: "png", captureBeyondViewport: true, clip: { x: caja.x, y: caja.y, width: caja.w, height: Math.min(caja.h, 2400), scale: 1 } });
writeFileSync(salida, Buffer.from(foto.result.data, "base64"));
console.log("errores JS:", JSON.stringify(await evaluar("__e")), "ancho documento:", await evaluar("document.documentElement.scrollWidth"));
ws.close(); edge.kill(); process.exit(0);
