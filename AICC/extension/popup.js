// ============================================================================
// POPUP SCRIPT - RPA AICC MAESTRO
// ============================================================================

document.addEventListener('DOMContentLoaded', () => {
  const toggleSistema = document.getElementById('toggleSistema');
  const toggleSubtitle = document.getElementById('toggleSubtitle');
  const statusBadge = document.getElementById('statusBadge');
  const faseActualVal = document.getElementById('faseActualVal');
  const timerVal = document.getElementById('timerVal');

  const inputTiempoPausa = document.getElementById('inputTiempoPausa');
  const inputTiempoFlash = document.getElementById('inputTiempoFlash');
  const inputMotivoPausa = document.getElementById('inputMotivoPausa');
  const btnGuardarConfig = document.getElementById('btnGuardarConfig');
  const saveFeedback = document.getElementById('saveFeedback');

  let activeTabId = null;

  // Cargar configuración guardada
  if (chrome.storage && chrome.storage.local) {
    chrome.storage.local.get(['TIEMPO_PAUSA_SEGUNDOS', 'TIEMPO_DESPAUSA_SEGUNDOS', 'MOTIVO_PAUSA'], (res) => {
      if (res.TIEMPO_PAUSA_SEGUNDOS) inputTiempoPausa.value = res.TIEMPO_PAUSA_SEGUNDOS;
      if (res.TIEMPO_DESPAUSA_SEGUNDOS) inputTiempoFlash.value = res.TIEMPO_DESPAUSA_SEGUNDOS;
      if (res.MOTIVO_PAUSA) inputMotivoPausa.value = res.MOTIVO_PAUSA;
    });
  }

  // Obtener pestaña activa
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs && tabs[0]) {
      activeTabId = tabs[0].id;
      actualizarEstadoDesdePagina();
    }
  });

  function actualizarUI(data) {
    if (!data) return;

    toggleSistema.checked = !!data.sistemaEncendido;
    toggleSubtitle.textContent = data.sistemaEncendido ? 'Sistema activo (F9 para pausar)' : 'Presiona F9 o activa aquí';

    if (data.sistemaEncendido) {
      if (data.faseActual === 'PAUSA') {
        statusBadge.textContent = 'En Pausa';
        statusBadge.className = 'status-indicator active';
      } else if (data.faseActual === 'DISPONIBLE_FLASH') {
        statusBadge.textContent = 'Flash';
        statusBadge.className = 'status-indicator flash';
      } else {
        statusBadge.textContent = 'Activo';
        statusBadge.className = 'status-indicator active';
      }
    } else {
      statusBadge.textContent = 'Apagado';
      statusBadge.className = 'status-indicator inactive';
    }

    faseActualVal.textContent = data.faseActual || 'DETENIDO';
    timerVal.textContent = data.segundosRestantes > 0 ? `${data.segundosRestantes}s` : '--';

    if (data.config) {
      if (!inputTiempoPausa.matches(':focus')) inputTiempoPausa.value = data.config.TIEMPO_PAUSA_SEGUNDOS;
      if (!inputTiempoFlash.matches(':focus')) inputTiempoFlash.value = data.config.TIEMPO_DESPAUSA_SEGUNDOS;
      if (!inputMotivoPausa.matches(':focus')) inputMotivoPausa.value = data.config.MOTIVO_PAUSA;
    }
  }

  function actualizarEstadoDesdePagina() {
    if (!activeTabId) return;
    chrome.tabs.sendMessage(activeTabId, { action: 'GET_STATUS' }, (response) => {
      if (chrome.runtime.lastError) {
        // La página no tiene cargado el script o es una URL interna de Edge (ej: edge://extensions)
        statusBadge.textContent = 'Sin conexión';
        statusBadge.className = 'status-indicator';
        faseActualVal.textContent = 'Pestaña no compatible';
        timerVal.textContent = '--';
        return;
      }
      actualizarUI(response);
    });
  }

  // Polling para refrescar contador mientras el popup esté abierto
  const intervalId = setInterval(actualizarEstadoDesdePagina, 1000);
  window.addEventListener('unload', () => clearInterval(intervalId));

  // Switch de Encendido / Apagado
  toggleSistema.addEventListener('change', () => {
    if (!activeTabId) return;
    const nuevoEstado = toggleSistema.checked;
    chrome.tabs.sendMessage(activeTabId, { action: 'TOGGLE_SISTEMA', forzarEstado: nuevoEstado }, (response) => {
      if (!chrome.runtime.lastError && response) {
        actualizarUI(response);
      }
    });
  });

  // Guardar configuración
  btnGuardarConfig.addEventListener('click', () => {
    const config = {
      TIEMPO_PAUSA_SEGUNDOS: parseInt(inputTiempoPausa.value, 10) || 60,
      TIEMPO_DESPAUSA_SEGUNDOS: parseInt(inputTiempoFlash.value, 10) || 3,
      MOTIVO_PAUSA: inputMotivoPausa.value.trim() || 'Pausa'
    };

    if (chrome.storage && chrome.storage.local) {
      chrome.storage.local.set(config, () => {
        saveFeedback.textContent = '¡Guardado correctamente!';
        setTimeout(() => { saveFeedback.textContent = ''; }, 2000);
      });
    }

    if (activeTabId) {
      chrome.tabs.sendMessage(activeTabId, { action: 'UPDATE_CONFIG', config }, () => {
        if (!chrome.runtime.lastError) {
          actualizarEstadoDesdePagina();
        }
      });
    }
  });
});
