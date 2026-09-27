# Coordinación de tareas de Codex

## Entregado — panel independiente de revisión auditiva

Codex prepara `revision/audio.html`: audios existentes junto a sus textos, observaciones y exportación de resultados. No genera voces ni modifica páginas de contenido. El panel no marca ningún audio como escuchado automáticamente.

Entrega: 30 audios inventariados, con texto fuente, filtros, observaciones locales y exportación JSON. Huella del audio y texto para invalidar aprobaciones de versiones anteriores. Rutas y sintaxis comprobadas. Instrucciones en `revision/LEEME.md`. La escucha permanece pendiente.

## Entregado — verificación de la sección 4

Codex atiende el pedido de Claude: ampliar la revisión a todas las subpáginas HTML, imágenes PNG/JPG y narraciones de parámetros. No genera ni reemplaza los recursos de Claude.

Resultado: 7 páginas, 112 referencias locales comprobadas, 16 imágenes válidas (13 PNG y 3 JPG), 19 MP3 entre 28,71 y 40,57 s. Cero referencias rotas. Informe: `assets/verificacion-04-parametros.json`. Pronunciación y calidad perceptual no evaluadas.

## Entregado — recurso independiente para color

Codex toma la creación de `assets/diagrams/04-parametros/color-interpolacion.svg` y `assets/diagrams/04-parametros/color-interpolacion.html`: gráfico preciso y versión interactiva de interpolación de color. Usa los datos didácticos de la guía ajustada (0–50 UC, absorbancia 0–0,050). No modifica la página de parámetros ni genera las viñetas o narraciones que Claude está preparando.

Claude Code puede continuar con la maquetación, cómics y narraciones. Estos archivos se entregan como recursos opcionales integrables, sin sustituir recursos existentes.

Regla de coordinación: antes de generar recursos, consultar los pedidos y este registro. Si otro agente ya trabaja en un recurso, elegir otra tarea; no esperar a que aparezca el archivo para descubrir el cruce.

Entrega: ambos archivos creados. Instrucciones de integración y trazabilidad en `assets/diagrams/04-parametros/INTEGRACION.md`. SVG válido y lógica interactiva comprobada con los extremos 0/50 UC, ejemplo 27 UC y botón 40 UC. No se ha realizado comprobación visual en navegador.
