# Revisión auditiva

Abrir `audio.html` en el navegador. Contiene las 30 narraciones existentes al generar el panel, con el párrafo de la página asociado a cada botón de audio.

1. Escuchar y comparar con el texto; las unidades pueden estar pronunciadas con palabras.
2. Registrar «conforme» o «requiere corrección», incluyendo el segundo aproximado y la palabra o problema observado.
3. Exportar el JSON para conservar y compartir la revisión con el equipo.

Las notas permanecen en el almacenamiento local del navegador cuando está disponible. En páginas abiertas mediante `file://`, su persistencia depende del navegador: conviene exportar antes de cerrar. No se envía información a servicios externos.

Si cambia el audio o el texto y se regenera el panel, su revisión vuelve a pendiente. Solo se conserva una aprobación local cuando coincide la huella SHA-256 de ambos contenidos. El panel nunca aprueba automáticamente un audio al reproducirlo.

Para incorporar nuevas narraciones: `python Enciclopedia/scripts/crear_revision_audio.py`. Este comando reconstruye el panel y el inventario, no modifica las narraciones ni las páginas fuente.

Comprobado: 30 entradas únicas, textos no vacíos, rutas de audio y páginas existentes, sintaxis JavaScript válida. No se ha realizado revisión auditiva ni prueba de interfaz en navegador.
