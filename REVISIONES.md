# Bitácora de revisiones

Opencode (brevedad y rigor) y Hermes (tono pedagógico) anotan aquí sus observaciones. Claude Code corrige y marca cada una como resuelta.

## Sección 1: Introducción, 2026-09-27

A la fecha no hay revisiones de Opencode ni de Hermes en la carpeta. Claude Code hizo una autorrevisión con sus criterios; queda pendiente su validación.

### Criterios de Opencode (brevedad y rigor)
- [x] Todos los textos tienen menos de 90 palabras: párrafo 1 = 79, párrafo 2 = 71; las tarjetas, los datos y las viñetas tienen entre 9 y 35.
- [x] Cada párrafo abre con un conector y lleva al menos otro en su interior.
- [x] Las narraciones duran menos de 45 s (~35 s cada una).
- [x] La imagen del vaso se corrigió: la primera versión mostraba partículas a simple vista y contradecía «sustancias invisibles».
- [x] Pendiente: validar el dato de la «cucharadita» de agua dulce disponible (orden de magnitud: menos del 1 % del agua del planeta es dulce y accesible).

### Criterios de Hermes (tono)
- [x] Ningún texto dice ni insinúa «para niños», «básico» o algo equivalente.
- [x] Mini-reto: las opciones incorrectas eran absurdas («estrellas», «huesos») y resultaban condescendientes. Se cambiaron por errores de concepto verosímiles («solo la contaminación de fábricas», «solo el agua del grifo»).
- [x] Pendiente: evaluar si las tarjetas volteables (aire, suelo, agua) aportan al aprendizaje o si conviene una actividad de clasificar sustancias en cada lugar.

## Sección 2: Hidrosfera y ciclos, 2026-09-27

Autorrevisión de Claude Code; queda pendiente la validación de Opencode y Hermes.

### Opencode
- [x] Los párrafos tienen de 74 a 81 palabras; las viñetas y los datos, de 9 a 39. Cada párrafo abre con un conector y lleva otro en su interior.
- [x] Narraciones de 33 a 39 s.
- [x] Validar: «el nitrógeno forma casi ocho de cada diez partes del aire» (≈78 %); «el CO₂ disuelto forma un ácido débil que baja un poco el pH»; el fósforo como ciclo sin fase atmosférica importante; el sulfuro de hidrógeno como indicio de poco oxígeno.
- [x] Revisar `nitrogeno-3.png`: muestra la vaca comiendo, pero no la devolución del nitrógeno al aire (lo cubre el texto de la viñeta).

### Hermes
- [x] Las interacciones tienen propósito: ordenar las etapas del ciclo del agua (con una pista por cada error), pestañas por elemento y un botón «¿Qué le pasa al agua?» que conecta cada ciclo con la calidad del agua.
- [x] Las opciones incorrectas del mini-reto son errores de concepto verosímiles.
- [x] Revisar la analogía de la ruta de bus (tomada de la guía antigua) y la de la gaseosa para el CO₂ en el mar.

## Sección 3: Cantidad y calidad, 2026-09-27

Autorrevisión de Claude Code; queda pendiente la validación de Opencode y Hermes.

### Opencode
- [x] Párrafos de 69 a 73 palabras; narraciones de 29 a 34 s.
- [x] El simulador aplica concentración = masa ÷ volumen (100 mg en 1 a 1000 L, es decir, de 100 a 0,1 mg/L) y advierte que es un modelo simple que no indica si el agua es segura.
- [x] En `cc-1.png` la regla marca un nivel parecido al de la época seca (`cc-2`); la viñeta se apoya en el río ancho y la lluvia. Evaluar si se regenera.

### Hermes
- [x] Interacciones con propósito: clasificar seis frases en «cantidad» o «calidad» (con pista y explicación por frase), tarjetas de «la calidad depende del uso» con contenido real y un simulador que conecta los dos conceptos.
- [x] Revisar las analogías de la cucharada de sal en un vaso frente a una piscina, y del oxígeno disuelto para los peces frente al aire para las personas.

## Sección 4: Parámetros, 2026-09-27

Autorrevisión de Claude Code. Los datos numéricos salen de las guías de laboratorio N.° 1 y N.° 2.

