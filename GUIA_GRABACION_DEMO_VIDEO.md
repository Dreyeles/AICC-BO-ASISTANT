# 🎬 Guía Maestra para Grabar el Video Demo: AICC BO Assistant

**Proyecto:** AICC BO Assistant (Powered by Huawei Cloud MaaS / Ascend 910B)  
**Equipo:** Los Ejecutores (Drey Aymituma, Hector Poma, Gean Franco Quinto)  
**Atajo de Grabación en Windows:** <kbd>Win + Alt + R</kbd> (Xbox Game Bar) u OBS Studio.

---

## 📌 Estructura del Video (Duración recomendada: 2m 30s a 3m)

El video demuestra la **integración punta a punta** de los 3 sistemas operacionales de Backoffice N2 más el Portal de Calidad y Formación, resolviendo el problema de la sobrecarga operativa y la pérdida de tipificaciones.

```mermaid
flowchart LR
    A["1. Huawei AICC (Telefonía)"] -->|Colgar y Sincronizar| B["2. SIAC Único (Reclamos)"]
    B -->|Validar Plantilla| C["3. BMC Helix (Remedy)"]
    C -->|Verificación Actividad| D["4. Portal Calidad & Formación"]
    
    style A fill:#cf0a2c,color:#fff
    style B fill:#da291c,color:#fff
    style C fill:#e65100,color:#fff
    style D fill:#00875a,color:#fff
```

---

## 🕒 Minuto a Minuto de la Grabación

