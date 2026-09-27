# Generadores de páginas

Scripts de Claude Code que generan o mejoran las páginas. Se ejecutan con `python <script>` desde esta carpeta; las rutas del proyecto están escritas de forma absoluta.

## Orden para regenerar
1. **Sección 4:** `gen_sec4.py` y luego `mejoras_4.py` (laboratorios, calculadoras, ejemplos y el cómic de la curva, desde `comic_curva.py`).
2. **Sección 5:** `gen_sec5.py` y luego `gen_sec5b.py` (laboratorios de DBO₅ y DQO, calculadoras y 4 subpáginas).
3. **Sección 6:** `gen_sec6.py` y luego `mejoras_6.py` (calculadora del IRCA).
4. `gen_calculadoras.py`: página central de calculadoras y enlace «🧮 Calculadoras» en el menú.
5. `narrar.py <carpeta o página>`: narra con ElevenLabs los párrafos que aún no tienen MP3. Por ejemplo: `python narrar.py 05-otros-parametros/iones.html`.

Las secciones 1 a 3 se editan directamente en su HTML, porque no tienen generador.

## Piezas compartidas
- `plantilla.py`: cabecera, menú y pie de las secciones 5 y 6.
- `componentes.py`: HTML de laboratorios (`lab`, `paso`), calculadoras (`calc`), ejemplos resueltos, casos, tablas, comparaciones y flujos. El comportamiento está en `js/laboratorio.js`.
- `bfl_pro.py`: imágenes sin personaje (flux-pro-1.1), a partir de un JSON `{archivo: prompt}`. BFL entrega PNG: después se convierten a WebP (calidad 82), porque el sitio publicado usa WebP. Los PNG originales se guardan en `MQAT/originales_imagenes/`.

## Pruebas
- `node qa_cdp.mjs salida.json`: recorre todas las páginas en Edge a 1280 y 390 px. Ejecuta cada laboratorio y cada calculadora, y revisa errores, imágenes, enlaces y desplazamiento horizontal.
- `node cdp_foto.mjs <página> <selector> <salida.png> [js] [ancho]`: captura una parte de una página.
- `python ../verificar_multimedia.py --section todas --report`: referencias, imágenes y audios.
