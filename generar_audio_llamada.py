import asyncio
import json
import edge_tts

# Voces peruanas oficiales de Microsoft Azure Speech
VOZ_ASESOR = "es-PE-AlexNeural"      # Drey Aymituma (Asesor N2 Claro / Hitss)
VOZ_CLIENTE = "es-PE-CamilaNeural"   # Magdalena Terán (Cliente)

DIALOGO = [
    {
        "id": 1,
        "hablante": "asesor",
        "nombre": "Drey Aymituma (Asesor N2)",
        "voz": VOZ_ASESOR,
        "texto": "Buenos días, le saluda Drey Aymituma del soporte técnico de segundo nivel de Claro. ¿Me comunico con la señora Magdalena Terán?",
        "descarte_detectado": "Saludo institucional y verificación de titularidad",
        "entidad": "VALIDACION_TITULAR",
        "sentimiento": "neutral"
    },
    {
        "id": 2,
        "hablante": "cliente",
        "nombre": "Magdalena Terán (Cliente)",
        "voz": VOZ_CLIENTE,
        "texto": "Buenos días joven Drey, sí con ella misma. Menos mal me llaman, tengo problemas con el internet en mi casa, está súper lento, el wifi se me para cortando y no puedo ni ver mis canales.",
        "descarte_detectado": "Problema reportado: Lentitud, intermitencia WiFi y streaming",
        "entidad": "SINTOMA_REPORTADO",
        "sentimiento": "frustrado"
    },
    {
        "id": 3,
        "hablante": "asesor",
        "nombre": "Drey Aymituma (Asesor N2)",
        "voz": VOZ_ASESOR,
        "texto": "Comprendo perfectamente su molestia señora Magdalena, descuide que hoy mismo lo solucionamos. Permítame unos segundos mientras realizo los descartes en línea. Estoy validando la plataforma Incógnito: su módem aparece aprovisionado y con señal activa. Asimismo en Schaman no registramos averías masivas en su zona.",
        "descarte_detectado": "Incógnito: Online y aprovisionado | Schaman: Sin alertas masivas",
        "entidad": "DESCARTE_INCOGNITO_SCHAMAN",
        "sentimiento": "empatico"
    },
    {
        "id": 4,
        "hablante": "cliente",
        "nombre": "Magdalena Terán (Cliente)",
        "voz": VOZ_CLIENTE,
        "texto": "Menos mal joven, porque pensé que era una caída general de toda la cuadra.",
        "descarte_detectado": "Confirmación de cliente: Avería individual",
        "entidad": "FEEDBACK_CLIENTE",
        "sentimiento": "aliviado"
    },
    {
        "id": 5,
        "hablante": "asesor",
        "nombre": "Drey Aymituma (Asesor N2)",
        "voz": VOZ_ASESOR,
        "texto": "Es una saturación interna en su router. En este momento estoy ingresando por TR-069: veo que la opción de AutoSelect estaba activada y saturando el canal. Procedo a apagar el AutoSelect y a separar las redes wifi en frecuencias independientes de dos punto cuatro y cinco gigahertz. ¿Me confirma si ya puede visualizar ambas redes en su celular?",
        "descarte_detectado": "TR-069: AutoSelect OFF | Bandas 2.4G y 5G separadas exitosamente",
        "entidad": "SOLUCION_TR069_WIFI",
        "sentimiento": "tecnico_asertivo"
    },
    {
        "id": 6,
        "hablante": "cliente",
        "nombre": "Magdalena Terán (Cliente)",
        "voz": VOZ_CLIENTE,
        "texto": "A ver... ¡Sí! Ya me aparecieron las dos redes, me conecté a la de cinco y ya me cargó el video al instante. ¡Qué rápido joven, de verdad muchas gracias!",
        "descarte_detectado": "Prueba exitosa en cliente: Navegación y canales restablecidos",
        "entidad": "CLIENTE_SATISFECHO",
        "sentimiento": "feliz"
    },
    {
        "id": 7,
        "hablante": "asesor",
        "nombre": "Drey Aymituma (Asesor N2)",
        "voz": VOZ_ASESOR,
        "texto": "Excelente señora Magdalena, queda configurado y estabilizado. Se despide Drey Aymituma de Claro. Que tenga un excelente día.",
        "descarte_detectado": "Cierre protocolar y despedida institucional",
        "entidad": "CIERRE_PROTOCOLO",
        "sentimiento": "positivo"
    },
    {
        "id": 8,
        "hablante": "cliente",
        "nombre": "Magdalena Terán (Cliente)",
        "voz": VOZ_CLIENTE,
        "texto": "Muchas gracias joven Drey, hasta luego.",
        "descarte_detectado": "Fin de comunicación",
        "entidad": "FIN_LLAMADA",
        "sentimiento": "agradecido"
    }
]

async def generar_audio_completo():
    archivos_temporales = []
    dialogo_con_tiempos = []
    
    print("Generando líneas de audio con voces neurales peruanas...")
    
    tiempo_acumulado = 0.0
    
    for i, linea in enumerate(DIALOGO):
        temp_file = f"linea_{i}.mp3"
        rate = "+3%" if linea["hablante"] == "asesor" else "+0%"
        pitch = "+0Hz"
        
        communicate = edge_tts.Communicate(linea["texto"], linea["voz"], rate=rate, pitch=pitch)
        await communicate.save(temp_file)
        archivos_temporales.append(temp_file)
        
        # Estimar duración en base al tamaño y bitrate aproximado (~48kbps / ~6000 bytes por seg)
        with open(temp_file, "rb") as f:
            bytes_len = len(f.read())
        # Un cálculo más preciso usando bitrate estándar de edge_tts mono
        duracion_est = round(bytes_len / 6000.0, 2)
        
        item = dict(linea)
        item["tiempo_inicio"] = round(tiempo_acumulado, 2)
        item["tiempo_fin"] = round(tiempo_acumulado + duracion_est, 2)
        item["duracion"] = duracion_est
        dialogo_con_tiempos.append(item)
        
        tiempo_acumulado += duracion_est
        print(f"[{linea['hablante'].upper()}] {linea['texto'][:40]}... -> {duracion_est}s")

    # Concatenar en llamada_drey_magdalena.mp3
    archivo_final = "llamada_drey_magdalena.mp3"
    with open(archivo_final, "wb") as fout:
        for temp_file in archivos_temporales:
            with open(temp_file, "rb") as fin:
                fout.write(fin.read())
                
    # Limpiar temporales
    import os
    for temp_file in archivos_temporales:
        try:
            os.remove(temp_file)
        except:
            pass

    # Guardar metadata JSON para que el teleprompter web lo consuma con precisión milimétrica
    with open("dialogo_llamada.json", "w", encoding="utf-8") as fj:
        json.dump(dialogo_con_tiempos, fj, ensure_ascii=False, indent=2)
        
    print(f"\n¡Éxito total! Archivo generado: '{archivo_final}' (Duración aprox: {round(tiempo_acumulado, 1)}s)")
    print("Metadatos guardados en 'dialogo_llamada.json'")

if __name__ == "__main__":
    asyncio.run(generar_audio_completo())

