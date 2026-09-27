# TECH_SPEC: Enciclopedia Interactiva sobre Calidad del Agua

## Tecnología
Páginas HTML estáticas que se abren con `file://`, sin compilación ni dependencias. Solo usan Google Fonts (Nunito), con fuentes del sistema como respaldo.

## Estructura
```
Enciclopedia/
├── css/estilos.css          estilos compartidos (tokens en :root)
├── js/enciclopedia.js       componentes compartidos
├── secciones/NN-nombre/index.html   (la sección 04 tiene además 6 subpáginas .html)
├── assets/images/NN-nombre/*.png|jpg
├── assets/audio/NN-nombre/*.mp3
├── assets/diagrams/         recursos vectoriales de Codex
├── scripts/                 utilidades de Codex (generar y verificar multimedia)
├── PEDIDOS_CODEX.md         pedidos y estado de multimedia
├── REVISIONES.md            bitácora de Opencode y Hermes
└── docs/PRD.md, docs/TECH_SPEC.md
```

## Componentes en `js/enciclopedia.js` (se activan por clase CSS)
| Clase | Datos | Comportamiento |
|---|---|---|
| `.imagen img` | `data-pendiente` en el contenedor | Si la imagen falta, muestra un recuadro punteado. |
| `.tarjeta` | `aria-pressed` | Tarjeta que se voltea. |
| `.btn-descubrir` | `aria-controls` | Muestra u oculta un dato. |
| `.reto .opcion` | `data-correcta`, `data-retro` | Mini-reto de opción múltiple. |
| `[role=tablist]` | `aria-controls` | Pestañas, con navegación por flechas. |
| `.ordenar .etapa` | `data-orden`, `data-pista`; `data-exito` en el contenedor | Tocar las etapas en orden. |
| `.clasificar .item` | `data-respuesta`, `data-explica`; `data-opcion` en los botones | Clasificar frases en dos grupos. |
| `.simulador` | `data-masa`, `data-alta/media/baja` | Concentración = masa ÷ volumen. |
| `.curva` | `data-pendiente`, `data-max-x`, `data-max-y`, `data-dentro/fuera` | Interpolación en una curva de calibración. |
| `.escala-ph` | `data-ejemplos` (JSON 0-14) | Escala de pH con ejemplos cotidianos. |
| `.titulacion` | `data-fin`, `data-paso`, `data-factor`, colores y textos | Titulación virtual. |
| `.comparador` | `data-valores` (JSON por tipo y parámetro); `data-max` por fila | Barras para comparar tipos de agua. |
| `.btn-audio` | `data-audio` | Aparece solo si el MP3 existe. |

## Convenciones de multimedia
- **Imágenes:** BFL. Con Gotita se usa `flux-kontext-pro` y `assets/images/01-introduccion/gotita-lupa.png` como referencia; las escenas con muchos objetos se hacen con `flux-pro-1.1`. Nada de texto dentro de las imágenes.
- **Audio:** ElevenLabs, voz `YFz1BE3aN7fQBZrEgdBE` (James), `eleven_multilingual_v2`, `speed` 0.95, pausa `<break time="0.4s" />` después del conector inicial y 45 s como máximo. Los símbolos se convierten en palabras antes de narrar («mg CaCO₃/L», «°C», «UC», «NTU»).
- **Nombres:** el MP3 se guarda en la ruta de `data-audio` del botón que está junto al párrafo narrado.

## Plantilla de página
La cabecera `.barra` lleva el menú de las 6 secciones (las que aún no existen, como `span.pendiente`). Luego vienen la `.portada`, los bloques `section.bloque` (fondo alterno), el mini-reto y el enlace `.btn-siguiente`.

## Ampliación (2026-09-27): `js/laboratorio.js`
Todas las páginas cargan este archivo después de `enciclopedia.js`. Sus componentes leen la configuración desde un `<script type="application/json">` interno, y el HTML lo generan `scripts/generadores/componentes.py` (`lab`, `paso`, `calc`).

| Clase | Configuración | Comportamiento |
|---|---|---|
| `.lab` | `escena` (`medidor`, `titulacion`, `caja`, `filtracion`), `equipo`, `unidad`, `titulante`, `indicadores`, `vaso`, `pasos[]` | Laboratorio paso a paso. Dibuja un SVG con los rótulos de reactivos e indicadores y la pantalla del equipo. Cada paso puede llevar `pantalla`, `animar`, `liquido`, `titular` (volumen y cambio de color), `colonias`, `registro` (cuaderno) y `resultado`. |
| `.calculadora` | `entradas[]`, `pasos[]` con `{Var}` y `{=expresión}`, `resultado.expr`, `interpretar[]` | Muestra la fórmula, la sustitución y el resultado, e interpreta el valor. |
| `.calc-ph` | Deslizador de 0 a 14 | Muestra [H⁺] como decimal y lo compara con el agua neutra. |
| `.irca` | `parametros[]` con puntaje, `min`/`max` y valor | Calcula el IRCA de la Resolución 2115 paso a paso y el nivel de riesgo. |

Otros estilos nuevos: `.ejemplo` (ejemplo resuelto), `.caso` (caso real), `.tabla-datos`, `.comparacion`, `.flujo.vertical`. El menú se reparte en varias filas y solo queda fijo arriba en pantallas de 900 px o más.
- `.ica`: calculadora del ICA del IDEAM (5 o 6 variables); `.linea-tiempo` y `.escalera`: normas.
