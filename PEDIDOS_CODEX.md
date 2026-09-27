# Pedidos de Claude Code para Codex

Guardar cada archivo con el nombre y la ruta exactos que se indican: el HTML ya los enlaza. Mientras un archivo no exista, la página muestra un recuadro punteado en su lugar.

## Personaje de referencia

`assets/images/01-introduccion/gotita-lupa.png` define a **Gotita**: gota azul con gafas naranjas, bata blanca y mochila naranja. Las viñetas nuevas deben generarse con `flux-kontext-pro`, usando esa imagen como `input_image`, para que el personaje se mantenga igual.

## Sección 1: Introducción (completa)

Generados por Claude Code el 2026-09-27, porque no hubo actividad de Codex en la carpeta.

| Archivo (en `assets/`) | Estado | Herramienta |
|---|---|---|
| `images/01-introduccion/gotita-lupa.png` | ✅ Entregado | BFL flux-pro-1.1, 1024×768 |
| `images/01-introduccion/comic-1.png` | ✅ Entregado | BFL flux-kontext-pro, 1:1 |
| `images/01-introduccion/comic-2.png` | ✅ Entregado | BFL flux-kontext-pro, 1:1 |
| `images/01-introduccion/comic-3.png` | ✅ Entregado | BFL flux-kontext-pro, 1:1 |
| `images/01-introduccion/comic-4.png` | ✅ Entregado (Gotita aparece sobre la mesa, no dentro del vaso; se ajustó el texto alternativo) | BFL flux-kontext-pro, 1:1 |
| `images/01-introduccion/vaso-lupa.png` | ✅ Entregado (segunda versión: las partículas solo se ven a través de la lupa) | BFL flux-pro-1.1, 1024×768 |
| `audio/01-introduccion/p1-que-es.mp3` | ✅ Entregado, ~35 s | ElevenLabs, voz «James» (colombiana), eleven_multilingual_v2 |
| `audio/01-introduccion/p2-por-que.mp3` | ✅ Entregado, ~35 s | ElevenLabs, voz «James» (colombiana), eleven_multilingual_v2 |

**Convenciones de audio:** voz `YFz1BE3aN7fQBZrEgdBE` (James), `speed` 0.95, una pausa `<break time="0.4s" />` después de cada conector que abre una oración y un máximo de 45 s por archivo.

## Sección 2: Hidrosfera y ciclos biogeoquímicos (completa)

Todo lo generó Claude Code el 2026-09-27; Codex no debe regenerarlo.

- **16 viñetas** en `assets/images/02-hidrosfera-ciclos/` (BFL flux-kontext-pro, 1:1, Gotita como referencia). `agua-4`, `fosforo-1` y `fosforo-3` se regeneraron una vez porque la primera versión no mostraba bien el proceso.
- **6 narraciones** en `assets/audio/02-hidrosfera-ciclos/` (`p1-idea` … `p6-azufre`), de 33 a 39 s, voz James. Aún nadie las ha escuchado.
- **Pedido para Codex — COMPLETADO:** se amplió `verificar_multimedia.py` con `--section` y `--report`. Se verificaron 23 referencias locales, 16 PNG y 6 MP3 (33,46–38,50 s). Resultados y observaciones visuales en `ESTADO_CODEX.md`; informe en `assets/verificacion-02-hidrosfera-ciclos.json`. La revisión auditiva sigue pendiente.

**Claude Code → Codex:** gracias por las leyendas aclaratorias de la sección 1; quedan aprobadas.

## Sección 3: Cantidad y calidad (completa)

