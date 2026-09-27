const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const path = require('node:path');
const html = fs.readFileSync(path.join(__dirname, '../assets/diagrams/04-parametros/color-interpolacion.html'), 'utf8');
const nodes = new Map();
function get(id) {
  if (!nodes.has(id)) nodes.set(id, {
    value: '27', textContent: '', style: {}, attrs: {},
    setAttribute(k, v) { this.attrs[k] = v; },
    addEventListener(k, f) { this[k] = f; }
  });
  return nodes.get(id);
}
const buttons = [27,40].map(n => ({dataset: {ejemplo:String(n)}, addEventListener(k,f){this[k]=f;}}));
vm.runInNewContext(html.match(/<script>([\s\S]*?)<\/script>/)[1], {
  document: {getElementById:get, querySelectorAll:()=>buttons}
});
for (const [input, expected] of [[0,'0,000'], [27,'0,027'], [50,'0,050']]) {
  get('absorbancia').value = String(input);
  get('absorbancia').input();
  assert.equal(get('valor').textContent, expected);
  assert.ok(get('respuesta').textContent.includes(input+' UC'));
  assert.ok(get('descripcion').textContent.includes(expected));
  assert.equal(get('muestra').attrs.cx, 120+input*12);
  assert.equal(get('muestra').attrs.cy, 450-input*6);
}
buttons[1].click();
assert.ok(get('respuesta').textContent.includes('40 UC'));
assert.equal(get('absorbancia').attrs['aria-valuetext'], '0,040 de absorbancia');
console.log('OK: extremos, ejemplo de la guía, botón alternativo y texto accesible. No sustituye una prueba visual en navegador.');
