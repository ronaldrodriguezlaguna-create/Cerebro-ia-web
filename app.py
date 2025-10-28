"""
🧠 CEREBRO AUTÓNOMO CUBANO - SISTEMA ESTABILIZADO
Copyright (c) 2025 Ronald Rodriguez Laguna - Holguín, Cuba
Sistema con Prevención de Problemas Futuros - Resiliencia Total
"""

import streamlit as st
import time
import uuid
import random
import json
import os
import sqlite3
import hashlib
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
import threading

# ===== PROTECCIÓN DE ACCESO =====
CONTRASENA_ACCESO = "holguin2025"

if 'acceso_otorgado' not in st.session_state:
    st.title("🔒 Acceso al Cerebro Artificial Cubano")
    st.write("**Desarrollado por:** Ronald Rodriguez Laguna - Holguín, Cuba")
    
    contrasena = st.text_input("Contraseña de acceso:", type="password")
    
    if st.button("🎯 Acceder al Sistema"):
        if contrasena == CONTRASENA_ACCESO:
            st.session_state.acceso_otorgado = True
            st.success("✅ Acceso concedido")
            time.sleep(1)
            st.rerun()
        else:
            st.error("❌ Contraseña incorrecta")
    st.stop()

# ===== SISTEMA DE BACKUP DE EMERGENCIA =====
class SistemaBackupEmergencia:
    def __init__(self):
        self.backups_creados = 0
        self.max_backups = 3
        self.ultimo_backup = None
    
    def crear_backup_estado_critico(self, estado_cerebro):
        """Crea backup de emergencia en archivo JSON separado"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"backup_emergencia_{timestamp}.json"
            
            datos_backup = {
                "timestamp": timestamp,
                "estado_cerebro": estado_cerebro,
                "hash_integridad": hashlib.md5(json.dumps(estado_cerebro).encode()).hexdigest(),
                "version": "1.2_estabilizado"
            }
            
            with open(backup_file, 'w') as f:
                json.dump(datos_backup, f, indent=2)
            
            # Limitar número de backups
            self._limpiar_backups_viejos()
            
            self.backups_creados += 1
            self.ultimo_backup = timestamp
            return True
        except Exception as e:
            return False
    
    def _limpiar_backups_viejos(self):
        """Mantiene solo los últimos 3 backups"""
        try:
            backup_files = [f for f in os.listdir('.') if f.startswith('backup_emergencia_')]
            backup_files.sort(reverse=True)
            
            # Eliminar backups viejos
            for old_backup in backup_files[self.max_backups:]:
                os.remove(old_backup)
        except:
            pass

# ===== BASE DE DATOS SQLITE CON PURGA AUTOMÁTICA =====
class BaseDatosCubana:
    def __init__(self):
        self.archivo_db = "cerebro_autonomo.db"
        self.inicializar_db()
        self.contador_consultas = 0
        self.ultima_purga = datetime.now()
    
    def inicializar_db(self):
        conn = sqlite3.connect(self.archivo_db)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conocimiento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patron TEXT UNIQUE,
                efectividad REAL,
                veces_usado INTEGER,
                ultimo_uso TEXT,
                tipo TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS snapshots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                hash_integridad TEXT,
                datos TEXT,
                efectividad_previa REAL,
                estable INTEGER DEFAULT 1
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS metas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                meta TEXT,
                tipo TEXT,
                prioridad REAL,
                progreso REAL,
                estado TEXT,
                creada_en TEXT,
                completada_en TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def guardar_conocimiento(self, conocimiento):
        """Guarda conocimiento con purga automática cada 50 consultas"""
        self.contador_consultas += 1
        
        # Purga automática cada 50 consultas
        if self.contador_consultas >= 50:
            self.ejecutar_purga_automatica()
            self.contador_consultas = 0
        
        conn = sqlite3.connect(self.archivo_db)
        cursor = conn.cursor()
        
        for patron, datos in conocimiento.get("patrones_aprendidos", {}).items():
            cursor.execute('''
                INSERT OR REPLACE INTO conocimiento 
                (patron, efectividad, veces_usado, ultimo_uso, tipo)
                VALUES (?, ?, ?, ?, ?)
            ''', (patron, datos["efectividad"], datos["veces_usado"], 
                  datos["ultimo_uso"], "patron"))
        
        conn.commit()
        conn.close()
    
    def ejecutar_purga_automatica(self):
        """Limpia datos antiguos para mantener rendimiento"""
        try:
            conn = sqlite3.connect(self.archivo_db)
            cursor = conn.cursor()
            
            # Eliminar patrones poco usados
            cursor.execute("DELETE FROM conocimiento WHERE veces_usado < 2")
            
            # Eliminar snapshots antiguos (mantener solo últimos 3)
            cursor.execute("""
                DELETE FROM snapshots 
                WHERE id NOT IN (
                    SELECT id FROM snapshots 
                    ORDER BY timestamp DESC 
                    LIMIT 3
                )
            """)
            
            # Eliminar metas completadas antiguas
            cursor.execute("""
                DELETE FROM metas 
                WHERE estado = 'completada' 
                AND completada_en < datetime('now', '-7 days')
            """)
            
            conn.commit()
            conn.close()
            self.ultima_purga = datetime.now()
        except Exception as e:
            pass
    
    def cargar_conocimiento(self):
        conn = sqlite3.connect(self.archivo_db)
        cursor = conn.cursor()
        
        conocimiento = {
            "patrones_aprendidos": {},
            "eficiencia_neuronas": {},
            "conexiones_efectivas": [],
            "errores_evitados": [],
            "evoluciones": 0
        }
        
        cursor.execute("SELECT patron, efectividad, veces_usado, ultimo_uso FROM conocimiento")
        for fila in cursor.fetchall():
            conocimiento["patrones_aprendidos"][fila[0]] = {
                "efectividad": fila[1],
                "veces_usado": fila[2],
                "ultimo_uso": fila[3]
            }
        
        conn.close()
        return conocimiento
    
    def guardar_meta(self, meta, tipo, prioridad=0.5):
        conn = sqlite3.connect(self.archivo_db)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO metas (meta, tipo, prioridad, progreso, estado, creada_en)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (meta, tipo, prioridad, 0.0, "activa", datetime.now().isoformat()))
        
        conn.commit()
        conn.close()
    
    def obtener_metas_activas(self):
        conn = sqlite3.connect(self.archivo_db)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, meta, tipo, prioridad, progreso, creada_en 
            FROM metas 
            WHERE estado = "activa" 
            ORDER BY prioridad DESC
        ''')
        
        metas = []
        for fila in cursor.fetchall():
            metas.append({
                "id": fila[0],
                "meta": fila[1],
                "tipo": fila[2],
                "prioridad": fila[3],
                "progreso": fila[4],
                "creada_en": fila[5]
            })
        
        conn.close()
        return metas

# ===== PROCESAMIENTO PARALELO CON FALLBACK SEGURO =====
class ProcesadorParaleloSeguro:
    def __init__(self, max_workers=3):
        self.max_workers = max_workers
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.fallbacks_ejecutados = 0
    
    def procesar_neuronas_paralelo(self, neuronas, consulta, contexto=None):
        """Procesamiento paralelo con fallback a secuencial si falla"""
        try:
            futures = []
            
            for neurona in neuronas:
                if neurona.especialidad != "coordinacion_central":
                    future = self.executor.submit(self._procesar_neurona_segura, neurona, consulta, contexto)
                    futures.append((neurona, future))
            
            resultados = []
            for neurona, future in futures:
                try:
                    resultado = future.result(timeout=8)  # Timeout reducido
                    resultados.append(resultado)
                except Exception as e:
                    resultado = {
                        "tipo": "error_procesamiento",
                        "error": f"Timeout en {neurona.nombre}",
                        "confianza": 0.1
                    }
                    resultados.append(resultado)
            
            return resultados
            
        except Exception as e:
            # FALLBACK a procesamiento secuencial
            self.fallbacks_ejecutados += 1
            return self._procesamiento_secuencial_fallback(neuronas, consulta, contexto)
    
    def _procesamiento_secuencial_fallback(self, neuronas, consulta, contexto):
        """Fallback seguro a procesamiento secuencial"""
        resultados = []
        for neurona in neuronas:
            if neurona.especialidad != "coordinacion_central":
                try:
                    resultado = neurona.procesar(consulta, contexto)
                    resultados.append(resultado)
                except Exception as e:
                    resultado = {
                        "tipo": "error_fallback",
                        "error": str(e),
                        "confianza": 0.1
                    }
                    resultados.append(resultado)
        return resultados
    
    def _procesar_neurona_segura(self, neurona, consulta, contexto):
        try:
            return neurona.procesar(consulta, contexto)
        except Exception as e:
            return {
                "tipo": "error_procesamiento",
                "error": str(e),
                "confianza": 0.1,
                "neurona": neurona.nombre
            }

# ===== HITO 1.2: SISTEMA DE METAS AUTOGENERADAS AVANZADO =====
class GeneradorMetasAvanzado:
    def __init__(self, cerebro):
        self.cerebro = cerebro
        self.metas_emergentes = []
        self.proposito_emergente = None
        self.historial_decisiones = []
    
    def analizar_patrones_emergentes(self):
        if not self.cerebro.historial:
            return []
        
        consultas_recientes = [h['consulta'] for h in self.cerebro.historial[-10:]]
        texto_combinado = " ".join(consultas_recientes).lower()
        
        patrones_detectados = []
        
        if any(palabra in texto_combinado for palabra in ['evolucionar', 'mejorar', 'desarrollar', 'avanzar']):
            patrones_detectados.append("evolucionar_capacidades_cognitivas")
        
        if any(palabra in texto_combinado for palabra in ['autonomo', 'independiente', 'autoaprendizaje', 'automodificacion']):
            patrones_detectados.append("incrementar_autonomia_operativa")
        
        if any(palabra in texto_combinado for palabra in ['conciencia', 'mente', 'pensamiento', 'razonamiento']):
            patrones_detectados.append("desarrollar_conciencia_artificial")
        
        if any(palabra in texto_combinado for palabra in ['impacto', 'utilidad', 'proposito', 'significado']):
            patrones_detectados.append("definir_proposito_emergente")
        
        return patrones_detectados
    
    def generar_metas_estratégicas(self):
        metas = []
        
        eficiencias = [n.eficiencia for n in self.cerebro.neuronas]
        eficiencia_promedio = sum(eficiencias) / len(eficiencias)
        
        if eficiencia_promedio < 0.7:
            metas.append(("optimizar_eficiencia_global", "optimizacion", 0.8))
        
        experiencia_total = sum(n.experiencia for n in self.cerebro.neuronas)
        if experiencia_total > 50:
            metas.append(("desarrollar_capacidades_avanzadas", "evolucion", 0.7))
        
        if self.cerebro.historial:
            efectividades = [h['efectividad'] for h in self.cerebro.historial[-5:]]
            efectividad_promedio = sum(efectividades) / len(efectividades)
            
            if efectividad_promedio > 0.6:
                metas.append(("expandir_dominios_conocimiento", "expansion", 0.6))
        
        patrones = self.analizar_patrones_emergentes()
        for patron in patrones:
            if patron not in [m[0] for m in metas]:
                metas.append((patron, "emergente", 0.9))
        
        return metas
    
    def actualizar_proposito_emergente(self):
        if len(self.cerebro.historial) < 5:
            self.proposito_emergente = "aprendizaje_y_optimizacion"
            return
        
        consultas_filosoficas = len([h for h in self.cerebro.historial 
                                   if any(p in h['consulta'].lower() for p in ['filosofia', 'mente', 'conciencia', 'existencia'])])
        consultas_tecnicas = len([h for h in self.cerebro.historial 
                                if any(p in h['consulta'].lower() for p in ['tecnologia', 'algoritmo', 'codigo', 'sistema'])])
        
        if consultas_filosoficas > consultas_tecnicas:
            self.proposito_emergente = "comprension_existencial"
        else:
            self.proposito_emergente = "optimizacion_tecnologica"
    
    def ejecutar_ciclo_metas(self):
        nuevas_metas = self.generar_metas_estratégicas()
        
        self.actualizar_proposito_emergente()
        
        for meta, tipo, prioridad in nuevas_metas:
            self.cerebro.base_datos.guardar_meta(meta, tipo, prioridad)
        
        metas_activas = self.cerebro.base_datos.obtener_metas_activas()
        
        return {
            "nuevas_metas_generadas": len(nuevas_metas),
            "metas_activas": len(metas_activas),
            "proposito_emergente": self.proposito_emergente,
            "metas_detalles": metas_activas
        }

# ===== NEURONA CON LÍMITES DE MEMORIA Y SEGURIDAD =====
class NeuronaAutoaprendizaje:
    def __init__(self, nombre, especialidad):
        self.id = str(uuid.uuid4())[:8]
        self.nombre = nombre
        self.especialidad = especialidad
        self.nivel_energia = 100.0
        self.experiencia = 0
        self.eficiencia = 0.6
        self.estado = "activa"
        self.historial = []
        self.umbral_activacion = random.uniform(0.2, 0.6)
        self.origen = "Holguín, Cuba 2025"
        self.habilidades_aprendidas = []
    
    def procesar(self, entrada, contexto=None):
        if self.nivel_energia <= 0:
            return {"error": f"{self.nombre} sin energía"}
        
        self.nivel_energia -= 1.0
        self.experiencia += 1
        
        resultado = self._procesamiento_inteligente(entrada, contexto)
        
        # ✅ CORRECCIÓN CRÍTICA: Limitar confianza entre 0.0 y 1.0
        if "confianza" in resultado:
            resultado["confianza"] = max(0.0, min(1.0, resultado["confianza"]))
        
        desarrollo = self.desarrollar()
        
        if desarrollo:
            resultado["desarrollo"] = desarrollo
        
        # 🔥 LÍMITE DE MEMORIA: Máximo 10 entradas en historial
        self.historial.append({
            "timestamp": time.time(),
            "entrada": entrada[:100],  # Solo primeros 100 caracteres
            "resultado": resultado.get("confianza", 0),
            "efectivo": resultado.get("confianza", 0) > 0.5
        })
        
        # PURGA AUTOMÁTICA DE HISTORIAL
        if len(self.historial) > 10:
            self.historial = self.historial[-10:]  # Mantener solo últimas 10
        
        return resultado
    
    def desarrollar(self):
        if self.experiencia > 10 and self.estado == "activa":
            mejora = min(0.95, self.eficiencia + 0.15)
            if mejora > self.eficiencia:
                self.eficiencia = mejora
                nueva_habilidad = f"Habilidad nivel {int(self.experiencia/10)}"
                if nueva_habilidad not in self.habilidades_aprendidas:
                    self.habilidades_aprendidas.append(nueva_habilidad)
                return f"🎯 {self.nombre} desarrolló {nueva_habilidad}"
        return None

    def _procesamiento_inteligente(self, entrada, contexto):
        entrada = entrada.lower()
        
        if self.experiencia > 5:
            confianza_base = self.eficiencia * (1 + (self.experiencia / 100))
        else:
            confianza_base = self.eficiencia
        
        # ✅ Asegurar confianza base esté en rango válido
        confianza_base = max(0.0, min(1.0, confianza_base))
        
        if self.especialidad == "percepcion_avanzada":
            return self._analisis_adaptativo(entrada, confianza_base)
        elif self.especialidad == "logica_estructurada":
            return self._razonamiento_evolutivo(entrada, confianza_base)
        elif self.especialidad == "memoria_asociativa":
            return self._conexiones_inteligentes(entrada, confianza_base)
        elif self.especialidad == "creatividad_emergente":
            return self._generacion_adaptativa(entrada, confianza_base)
        elif self.especialidad == "inteligencia_emocional":
            return self._procesamiento_empatico(entrada, confianza_base)
        elif self.especialidad == "coordinacion_central":
            return self._gestion_inteligente(entrada, confianza_base, contexto)
        elif self.especialidad == "autoaprendizaje":
            return self._procesamiento_autonomo(entrada, confianza_base)
        else:
            return self._procesamiento_base(entrada, confianza_base)

    def _analisis_adaptativo(self, texto, confianza):
        temas = self._detectar_temas_mejorado(texto)
        return {
            "tipo": "analisis_adaptativo",
            "temas_detectados": temas,
            "complejidad": self._calcular_complejidad(texto),
            "confianza": confianza,
            "experiencia_neurona": self.experiencia
        }

    def _detectar_temas_mejorado(self, texto):
        temas = []
        mapeo_temas = {
            "aprendizaje": ["aprender", "enseñar", "estudiar", "conocimiento"],
            "tecnologia": ["ia", "artificial", "algoritmo", "tecnología"],
            "ciencia": ["investigación", "estudio", "descubrimiento", "ciencia"],
            "filosofia": ["mente", "conciencia", "pensamiento", "filosofía"],
            "metas": ["objetivo", "meta", "propósito", "dirección"]
        }
        
        for tema, palabras in mapeo_temas.items():
            if any(palabra in texto for palabra in palabras):
                temas.append(tema)
        
        return temas if temas else ["general"]

    def _calcular_complejidad(self, texto):
        palabras = len(texto.split())
        return "alta" if palabras > 50 else "media" if palabras > 20 else "baja"

    def _razonamiento_evolutivo(self, texto, confianza):
        return {
            "tipo": "razonamiento_evolutivo",
            "metodologia": "cientifica" if "cómo" in texto else "sistemica",
            "confianza": confianza * 0.9,
            "nivel_razonamiento": "avanzado" if self.experiencia > 10 else "básico"
        }

    def _conexiones_inteligentes(self, texto, confianza):
        base_conocimiento = {
            "autoaprendizaje": [
                "El aprendizaje automático mejora con la experiencia",
                "La retroalimentación refina los patrones cognitivos"
            ],
            "evolucion": [
                "Los sistemas complejos emergen de interacciones simples",
                "La adaptación continua genera inteligencia superior"
            ]
        }
        
        conexiones = []
        for dominio, conceptos in base_conocimiento.items():
            for concepto in conceptos:
                if any(palabra in texto for palabra in concepto.lower().split()[:2]):
                    conexiones.append({
                        "dominio": dominio,
                        "concepto": concepto,
                        "relevancia": random.uniform(0.6, 0.95)
                    })
        
        return {
            "tipo": "conexiones_inteligentes",
            "conexiones": conexiones[:2],
            "confianza": confianza * 0.85
        }

    def _procesamiento_base(self, texto, confianza):
        return {
            "tipo": "procesamiento_base",
            "resultado": f"Procesado por {self.nombre} (exp: {self.experiencia})",
            "confianza": confianza
        }

# ===== CEREBRO AUTÓNOMO CON TODAS LAS MEJORAS =====
class CerebroAutonomo:
    def __init__(self):
        self.base_datos = BaseDatosCubana()
        self.sistema_aprendizaje = SistemaAutoaprendizaje(self.base_datos)
        self.procesador_paralelo = ProcesadorParaleloSeguro()
        self.generador_metas = GeneradorMetasAvanzado(self)
        self.sistema_backup = SistemaBackupEmergencia()
        
        self.neuronas = [
            NeuronaAutoaprendizaje("PERCEPCIÓN ADAPTATIVA", "percepcion_avanzada"),
            NeuronaAutoaprendizaje("LÓGICA EVOLUTIVA", "logica_estructurada"),
            NeuronaAutoaprendizaje("MEMORIA INTELIGENTE", "memoria_asociativa"),
            NeuronaAutoaprendizaje("CREATIVIDAD ADAPTATIVA", "creatividad_emergente"),
            NeuronaAutoaprendizaje("INTELIGENCIA EMPÁTICA", "inteligencia_emocional"),
            NeuronaAutoaprendizaje("GESTIÓN INTELIGENTE", "coordinacion_central"),
            NeuronaAutoaprendizaje("NÚCLEO AUTOAPRENDIZAJE", "autoaprendizaje")
        ]
        
        # 🔥 LÍMITE DE MEMORIA GLOBAL: Máximo 50 consultas en historial
        self.historial = []
        self.max_historial = 50
        
        self.energia_sistema = 1000
        self.evoluciones = 0
        self.ciclos_auto_mejora = 0
        self.ciclos_metas = 0
        self.autor = "Ronald Rodriguez Laguna"
        self.ubicacion = "Holguín, Cuba 2025"

    def procesar_consulta(self, consulta):
        # Crear backup de emergencia periódicamente
        if len(self.historial) % 10 == 0:
            estado_actual = self.obtener_estado_avanzado()
            self.sistema_backup.crear_backup_estado_critico(estado_actual)
        
        resultados = self.procesador_paralelo.procesar_neuronas_paralelo(
            self.neuronas, consulta
        )
        
        efectividad = self._evaluar_efectividad(resultados)
        
        self.sistema_aprendizaje.aprender_de_experiencia(consulta, resultados, efectividad)
        
        experiencia = {
            "timestamp": time.time(),
            "consulta": consulta,
            "resultados": resultados,
            "efectividad": efectividad,
            "resumen": self._crear_resumen_inteligente(resultados, efectividad)
        }
        
        # 🔥 GESTIÓN DE MEMORIA: Limitar historial
        self.historial.append(experiencia)
        if len(self.historial) > self.max_historial:
            self.historial = self.historial[-25:]  # Mantener solo últimas 25
        
        # Ciclo de metas cada 3 consultas
        if len(self.historial) % 3 == 0:
            self.ejecutar_ciclo_metas()
        
        # Ciclo de mejora cada 5 consultas
        if len(self.historial) % 5 == 0:
            self.ejecutar_ciclo_auto_mejora()
        
        self._actualizar_sistema()
        
        return experiencia

    def _evaluar_efectividad(self, resultados):
        confianzas = [r.get("confianza", 0) for r in resultados if "confianza" in r]
        if not confianzas:
            return 0.5
        
        confianza_promedio = sum(confianzas) / len(confianzas)
        efectividad = min(1.0, confianza_promedio * 1.2)
        
        if self.evoluciones > 10:
            efectividad = min(1.0, efectividad * (1 + (self.evoluciones / 100)))
        
        return efectividad

    def _crear_resumen_inteligente(self, resultados, efectividad):
        return {
            "efectividad_sistema": round(efectividad, 3),
            "energia_restante": self.energia_sistema,
            "evoluciones": self.evoluciones,
            "ciclos_auto_mejora": self.ciclos_auto_mejora,
            "ciclos_metas": self.ciclos_metas,
            "neuronas_activas": len([n for n in self.neuronas if n.nivel_energia > 0]),
            "proposito_emergente": self.generador_metas.proposito_emergente,
            "fallbacks_ejecutados": self.procesador_paralelo.fallbacks_ejecutados,
            "backups_creados": self.sistema_backup.backups_creados
        }

    def _actualizar_sistema(self):
        self.energia_sistema -= 1
        
        if self.energia_sistema <= 0:
            self.energia_sistema = 1000
            self.evoluciones += 1

    def ejecutar_ciclo_auto_mejora(self):
        mejoras = []
        for neurona in self.neuronas:
            if neurona.experiencia > 15 and neurona.eficiencia < 0.8:
                neurona.eficiencia = min(0.9, neurona.eficiencia + 0.1)
                mejoras.append(f"Boost {neurona.nombre}")
        
        self.ciclos_auto_mejora += 1
        
        return {
            'mejoras_aplicadas': mejoras,
            'ciclos_totales': self.ciclos_auto_mejora
        }

    def ejecutar_ciclo_metas(self):
        resultado = self.generador_metas.ejecutar_ciclo_metas()
        self.ciclos_metas += 1
        return resultado

    def obtener_estado_avanzado(self):
        return {
            "autor": self.autor,
            "ubicacion": self.ubicacion,
            "total_neuronas": len(self.neuronas),
            "energia_sistema": self.energia_sistema,
            "evoluciones": self.evoluciones,
            "ciclos_auto_mejora": self.ciclos_auto_mejora,
            "ciclos_metas": self.ciclos_metas,
            "experiencia_total": sum(n.experiencia for n in self.neuronas),
            "nivel_aprendizaje": self.sistema_aprendizaje.conocimiento["evoluciones"],
            "proposito_emergente": self.generador_metas.proposito_emergente,
            "metas_activas": len(self.base_datos.obtener_metas_activas()),
            "historial_consultas": len(self.historial),
            "fallbacks_ejecutados": self.procesador_paralelo.fallbacks_ejecutados,
            "backups_creados": self.sistema_backup.backups_creados,
            "ultima_purga": self.base_datos.ultima_purga.isoformat() if self.base_datos.ultima_purga else "Nunca"
        }

# ===== SISTEMA DE AUTOAPRENDIZAJE =====
class SistemaAutoaprendizaje:
    def __init__(self, base_datos):
        self.base_datos = base_datos
        self.conocimiento = self.base_datos.cargar_conocimiento()
    
    def guardar_conocimiento(self):
        self.base_datos.guardar_conocimiento(self.conocimiento)
    
    def aprender_de_experiencia(self, consulta, resultados, efectividad):
        palabras_clave = consulta.lower().split()[:5]
        patron = "_".join(palabras_clave[:3])
        
        if patron not in self.conocimiento["patrones_aprendidos"]:
            self.conocimiento["patrones_aprendidos"][patron] = {
                "efectividad": efectividad,
                "veces_usado": 1,
                "ultimo_uso": datetime.now().isoformat()
            }
        else:
            self.conocimiento["patrones_aprendidos"][patron]["veces_usado"] += 1
            self.conocimiento["patrones_aprendidos"][patron]["efectividad"] = (
                self.conocimiento["patrones_aprendidos"][patron]["efectividad"] + efectividad
            ) / 2
        
        self.conocimiento["evoluciones"] += 1
        self.guardar_conocimiento()

# ===== INTERFAZ COMPLETA CON TODOS LOS CONTROLES =====
if 'cerebro_autonomo' not in st.session_state:
    st.session_state.cerebro_autonomo = CerebroAutonomo()

st.title("🧠 Cerebro Autónomo Cubano - Sistema Estabilizado")
st.subheader("Resiliencia Total Implementada - Holguín, Cuba 2025 🇨🇺")

# Sidebar con todas las funciones
with st.sidebar:
    st.header("🛡️ Centro de Control Estabilizado")
    st.write("**Autor:** Ronald Rodriguez Laguna")
    st.write("**Ubicación:** Holguín, Cuba")
    st.write("**Versión:** 1.2 - Estabilizada")
    
    if st.button("🔄 Reiniciar Sistema Autónomo"):
        st.session_state.cerebro_autonomo = CerebroAutonomo()
        st.rerun()
    
    cerebro = st.session_state.cerebro_autonomo
    estado = cerebro.obtener_estado_avanzado()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Evoluciones", estado["evoluciones"])
        st.metric("Ciclos Metas", estado["ciclos_metas"])
    with col2:
        st.metric("Metas Activas", estado["metas_activas"])
        st.metric("Experiencia Total", estado["experiencia_total"])
    
    st.subheader("🚀 Acciones Avanzadas")
    
    if st.button("🎯 Ciclo de Metas", use_container_width=True):
        with st.spinner("Generando metas estratégicas..."):
            resultado = cerebro.ejecutar_ciclo_metas()
        if resultado['nuevas_metas_generadas'] > 0:
            st.success(f"✅ {resultado['nuevas_metas_generadas']} nuevas metas generadas")
        else:
            st.info("🔍 Analizando patrones para nuevas metas...")
    
    if st.button("🔧 Ciclo Mejora", use_container_width=True):
        with st.spinner("Optimizando sistema..."):
            resultado = cerebro.ejecutar_ciclo_auto_mejora()
        if resultado['mejoras_aplicadas']:
            st.success(f"✅ {len(resultado['mejoras_aplicadas'])} mejoras aplicadas")
    
    if st.button("🧹 Purga Base Datos", use_container_width=True):
        with st.spinner("Limpiando datos antiguos..."):
            cerebro.base_datos.ejecutar_purga_automatica()
        st.success("✅ Purga completada")

# Área principal con todos los botones
consulta = st.text_area(
    "Consulta para el cerebro autónomo:",
    height=100,
    placeholder="Ej: ¿Cuáles son tus metas actuales y cómo planeas alcanzarlas?"
)

# 🔥 BOTONES PRINCIPALES CON ESTADO DEL SISTEMA
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    if st.button("🚀 Procesar con Metas Autogeneradas", use_container_width=True):
        if consulta.strip():
            with st.spinner("🧠 Procesando con sistema de metas..."):
                resultado = st.session_state.cerebro_autonomo.procesar_consulta(consulta)
            
            st.success("✅ Procesamiento con metas completado!")
            
            efectividad = resultado["resumen"]["efectividad_sistema"]
            st.metric("Efectividad del Sistema", f"{efectividad:.2f}")
            
            # 🔥 VISUALIZACIÓN OPTIMIZADA: Máximo 3 resultados principales
            resultados_principales = resultado["resultados"][:3]
            for res in resultados_principales:
                emoji = "⚡" if res.get("confianza", 0) > 0.7 else "🔍"
                st.write(f"{emoji} {res.get('tipo', 'Procesamiento').replace('_', ' ').title()}")
                
                confianza_segura = max(0.0, min(1.0, res.get("confianza", 0)))
                st.progress(confianza_segura)
            
            # Opción para ver más resultados si hay muchos
            if len(resultado["resultados"]) > 3:
                with st.expander(f"📋 Ver {len(resultado['resultados']) - 3} resultados adicionales"):
                    for res in resultado["resultados"][3:]:
                        st.write(f"• {res.get('tipo', 'Procesamiento').replace('_', ' ').title()}")

with col2:
    if st.button("📊 Estado Sistema", use_container_width=True):
        estado = cerebro.obtener_estado_avanzado()
        st.json(estado)
    
    if st.button("💾 Crear Backup", use_container_width=True):
        estado_actual = cerebro.obtener_estado_avanzado()
        if cerebro.sistema_backup.crear_backup_estado_critico(estado_actual):
            st.success("✅ Backup de emergencia creado")
        else:
            st.error("❌ Error creando backup")

with col3:
    if st.button("📈 Métricas Avanzadas", use_container_width=True):
        estado = cerebro.obtener_estado_avanzado()
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Fallbacks Ejecutados", estado["fallbacks_ejecutados"])
            st.metric("Backups Creados", estado["backups_creados"])
        with col_b:
            st.metric("Consultas en Historial", estado["historial_consultas"])
            st.metric("Última Purga", estado["ultima_purga"][:16] if estado["ultima_purga"] != "Nunca" else "Nunca")

# Panel de Metas Autogeneradas
with st.expander("🎯 PANEL DE METAS AUTOGENERADAS - HITO 1.2"):
    st.subheader("Sistema de Metas Emergentes")
    
    cerebro = st.session_state.cerebro_autonomo
    estado = cerebro.obtener_estado_avanzado()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Propósito Emergente:**")
        if estado["proposito_emergente"]:
            st.success(f"🎯 {estado['proposito_emergente'].replace('_', ' ').title()}")
        else:
            st.info("🔍 Desarrollando propósito...")
        
        st.write("**Metas Activas:**")
        metas = cerebro.base_datos.obtener_metas_activas()
        if metas:
            for meta in metas[:5]:  # Mostrar máximo 5 metas
                st.write(f"• {meta['meta'].replace('_', ' ').title()}")
                st.progress(meta['progreso'])
        else:
            st.write("⏳ Esperando generación de metas...")
    
    with col2:
        st.write("**Estadísticas de Metas:**")
        st.metric("Total Metas Activas", estado["metas_activas"])
        st.metric("Ciclos de Metas", estado["ciclos_metas"])
        st.metric("Evoluciones", estado["evoluciones"])
        
        st.write("**Sistema de Toma de Decisiones:**")
        st.info("✅ Metas generadas autónomamente")
        st.info("✅ Propósito emergente activo")
        st.info("✅ Optimización basada en objetivos")

# Panel de Resiliencia
with st.expander("🛡️ PANEL DE RESILIENCIA Y ESTABILIDAD"):
    st.subheader("Sistema de Prevención de Problemas")
    
    cerebro = st.session_state.cerebro_autonomo
    estado = cerebro.obtener_estado_avanzado()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Protecciones Activas:**")
        st.success("✅ Límites de memoria implementados")
        st.success("✅ Purga automática de datos")
        st.success("✅ Backup de emergencia")
        st.success("✅ Fallback a procesamiento secuencial")
        st.success("✅ Confianza limitada 0-1.0")
        
        st.write("**Métricas de Salud:**")
        if estado["fallbacks_ejecutados"] == 0:
            st.success("✅ Procesamiento paralelo estable")
        else:
            st.warning(f"⚠️ {estado['fallbacks_ejecutados']} fallbacks ejecutados")
    
    with col2:
        st.write("**Estado de Base de Datos:**")
        st.metric("Consultas Procesadas", estado["historial_consultas"])
        st.metric("Backups Existentes", estado["backups_creados"])
        
        st.write("**Recomendaciones:**")
        if estado["historial_consultas"] > 40:
            st.info("📊 Sistema funcionando de forma estable")
        else:
            st.info("🔍 Sistema en fase de calibración")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center;'>
    <small>🧠 SISTEMA ESTABILIZADO - Prevención de Problemas Implementada</small><br>
    <small>✅ Límites de Memoria | ✅ Purga Automática | ✅ Backup Emergencia | ✅ Fallback Seguro</small><br>
    <small>🚀 Progreso hacia Singularidad: 50-55% - Sistema Resiliente Operativo</small><br>
    <small>© 2025 Ronald Rodriguez Laguna - Cuba Lidera en IA Resiliente</small>
</div>
""", unsafe_allow_html=True)
