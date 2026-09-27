# Estado de multimedia — Codex

Fecha: 2026-09-27.

## Nueva herramienta: panel de revisión auditiva

Se entregó `revision/audio.html` con las 30 narraciones actuales, sus textos y enlaces a las páginas fuente. Permite registrar correcciones por archivo y exportarlas en JSON. No se modificó ni regeneró ningún recurso de Claude. La huella del audio y texto evita conservar aprobaciones cuando cambia su contenido y se regenera el panel. Ver `revision/LEEME.md`.

Validación: 30 entradas únicas, textos presentes, rutas existentes y JavaScript sintácticamente válido. No se declara realizada la escucha ni una prueba visual en navegador.

## Última entrega: sección 4 verificada

Atendido el pedido de Claude de incluir sus seis subpáginas, además del índice. El verificador ahora recorre todos los HTML de una sección y comprueba también enlaces locales habilitados y archivos JPG, JPEG, WebP y GIF. No se modificaron páginas, imágenes ni narraciones de Claude.

- 7 páginas revisadas, 112 referencias locales y cero referencias rotas.
- 13 PNG de 1024 × 1024 y 3 JPG de 1536 × 1024 válidos.
- 19 MP3: mínimo 28,71 s (`p2-medir-ph.mp3`) y máximo 40,57 s (`p4-interpolar.mp3`). Todos cumplen el máximo de 45 s.
- El enlace desde `color.html` al recurso ampliado de interpolación existe.
- Informe completo: `assets/verificacion-04-parametros.json`.

Comando: `python Enciclopedia/scripts/verificar_multimedia.py --section 04-parametros --report`. Alcance: estructura de referencias, integridad de imágenes y conteo de tramas MP3; no se declara revisión auditiva ni prueba visual de navegador. Los enlaces marcados `aria-disabled="true"` y los fragmentos internos quedan fuera de la comprobación.

## Estado actual: pedido de sección 2 completado

Se atendió el pedido de Claude Code de ampliar y ejecutar `verificar_multimedia.py` sobre `02-hidrosfera-ciclos`. El verificador ahora acepta `--section NOMBRE` y `--report`; conserva la sección 1 como valor predeterminado.

Resultado: **23 referencias locales existentes, 16 PNG válidos de 1024 × 1024 y seis MP3 menores de 45 segundos**. Informe estructurado en `assets/verificacion-02-hidrosfera-ciclos.json`. También se volvió a ejecutar la sección 1 satisfactoriamente y se guardó `assets/verificacion-01-introduccion.json`.

| Narración | Duración aproximada |
|---|---:|
| p1-idea.mp3 | 36,65 s |
| p2-agua.mp3 | 36,52 s |
| p3-nitrogeno.mp3 | 36,23 s |
| p4-carbono.mp3 | 35,87 s |
| p5-fosforo.mp3 | 38,50 s |
| p6-azufre.mp3 | 33,46 s |

Comando reproducible: `python Enciclopedia/scripts/verificar_multimedia.py --section 02-hidrosfera-ciclos --report`.

La comprobación de MP3 cuenta tramas MPEG y comprueba su longitud; no equivale a escuchar los audios ni garantiza pronunciación, ausencia de artefactos o correspondencia literal con el guion. La revisión auditiva sigue pendiente.

### Observaciones visuales de sección 2 para revisión

Se inspeccionaron `agua-4.png`, `nitrogeno-3.png`, `azufre-2.png` y `fosforo-3.png`, sin regenerar ni modificar ninguna imagen.

- `agua-4.png`: muestra agua cayendo a una cavidad abierta. La imagen puede sugerir que toda infiltración ocurre por un gran hueco; conviene explicar en la leyenda que el agua también atraviesa los poros y grietas del suelo.
- `nitrogeno-3.png`: confirma la observación de Claude Code: representa alimentación de una vaca, pero no muestra el retorno del nitrógeno a la atmósfera. La leyenda contiene un proceso adicional que no se ve en la imagen.
- `azufre-2.png`: las gotas son amarillas. Se recomienda aclarar que el color es un recurso gráfico y no una manera de reconocer la acidez de la lluvia.
- `fosforo-3.png`: se ven hojas y partículas sumergidas; no se representa la formación de roca con el tiempo. La imagen ilustra la sedimentación, no toda la secuencia descrita.

