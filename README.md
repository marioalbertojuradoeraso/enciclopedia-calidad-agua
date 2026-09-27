# Enciclopedia Interactiva sobre Calidad del Agua

## 👉 [Abrir la enciclopedia](https://marioalbertojuradoeraso.github.io/enciclopedia-calidad-agua/)

Un recorrido de unas dos horas por la química del agua: ciclos biogeoquímicos, cantidad y calidad, parámetros de laboratorio, otros parámetros de la norma y la normatividad colombiana. Incluye cómics, narraciones, 15 laboratorios virtuales paso a paso y 21 calculadoras, entre ellas la del IRCA (Resolución 2115 de 2007) y la del ICA (IDEAM).

**Para verla:** abrir la página publicada con GitHub Pages o, en local, abrir `index.html` con doble clic.

## Estructura
- `index.html`: portada y ruta de las 6 secciones.
- `calculadoras.html`: todas las calculadoras.
- `secciones/`: las 6 secciones; la 4 y la 5 tienen subpáginas.
- `css/`, `js/`: estilos y componentes interactivos (`enciclopedia.js`, `laboratorio.js`).
- `assets/images` (WebP), `assets/audio` (MP3) y `assets/diagrams`.
- `docs/`: PRD, especificación técnica, QA y entrega.
- `scripts/`: verificador de multimedia y generadores de páginas (`scripts/generadores/LEEME.md`).

Las claves de API no forman parte del repositorio: los scripts las leen de archivos locales fuera de esta carpeta.
