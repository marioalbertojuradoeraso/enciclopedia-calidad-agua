# Entrega: Enciclopedia Interactiva sobre Calidad del Agua

**Cómo abrirla:** doble clic en `Enciclopedia/index.html`. Funciona sin servidor; solo la fuente Nunito necesita internet.

## Contenido

| Parada | Archivo | Tiempo | Actividades destacadas |
|---|---|---|---|
| Portada | `index.html` | — | Ruta de las 6 paradas |
| 1. Introducción a la química ambiental | `secciones/01-introduccion/` | 10 min | Cómic de Gotita, tarjetas, mini-reto |
| 2. Hidrosfera y ciclos biogeoquímicos | `secciones/02-hidrosfera-ciclos/` | 25 min | 16 viñetas, ordenar el ciclo del agua, pestañas N/C/P/S |
| 3. Cantidad y calidad | `secciones/03-cantidad-calidad/` | 15 min | Clasificar, simulador de concentración |
| 4. Parámetros (6 subpáginas) | `secciones/04-parametros/` | 40 min | Escala de pH, curva de color, titulaciones de alcalinidad y dureza, 3 cómics del usuario |
| 5. Otros parámetros y tipos de agua | `secciones/05-otros-parametros/` | 20 min | DBO₅ en viñetas, comparador natural/residual |
| 6. Normatividad en Colombia | `secciones/06-normatividad/` | 10 min | Límites de la Resolución 2115, «¿cumple la norma?», IRCA, línea de tiempo |

En total: 13 páginas, 41 narraciones (23 min de audio), unas 50 imágenes generadas, 3 cómics antiguos reutilizados, 29 actividades interactivas y un recorrido de unos 130 minutos.

## Documentos de soporte
- `docs/PRD.md` y `docs/TECH_SPEC.md`: alcance, reglas y componentes.
- `docs/QA.md`: verificación final, sin fallos bloqueantes.
- `REVISIONES.md`: bitácora de Opencode y Hermes, con todas las observaciones cerradas.
- `PEDIDOS_CODEX.md` y `ESTADO_CODEX.md`: historial de multimedia.

## Pendientes conocidos (no bloqueantes)
1. Escuchar las 41 narraciones para confirmar la pronunciación.
2. Revisar el sitio en un teléfono real.
3. Cotejar los valores de la Resolución 2115 de 2007 con su texto oficial, que no está en `Normatividad Agua/`.
4. Nadie la ha publicado todavía: hoy solo existe como archivos locales.

## Ampliación del 2026-09-27
- **Página nueva:** `calculadoras.html`, con 19 calculadoras más el IRCA y el ICA, cada una con su fórmula paso a paso. También está en el menú como «🧮 Calculadoras».
- **15 laboratorios virtuales paso a paso**, con reactivos e indicadores rotulados en el dibujo y un cuaderno de laboratorio.
- **Sección 5:** 4 subpáginas nuevas: `oxigeno-disuelto.html`, `cloro-residual.html`, `microbiologicos.html` e `iones.html`.
- **Profundidad y ejemplos** en las secciones 1 a 4, casos reales de eutrofización y un cómic de la curva de calibración.
- **Generadores guardados** en `scripts/generadores/`; la guía de uso está en `LEEME.md`.
- **ICA del IDEAM** en la sección 6 y en `calculadoras.html`; línea de tiempo con 20 normas, cada una con cuándo se usa.
- **Nuevo pendiente:** cotejar con la norma oficial los puntajes del IRCA y los límites de la Resolución 2115 que se escribieron de memoria (hierro, cloruros, sulfatos, nitritos, nitratos, aluminio y fluoruros).

## Publicación en la web (2026-09-27)
- **Dirección para compartir:** https://marioalbertojuradoeraso.github.io/enciclopedia-calidad-agua/
- **Repositorio:** https://github.com/marioalbertojuradoeraso/enciclopedia-calidad-agua (público, rama `main`, GitHub Pages).
- **Imágenes:** convertidas a WebP (de 78,7 MB a 4,8 MB); los PNG originales quedan en `MQAT/originales_imagenes/`. El sitio completo pesa unos 39 MB.
- **Verificación sobre la dirección publicada:** 19 páginas a 1280 y 390 px, 0 fallas; navegación y audios reproducidos en Edge.
- **Para actualizar:** editar los archivos y luego ejecutar `git add -A`, `git commit -m "…"` y `git push` desde la carpeta `Enciclopedia`. GitHub Pages vuelve a publicar solo, en uno o dos minutos.
