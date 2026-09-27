/* ==========================================================
   Enciclopedia Interactiva sobre Calidad del Agua
   Interactividad compartida por todas las secciones
   ========================================================== */

document.addEventListener("DOMContentLoaded", () => {
  // Imágenes: si Codex aún no entrega el archivo, se muestra el espacio reservado.
  document.querySelectorAll(".imagen img").forEach((img) => {
    const marcar = () => img.closest(".imagen").classList.add("sin-imagen");
    if (img.complete && img.naturalWidth === 0) marcar();
    img.addEventListener("error", marcar);
  });

  // Tarjetas volteables.
  document.querySelectorAll(".tarjeta").forEach((tarjeta) => {
    tarjeta.addEventListener("click", () => {
      const volteada = tarjeta.getAttribute("aria-pressed") === "true";
      tarjeta.setAttribute("aria-pressed", String(!volteada));
    });
  });

  // Botones de descubrir.
  document.querySelectorAll(".btn-descubrir").forEach((boton) => {
    const panel = document.getElementById(boton.getAttribute("aria-controls"));
    boton.addEventListener("click", () => {
      const abierto = boton.getAttribute("aria-expanded") === "true";
      boton.setAttribute("aria-expanded", String(!abierto));
      panel.hidden = abierto;
    });
  });

  // Mini-retos de opción múltiple.
  document.querySelectorAll(".reto").forEach((reto) => {
    const retro = reto.querySelector(".retro");
    reto.querySelectorAll(".opcion").forEach((opcion) => {
      opcion.addEventListener("click", () => {
        const acierto = opcion.dataset.correcta === "true";
        reto.querySelectorAll(".opcion").forEach((o) => o.classList.remove("correcta", "incorrecta"));
        opcion.classList.add(acierto ? "correcta" : "incorrecta");
        retro.textContent = opcion.dataset.retro;
      });
    });
  });

  // Pestañas.
  document.querySelectorAll("[role=tablist]").forEach((lista) => {
    const pestanas = [...lista.querySelectorAll("[role=tab]")];
    const activar = (pestana) => {
      pestanas.forEach((p) => {
        const activa = p === pestana;
        p.setAttribute("aria-selected", String(activa));
        p.tabIndex = activa ? 0 : -1;
        document.getElementById(p.getAttribute("aria-controls")).hidden = !activa;
      });
    };
    pestanas.forEach((p, i) => {
      p.addEventListener("click", () => activar(p));
      p.addEventListener("keydown", (e) => {
        const paso = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
        if (!paso) return;
        const destino = pestanas[(i + paso + pestanas.length) % pestanas.length];
        activar(destino);
        destino.focus();
      });
    });
  });

  // Actividad de ordenar: se tocan las etapas en el orden correcto (data-orden = 1, 2, 3...).
  document.querySelectorAll(".ordenar").forEach((actividad) => {
    const etapas = [...actividad.querySelectorAll(".etapa")];
    const retro = actividad.querySelector(".retro");
    let siguiente = 1;
    const reiniciar = () => {
      siguiente = 1;
      etapas.forEach((e) => { e.disabled = false; e.classList.remove("hecha", "fallo"); e.dataset.puesto = ""; });
      retro.textContent = "";
    };
    etapas.forEach((etapa) => {
      etapa.addEventListener("click", () => {
        etapas.forEach((e) => e.classList.remove("fallo"));
        if (Number(etapa.dataset.orden) === siguiente) {
          etapa.classList.add("hecha");
          etapa.dataset.puesto = siguiente;
          etapa.disabled = true;
          siguiente += 1;
          retro.textContent = siguiente > etapas.length ? actividad.dataset.exito : "";
        } else {
          etapa.classList.add("fallo");
          retro.textContent = etapa.dataset.pista;
        }
      });
    });
    actividad.querySelector(".btn-reiniciar")?.addEventListener("click", reiniciar);
  });

  // Clasificar: cada frase tiene data-respuesta y sus botones data-opcion.
  document.querySelectorAll(".clasificar").forEach((actividad) => {
    const items = [...actividad.querySelectorAll(".item")];
    const marcador = actividad.querySelector(".marcador");
    const contar = () => {
      const bien = items.filter((i) => i.classList.contains("correcto")).length;
      marcador.textContent = bien === items.length ? actividad.dataset.exito : `${bien} de ${items.length}`;
    };
    items.forEach((item) => {
      const retro = item.querySelector(".retro-item");
      item.querySelectorAll("[data-opcion]").forEach((boton) => {
        boton.addEventListener("click", () => {
          if (boton.dataset.opcion === item.dataset.respuesta) {
            item.classList.remove("incorrecto");
            item.classList.add("correcto");
            item.querySelectorAll("[data-opcion]").forEach((b) => { b.disabled = true; });
            retro.textContent = item.dataset.explica;
            contar();
          } else {
            item.classList.add("incorrecto");
            retro.textContent = actividad.dataset.pista;
          }
        });
      });
    });
    contar();
  });

  // Simulador de concentración: la misma masa se reparte en más o menos agua.
  document.querySelectorAll(".simulador").forEach((sim) => {
    const masa = Number(sim.dataset.masa);
    const control = sim.querySelector("input[type=range]");
    const salidaVolumen = sim.querySelector(".volumen");
    const salidaConc = sim.querySelector(".conc");
    const mensaje = sim.querySelector(".mensaje");
    const agua = sim.querySelector(".agua");
    for (let i = 0; i < 40; i++) {
      const punto = document.createElement("span");
      // Secuencia R2: reparte los puntos de forma pareja, sin patrones visibles.
      punto.style.left = `${4 + 88 * ((0.5 + i * 0.7548776662) % 1)}%`;
      punto.style.top = `${4 + 84 * ((0.5 + i * 0.5698402910) % 1)}%`;
      agua.append(punto);
    }
    const formato = (n) => n.toLocaleString("es-CO", { maximumFractionDigits: n >= 10 ? 0 : n >= 1 ? 1 : 2 });
    const actualizar = () => {
      const exponente = Number(control.value);
      const volumen = Math.round(10 ** exponente);
      const conc = masa / volumen;
      salidaVolumen.textContent = formato(volumen);
      salidaConc.textContent = formato(conc);
      agua.style.height = `${15 + 85 * (exponente / Number(control.max))}%`;
      mensaje.textContent = conc >= 20 ? sim.dataset.alta : conc >= 2 ? sim.dataset.media : sim.dataset.baja;
    };
    control.addEventListener("input", actualizar);
    actualizar();
  });

  // Curva de calibración: se elige una absorbancia y se interpola el valor en la recta.
  document.querySelectorAll(".curva").forEach((curva) => {
    const pendiente = Number(curva.dataset.pendiente);
    const maxX = Number(curva.dataset.maxX);
    const maxY = Number(curva.dataset.maxY);
    const control = curva.querySelector("input[type=range]");
    const lecturaAbs = curva.querySelector(".abs");
    const lecturaValor = curva.querySelector(".valor");
    const mensaje = curva.querySelector(".mensaje");
    const guiaH = curva.querySelector(".guia-h");
    const guiaV = curva.querySelector(".guia-v");
    const punto = curva.querySelector(".punto");
    // Área del gráfico dentro del viewBox 0 0 400 300.
    const x0 = 70, x1 = 380, y0 = 260, y1 = 20;
    const px = (x) => x0 + (x / maxX) * (x1 - x0);
    const py = (y) => y0 - (y / maxY) * (y0 - y1);
    const actualizar = () => {
      const abs = Number(control.value);
      const valor = abs / pendiente;
      const dentro = valor <= maxX;
      const xv = px(Math.min(valor, maxX));
      lecturaAbs.textContent = abs.toFixed(3).replace(".", ",");
      lecturaValor.textContent = dentro ? Math.round(valor) : "¿?";
      guiaH.setAttribute("x2", xv);
      guiaH.setAttribute("y1", py(abs));
      guiaH.setAttribute("y2", py(abs));
      guiaV.setAttribute("x1", xv);
      guiaV.setAttribute("x2", xv);
      guiaV.setAttribute("y1", py(Math.min(abs, maxX * pendiente)));
      guiaV.style.display = dentro ? "" : "none";
      punto.setAttribute("cx", xv);
      punto.setAttribute("cy", py(Math.min(abs, maxX * pendiente)));
      mensaje.classList.toggle("fuera", !dentro);
      mensaje.textContent = dentro ? curva.dataset.dentro.replaceAll("{v}", Math.round(valor)) : curva.dataset.fuera;
    };
    control.addEventListener("input", actualizar);
    actualizar();
  });

  // Escala de pH: el control muestra un ejemplo cotidiano para cada valor.
  document.querySelectorAll(".escala-ph").forEach((escala) => {
    const ejemplos = JSON.parse(escala.dataset.ejemplos);
    const control = escala.querySelector("input[type=range]");
    const valor = escala.querySelector(".valor");
    const tipo = escala.querySelector(".tipo");
    const ejemplo = escala.querySelector(".ejemplo");
    const actualizar = () => {
      const ph = Number(control.value);
      valor.textContent = ph;
      tipo.textContent = ph < 7 ? "Ácido" : ph === 7 ? "Neutro" : "Básico";
      ejemplo.textContent = ejemplos[ph] || "";
    };
    control.addEventListener("input", actualizar);
    actualizar();
  });

  // Titulación virtual: se agregan porciones de titulante hasta que el indicador cambia de color.
  document.querySelectorAll(".titulacion").forEach((tit) => {
    const paso = Number(tit.dataset.paso);
    const fin = Number(tit.dataset.fin);
    const factor = Number(tit.dataset.factor);
    const liquido = tit.querySelector(".liquido");
    const gota = tit.querySelector(".btn-gota");
    const vol = tit.querySelector(".vol");
    const mensaje = tit.querySelector(".mensaje");
    const coma = (n) => n.toFixed(1).replace(".", ",");
    let volumen = 0;
    const pintar = () => {
      const cerca = fin - volumen <= 1 && volumen < fin;
      liquido.setAttribute("fill", volumen >= fin ? tit.dataset.final : cerca ? tit.dataset.medio : tit.dataset.inicio);
      vol.textContent = coma(volumen);
      gota.disabled = volumen >= fin;
      mensaje.textContent = volumen >= fin
        ? tit.dataset.textoFin.replaceAll("{v}", coma(volumen)).replaceAll("{r}", Math.round(volumen * factor))
        : cerca ? tit.dataset.textoCerca : volumen > 0 ? tit.dataset.textoAntes : "";
    };
    gota.addEventListener("click", () => { volumen = Math.min(fin, volumen + paso); pintar(); });
    tit.querySelector(".btn-reiniciar").addEventListener("click", () => { volumen = 0; pintar(); });
    pintar();
  });

  // Comparador: barras con valores típicos de distintos tipos de agua.
  document.querySelectorAll(".comparador").forEach((comp) => {
    const valores = JSON.parse(comp.dataset.valores);
    const botones = comp.querySelectorAll("[data-tipo]");
    const mostrar = (tipo) => {
      botones.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.tipo === tipo)));
      comp.querySelectorAll(".fila").forEach((fila) => {
        const v = valores[tipo][fila.dataset.param];
        fila.querySelector(".relleno").style.width = `${Math.max(1, (v / Number(fila.dataset.max)) * 100)}%`;
        fila.querySelector(".cifra").textContent = `${v.toLocaleString("es-CO")} mg/L`;
      });
    };
    botones.forEach((b) => b.addEventListener("click", () => mostrar(b.dataset.tipo)));
    mostrar(botones[0].dataset.tipo);
  });

  // Narraciones: el audio se carga al pulsar el botón; así funciona también al abrir los archivos con doble clic.
  let sonando = null;
  document.querySelectorAll(".btn-audio").forEach((boton) => {
    boton.hidden = false;
    let audio = null;
    const reposo = () => { boton.textContent = "🔊 Escuchar"; };
    boton.addEventListener("click", () => {
      if (!audio) {
        audio = new Audio(boton.dataset.audio);
        audio.addEventListener("ended", reposo);
        audio.addEventListener("pause", reposo);
        audio.addEventListener("error", () => { boton.textContent = "⚠ Audio no disponible"; });
      }
      if (sonando && sonando !== audio) sonando.pause();
      if (audio.paused) {
        boton.textContent = "⏸ Pausar";
        sonando = audio;
        audio.play().catch(() => { boton.textContent = "⚠ El navegador bloqueó el audio"; });
      } else {
        audio.pause();
      }
    });
  });

  // Barra de progreso de lectura.
  const barra = document.querySelector(".progreso span");
  if (barra) {
    const actualizar = () => {
      const total = document.documentElement.scrollHeight - innerHeight;
      barra.style.width = total > 0 ? `${(scrollY / total) * 100}%` : "100%";
    };
    addEventListener("scroll", actualizar, { passive: true });
    actualizar();
  }
});