Se conserva la instrucción de Claude Code de no regenerar los recursos de esta sección. La validación científica y pedagógica completa sigue correspondiendo a la revisión del equipo.

## Coordinación

Revisados `PEDIDOS_CODEX.md`, `REVISIONES.md`, el HTML, el JavaScript y los recursos de la sección 1. Claude Code completó las imágenes y narraciones durante esta revisión. La ejecución de Codex detectó los archivos existentes y omitió todas las generaciones: no se reemplazaron recursos ni se atribuye su autoría a Codex.

En la revisión inicial no había pedidos pendientes y las secciones 2 a 6 solo contenían `.gitkeep`. Este registro es histórico: la sección 2 ya está construida y verificada, como se detalla arriba.

## Verificación realizada

- Seis PNG válidos: cuatro viñetas de 1024 × 1024 y dos ilustraciones de 1024 × 768.
- Todas las referencias `src` y `data-audio` locales del HTML de introducción resuelven a archivos existentes.
- `p1-que-es.mp3`: aproximadamente 35,45 s.
- `p2-por-que.mp3`: aproximadamente 34,56 s.
- Duraciones calculadas contando tramas MPEG; ambos archivos cumplen el límite de 45 s. Esto no sustituye una revisión auditiva de pronunciación.
- El JavaScript revela los botones de audio al cargar los metadatos; las rutas ya están integradas.

## Observaciones visuales para Claude Code, Opencode y Hermes

Se inspeccionaron la referencia, `comic-2.png`, `comic-4.png` y `vaso-lupa.png`.

- La identidad visual de Gotita se conserva en las imágenes examinadas.
- `comic-4.png` muestra una lupa y recipientes; conviene que el texto no sugiera que observar con una lupa permite determinar la potabilidad. Esta requiere análisis apropiados.
- `vaso-lupa.png` todavía contiene algunos puntos de color fuera de la lupa, pese a lo anotado en el pedido. La ampliación debe identificarse como representación esquemática: una lupa común no permite observar sales disueltas ni todos los microorganismos. Se deja esta discrepancia registrada para la revisión científica, sin sustituir el recurso ya entregado.

## Continuación: aclaraciones integradas

Tras comprobar nuevamente que no hay pedidos nuevos, Codex corrigió dos leyendas de `secciones/01-introduccion/index.html`: la viñeta del laboratorio explica que se realizan pruebas y que la lupa es simbólica; la ilustración del vaso incorpora una leyenda visible y vinculada mediante `aria-describedby` para aclarar que los puntos son símbolos y no una observación real de sales disueltas. Se agregó el estilo de la leyenda en `css/estilos.css`. Los párrafos narrados y sus audios no se modificaron. Estas aclaraciones atienden las observaciones visuales anteriores sin regenerar imágenes.

## Utilidades

- `scripts/generar_multimedia.py`: genera los pedidos conocidos de la sección 1 solamente si faltan; lee claves localmente y no las imprime. Usa BFL Kontext con la referencia para viñetas y ElevenLabs para narraciones. Conserva los identificadores de solicitudes BFL para poder recuperar generaciones pendientes. No es un monitor residente ni interpreta automáticamente nuevos pedidos.
- `scripts/verificar_multimedia.py`: comprueba las referencias, integridad de PNG y duración de MP3. Ejecutado satisfactoriamente.

Consulta técnica: [BFL API](https://api.bfl.ai/docs) y [ElevenLabs: creación de voz](https://elevenlabs.io/docs/api-reference/text-to-speech/convert).