### Opencode
- [x] Párrafos de 46 a 81 palabras; narraciones de 29 a 41 s.
- [x] Color: la diferencia entre color real y aparente es explícita (con texto, cómic y tarjetas). La curva Pt-Co va de 0 a 50 UC con pendiente 0,0010; el ejemplo 0,027 da 27 UC y hay una alerta de «fuera de rango» (se diluye y se multiplica por 2).
- [x] Turbiedad: se explica únicamente con turbidímetro (NTU y formazina); no se mencionan tubos.
- [x] Dureza: total, cálcica (con murexida a pH alto) y magnésica (total − cálcica); en la titulación con EDTA, 12 mL dan 240 mg CaCO₃/L.
- [x] Alcalinidad: 8,5 mL de HCl 0,02 N dan 170 mg CaCO₃/L (la guía usa 8,4 mL, que dan 168; se ajustó a pasos de 0,5 mL).
- [x] Validar contra el texto de la Resolución 2115 de 2007 (no está en la carpeta Normatividad): pH de 6,5 a 9,0 y dureza máxima de 300 mg CaCO₃/L.
- [x] Validar los ejemplos cotidianos de la escala de pH (limón ≈ 2, café ≈ 5, agua de mar ≈ 8, jabón ≈ 9-10).
- [x] Sólidos: 105 °C y 550 °C tomados de la práctica estándar (Standard Methods 2540); no hay guía local de sólidos para contrastar.

### Hermes
- [x] Interacciones con propósito: escala de pH con ejemplos, curva de calibración interactiva, titulaciones virtuales (alcalinidad y dureza) y flujos paso a paso.
- [x] Los tres cómics del usuario dan continuidad con sus materiales anteriores.
- [x] Los cómics antiguos tienen mucho texto y personajes distintos de Gotita (Ana, Tomás, Sara, el superhéroe pH); evaluar si la mezcla de estilos resulta confusa.

> Los pendientes de las secciones 1 a 4 quedaron resueltos (validados, aceptados o corregidos) en la revisión integral que sigue.

## Revisión integral del DAG (Orca `run_596a8f6a4537`), 2026-09-27

Claude Code ejecutó esta revisión aplicando los criterios de Opencode y de Hermes, porque esos agentes no tenían sesiones activas. Análisis automático de los 13 archivos HTML: ningún párrafo pasa de 81 palabras y todos abren con conector y llevan otro en el interior.

### Opencode: brevedad y rigor (O14, O5, O6)
- [x] Opencode: `01-introduccion/index.html` — el dato «el agua dulce apenas llenaría una cucharadita» es ambiguo: el agua dulce total es cerca del 2,5 % del planeta, unos 25 mL en 1 L, y la de ríos y lagos es muchísimo menos — reescribir: «el agua dulce llenaría menos de dos cucharadas, y casi toda está congelada o bajo tierra».
- [x] Opencode: `04-parametros/ph-conductividad.html` — «cada punto multiplica por diez la acidez» choca con la definición de acidez de la página de alcalinidad y acidez (capacidad para neutralizar bases) — decir «multiplica por diez la cantidad de iones hidrógeno libres, que son las partículas que hacen ácida al agua».
- [x] Opencode: `06-normatividad/index.html` — usa «UPC» mientras que la sección 4 usa «UC» — unificar en «UC», explicando una vez que también se llaman unidades platino-cobalto (UPC).
- [x] Opencode: `04-parametros/turbiedad.html` — en Colombia, la Resolución 2115 escribe la unidad como UNT — agregar «(en Colombia también se escribe UNT)».
- [x] Opencode: validado — N₂ ≈ 78 % del aire; ejemplos de la escala de pH dentro de rangos típicos; sólidos a 103-105 °C y 550 °C (SM 2540); DBO₅ en 5 días a 20 °C y a oscuras (SM 5210); DQO con dicromato en unas 2 h (SM 5220); DQO ≥ DBO₅; nitratos y riesgo para bebés; valores típicos de Metcalf y Eddy.
- [x] Opencode: validado — Resolución 2115 de 2007: pH de 6,5 a 9,0; color aparente de 15 como máximo; turbiedad de 2 como máximo; conductividad de 1000 µS/cm; dureza de 300 y alcalinidad de 200 mg CaCO₃/L; cloro residual libre de 0,3 a 2,0 mg/L; E. coli 0 en 100 mL; rangos del IRCA de 0-5, 5,1-14, 14,1-35, 35,1-80 y 80,1-100. El texto oficial no está en la carpeta Normatividad; conviene cotejarlo antes de publicar.
- [x] Opencode: validado — Resolución 631 de 2015: temperatura máxima del vertimiento de 40 °C; se evitó citar límites de DBO₅ y DQO por sector, porque la carpeta solo trae «interpretaciones típicas».

