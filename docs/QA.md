# QA final: Enciclopedia Interactiva sobre Calidad del Agua

Fecha: 2026-09-27. Tarea de Orca `task_18dc33504eca` (Run `run_596a8f6a4537`). La ejecutó Claude Code con los criterios de Opencode.

## Resultado: sin fallos bloqueantes ✅

### 1. Referencias y multimedia
Comando: `python scripts/verificar_multimedia.py --section todas --report`. Informe en `assets/verificacion-completa.json`.

| Páginas | Referencias locales | MP3 (todos de 45 s o menos) | Archivos sin uso | Referencias rotas |
|---|---|---|---|---|
| 13 | 260 | 41 (23,3 min en total) | 0 | 0 |

### 2. Pruebas automáticas en navegador (Edge sin interfaz, anchos de 1280 y 390 px)
En cada página, un script ejercitó todos los componentes y comprobó que no hubiera errores de JavaScript, que todas las imágenes cargaran, que no hubiera desplazamiento horizontal y que los botones de audio fueran visibles.

| Página | Pruebas | Resultado |
|---|---|---|
| Portada `index.html` | 6 | OK en los dos anchos |
| 1. Introducción | 15 | OK |
| 2. Hidrosfera y ciclos (pestañas, ordenar) | 32 | OK |
| 3. Cantidad y calidad (clasificar, simulador) | 15 | OK |
| 4. Parámetros: índice | 2 | OK |
| 4. pH y conductividad (escala de pH) | 12 | OK |
| 4. Color (curva de calibración) | 12 | OK |
| 4. Turbiedad | 12 | OK |
| 4. Alcalinidad y acidez (titulación) | 8 | OK |
| 4. Dureza (titulación) | 13 | OK |
| 4. Sólidos | 9 | OK |
| 5. Otros parámetros (comparador, clasificar) | 24 | OK |
| 6. Normatividad (clasificar) | 15 | OK |

Componentes probados: tarjetas volteables, botones de descubrir, mini-retos, pestañas, ordenar, clasificar, simulador de concentración, curva de calibración, escala de pH, titulación virtual, comparador e imágenes.

### 3. Texto
- Ningún párrafo pasa de 81 palabras (el límite es 90). Todos abren con un conector y llevan otro en el interior.
- No se encontró lenguaje condescendiente. La segunda persona solo aparece en instrucciones de interfaz (excepción aceptada en `REVISIONES.md`).
- Todas las observaciones de Opencode y Hermes en `REVISIONES.md` están cerradas (0 pendientes).

### 4. Duración estimada del recorrido
Unos 130 min: 7547 palabras visibles leídas a 120 palabras por minuto (≈63 min), 29 actividades de unos 2 min cada una (≈58 min) y 30 viñetas y cómics (≈9 min). Cumple la meta de unas 2 horas.

## Limitaciones conocidas (no bloqueantes)
- **Narraciones:** nadie las ha escuchado. Solo se verificaron su duración y su integridad.
- **Ancho de 390 px:** Edge sin interfaz puede imponer un ancho mínimo de unos 500 px, así que la prueba de móvil equivale a unos 500 px. Conviene revisar en un teléfono real.
- **Resolución 2115 de 2007:** los valores se validaron con conocimiento de la norma, porque su texto oficial no está en `Normatividad Agua/`. Cotejarlos antes de publicar.
- **Fuente Nunito:** se carga desde Google Fonts; sin internet se usa la fuente del sistema.

## Corrección posterior (2026-09-27): enlaces y audios al abrir con doble clic
- **Falla reportada por el usuario:** al abrir con `file://`, los enlaces a carpetas (`secciones/01-introduccion/`) mostraban el listado de la carpeta, y los audios no funcionaban.
- **Causa 1:** los enlaces terminaban en `/`. Sin servidor web, el navegador no abre `index.html` por sí solo. La prueba anterior solo comprobaba que el destino existiera, sin seguir el enlace. **Corrección:** 98 enlaces apuntan ahora explícitamente a `…/index.html`; también se corrigieron las plantillas.
- **Causa 2:** el botón de audio esperaba a que el navegador precargara el archivo, y algunos navegadores no precargan audio local, así que el botón nunca aparecía. **Corrección:** el botón es siempre visible, el audio se carga al pulsar y, si el navegador bloquea la reproducción, el botón lo avisa.
- **Verificación en Edge real** (protocolo de depuración): «Empezar el recorrido», el menú, las tarjetas y la marca navegan a la página correcta; en las secciones 1, 4 (dureza) y 6, el audio avanza unos 2 s tras pulsar. `ffmpeg` decodifica los 41 MP3 y todos tienen voz audible. Los 151 enlaces locales apuntan a archivos existentes.

