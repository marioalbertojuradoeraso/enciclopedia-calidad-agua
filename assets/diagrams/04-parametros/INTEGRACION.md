# Recurso de interpolación del color — entrega de Codex

- `color-interpolacion.svg`: gráfico vectorial estático, ejemplo 0,027 → 27 UC, con títulos accesibles y ejes rotulados.
- `color-interpolacion.html`: versión interactiva autónoma, sin dependencias ni acceso a red. Incluye control por teclado, tabla de patrones, explicación de la ecuación y ejemplo de dilución.

Desde `secciones/04-parametros/index.html` se puede enlazar `../../assets/diagrams/04-parametros/color-interpolacion.html`. Para usar el gráfico estático:

```html
<img src="../../assets/diagrams/04-parametros/color-interpolacion.svg"
     alt="Interpolación: desde una absorbancia de 0,027 se llega a la recta y se baja hasta 27 unidades de color Pt-Co.">
```

El recurso se entrega por separado: no se modificó la maquetación de Claude ni sus recursos en curso.

Fuente: `Guias de Laboratorio/Guia_Color_Turbidez_Dureza_AJUSTADAdocx.md`, apartados «Curva de calibración», «Qué hacer si la muestra queda fuera del rango» y tabla 6. Valores didácticos: 0, 10, 20, 30, 40, 50 UC y absorbancias de 0,000 a 0,050 a 455 nm. La pendiente 0,001 no se presenta como una constante universal; la calibración experimental debe obtenerse con los patrones del laboratorio.

Se usa «color de la muestra original» al corregir una dilución, para no confundir esa corrección con la distinción analítica entre color real y aparente. El diagrama no determina la potabilidad ni sustituye el método del laboratorio.

El SVG se construyó mediante código para mantener exactos los ejes y la interpolación; no se usaron APIs de imágenes ni se consumieron créditos. Generador: `scripts/crear_diagrama_color.py`. Comprobación funcional: `node Enciclopedia/scripts/verificar_diagrama_color.cjs`.
