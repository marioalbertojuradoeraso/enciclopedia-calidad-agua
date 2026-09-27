# PRD: Enciclopedia Interactiva sobre Calidad del Agua

## Objetivo
Construir una enciclopedia web interactiva, al estilo de Encarta, que se recorra en unas dos horas y deje un aprendizaje completo sobre calidad del agua. El nivel cognitivo es de primaria, pero el tono es universal: nunca se dice que el material es «para niños».

## Alcance (MVP)
1. Introducción a la química ambiental. **Hecha.**
2. Hidrosfera y ciclos biogeoquímicos (agua, N, C, P, S) con mini-cómics. **Hecha.**
3. Cantidad y calidad del agua. **Hecha.**
4. Parámetros: pH y conductividad; color (real frente a aparente, curva de calibración e interpolación); turbiedad (solo turbidímetro); alcalinidad y acidez; dureza (total, cálcica y magnésica); sólidos (totales y volátiles). **Hecha.**
5. Otros parámetros (DBO₅, DQO, nitrógeno total, fósforo) y aguas naturales frente a residuales. **Hecha.**
6. Normatividad colombiana adaptada al lector. **Hecha.**
7. Portada general con la ruta de unas dos horas. **Hecha.**

## Reglas de contenido (obligatorias)
- Tercera persona impersonal; como máximo 90-95 palabras por párrafo; una idea por párrafo.
- Cada párrafo abre con un conector discursivo y lleva otro en su interior.
- Cada término técnico se explica en el mismo párrafo con una analogía cotidiana; nada de metáforas confusas ni relleno académico.
- Narraciones de 45 s como máximo; interacciones con propósito pedagógico.

## Roles
- **Claude Code**: orquestación, desarrollo y maquetación (HTML, CSS y JS).
- **Codex**: imágenes (BFL) y narraciones (ElevenLabs); verificación de multimedia.
- **Opencode**: brevedad y rigor científico; tiene veto sobre el texto.
- **Hermes**: tono pedagógico, analogías y propósito de las interacciones.

## Fuera de alcance
Cuentas de usuario, servidor o base de datos, publicación en internet e idiomas distintos del español.
