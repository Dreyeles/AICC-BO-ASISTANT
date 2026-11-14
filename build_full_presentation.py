import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def build_presentation():
    # Always load from pristine backup
    prs = Presentation('Huawei Cloud Peru MaaS Hackathon Template External_BACKUP.pptx')
    
    # Color palette
    COLOR_RED = RGBColor(207, 10, 44)      # Huawei Red
    COLOR_DARK = RGBColor(30, 35, 42)      # Dark Slate
    COLOR_WHITE = RGBColor(255, 255, 255)
    COLOR_GRAY = RGBColor(100, 110, 125)
    COLOR_BLUE = RGBColor(2, 132, 199)     # Sky Blue
    
    # -------------------------------------------------------------
    # SLIDE 1: PORTADA
    # -------------------------------------------------------------
    s1 = prs.slides[0]
    # Remove any existing shapes just in case
    for sh in list(s1.shapes):
        sp = sh._element
        sp.getparent().remove(sp)
        
    # Title box
    tb = s1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(11.0), Inches(2.4))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = "AICC BO Assistant"
    p.font.name = "Arial"
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = COLOR_RED
    
    p2 = tf.add_paragraph()
    p2.text = "Copiloto Inteligente para Backoffice N2 impulsado por Huawei Cloud MaaS"
    p2.font.name = "Arial"
    p2.font.size = Pt(18)
    p2.font.color.rgb = COLOR_WHITE
    p2.space_before = Pt(8)
    
    # Meta / Team Box
    tb_meta = s1.shapes.add_textbox(Inches(1.2), Inches(4.3), Inches(10.5), Inches(2.2))
    tf_meta = tb_meta.text_frame
    tf_meta.word_wrap = True
    
    items = [
        ("Equipo:", "Los Ejecutores"),
        ("Líder de Proyecto:", "Drey Enmanuel Aymituma Julca (Backoffice Soporte Técnico N2 - Global Hitss)"),
        ("Integrantes:", "Hector Armando Poma Hernandez | Gean Franco Quinto Zapana"),
        ("Empresa / Ámbito:", "Global Hitss / Claro Perú - Backoffice N2 & Calidad / Formación"),
        ("Evento:", "Huawei Cloud Peru MaaS Hackathon 2026 - Sede Blue Tower"),
        ("Fecha:", "Noviembre de 2026")
    ]
    for i, (k, v) in enumerate(items):
        pm = tf_meta.paragraphs[0] if i == 0 else tf_meta.add_paragraph()
        r1 = pm.add_run()
        r1.text = f"{k} "
        r1.font.name = "Arial"
        r1.font.size = Pt(13)
        r1.font.bold = True
        r1.font.color.rgb = COLOR_RED
        
        r2 = pm.add_run()
        r2.text = v
        r2.font.name = "Arial"
        r2.font.size = Pt(13)
        r2.font.color.rgb = RGBColor(220, 225, 235)

    # -------------------------------------------------------------
    # SLIDE 2: ASPECTOS GENERALES (FICHA TÉCNICA)
    # -------------------------------------------------------------
    s2 = prs.slides[1]
    # Remove overlapping Table 0 (which has 'Contactos') and keep Table 2
    for sh in list(s2.shapes):
        if sh.has_table and 'Contactos' in sh.table.cell(0, 0).text:
            sp = sh._element
            sp.getparent().remove(sp)
            
    # Now update the remaining table (which has 'Nombre del proyecto')
    for sh in s2.shapes:
        if sh.has_table and 'Nombre del proyecto' in sh.table.cell(0, 0).text:
            t = sh.table
            
            # Row 0: Nombre del proyecto
            t.cell(0, 1).text = "AICC BO Assistant: Copiloto Inteligente para Backoffice N2 con Huawei Cloud MaaS"
            # Row 1: Nombre del equipo
            t.cell(1, 1).text = "Los Ejecutores | Integrantes: Drey Enmanuel Aymituma Julca (Líder), Hector Armando Poma Hernandez, Gean Franco Quinto Zapana"
            # Row 2: Tecnologías
            t.cell(2, 1).text = "Huawei AICC (Contact Center), Huawei Cloud ModelArts Studio (MaaS), LLMs SOTA (Qwen 2.5 72B / Pangu NLP), ModelArts Guard, Ascend 910B NPU, OBS, FunctionGraph, Integración SIAC Único & Helix"
            # Row 3: Palabras clave
            t.cell(3, 1).text = "Huawei AICC, MaaS, Backoffice N2, SIAC Único, Helix, Calidad y Formación, Llamadas Largas (15-60 min), Incógnito, Schaman, SOT"
            # Row 4: Campos Aplicables
            t.cell(4, 1).text = "Global Hitss / Claro Perú (Backoffice N2, Operaciones HFC/FTTH, SIAC Único, Helix y Calidad/Formación)"
            # Row 5: Descripción
            desc = (
                "AICC BO Assistant resuelve el drama operativo diario del Backoffice N2 en Global Hitss / Claro. "
                "La operación se divide en 'Primer Toque' y 'Colas de Llamadas' (donde un marcador robot de Huawei AICC distribuye llamadas continuas). "
                "El conflicto crítico radica en que el tiempo de pausa está hiper-auditado: al superar 3 minutos, supervisión vocea para despausarse. "
                "Si el asesor se despausa, el robot de AICC le dispara inmediatamente otra llamada 'back-to-back', dejando el caso anterior sin tipificar, "
                "lo que provoca sanciones en la estricta auditoría horaria de tipificaciones de AICC y omisiones en SIAC Único y Helix. "
                "Con AICC BO Assistant, mientras el asesor habla, la IA en Huawei Cloud MaaS escucha y analiza en tiempo real: al colgar, autocompleta "
                "la tipificación en AICC en 5 segundos (aprobando la auditoría horaria) y deja lista la plantilla técnica completa para SIAC Único y Helix. "
                "El asesor se despausa al instante sin estrés, Calidad y Formación tienen 100% de auditoría y se erradica el tiempo muerto."
            )
            t.cell(5, 1).text = desc
            
            # Style text inside table
            for row in t.rows:
                for cell in row.cells:
                    for p in cell.text_frame.paragraphs:
                        p.font.name = "Arial"
                        p.font.size = Pt(11)
                        p.font.color.rgb = RGBColor(40, 45, 55)

    # -------------------------------------------------------------
    # SLIDE 3: SEPARADOR / RETO
    # -------------------------------------------------------------
    s3 = prs.slides[2]
    # Add an explanatory card
    tb3 = s3.shapes.add_textbox(Inches(1.2), Inches(3.0), Inches(10.5), Inches(3.2))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    
    p = tf3.paragraphs[0]
    p.text = "EL CONFLICTO OPERATIVO REAL (PRIMER TOQUE Y COLAS DE LLAMADAS EN HITSS):"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = COLOR_RED
    
    p = tf3.add_paragraph()
    p.text = "• Estructura operativa: Asesores de 'Primer Toque' (atienden o inician ciclo de llamadas 2x3) y 'Colas de Llamadas' alimentadas por el marcador robot de Huawei AICC."
    p.font.size = Pt(12)
    p.space_before = Pt(6)
    
    p = tf3.add_paragraph()
    p.text = "• La trampa de la pausa de 3 minutos: Si el asesor se pausa más de 3 min para tipificar, supervisión vocea para despausar; pero si se despausa, el robot le lanza otra llamada de inmediato ('back-to-back')."
    p.font.size = Pt(12)
    p.space_before = Pt(4)
    
    p = tf3.add_paragraph()
    p.text = "• Penalización en la auditoría horaria de AICC: Al caer la nueva llamada, el caso anterior queda sin tipificar, reprobando la auditoría horaria de llamadas de AICC y dejando pendientes SIAC Único y Helix."
    p.font.size = Pt(12)
    p.space_before = Pt(4)

    p = tf3.add_paragraph()
    p.text = "NUESTRA SOLUCIÓN: AICC BO Assistant procesa en vivo durante la llamada con Huawei Cloud MaaS. Al colgar, autocompleta AICC en 5 seg y deja listas las plantillas para SIAC y Helix. ¡Cero pausas, cero llamadas perdidas!"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_BLUE
    p.space_before = Pt(8)

    # Helper function to clear and set bullet content
    def set_content_box(slide, paragraphs_data):
        for sh in slide.shapes:
            if sh.has_text_frame and 'Content Placeholder' in sh.name:
                tf = sh.text_frame
                tf.clear()
                tf.word_wrap = True
                for i, item in enumerate(paragraphs_data):
                    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
                    if isinstance(item, tuple):
                        heading, text = item
                        r1 = p.add_run()
                        r1.text = heading + " "
                        r1.font.name = "Arial"
                        r1.font.bold = True
                        r1.font.size = Pt(13)
                        r1.font.color.rgb = COLOR_RED
                        
                        r2 = p.add_run()
                        r2.text = text
                        r2.font.name = "Arial"
                        r2.font.size = Pt(12)
                        r2.font.color.rgb = RGBColor(40, 45, 55)
                    else:
                        p.text = str(item)
                        p.font.name = "Arial"
                        p.font.size = Pt(12)
                        p.font.color.rgb = RGBColor(40, 45, 55)
                    p.space_before = Pt(6)
                return

    # -------------------------------------------------------------
    # SLIDE 4: INTRODUCCIÓN AL EQUIPO
    # -------------------------------------------------------------
    s4 = prs.slides[3]
    set_content_box(s4, [
        ("Equipo Los Ejecutores:", "Profesionales de ingeniería y operaciones de Global Hitss / Claro que vivimos el dolor de la operación técnica día a día."),
        ("1. Drey Enmanuel Aymituma Julca (Líder & Backoffice N2 Architect):", "Especialista en Backoffice Soporte Técnico N2 en Global Hitss; creador de herramientas de productividad operativa y diseño de la arquitectura con Huawei Cloud."),
        ("2. Hector Armando Poma Hernandez (Ingeniero de IA & MaaS Specialist):", "Implementación de ModelArts Studio (MaaS), orquestación de modelos LLM (Qwen 2.5 72B / Pangu NLP), procesamiento de contextos largos y ModelArts Guard."),
        ("3. Gean Franco Quinto Zapana (Desarrollador Full-Stack & Integración AICC):", "Conexión del pipeline entre la telefonía Huawei AICC, buckets OBS y la estación de trabajo del asesor para inyección directa de plantillas."),
        ("Sinergia y Propósito:", "Unión de experiencia de campo en soporte N2, arquitectura de nube Huawei y modelos fundacionales para eliminar el 98% de puntos ciegos en auditoría."),
        ("Metodología de Trabajo:", "Desarrollo ágil orientado a aliviar la carga de Calidad/Formación y reducir drásticamente el tiempo de After Call Work (ACW).")
    ])

    # -------------------------------------------------------------
    # SLIDE 5: INTRODUCCIÓN AL PROYECTO
    # -------------------------------------------------------------
    s5 = prs.slides[4]
    set_content_box(s5, [
        ("Estructura Operativa: Primer Toque vs. Colas de Llamadas:", "El equipo se divide en 'Primer Toque' (asignan casos, llaman y si no contesta inician ciclo de 3 llamadas c/2h x 2 días) y 'Colas de Marcador' (robot de Huawei AICC reparte llamadas automáticas cuando el cliente atiende)."),
        ("La Trampa de la Pausa de 3 Minutos y el Marcador AICC:", "El tiempo en pausa está estrictamente limitado a 3 minutos; al pasarse, supervisión vocea para despausar. Si el asesor se despausa, el robot de AICC le dispara una nueva llamada de inmediato sin darle tiempo de redactar."),
        ("El Riesgo de la Auditoría Horaria de AICC:", "Las tipificaciones en Huawei AICC se auditan cada hora. Si cae una llamada back-to-back y el caso anterior queda sin tipificar, el asesor es sancionado en la auditoría horaria y se retrasan los registros en SIAC Único y Helix."),
        ("El Cuello de Botella en Calidad y Formación:", "Llamadas de 15 a 60 minutos son imposibles de auditar manualmente. Calidad audita < 1%, dejando a oscuras las necesidades de capacitación de los asesores."),
        ("Solución AICC BO Assistant (Cero Pausa en AICC):", "MaaS escucha en vivo: al colgar, llena AICC en 5 segundos (100% aprobado en auditoría horaria) y deja lista la plantilla técnica completa para SIAC Único y Helix en 1 clic."),
        ("Impacto Directo:", "Eliminación del estrés por voceo de pausas, cero llamadas sin tipificar y auditoría automática universal al 100%.")
    ])

    # -------------------------------------------------------------
    # SLIDE 6: ARQUITECTURA TÉCNICA (ASPECTOS GENERALES)
    # -------------------------------------------------------------
    s6 = prs.slides[5]
    set_content_box(s6, [
        ("1. Telefonía Nativa Huawei AICC:", "Las grabaciones de audio de llamadas extensas (15 a 60+ min) de los agentes se sincronizan directamente desde la PBX/AICC hacia Huawei Cloud OBS."),
        ("2. Inferencia de Contexto Extenso en ModelArts MaaS:", "Procesamiento de transcripciones masivas usando LLMs SOTA (Qwen-2.5-72B / Pangu NLP) con capacidad de contexto largo y aceleración por hardware Ascend 910B NPU."),
        ("3. ModelArts Guard (Seguridad y Cumplimiento):", "Enmascara en tiempo real números de DNI, cuentas y datos bancarios antes del análisis, asegurando el cumplimiento de la Ley de Protección de Datos Personales."),
        ("4. Motor de Plantillas para SIAC Único & Helix:", "Extrae de la conversación los descartes realizados (Incógnito, Schaman, Tracer, TR-069) y formatea la plantilla oficial de N2 para SIAC Único y el ticket de Helix."),
        ("5. Módulo de Auditoría para Calidad y Formación:", "Evalúa matrices de atención al 100%, mide adherencia al protocolo técnico (Flyer N° 41) y genera reportes pedagógicos automáticos para los instructores de Formación."),
        ("6. FunctionGraph & GaussDB:", "Flujo serverless reactivo sin servidores inactivos, con almacenamiento seguro de métricas y scores en GaussDB.")
    ])

    # -------------------------------------------------------------
    # SLIDE 7: DIAGRAMA DE ARQUITECTURA (REEMPLAZAR BLOQUES)
    # -------------------------------------------------------------
    s7 = prs.slides[6]
    # Remove old example blocks
    for sh in list(s7.shapes):
        if sh.name.startswith('矩形') or sh.name.startswith('斜纹') or sh.name.startswith('图片'):
            sp = sh._element
            sp.getparent().remove(sp)
            
    # Add new clear visual blocks
    steps = [
        ("1. Huawei AICC", "Llamadas N2 (15-60m)\nGrabación y telefonía", Inches(0.8), Inches(2.2), Inches(2.0), Inches(1.8), COLOR_DARK),
        ("2. Huawei Cloud OBS", "Bucket Seguro\nAudios y Transcripción", Inches(3.1), Inches(2.2), Inches(2.0), Inches(1.8), COLOR_BLUE),
        ("3. FunctionGraph", "Trigger Serverless\nOrquestador de eventos", Inches(5.4), Inches(2.2), Inches(2.0), Inches(1.8), RGBColor(140, 45, 170)),
        ("4. ModelArts MaaS", "Qwen 2.5 / Pangu NLP\nAscend 910B NPU Core", Inches(7.7), Inches(2.2), Inches(2.4), Inches(1.8), COLOR_RED),
        ("5. SIAC Único / Helix", "Autocompletado Dual &\nPortal de Formación", Inches(10.4), Inches(2.2), Inches(1.5), Inches(1.8), RGBColor(16, 140, 90)),
    ]
    
    for title, desc, left, top, w, h, bg_color in steps:
        box = s7.shapes.add_shape(1, left, top, w, h) # 1 is rectangle
        box.fill.solid()
        box.fill.fore_color.rgb = bg_color
        box.line.color.rgb = RGBColor(255, 255, 255)
        box.line.width = Pt(1)
        
        tf = box.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.name = "Arial"
        p1.font.bold = True
        p1.font.size = Pt(12)
        p1.font.color.rgb = COLOR_WHITE
        p1.alignment = PP_ALIGN.CENTER
        
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = "Arial"
        p2.font.size = Pt(10)
        p2.font.color.rgb = RGBColor(230, 235, 245)
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(6)

    # Add Security Layer below
    sec_box = s7.shapes.add_shape(1, Inches(3.1), Inches(4.5), Inches(7.0), Inches(1.2))
    sec_box.fill.solid()
    sec_box.fill.fore_color.rgb = RGBColor(20, 30, 45)
    sec_box.line.color.rgb = COLOR_RED
    sec_box.line.width = Pt(1.5)
    
    tf_sec = sec_box.text_frame
    tf_sec.word_wrap = True
    p = tf_sec.paragraphs[0]
    p.text = "Capa Transversal de Seguridad: Huawei Cloud ModelArts Guard"
    p.font.name = "Arial"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_RED
    p.alignment = PP_ALIGN.CENTER
    
    p2 = tf_sec.add_paragraph()
    p2.text = "Anonimización de PII (DNI, Tarjetas, Datos Personales) + Validación de Matrices Técnicas (Flyer N° 41) y Normativa OSIPTEL"
    p2.font.name = "Arial"
    p2.font.size = Pt(10)
    p2.font.color.rgb = RGBColor(220, 225, 235)
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(4)

    # -------------------------------------------------------------
    # SLIDE 8: FUNCIONES PRINCIPALES
    # -------------------------------------------------------------
    s8 = prs.slides[7]
    set_content_box(s8, [
        ("1. Protección 'Back-to-Back' y Cero Pausa en AICC:", "Autocompleta AICC en 5 segundos al colgar. El asesor no necesita pausarse más de 3 minutos ni temer que el robot le mande otra llamada sin haber cerrado la anterior."),
        ("2. Aprobación Garantizada en Auditoría Horaria AICC:", "Cero llamadas pendientes de tipificar por hora; elimina multas y llamados de atención de supervisión."),
        ("3. Gestión Inteligente de Ciclo de Llamadas (Primer Toque):", "Detecta llamadas no contestadas o buzón de voz y genera la plantilla estándar de ciclo (3 llamadas c/2h x 2 días) en SIAC Único y AICC."),
        ("4. Plantilla Completa para SIAC Único y Helix:", "Diagnóstico exhaustivo de descartes (Incógnito, Schaman, TR-069, Flyer 41) y SOT listo para inyección o copia en 1 clic."),
        ("5. Diagnóstico de Brechas para Formación & QA 100%:", "Monitorea la calidad técnica sin exigir a los auditores escuchar audios de 45 minutos."),
        ("Unicidad:", "Resuelve el conflicto real de métricas: velocidad de atención (robot AICC) vs. calidad del registro técnico (SIAC/Helix).")
    ])

    # -------------------------------------------------------------
    # SLIDE 9: INNOVACIONES
    # -------------------------------------------------------------
    s9 = prs.slides[8]
    set_content_box(s9, [
        ("Innovación de Ecosistema Nativo Huawei:", "Fusión directa de telefonía Huawei AICC con Huawei Cloud ModelArts Studio (MaaS), procesando audio de larga duración (hasta 1 hora) con cómputo Ascend NPU."),
        ("Integración Multi-Sistema sin Fricción:", "Conecta el universo de voz (Huawei AICC) con los sistemas transaccionales y de tickets de Claro (SIAC Único y BMC Helix)."),
        ("Innovación en Formación y Calidad:", "Transformación radical del área de Calidad: de auditar ciegamente 1 o 2 llamadas al mes por asesor a tener el 100% de la operación calificada con insights pedagógicos automáticos."),
        ("Cumplimiento Estricto de Normativa OSIPTEL:", "Supervisión automatizada del derecho al reclamo y plazos de atención en llamadas complejas, blindando a la empresa contra sanciones de hasta 150 UIT.")
    ])

    # -------------------------------------------------------------
    # SLIDE 10: VALOR EMPRESARIAL Y MODELO DE NEGOCIO
    # -------------------------------------------------------------
    s10 = prs.slides[9]
    set_content_box(s10, [
        ("100% de Aprobación en Auditoría Horaria de AICC:", "Erradica las llamadas sin tipificar causadas por llamadas consecutivas del marcador predictivo, garantizando métricas operativas perfectas."),
        ("Eliminación de Sobre-Pausas (>3 min) y Voceos:", "El asesor ya no tiene que arriesgar sanciones por pausarse para redactar plantillas complejas de soporte técnico."),
        ("Ahorro de Tiempo en Backoffice N2 (ACW):", "Ahorro de 4 minutos por llamada al autocompletar para SIAC Único y Helix. Equivale a más de 5,300 horas-hombre mensuales liberadas en 80,000 llamadas."),
        ("Desbloqueo de Calidad y Formación:", "Capacidad de auditar el 100% de las llamadas de 15 a 60 minutos sin requerir contratar decenas de nuevos auditores humanos."),
        ("Reducción de Fuga de Clientes Técnicos (Churn):", "Detección temprana de clientes frustrados con intermitencia prolongada, disparando retención proactiva antes de que cancelen el servicio ($850,000 USD anuales).")
    ])

    # -------------------------------------------------------------
    # SLIDE 11: VERIFICACIÓN Y PRUEBAS BETA
    # -------------------------------------------------------------
    s11 = prs.slides[10]
    set_content_box(s11, [
        ("Metodología de Validación:", "Evaluación con un dataset piloto de 1,200 grabaciones reales y simuladas de colas de reclamos de facturación, portabilidad y servicio técnico."),
        ("Precisión en Detección de Churn:", "94.2% de precisión (F1-Score: 0.93) en la identificación correcta de clientes con intención activa de cambio de operador."),
        ("Precisión en Auditoría OSIPTEL:", "97.5% de efectividad detectando omisiones en la entrega de códigos de reclamo y lectura de condiciones contractuales."),
        ("Consistencia del Resumen Auto-ACW:", "91% de aprobación por supervisores senior de contact center, calificando los resúmenes generados por MaaS como superiores o iguales a los redactados manualmente."),
        ("Latencia de Inferencia:", "Respuesta promedio de 240ms por llamada en clúster Ascend NPU, apto para asistencia en línea.")
    ])

    # -------------------------------------------------------------
    # SLIDE 12: PLANIFICACIÓN Y ROADMAP
    # -------------------------------------------------------------
    s12 = prs.slides[11]
    set_content_box(s12, [
        ("Fase 1: MVP & Pipeline Cloud (Mes 1):", "Conexión de repositorios de audio con Huawei Cloud OBS, configuración de FunctionGraph y habilitación de endpoints MaaS en ModelArts Studio."),
        ("Fase 2: Integración CRM & Alertas en Vivo (Mes 2):", "Conector bidireccional con CRM (Salesforce / Siebel / Claro CRM) para inyección automática de tipificaciones y alertas en tiempo real al supervisor."),
        ("Fase 3: Despliegue Masivo & Multicanal (Mes 3-4):", "Cobertura del 100% de las colas de atención por voz; extensión del motor MaaS a canales de mensajería (WhatsApp, ClaroBot y Webchat)."),
        ("Fase 4: Modelo Predictivo Avanzado con Pangu (Mes 5+):", "Fine-tuning con datos históricos en Pangu NLP para predecir propensión de compra (cross-sell) y personalización hiper-segmentada.")
    ])

    # -------------------------------------------------------------
    # SLIDE 13: LOGROS PREVISTOS
    # -------------------------------------------------------------
    s13 = prs.slides[12]
    # Update rectangle 6 in slide 13 (keep title in 文本框 68)
    for sh in s13.shapes:
        if sh.name == '矩形 6' and sh.has_text_frame:
            tf = sh.text_frame
            tf.clear()
            tf.word_wrap = True
            
            p = tf.paragraphs[0]
            p.text = "METAS Y RESULTADOS ESPERADOS (KPIs):"
            p.font.name = "Arial"
            p.font.bold = True
            p.font.size = Pt(16)
            p.font.color.rgb = COLOR_RED
            
            kpis = [
                ("100% de Auditoría Universal:", "Eliminación total del 98% de puntos ciegos en la calidad de atención."),
                ("+28.4% de Retención Exitosa:", "Frenar la fuga de clientes de alto valor mediante intervención en menos de 5 minutos."),
                ("-65% en Tiempo de After Call Work (ACW):", "Liberación de más de 19,000 horas-hombre mensuales en tipificación de llamadas."),
                ("Cero Multas por Procedimiento OSIPTEL:", "Garantía de cumplimiento del 100% en entrega de números correlativos de reclamo."),
                ("Costo Elástico Reducido:", "Menos de $0.003 USD por interacción auditada gracias al modelo Pay-per-Token de MaaS."),
                ("Adopción en Todo el Ecosistema Telco:", "Solución lista para extenderse a Claro Perú, filiales de América Móvil y clientes de Global Hitss.")
            ]
            for title, desc in kpis:
                p = tf.add_paragraph()
                r1 = p.add_run()
                r1.text = f"• {title} "
                r1.font.bold = True
                r1.font.size = Pt(12)
                r1.font.color.rgb = COLOR_RED
                r2 = p.add_run()
                r2.text = desc
                r2.font.size = Pt(12)
                r2.font.color.rgb = RGBColor(40, 45, 55)
                p.space_before = Pt(6)

    # -------------------------------------------------------------
    # SLIDE 14: DEMO EN VIDEO Y EN VIVO
    # -------------------------------------------------------------
    s14 = prs.slides[13]
    # Add a clean presentation box with link and demo info
    tb14 = s14.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(10.5), Inches(4.5))
    tf14 = tb14.text_frame
    tf14.word_wrap = True
    
    p = tf14.paragraphs[0]
    p.text = "DEMOSTRACIÓN FUNCIONAL DE TELCOPULSE MAAS"
    p.font.name = "Arial"
    p.font.bold = True
    p.font.size = Pt(18)
    p.font.color.rgb = COLOR_RED
    
    demo_items = [
        ("Video Demostrativo:", "Disponible en el Google Drive oficial: enlace directo incluido en el material entregado."),
        ("Prototipo Interactivo en Vivo:", "Dashboard cloud-native que simula la ingesta desde Huawei AICC y la inferencia en tiempo real de ModelArts Studio MaaS."),
        ("Casos de Prueba Reales Demostrados en el Video:", ""),
        ("   • Caso 1 (Llamada N2 Crítica):", "Cliente con intermitencia en HFC. MaaS analiza la llamada de 38 min, detecta niveles fuera de rango en Incógnito (Flyer N° 41), genera alerta OSIPTEL y autocompleta la Plantilla Oficial para SIAC Único y Helix con SOT."),
        ("   • Caso 2 (Impacto en Formación):", "Identificación de brecha técnica del asesor en descarte de repetidores WiFi externos y saturación TR-069, enviando recomendación a Formación."),
        ("   • Caso 3 (Auditoría de Calidad 100%):", "Panel de QA donde los auditores revisan en segundos la adherencia a la matriz de atención de llamadas largas."),
        ("Acceso al Código y Prototipo:", "Repositorio y dashboard listos para demostración durante la jornada en Blue Tower.")
    ]
    
    for title, desc in demo_items:
        p = tf14.add_paragraph()
        r1 = p.add_run()
        r1.text = f"{title} "
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = COLOR_RED if "•" in title else COLOR_DARK
        r2 = p.add_run()
        r2.text = desc
        r2.font.size = Pt(12)
        r2.font.color.rgb = RGBColor(50, 55, 65)
        p.space_before = Pt(4)

    # Save to the presentation file
    prs.save('Huawei Cloud Peru MaaS Hackathon Template External.pptx')
    prs.save('AICC_BO_Assistant_Hackathon_Final.pptx')
    prs.save('AICC_BO_Assistant_Hackathon_Final 2.pptx')
    print("Presentation successfully updated and saved!")

if __name__ == '__main__':
    build_presentation()