### 📍 Acto 1: La Llamada en Huawei AICC + Teleprompter en Vivo (0:00 - 0:50)
1. **Abre:** [`AICC/index.html`](file:///c:/Users/Drewg/OneDrive/Escritorio/proyecto%20huawei/AICC/index.html).
2. **Qué se ve en pantalla:**
   - La consola oficial de **Huawei Customer Service Cloud** con la llamada activa al `976302352` (Magdalena Terán Panaifo, caso `0061568299`).
   - El widget flotante a la derecha: **`AICC BO Assistant | Teleprompter MaaS`**.
3. **Qué hacer:**
   - Pulsa el botón verde **`▶️ Reproducir Llamada Demo con IA (98s)`**.
   - *(Opción A con voz propia):* Pulsa el botón `🔊` para silenciar el audio de la IA y habla tú mismo al micrófono siguiendo las líneas del teleprompter.
   - *(Opción B 100% IA):* Deja que suenen las voces neurales peruanas oficiales de Drey y Magdalena.
4. **Lo que resalta en el video:**
   - Las burbujas de diálogo se iluminan en tiempo real distinguiendo a **Drey (Asesor)** de **Magdalena (Cliente)**.
   - Conforme se mencionan los descartes, los chips inferiores se marcan en verde con checkmark:
     - `✔ Saludo y Titular`
     - `✔ Incógnito Online`
     - `✔ Schaman sin Alertas`
     - `✔ TR-069 AutoSelect OFF`
     - `✔ Bandas 2.4G / 5G Separadas`
     - `✔ Solución Confirmada`
   - El cumplimiento sube al **100%**.
5. **Cierre de la llamada:**
   - Haz clic en **`📴 Colgar y Sincronizar Todo`** (o espera que finalice el audio).
   - Se observa cómo en 5 segundos AICC autocompleta el Resultado del Negocio, guarda la tipificación horaria, cambia el agente a **Disponible** y aparece la ventana:
     **`🎉 ¡Sincronización Multi-Sistema Exitosa!`**.

---

### 📍 Acto 2: Verificación Inmediata en SIAC Único (0:50 - 1:25)
1. **Transición:** Haz clic en el enlace del modal **`🔗 Abrir SIAC Único`** o cambia a la pestaña de [`siac unico/index.html`](file:///c:/Users/Drewg/OneDrive/Escritorio/proyecto%20huawei/siac%20unico/index.html).
2. **Qué hacer en pantalla:**
   - En **Búsqueda De Casos**, el caso `0061568299` ya está listo. Haz clic en la fila o en **Buscar**.
   - Entras a la pantalla oficial de **Creación De Interacción**.
   - Se resalta el banner verde:
     `⚡ AICC BO Assistant (MaaS AI): Nota técnica y descartes sincronizados automáticamente.`
   - Haz clic en **`📄 Ver Notas`** (o en la barra flotante `👁️ Ver Notas`).
3. **Qué narrar / destacar:**
   - *"El asesor no tuvo que redactar nada a mano. La plantilla completa de Backoffice Hitss con la validación de Incógnito, Schaman, TR-069 y separación de bandas ya se encuentra registrada en SIAC Reclamos."*

---

### 📍 Acto 3: Verificación en BMC Helix ITSM - Remedy (1:25 - 1:55)
1. **Transición:** Cambia a la pestaña de [`bmc helix/index.html`](file:///c:/Users/Drewg/OneDrive/Escritorio/proyecto%20huawei/bmc%20helix/index.html).
2. **Qué hacer en pantalla:**
   - En la lista de tickets, abre el caso `INC000001802027` (Magdalena Terán Panaifo).
   - Dirige la mirada al panel derecho de **Actividad**.
3. **Qué resaltar en el video:**
   - En la parte superior de la actividad aparece la nueva nota con el avatar de Drey y la etiqueta:
     **`DREY E AYMITUMA JULCA (vía AICC BO Assistant MaaS) - ⚡ Sincronizado en Vivo`**.
   - Se muestra la plantilla técnica idéntica con el formato oficial de Backoffice Hitss.
   - *"Se ahorraron más de 4 minutos de ACW manual y se elimina el riesgo de error humano."*

---

### 📍 Acto 4: Almacenamiento en Data Lake y Portal de Calidad / Formación (1:55 - 2:40)
1. **Transición:** Cambia al Dashboard principal en [`index.html`](file:///c:/Users/Drewg/OneDrive/Escritorio/proyecto%20huawei/index.html) y haz clic en la pestaña **`Portal de Calidad y Formación`**.
2. **Qué mostrar en pantalla:**
   - Los KPIs de impacto: **100% de llamadas auditadas** (vs 0.8% manual), **+5,300 horas ahorradas al mes** y **$1.35M mitigados en multas**.
   - Baja a la sección: **`Base de Datos de Transcripciones y Calidad N2 (GaussDB + OBS Storage)`**.
   - Muestra cómo interactuar con los filtros:
     - Pulsa **`🟢 Llamadas Buenas (1,465 - 92%)`**: Aparece en primer lugar la llamada de Drey con Magdalena con Score **98/100 (Óptima)**.
     - Pulsa **`🔴 Llamadas Observadas (127 - 8%)`**: Muestra cómo el sistema detecta asesores que omitieron TR-069 o tuvieron silencios y les asigna automáticamente cursos pedagógicos en la plataforma e-learning de Formación.
   - Pulsa **`Ver Transcripción`** en la llamada de Drey para mostrar la diarización completa y el audio sincronizado.

---

## 🎙️ Guion de Locución para el Video (Voz de Drey)

> "Buenas tardes jurado de Huawei Cloud. Soy Drey Aymituma de Los Ejecutores.  
> En el soporte técnico N2 para Claro sobre Huawei AICC, nuestras llamadas duran de quince a sesenta minutos por descartes complejos en Incógnito, Schaman y TR-069.  
> El drama diario es que tenemos el tiempo de pausa hiper-auditado a tres minutos, y si nos despausamos rápido, el robot de AICC nos lanza otra llamada sin darnos tiempo de tipificar en SIAC Único ni en BMC Helix.  
> 
> Aquí entra **AICC BO Assistant**.  
> Mientras atiendo a la señora Magdalena Terán, nuestro modelo en ModelArts Studio MaaS con procesadores Ascend 910B escucha en tiempo real. Como ven en el teleprompter, la IA diariza la conversación y valida cada descarte técnico en vivo: Incógnito aprovisionado, Schaman sin averías y TR-069 con AutoSelect apagado.  
> 
> Al colgar, la magia ocurre en cinco segundos:  
> Primero: AICC se autotipifica y aprueba la auditoría horaria al cien por ciento.  
> Segundo: Entramos a SIAC Único y en 'Ver Notas' ya está registrada la plantilla oficial de Backoffice Hitss.  
> Tercero: Pasamos a BMC Helix y en la barra lateral de Actividad la nota técnica ya está publicada.  
> Y cuarto: En nuestro Portal de Calidad y Formación respaldado por GaussDB y OBS, pasamos de auditar una muestra ciega del uno por ciento al cien por ciento de llamadas, clasificando automáticamente llamadas óptimas y asignando módulos de reentrenamiento para llamadas observadas.  
> 
> Transformamos el estrés operativo de cientos de asesores en excelencia técnica certificada. Muchas gracias."

---

## 🛠️ Consejos Técnicos de Grabación
- **Resolución:** Graba a 1080p (1920x1080) en pantalla completa.
- **Navegador:** Presiona <kbd>F11</kbd> en tu navegador para ocultar barras de marcadores si deseas una vista 100% limpia y cinematográfica.
- **Lanzador todo-en-uno:** Puedes usar [`abrir_suite_demo.bat`](file:///c:/Users/Drewg/OneDrive/Escritorio/proyecto%20huawei/abrir_suite_demo.bat) opción `[5]` para abrir los 3 sistemas en pestañas continuas antes de empezar a grabar.