## Ampliación de contenidos (2026-09-27), a partir de la revisión del usuario
**Qué se agregó:**
- **Dibujos y diagramas:** agua dulce, chequeo del laboratorio, ruta de bus, transpiración, nódulos, desnitrificación, fotosíntesis, caso de eutrofización, acuífero en SVG, caudal, cloro, colonias, oxígeno y un cómic de 4 viñetas de la curva de calibración.
- **Profundidad:** el viaje completo del nitrógeno, la receta de la fotosíntesis contando átomos, casos reales (lago Erie en 2014 y embalse del Muña), lluvia ácida con datos, la cantidad de agua más allá de los ríos, pH frente a acidez y alcalinidad, y cómo se calcula el pH.
- **15 laboratorios virtuales paso a paso:** pHmetro, conductímetro, espectrofotómetro, turbidímetro, alcalinidad, acidez, dureza total, dureza cálcica, sólidos, DBO₅, DQO, Winkler, cloro DPD, filtración por membrana y cloruros de Mohr.
- **19 calculadoras** más la calculadora del IRCA. Hay una página central, `calculadoras.html`, enlazada en el menú.
- **Parámetros de la norma que faltaban:** oxígeno disuelto, cloro residual, coliformes y E. coli, cloruros, sulfatos, hierro, nitritos y nitratos, con su unidad y su método estándar (SM).
- **Mini-retos reescritos** para que cada pregunta traiga los datos o se responda con lo explicado en la misma página.
- **Menú superior:** ahora muestra todos los botones, repartidos en varias filas.

**Verificación:**
- `qa_cdp.mjs` recorrió las 19 páginas en Edge a 1280 px y a 390 px (esta vez con emulación móvil real) y ejecutó de punta a punta cada laboratorio y cada calculadora. Resultado: **0 fallas** (sin errores de JavaScript, imágenes rotas, marcadores sin reemplazar ni desplazamiento horizontal).
- `verificar_multimedia.py --section todas`: 17 páginas, 375 referencias, 54 MP3 (todos de 45 s o menos), 0 archivos sin uso y 0 referencias rotas.
- Ningún párrafo pasa de 90 palabras, y todos abren con conector y llevan otro en el interior.

**Pendiente:** cotejar con el texto oficial de la Resolución 2115 los puntajes de riesgo del IRCA y los límites de hierro, cloruros, sulfatos, nitritos, nitratos, aluminio y fluoruros; también el mínimo de oxígeno disuelto del Decreto 1076. Todos se escribieron de memoria.

## Ajustes (2026-09-27, segunda revisión del usuario)
- ICA del IDEAM: calculadora `.ica` en la sección 6. Con los datos del ejemplo, OD 80 % → 0,80; SST 50 → 0,87; DQO 30 → 0,51; CE 120 → 0,664; pH 7,5 → 1, así que ICA = 0,77, aceptable. Con 6 variables (NT/PT = 16 → 0,8) también da 0,77.
- Decimales de los pasos intermedios corregidos: la DBO₅ muestra «P = 6 ÷ 300 = 0,02» y el resultado, 260 mg/L.
- Sección 6 ampliada: escalera normativa, 20 normas en la línea de tiempo, guía de uso y clasificar. Hay 2 narraciones nuevas (34 y 37 s).
- `verificar_multimedia.py`: 17 páginas, 376 referencias, 56 MP3, 0 archivos sin uso y 0 referencias rotas.
- Con el documento del usuario sobre el Decreto 774 de 2025 y la Resolución 0565 de 2026 se agregaron dos bloques en la sección 6 (criterios por uso y biosólidos), 2 narraciones y un mini-reto, y se actualizó el mínimo de oxígeno disuelto a 5 mg/L. Verificador: 378 referencias, 58 MP3, 0 rotas.
- Revisión de errores (pedido «no dejes errores»):
  - Los valores de la Resolución 2115 y los 22 puntajes del IRCA se cotejaron con su texto oficial (SISJUR, Alcaldía de Bogotá); todos coinciden.
  - Se corrigió un dato del ciclo del nitrógeno: los rayos producen óxidos que llegan al suelo como nitratos, no amonio.
  - HTML: 0 etiquetas mal cerradas, 0 identificadores duplicados, 0 referencias ARIA rotas, 22 de 22 anclas entre páginas válidas y todas las imágenes con texto alternativo.
  - Ortografía: sin palabras repetidas ni tildes faltantes detectadas.
- Validación del usuario (2026-09-27): las narraciones suenan bien y la enciclopedia funciona bien en un teléfono real. Quedan cerradas las dos limitaciones pendientes.