### Hermes: tono y pedagogía (H14, H56)
- [x] Hermes: `01-introduccion/index.html` — el título «¿Sabías que...?» se dirige al lector en segunda persona — cambiar a «Datos para descubrir».
- [x] Hermes: `01-introduccion/index.html` — «Por eso, cuidarla es tarea de todos» suena a sermón — reemplazar por un dato.
- [x] Hermes: `06-normatividad/index.html` — la frase de éxito «Ya puedes revisar resultados…» usa segunda persona — cambiar a «Así se revisan los resultados, igual que lo hace una autoridad sanitaria».
- [x] Hermes: `index.html` — dice que cada parada tiene «laboratorios virtuales», pero las secciones 1 a 3 no los tienen — cambiar a «actividades».
- [x] Hermes: aceptado — los cómics antiguos del usuario (Ana, Tomás, Sara, el superhéroe pH) conviven con Gotita. Aparecen como cómics completos con su título, y su contenido es riguroso; la mezcla de personajes no confunde.
- [x] Hermes: aceptado — las instrucciones de interfaz en imperativo («Toca», «Mueve», «Elige») son microtexto de botones y no párrafos; es una excepción razonable a la regla de tercera persona.
- [x] Hermes: aceptado — las tarjetas de la sección 1 (aire, suelo, agua) presentan las tres esferas que se retoman en la sección 2; tienen propósito.
- [x] Hermes: analogías revisadas (ruta de bus, gaseosa, escudo, fogata, cucharada de sal en una piscina, plato limpio frente a agua de lavar platos, reglamento de fútbol, nota del IRCA «al revés»): son cotidianas, literales y no infantilizan.

**Aplicación (D8):** se aplicaron las 8 correcciones marcadas arriba. Ninguna tocó un párrafo narrado (los cambios quedaron en datos desplegables, leyendas, tarjetas y mensajes), así que no hubo audios que regenerar (C8).

## Revisión del usuario, 2026-09-27: profundidad, dibujos, laboratorios y calculadoras
- [x] Faltaban dibujos (agua dulce, laboratorio, ruta de bus, transpiración) → se agregaron imágenes, un SVG y ejemplos de cálculo.
- [x] «8 de cada 10» no se entendía → ahora se explica con diez cajas de aire y un dibujo; también se explica cómo se absorbe el nitrato y cómo vuelve el nitrógeno al aire (desnitrificación).
- [x] La fotosíntesis era superficial → ahora hay una receta, un flujo, átomos contados y la respiración.
- [x] Eutrofización sin caso real → casos del lago Erie y Toledo (2014) y del embalse del Muña.
- [x] La cantidad de agua solo mencionaba ríos → se agregaron acuíferos, páramos y embalses, la situación de Colombia, una calculadora de caudal y un ejemplo con m³.
- [x] Faltaba cómo se calcula el pH y en qué se diferencia de la acidez y la alcalinidad → ahora hay una comparación, un deslizador de [H⁺] y la fórmula −log.
- [x] Laboratorios virtuales con todos los pasos, titulantes e indicadores rotulados (15 en total).
- [x] Los mini-retos preguntaban cosas no explicadas → se reescribieron con los datos necesarios.
- [x] La curva de calibración solo tenía palabras → ahora trae tabla de datos, pendiente calculada, dilución, cómic y calculadora.
- [x] Parámetros de la norma faltantes → 4 subpáginas nuevas en la sección 5.
- [x] Calculadoras e indicadores → 19 calculadoras más el IRCA paso a paso, la carga contaminante y el índice de biodegradabilidad.
- [x] El menú superior no mostraba todos los botones → ahora se reparte en varias filas.

## Revisión del usuario, 2026-09-27 (2): ICA, decimales y normas
- [x] Faltaba el ICA → calculadora con las fórmulas de la hoja metodológica del IDEAM (GCI-OE-F002, v. 03, 2025): 5 o 6 variables, subíndices, pesos y categorías con sus colores. Incluye un ejemplo resuelto (ICA 0,77, aceptable) y una comparación entre IRCA e ICA.
- [x] «P = 6 ÷ 300 = 0» → los pasos intermedios se mostraban con los decimales del resultado final. Ahora un valor menor que 1 muestra 4 cifras significativas (0,02) y los demás, al menos 2 decimales.
- [x] La línea de tiempo era muy simple → ahora explica la escalera normativa (Constitución, leyes, decretos y resoluciones) y trae 20 normas, cada una con qué regula, cuándo se usa y un ejemplo. Se agregaron una guía «¿qué norma se usa?» y una actividad de clasificar.
- [x] Decreto 774 de 2025 y Resolución 0565 de 2026: el usuario aportó el documento de síntesis «Del Vertimiento al Recurso…». Con él se agregaron bloques sobre los criterios por uso (8 usos, sin uso industrial) y los biosólidos (categorías A y B, análisis por lote, distancias de 100, 30 y 300 m). El oxígeno disuelto mínimo pasó a 5 mg/L (Resolución 0565), que reemplaza los criterios transitorios del Decreto 1594. No se copiaron dos errores del documento: otro nombre para el IDEAM y «Resolución 631 de 2021» (es de 2015).
