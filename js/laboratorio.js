/* ==========================================================
   Enciclopedia Interactiva sobre Calidad del Agua
   Laboratorios virtuales paso a paso, calculadoras y calculadora de IRCA.
   Cada componente lee su configuración de un <script type="application/json"> interno.
   ========================================================== */

(() => {
  const SVGNS = "http://www.w3.org/2000/svg";
  const leerDatos = (el) => JSON.parse(el.querySelector('script[type="application/json"]').textContent);
  const numero = (n, dec = 2) => Number(n).toLocaleString("es-CO", { maximumFractionDigits: dec, minimumFractionDigits: 0 });
  const esperar = (ms) => new Promise((r) => setTimeout(r, ms));

  // ---------------------------------------------------------------- escenas SVG
  // Todas comparten: equipo, pantalla, unidad, vaso (líneas de etiqueta) y color del líquido.
  function textoMultilinea(x, y, lineas, clase, alto = 14) {
    return lineas.map((l, i) => `<text x="${x}" y="${y + i * alto}" class="${clase}">${l}</text>`).join("");
  }

  const ESCENAS = {
    medidor: (d) => `
      <rect x="20" y="30" width="150" height="110" rx="14" class="equipo-caja"/>
      <rect x="36" y="48" width="118" height="50" rx="6" class="pantalla-fondo"/>
      <text x="95" y="82" class="pantalla-texto" data-pantalla>${d.pantalla || "—"}</text>
      <text x="95" y="118" class="equipo-nombre">${d.equipo}</text>
      <text x="95" y="132" class="equipo-unidad" data-unidad>${d.unidad || ""}</text>
      <path d="M170 90 C 220 90 230 60 250 60 L 250 150" class="cable"/>
      <rect x="243" y="120" width="14" height="110" rx="6" class="electrodo"/>
      <path d="M200 170 L200 280 Q200 292 212 292 L288 292 Q300 292 300 280 L300 170" class="vaso"/>
      <path d="M202 205 L298 205 L298 280 Q298 290 288 290 L212 290 Q202 290 202 280 Z" class="liquido" data-liquido fill="${d.liquido || "#cfeefc"}"/>
      <g data-vaso>${textoMultilinea(250, 312, d.vaso || [], "etiqueta")}</g>`,

    titulacion: (d) => `
      <rect x="30" y="296" width="170" height="10" rx="4" class="soporte"/>
      <rect x="44" y="20" width="8" height="280" class="soporte"/>
      <rect x="44" y="60" width="60" height="8" class="soporte"/>
      <rect x="100" y="14" width="18" height="190" rx="4" class="bureta"/>
      <rect x="102" y="40" width="14" height="162" class="bureta-liquido" data-bureta-liquido/>
      <path d="M104 204 L114 204 L110 222 L108 222 Z" class="bureta"/>
      <circle cx="109" cy="232" r="4" class="gota" data-gota opacity="0"/>
      <text x="126" y="30" class="etiqueta etiqueta-izq">Bureta: ${d.titulante || ""}</text>
      <text x="126" y="48" class="etiqueta etiqueta-izq" data-vol>V = 0,00 mL</text>
      <path d="M96 238 L96 262 L66 296 L152 296 L122 262 L122 238" class="vaso"/>
      <path d="M80 280 L138 280 L150 294 L68 294 Z" class="liquido" data-liquido fill="${d.liquido || "#f3f6f8"}"/>
      <g data-vaso>${textoMultilinea(158, 236, d.vaso || [], "etiqueta etiqueta-izq")}</g>
      <text x="138" y="84" class="etiqueta etiqueta-izq">Indicadores y reactivos:</text><g>${textoMultilinea(138, 102, (d.indicadores || []).map((i) => "💧 " + i), "etiqueta etiqueta-izq", 17)}</g>`,

    caja: (d) => `
      <rect x="40" y="70" width="240" height="160" rx="16" class="equipo-caja"/>
      <rect x="60" y="90" width="120" height="54" rx="6" class="pantalla-fondo"/>
      <text x="120" y="126" class="pantalla-texto" data-pantalla>${d.pantalla || "—"}</text>
      <text x="120" y="164" class="equipo-nombre">${d.equipo}</text>
      <text x="120" y="180" class="equipo-unidad" data-unidad>${d.unidad || ""}</text>
      <rect x="205" y="60" width="50" height="16" rx="4" class="equipo-caja"/>
      <rect x="215" y="20" width="30" height="62" rx="4" class="vaso"/>
      <rect x="217" y="36" width="26" height="44" class="liquido" data-liquido fill="${d.liquido || "#e9f7fb"}"/>
      <g data-vaso>${textoMultilinea(230, 252, d.vaso || [], "etiqueta")}</g>`,

    filtracion: (d) => `
      <path d="M40 60 L140 60 L110 130 L70 130 Z" class="vaso"/>
      <rect x="84" y="130" width="12" height="40" class="vaso"/>
      <path d="M50 170 L130 170 L140 290 L40 290 Z" class="vaso"/>
      <text x="90" y="310" class="etiqueta">Embudo con membrana de 0,45 µm</text>
      <circle cx="245" cy="170" r="70" class="placa"/>
      <circle cx="245" cy="170" r="60" class="agar" data-liquido fill="${d.liquido || "#b8323f"}"/>
      <g data-colonias></g>
      <text x="245" y="262" class="etiqueta">${d.equipo}</text>
      <rect x="185" y="30" width="120" height="34" rx="6" class="pantalla-fondo"/>
      <text x="245" y="54" class="pantalla-texto pantalla-chica" data-pantalla>${d.pantalla || "—"}</text>
      <g data-vaso>${textoMultilinea(245, 286, d.vaso || [], "etiqueta")}</g>`,
  };

  function dibujarColonias(svg, n) {
    const g = svg.querySelector("[data-colonias]");
    if (!g) return;
    g.innerHTML = "";
    for (let i = 0; i < n; i++) {
      const a = (0.5 + i * 0.7548776662) % 1, b = (0.5 + i * 0.5698402910) % 1;
      const r = 50 * Math.sqrt(a), t = 2 * Math.PI * b;
      const c = document.createElementNS(SVGNS, "circle");
      c.setAttribute("cx", 245 + r * Math.cos(t));
      c.setAttribute("cy", 170 + r * Math.sin(t));
      c.setAttribute("r", 4);
      c.setAttribute("class", i % 5 === 0 ? "colonia-azul" : "colonia");
      g.append(c);
    }
  }

  // ---------------------------------------------------------------- laboratorio paso a paso
  const montarLab = (lab) => {
    const d = leerDatos(lab);
    lab.insertAdjacentHTML("beforeend", `
      <div class="lab-escena"><svg viewBox="0 0 320 330" role="img" aria-label="${d.equipo}">${ESCENAS[d.escena](d)}</svg></div>
      <div class="lab-panel">
        <ol class="lab-pasos">${d.pasos.map((p) => `<li>${p.titulo}</li>`).join("")}</ol>
        <div class="lab-actual" aria-live="polite">
          <p class="lab-texto"></p>
          <div class="lab-botones"><button type="button" class="lab-boton"></button><button type="button" class="btn-reiniciar">Reiniciar</button></div>
        </div>
        <table class="lab-cuaderno"><caption>Cuaderno de laboratorio</caption><tbody></tbody></table>
        <div class="lab-resultado"></div>
      </div>`);
    const svg = lab.querySelector("svg");
    const items = [...lab.querySelectorAll(".lab-pasos li")];
    const texto = lab.querySelector(".lab-texto");
    const boton = lab.querySelector(".lab-boton");
    const cuaderno = lab.querySelector(".lab-cuaderno tbody");
    const resultado = lab.querySelector(".lab-resultado");
    const pantalla = svg.querySelector("[data-pantalla]");
    const liquido = svg.querySelector("[data-liquido]");
    const vol = svg.querySelector("[data-vol]");
    const buretaLiq = svg.querySelector("[data-bureta-liquido]");
    const gota = svg.querySelector("[data-gota]");
    const vaso = svg.querySelector("[data-vaso]");
    let paso = 0;
    let ocupado = false;

    const ponerVolumen = (v) => {
      if (!vol) return;
      vol.textContent = `V = ${numero(v, 2)} mL`;
      const cap = d.capacidadBureta || 25;
      buretaLiq.setAttribute("y", 40 + 162 * Math.min(v, cap) / cap);
      buretaLiq.setAttribute("height", 162 * (1 - Math.min(v, cap) / cap));
    };

    const mostrar = () => {
      items.forEach((li, i) => { li.classList.toggle("hecho", i < paso); li.classList.toggle("actual", i === paso); });
      if (paso < d.pasos.length) {
        texto.innerHTML = d.pasos[paso].texto;
        boton.textContent = d.pasos[paso].boton;
        boton.hidden = false;
      } else {
        texto.innerHTML = d.final || "Práctica terminada.";
        boton.hidden = true;
      }
    };

    const aplicar = async (e) => {
      if (e.vaso && vaso) vaso.innerHTML = textoMultilinea(vaso.querySelector("text")?.getAttribute("x") || 250, Number(vaso.querySelector("text")?.getAttribute("y") || 312), e.vaso, vaso.querySelector("text")?.getAttribute("class") || "etiqueta");
      if (e.unidad !== undefined) svg.querySelector("[data-unidad]").textContent = e.unidad;
      if (e.liquido && !e.titular) liquido.setAttribute("fill", e.liquido);
      if (e.colonias !== undefined) dibujarColonias(svg, e.colonias);
      if (e.animar) {
        const { de, a, decimales = 1, pasos = 14, sufijo = "" } = e.animar;
        for (let i = 0; i <= pasos; i++) {
          const f = i / pasos;
          const v = de + (a - de) * (1 - Math.pow(1 - f, 3));
          pantalla.textContent = numero(v, decimales).replace(/(,\d*?)$/, "$1") + sufijo;
          await esperar(90);
        }
        pantalla.textContent = numero(a, decimales) + sufijo;
      }
      if (e.titular) {
        // Titulación: el volumen sube; el color cambia al llegar al punto final.
        const { hasta, colorCerca, colorFinal } = e.titular;
        const desde = e.titular.desde || 0;
        const pasos = 24;
        for (let i = 1; i <= pasos; i++) {
          const v = desde + (hasta - desde) * i / pasos;
          ponerVolumen(v);
          gota.setAttribute("opacity", i % 2 ? 1 : 0);
          if (colorCerca && i >= pasos - 3 && i < pasos) liquido.setAttribute("fill", colorCerca);
          await esperar(i > pasos - 5 ? 260 : 70);
        }
        gota.setAttribute("opacity", 0);
        liquido.setAttribute("fill", colorFinal);
      }
      if (e.volumen !== undefined) ponerVolumen(e.volumen);
      if (e.pantalla !== undefined) pantalla.textContent = e.pantalla;
      if (e.registro) cuaderno.insertAdjacentHTML("beforeend", `<tr><th scope="row">${e.registro[0]}</th><td>${e.registro[1]}</td></tr>`);
      if (e.resultado) resultado.innerHTML = e.resultado;
    };

    boton.addEventListener("click", async () => {
      if (ocupado || paso >= d.pasos.length) return;
      ocupado = true;
      boton.disabled = true;
      await aplicar(d.pasos[paso]);
      paso += 1;
      boton.disabled = false;
      ocupado = false;
      mostrar();
    });

    lab.querySelector(".btn-reiniciar").addEventListener("click", () => {
      if (ocupado) return;
      lab.querySelectorAll(":scope > :not(script)").forEach((n) => n.remove());
      montarLab(lab);
    });

    if (vol) ponerVolumen(0);
    mostrar();
  };
  document.querySelectorAll(".lab").forEach(montarLab);

  // ---------------------------------------------------------------- calculadoras con pasos
  const evaluar = (expr, vars) => Function(...Object.keys(vars), `return (${expr});`)(...Object.values(vars));
  const rellenar = (plantilla, vars, dec) =>
    plantilla
      .replace(/\{=([^}]+)\}/g, (_, expr) => numeroPaso(evaluar(expr, vars), dec))
      .replace(/\{(\w+)\}/g, (_, k) => (k in vars ? numeroVariable(vars[k]) : `{${k}}`));
  // Los pasos intermedios nunca se redondean a cero: los menores que 1 muestran 4 cifras significativas
  // (6 ÷ 300 = 0,02) y los demás, al menos 2 decimales. Solo el resultado final usa los decimales pedidos.
  const numeroPaso = (v, dec) => (v !== 0 && Math.abs(v) < 1
    ? v.toLocaleString("es-CO", { maximumSignificantDigits: 4 })
    : numero(v, Math.max(dec, 2)));
  // Los valores muy pequeños (como 0,00004 mol/L) se muestran completos, con tres cifras significativas.
  const numeroVariable = (v) => (v !== 0 && Math.abs(v) < 0.01
    ? v.toLocaleString("es-CO", { maximumSignificantDigits: 3 })
    : numero(v, 4));

  document.querySelectorAll(".calculadora").forEach((calc) => {
    const d = leerDatos(calc);
    const ident = calc.id || "calc" + Math.random().toString(36).slice(2, 7);
    calc.insertAdjacentHTML("beforeend", `
      ${d.titulo ? `<p class="calc-titulo">🧮 ${d.titulo}</p>` : ""}
      <div class="calc-entradas">${d.entradas.map((e) => `
        <label class="calc-campo" for="${ident}-${e.id}">
          <span>${e.etiqueta}</span>
          <span class="calc-valor"><input id="${ident}-${e.id}" type="number" inputmode="decimal" step="${e.paso || "any"}" value="${e.valor}" data-var="${e.id}"><small>${e.unidad || ""}</small></span>
        </label>`).join("")}
      </div>
      <ol class="calc-pasos"></ol>
      <p class="calc-resultado"></p>
      <p class="calc-interpretacion"></p>`);
    const entradas = [...calc.querySelectorAll("input[data-var]")];
    const pasos = calc.querySelector(".calc-pasos");
    const res = calc.querySelector(".calc-resultado");
    const interp = calc.querySelector(".calc-interpretacion");
    const actualizar = () => {
      const vars = Object.fromEntries(entradas.map((i) => [i.dataset.var, Number(i.value)]));
      const dec = d.resultado.decimales ?? 2;
      let valor;
      try { valor = evaluar(d.resultado.expr, vars); } catch { valor = NaN; }
      if (!Number.isFinite(valor)) {
        pasos.innerHTML = "";
        res.textContent = "Revisa los datos: hay un valor vacío o una división entre cero.";
        interp.textContent = "";
        return;
      }
      pasos.innerHTML = d.pasos.map((p) => `<li>${rellenar(p, vars, dec)}</li>`).join("");
      res.innerHTML = `${d.resultado.etiqueta}: <strong>${numero(valor, dec)}</strong> ${d.resultado.unidad}`;
      const regla = (d.interpretar || []).find((r) => r.hasta === null || valor <= r.hasta);
      interp.textContent = regla ? rellenar(regla.texto, { ...vars, R: valor }, dec) : "";
      interp.dataset.nivel = regla?.nivel || "";
    };
    entradas.forEach((i) => i.addEventListener("input", actualizar));
    actualizar();
  });

  // ---------------------------------------------------------------- pH y concentración de H⁺
  document.querySelectorAll(".calc-ph").forEach((c) => {
    const control = c.querySelector("input[type=range]");
    const salida = c.querySelector(".h-decimal");
    const ph = c.querySelector(".ph-valor");
    const ceros = c.querySelector(".ph-ceros");
    const comparar = c.querySelector(".ph-comparar");
    const actualizar = () => {
      const n = Number(control.value);
      ph.textContent = n;
      salida.textContent = n === 0 ? "1" : "0," + "0".repeat(n - 1) + "1";
      ceros.textContent = n === 0 ? "El 1 queda antes de la coma." : `El 1 queda en la posición ${n} después de la coma.`;
      const d7 = 7 - n;
      comparar.textContent = d7 > 0 ? `Tiene ${numero(10 ** d7, 0)} veces más iones H⁺ que el agua neutra (pH 7).`
        : d7 < 0 ? `Tiene ${numero(10 ** -d7, 0)} veces menos iones H⁺ que el agua neutra (pH 7).` : "Es el punto neutro: iguales H⁺ y OH⁻.";
    };
    control.addEventListener("input", actualizar);
    actualizar();
  });

  // ---------------------------------------------------------------- ICA del IDEAM (hoja metodológica GCI-OE-F002, v. 03, 2025)
  const SUBINDICES = {
    od: (ps) => (ps <= 100 ? 1 - (1 - 0.01 * ps) : 1 - (0.01 * ps - 1)),
    sst: (x) => (x <= 4.5 ? 1 : x >= 320 ? 0 : 1 - (-0.02 + 0.003 * x)),
    dqo: (x) => (x <= 20 ? 0.91 : x <= 25 ? 0.71 : x <= 40 ? 0.51 : x <= 80 ? 0.26 : 0.125),
    ce: (x) => Math.max(0, 1 - 10 ** (-3.26 + 1.34 * Math.log10(x))),
    ph: (x) => (x < 4 ? 0.1 : x <= 7 ? 0.02628419 * Math.exp(x * 0.520025) : x <= 8 ? 1 : x <= 11 ? Math.exp((x - 8) * -0.5187742) : 0.1),
    ntpt: (r) => (r >= 15 && r <= 20 ? 0.8 : r > 10 && r < 15 ? 0.6 : r > 5 && r <= 10 ? 0.35 : 0.15),
  };
  const CATEGORIAS_ICA = [[0.25, "Muy malo", "#cc0000"], [0.5, "Malo", "#ff9900"], [0.7, "Regular", "#ffff00"], [0.9, "Aceptable", "#249406"], [1.0, "Bueno", "#0f45f1"]];
  document.querySelectorAll(".ica").forEach((ica) => {
    const campos = [
      ["od", "Oxígeno disuelto medido", "mg/L", 6.0], ["cp", "Oxígeno de saturación (según temperatura y altitud)", "mg/L", 7.5],
      ["sst", "Sólidos suspendidos totales (SST)", "mg/L", 50], ["dqo", "DQO", "mg/L", 30],
      ["ce", "Conductividad eléctrica", "µS/cm", 120], ["ph", "pH", "unidades", 7.5],
      ["nt", "Nitrógeno total (solo para 6 variables)", "mg/L", 2.4], ["pt", "Fósforo total (solo para 6 variables)", "mg/L", 0.15],
    ];
    ica.insertAdjacentHTML("beforeend", `
      <p class="calc-titulo">🧮 Índice de Calidad del Agua (ICA) del IDEAM</p>
      <label style="font-weight:700"><input type="checkbox" class="ica-seis"> Usar 6 variables (incluye la relación NT/PT)</label>
      <div class="calc-entradas" style="margin-top:12px">${campos.map(([k, e, u, v]) => `
        <label class="calc-campo"><span>${e}</span><span class="calc-valor"><input type="number" step="any" value="${v}" data-v="${k}"><small>${u}</small></span></label>`).join("")}
      </div>
      <div class="tabla-desplazable" style="margin-top:16px"><table class="tabla-datos"><thead><tr><th>Variable</th><th>Dato</th><th>Subíndice (0 a 1)</th><th>Peso</th><th>Aporte = peso × subíndice</th></tr></thead><tbody class="ica-filas"></tbody></table></div>
      <p class="calc-resultado"></p>
      <div class="barra-clases cinco ica-niveles" style="grid-template-columns:25fr 25fr 20fr 20fr 10fr">
        <div style="background:#cc0000;color:#fff"><strong>Muy malo</strong>0 a 0,25</div><div style="background:#ff9900"><strong>Malo</strong>0,26 a 0,50</div>
        <div style="background:#ffff00"><strong>Regular</strong>0,51 a 0,70</div><div style="background:#249406;color:#fff"><strong>Aceptable</strong>0,71 a 0,90</div>
        <div style="background:#0f45f1;color:#fff"><strong>Bueno</strong>0,91 a 1</div>
      </div>`);
    const val = (k) => Number(ica.querySelector(`[data-v="${k}"]`).value);
    const seis = ica.querySelector(".ica-seis");
    const actualizar = () => {
      const ps = (val("od") / val("cp")) * 100;
      const ratio = val("nt") / val("pt");
      const w = seis.checked ? { od: 0.17, sst: 0.17, dqo: 0.17, ce: 0.17, ph: 0.15, ntpt: 0.17 } : { od: 0.2, sst: 0.2, dqo: 0.2, ce: 0.2, ph: 0.2 };
      const filas = [
        ["od", "Oxígeno disuelto", `${numero(val("od"), 2)} ÷ ${numero(val("cp"), 2)} × 100 = ${numero(ps, 1)} % de saturación`, ps],
        ["sst", "SST", `${numero(val("sst"), 1)} mg/L`, val("sst")],
        ["dqo", "DQO", `${numero(val("dqo"), 1)} mg/L`, val("dqo")],
        ["ce", "Conductividad", `${numero(val("ce"), 0)} µS/cm`, val("ce")],
        ["ph", "pH", numero(val("ph"), 2), val("ph")],
        ["ntpt", "NT/PT", `${numero(val("nt"), 2)} ÷ ${numero(val("pt"), 3)} = ${numero(ratio, 1)}`, ratio],
      ].filter(([k]) => k in w);
      let total = 0;
      ica.querySelector(".ica-filas").innerHTML = filas.map(([k, nombre, dato, x]) => {
        const i = SUBINDICES[k](x);
        total += w[k] * i;
        return `<tr><th scope="row">${nombre}</th><td>${dato}</td><td>${numero(i, 3)}</td><td>${numero(w[k], 2)}</td><td>${numero(w[k] * i, 3)}</td></tr>`;
      }).join("");
      const cat = CATEGORIAS_ICA.find(([h]) => total <= h + 0.005) || CATEGORIAS_ICA[4];
      ica.querySelector(".calc-resultado").innerHTML = `ICA = suma de aportes = <strong>${numero(total, 2)}</strong>: calidad <strong>${cat[1].toLowerCase()}</strong>.`;
      ica.querySelectorAll(".ica-niveles div").forEach((d) => d.classList.toggle("activo", d.textContent.startsWith(cat[1])));
    };
    ica.addEventListener("input", actualizar);
    actualizar();
  });

  // ---------------------------------------------------------------- IRCA (Resolución 2115 de 2007)
  document.querySelectorAll(".irca").forEach((irca) => {
    const d = leerDatos(irca);
    irca.insertAdjacentHTML("beforeend", `
      <div class="tabla-desplazable"><table class="tabla-datos irca-tabla">
        <thead><tr><th>Analizar</th><th>Parámetro</th><th>Valor aceptable</th><th>Resultado</th><th>Puntaje de riesgo</th><th>¿Cumple?</th></tr></thead>
        <tbody>${d.parametros.map((p, i) => `
          <tr data-i="${i}">
            <td><input type="checkbox" ${p.valor !== null ? "checked" : ""} aria-label="Analizar ${p.nombre}"></td>
            <th scope="row">${p.nombre}</th>
            <td>${p.min !== undefined ? numero(p.min) + " a " + numero(p.max) : "≤ " + numero(p.max)} ${p.unidad}</td>
            <td><input type="number" step="any" value="${p.valor ?? ""}" aria-label="Resultado de ${p.nombre}"></td>
            <td>${numero(p.puntaje, 1)}</td>
            <td class="irca-estado"></td>
          </tr>`).join("")}
        </tbody></table></div>
      <ol class="calc-pasos"></ol>
      <p class="calc-resultado"></p>
      <div class="barra-clases cinco irca-niveles">
        <div><strong>Sin riesgo</strong>0 a 5</div><div><strong>Bajo</strong>5,1 a 14</div><div><strong>Medio</strong>14,1 a 35</div><div><strong>Alto</strong>35,1 a 80</div><div><strong>Inviable</strong>80,1 a 100</div>
      </div>`);
    const filas = [...irca.querySelectorAll("tbody tr")];
    const pasos = irca.querySelector(".calc-pasos");
    const res = irca.querySelector(".calc-resultado");
    const niveles = [...irca.querySelectorAll(".irca-niveles div")];
    const actualizar = () => {
      let total = 0, malos = 0;
      const fallan = [];
      filas.forEach((fila, i) => {
        const p = d.parametros[i];
        const activo = fila.querySelector('input[type="checkbox"]').checked;
        const valor = Number(fila.querySelector('input[type="number"]').value);
        const estado = fila.querySelector(".irca-estado");
        fila.classList.toggle("inactiva", !activo);
        if (!activo) { estado.textContent = "—"; return; }
        const cumple = valor <= p.max && (p.min === undefined || valor >= p.min);
        estado.textContent = cumple ? "✅ Sí" : "❌ No";
        total += p.puntaje;
        if (!cumple) { malos += p.puntaje; fallan.push(`${p.nombre} (${numero(p.puntaje, 1)})`); }
      });
      const valor = total ? (malos / total) * 100 : 0;
      const nivel = valor <= 5 ? 0 : valor <= 14 ? 1 : valor <= 35 ? 2 : valor <= 80 ? 3 : 4;
      pasos.innerHTML = `
        <li>Sumar los puntajes de todos los parámetros analizados: <strong>${numero(total, 1)}</strong>.</li>
        <li>Sumar los puntajes de los que <em>no</em> cumplen: ${fallan.length ? fallan.join(" + ") + " = " : ""}<strong>${numero(malos, 1)}</strong>.</li>
        <li>IRCA = (${numero(malos, 1)} ÷ ${numero(total, 1)}) × 100 = <strong>${numero(valor, 1)} %</strong>.</li>`;
      res.innerHTML = `IRCA: <strong>${numero(valor, 1)} %</strong>, nivel de riesgo <strong>${["sin riesgo", "bajo", "medio", "alto", "inviable sanitariamente"][nivel]}</strong>.`;
      niveles.forEach((n, i) => n.classList.toggle("activo", i === nivel));
    };
    irca.addEventListener("input", actualizar);
    irca.addEventListener("change", actualizar);
    actualizar();
  });
})();