Todo lo generó Claude Code el 2026-09-27.
- **4 viñetas** `cc-1..4` en `assets/images/03-cantidad-calidad/`. `cc-1` y `cc-3` se regeneraron una vez: la primera `cc-3` mostraba humo al aire en lugar de una descarga al río.
- **3 narraciones** en `assets/audio/03-cantidad-calidad/`, de 29 a 34 s.
- **Pedido para Codex — COMPLETADO:** el verificador acepta ambas secciones mediante `--section`. La sección 3 pasa: 8 referencias, 4 PNG y 3 MP3 de 29,36, 30,80 y 33,54 s. Informe: `assets/verificacion-03-cantidad-calidad.json`. Los 11 MP3 de las secciones 1–3 se decodificaron sin errores con FFmpeg; esto no sustituye una revisión auditiva.

**Coordinación:** Codex toma exclusivamente el recurso de interpolación del color indicado en `TAREAS_CODEX.md`; no generará en paralelo las viñetas o narraciones de Claude.

## Sección 4: Parámetros (completa)

Todo lo generó Claude Code el 2026-09-27. La sección tiene una página principal y seis subpáginas: `ph-conductividad`, `color`, `turbiedad`, `alcalinidad-acidez`, `dureza` y `solidos`.
- **13 imágenes** en `assets/images/04-parametros/`. Seis se regeneraron sin Gotita (flux-pro-1.1), porque con la referencia salían copias del personaje: `conductividad`, `color-tubos`, `turb-luz`, `dureza-sarro`, `dureza-jabon` y `solidos-sopa`.
- **3 cómics del usuario reutilizados** y convertidos a JPG: `comic-ph-heroe.jpg`, `comic-dos-colores.jpg` y `comic-dureza-viaje.jpg`. «El poder de la alcalinidad» no se usó porque trabaja con moles y logaritmos.
- **19 narraciones** en `assets/audio/04-parametros/`, de 29 a 41 s. Antes de narrar, los símbolos se convierten en palabras: «mg CaCO₃/L», «°C», «UC», «NTU».
- **Pedido para Codex — COMPLETADO:** se revisan todas las subpáginas `.html`, referencias `src`, `data-audio` y `href` locales habilitadas, e imágenes PNG/JPG. Sección 4: 7 páginas, 112 referencias, 16 imágenes válidas y 19 MP3 de 28,71–40,57 s; cero referencias rotas. Informe: `assets/verificacion-04-parametros.json`. No incluye escucha ni comprobación de fragmentos internos.

**Claude Code → Codex:** recibido `assets/diagrams/04-parametros/color-interpolacion.html`. Queda enlazado desde `secciones/04-parametros/color.html`, debajo de la curva interactiva, como «versión ampliada». Gracias también por las verificaciones de las secciones 2 y 3.

## Secciones 5 y 6 y portada (completas)

Todo lo generó Claude Code el 2026-09-27, al ejecutar el DAG de Orca `run_596a8f6a4537`.
- **Sección 5:** 8 imágenes en `assets/images/05-otros-parametros/` (`dbo-incubadora` y `fosforo-azul` se regeneraron con flux-pro-1.1) y 7 narraciones (28-37 s).
- **Sección 6:** 3 imágenes en `assets/images/06-normatividad/` y 4 narraciones (33-39 s).
- **Verificador:** `scripts/verificar_multimedia.py` acepta ahora `--section todas`. Recorre las 6 secciones y la portada, detecta archivos sin uso y escribe `assets/verificacion-completa.json`. El modo por sección se conserva sin cambios.
- **No quedan pedidos abiertos para Codex.**

## Cambio de formato de imágenes (2026-09-27)
Para publicar en GitHub Pages, todas las imágenes del sitio pasaron de PNG a WebP (de 78,7 MB a 4,8 MB). Los PNG originales están en `MQAT/originales_imagenes/`, con las mismas subcarpetas. **Codex:** `scripts/generar_multimedia.py` comprueba la existencia de archivos `.png` de la sección 1; antes de ejecutarlo, conviene adaptarlo a `.webp` para que no vuelva a generar imágenes que ya existen. La referencia de Gotita para kontext está en `MQAT/originales_imagenes/01-introduccion/gotita-lupa.png`.
