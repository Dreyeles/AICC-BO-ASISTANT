// ============================================================================
// RPA MAESTRO AICC - AUTO-TIPIFICACIÓN & CICLO ANTI-PAUSA / EVASIÓN
// ============================================================================
// Atajo de teclado: F9 (Activar / Desactivar)
// Estados en título: (●) Pausa activa | (⚡) Flash Disponible | (Tipificando...) | (APAGADO)
// ============================================================================

(function () {
    if (window._RPA_STEALTH_LOADED) {
        console.log("RPA ya activo");
        return;
    }
    window._RPA_STEALTH_LOADED = true;

    const CONFIG = {
        TIEMPO_PAUSA_SEGUNDOS: 60,
        TIEMPO_DESPAUSA_SEGUNDOS: 3,
        MOTIVO_PAUSA: 'Pausa',
        RUTA_TIPIFICACION: ['CONTACTO EFECTIVO', 'ATENDIDO', 'Confirmación de Atención']
    };

    let sistemaEncendido = false;
    let modoEvasionActivo = false;
    let temporizador = null;
    let segundosRestantes = 0;
    let faseActual = 'ESPERANDO';
    let esCambioAutomaticoRPA = false;
    let autoTipificado = false;
    let estadoAnterior = '';

    let tituloOriginal = document.title
        .replace('(●) ', '')
        .replace('(⚡) ', '')
        .replace('(APAGADO) ', '')
        .replace('(Tipificando...) ', '');

    function simularClic(elemento) {
        if (!elemento) return;
        try {
            ['mousedown', 'mouseup', 'click'].forEach(evt => {
                elemento.dispatchEvent(new MouseEvent(evt, { bubbles: true, cancelable: true, view: window }));
            });
        } catch (e) {}
    }

    function rellenarDatosYGuardar() {
        try {
            let valorCasosiac = "", valorNombre = "";
            const etiquetas = Array.from(document.querySelectorAll('.el-form-item__label'));

            const labelCasosiac = etiquetas.find(el => el.innerText.trim().toUpperCase() === 'CASOSIAC');
            if (labelCasosiac) {
                const spanValor = labelCasosiac.closest('.el-form-item').querySelector('.el-form-item__content span');
                if (spanValor) valorCasosiac = spanValor.innerText.trim();
            }

            const labelNombre = etiquetas.find(el => el.innerText.trim().toUpperCase() === 'NOMBRE');
            if (labelNombre) {
                const spanValor = labelNombre.closest('.el-form-item').querySelector('.el-form-item__content span');
                if (spanValor) valorNombre = spanValor.innerText.trim();
            }

            const labelDesc = etiquetas.find(el => el.innerText.trim() === 'Descripción del negocio');
            if (labelDesc) {
                const textarea = labelDesc.closest('.el-form-item').querySelector('textarea');
                if (textarea) {
                    let textoFinal = [];
                    if (valorCasosiac) textoFinal.push(valorCasosiac);
                    if (valorNombre) textoFinal.push(valorNombre);

                    if (textoFinal.length > 0) {
                        textarea.value = textoFinal.join(" - ");
                        textarea.dispatchEvent(new Event('input', { bubbles: true }));
                        textarea.dispatchEvent(new Event('change', { bubbles: true }));
                    }
                }
            }

            setTimeout(() => {
                const botones = Array.from(document.querySelectorAll('.el-button--primary'));
                const btnGuardar = botones.find(btn => btn.innerText.trim() === 'Guardar');
                if (btnGuardar) {
                    simularClic(btnGuardar);
                    console.log("Botón Guardar presionado.");
                }

                if (sistemaEncendido) {
                    setTimeout(() => {
                        const t = document.querySelector('.sign-tenant-status');
                        console.log("Reactivando evasión post-llamada...");
                        modoEvasionActivo = true;
                        faseActual = 'PAUSA';
                        segundosRestantes = CONFIG.TIEMPO_PAUSA_SEGUNDOS;
                        if (t && !t.innerText.trim().toLowerCase().includes('pausa')) {
                            ponerEnPausa();
                        }
                        document.title = "(●) " + tituloOriginal;
                    }, 1500);
                } else {
                    document.title = tituloOriginal;
                }
            }, 300);

        } catch (e) {}
    }

    function ejecutarFlujoTipificacion(intento = 1) {
        if (intento > 10) {
            console.log("Se abortó la tipificación por demasiadas interrupciones.");
            document.title = tituloOriginal;
            return;
        }

        const pestanaActiva = document.querySelector('.el-tabs__item.is-active');
        if (!pestanaActiva) {
            setTimeout(() => ejecutarFlujoTipificacion(intento + 1), 1000);
            return;
        }

        const textoPestana = pestanaActiva.innerText.toLowerCase();
        if (!textoPestana.includes('t_backoffice') && !textoPestana.includes('reservar llamadas')) {
            setTimeout(() => ejecutarFlujoTipificacion(intento + 1), 1000);
            return;
        }

        const labels = Array.from(document.querySelectorAll('.el-form-item__label'));
        const labelResultado = labels.find(el => el.innerText.trim() === 'Resultado de Negocio');

        if (!labelResultado) {
            const botones = Array.from(document.querySelectorAll('.el-button--primary'));
            const btnGuardar = botones.find(btn => btn.innerText.trim() === 'Guardar');

            if (btnGuardar) {
                console.log("Plan B activado: Guardando directamente...");
                rellenarDatosYGuardar();
                return;
            }
            setTimeout(() => ejecutarFlujoTipificacion(intento + 1), 1000);
            return;
        }

        const formItem = labelResultado.closest('.el-form-item');
        const comboBox = formItem.querySelector('.select-trigger');

        const poppers = Array.from(document.querySelectorAll('.el-popper.selectTreeClass')).filter(p => p.style.display !== 'none');

        if (poppers.length === 0) {
            if (comboBox) simularClic(comboBox);
            setTimeout(() => procesarArbol(0, intento), 600);
        } else {
            procesarArbol(0, intento);
        }
    }

    function procesarArbol(paso, intentoBase) {
        if (paso >= CONFIG.RUTA_TIPIFICACION.length) return;

        const poppers = Array.from(document.querySelectorAll('.el-popper.selectTreeClass')).filter(p => p.style.display !== 'none');
        if (poppers.length === 0) {
            setTimeout(() => ejecutarFlujoTipificacion(intentoBase + 1), 500);
            return;
        }

        const popper = poppers[poppers.length - 1];
        const labelsTree = Array.from(popper.querySelectorAll('.el-tree-node__label'));
        const targetLabel = labelsTree.find(el => el.innerText.trim() === CONFIG.RUTA_TIPIFICACION[paso]);

        if (targetLabel) {
            const treeNode = targetLabel.closest('.el-tree-node');
            if (paso === CONFIG.RUTA_TIPIFICACION.length - 1) {
                simularClic(targetLabel);
                setTimeout(rellenarDatosYGuardar, 800);
            } else {
                if (!treeNode.classList.contains('is-expanded')) {
                    const icon = treeNode.querySelector('.el-tree-node__expand-icon');
                    if (icon) simularClic(icon);
                }
                setTimeout(() => procesarArbol(paso + 1, intentoBase), 400);
            }
        } else {
            setTimeout(() => procesarArbol(paso, intentoBase), 400);
        }
    }

    function verificarYConfirmarModal() {
        try {
            const modales = document.querySelectorAll('.el-message-box');
            modales.forEach(modal => {
                if (modal && modal.innerText.toLowerCase().includes('teléfono suave')) {
                    const btnOk = modal.querySelector('.el-message-box__btns .el-button--primary');
                    if (btnOk) simularClic(btnOk);
                }
            });
        } catch (e) {}
    }

    function cambiarEstado(estadoDeseado) {
        esCambioAutomaticoRPA = true;
        const contenedorEstado = document.querySelector('.sign-tenant-status') || document.body;

        if (contenedorEstado) {
            simularClic(contenedorEstado);
            setTimeout(() => {
                const opciones = Array.from(document.querySelectorAll('.status-select .select-label'));
                const opcion = opciones.find(el => el.innerText.trim() === estadoDeseado);

                if (opcion) {
                    simularClic(opcion);
                    if (estadoDeseado === 'Disponible') {
                        setTimeout(verificarYConfirmarModal, 400);
                        setTimeout(verificarYConfirmarModal, 1000);
                        setTimeout(verificarYConfirmarModal, 2000);
                    }
                }
            }, 400);
        }
        setTimeout(() => { esCambioAutomaticoRPA = false; }, 3500);
    }

    function ponerEnPausa() { cambiarEstado(CONFIG.MOTIVO_PAUSA); }
    function ponerEnDisponible() { cambiarEstado('Disponible'); }

    function ejecutarCiclo() {
        if (!sistemaEncendido || !modoEvasionActivo) return;

        if (faseActual === 'PAUSA') {
            segundosRestantes--;
            if (segundosRestantes <= 0) {
                faseActual = 'DISPONIBLE_FLASH';
                segundosRestantes = CONFIG.TIEMPO_DESPAUSA_SEGUNDOS;
                ponerEnDisponible();
                document.title = "(⚡) " + tituloOriginal;
            }
        } else if (faseActual === 'DISPONIBLE_FLASH') {
            segundosRestantes--;
            if (segundosRestantes <= 0) {
                faseActual = 'PAUSA';
                segundosRestantes = CONFIG.TIEMPO_PAUSA_SEGUNDOS;
                ponerEnPausa();
                document.title = "(●) " + tituloOriginal;
            }
        }
    }

    function alternarSistema() {
        sistemaEncendido = !sistemaEncendido;
        if (sistemaEncendido) {
            console.log("=== SISTEMA MAESTRO ENCENDIDO ===");

            const pestanaActiva = document.querySelector('.el-tabs__item.is-active');
            const botones = Array.from(document.querySelectorAll('.el-button--primary'));
            const btnGuardar = botones.find(btn => btn.innerText.trim() === 'Guardar');

            if (pestanaActiva && (pestanaActiva.innerText.toLowerCase().includes('t_backoffice') || pestanaActiva.innerText.toLowerCase().includes('reservar llamadas')) && btnGuardar) {
                document.title = "(Tipificando...) " + tituloOriginal;
                autoTipificado = true;
                ejecutarFlujoTipificacion(1);
            } else {
                const t = document.querySelector('.sign-tenant-status');
                if (t && t.innerText.trim().toLowerCase().includes('pausa')) {
                    modoEvasionActivo = true;
                    faseActual = 'PAUSA';
                    segundosRestantes = CONFIG.TIEMPO_PAUSA_SEGUNDOS;
                    document.title = "(●) " + tituloOriginal;
                } else {
                    document.title = tituloOriginal;
                }
            }
        } else {
            console.log("=== SISTEMA MAESTRO APAGADO ===");
            modoEvasionActivo = false;
            document.title = "(APAGADO) " + tituloOriginal;
        }
    }

    const observer = new MutationObserver(() => {
        const t = document.querySelector('.sign-tenant-status');
        if (t) {
            const txt = t.innerText.trim().toLowerCase();
            if (esCambioAutomaticoRPA) return;

            const saliendoDeLlamada = (estadoAnterior.includes('llamada') || estadoAnterior.includes('llamando')) && !(txt.includes('llamada') || txt.includes('llamando'));

            if (txt.includes('llamada') || txt.includes('llamando')) {
                modoEvasionActivo = false;
                autoTipificado = false;
                if (sistemaEncendido) document.title = tituloOriginal;
            }

            if (saliendoDeLlamada || txt.includes('recapitulaci')) {
                modoEvasionActivo = false;
                if (sistemaEncendido && !autoTipificado) {
                    autoTipificado = true;
                    document.title = "(Tipificando...) " + tituloOriginal;
                    setTimeout(() => ejecutarFlujoTipificacion(1), 1000);
                }
            }

            if (txt.includes('disponible') && !txt.includes('recapitulaci')) {
                if (faseActual !== 'DISPONIBLE_FLASH') {
                    modoEvasionActivo = false;
                    if (sistemaEncendido && !autoTipificado) document.title = tituloOriginal;
                }
            } else if (txt.includes('pausa') && !txt.includes('recapitulaci')) {
                if (sistemaEncendido && !autoTipificado) {
                    if (!modoEvasionActivo || faseActual !== 'PAUSA') {
                        modoEvasionActivo = true;
                        faseActual = 'PAUSA';
                        segundosRestantes = CONFIG.TIEMPO_PAUSA_SEGUNDOS;
                        document.title = "(●) " + tituloOriginal;
                    }
                }
            }

            estadoAnterior = txt;
        }
    });

    observer.observe(document.body, { childList: true, subtree: true, characterData: true });

    window.addEventListener('keydown', (e) => {
        if (e.key === 'F9') {
            e.preventDefault();
            alternarSistema();
        }
    });

    temporizador = setInterval(ejecutarCiclo, 1000);

    console.log("RPA Maestro Listo. El seguro de tipificación ya no se quedará atascado.");
})();
