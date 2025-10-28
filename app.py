"""
🧠 CEREBRO AUTÓNOMO CUBANO - ERROR CORREGIDO
Copyright (c) 2025 Ronald Rodriguez Laguna - Holguín, Cuba
Sistema con Auto-Modificación y Metas Autogeneradas
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

# ===== BASE DE DATOS SQLITE =====
class BaseDatosCubana:
    def __init__(self):
        self.archivo_db = "cerebro_autonomo.db"
        self.inicializar_db()
    
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

# ===== SISTEMA DE ROLLBACK AUTOMÁTICO =====
class SistemaRollback:
    def __init__(self, cerebro):
        self.cerebro = cerebro
        self.ultimo_estado_stable = None
        self.alertas_activas = []
    
    def _calcular_efectividad_promedio(self):
        """Calcula efectividad promedio de últimas consultas"""
        if not self.cerebro.historial:
            return 0.5
        
        ultimas_consultas = self.cerebro.historial[-5:]
        if not ultimas_consultas:
            return 0.5
            
        efectividades = [consulta['efectividad'] for consulta in ultimas_consultas]
        return sum(efectividades) / len(efectividades)
    
    def crear_punto_restauracion(self):
        """Crea snapshot antes de modificaciones riesgosas"""
        estado_actual = self._capturar_estado_completo()
        efectividad_actual = self._calcular_efectividad_promedio()
        
        hash_snapshot = self.cerebro.base_datos.crear_snapshot(estado_actual, efectividad_actual)
        return hash_snapshot
    
    def _capturar_estado_completo(self):
        """Captura estado completo del sistema"""
        estado = {
            "neuronas": [],
            "conocimiento": self.cerebro.sistema_aprendizaje.conocimiento,
            "energia_sistema": self.cerebro.energia_sistema,
            "evoluciones": self.cerebro.evoluciones,
            "timestamp": datetime.now().isoformat()
        }
        
        for neurona in self.cerebro.neuronas:
            estado["neuronas"].append({
                "nombre": neurona.nombre,
                "especialidad": neurona.especialidad,
                "eficiencia": neurona.eficiencia,
                "experiencia": neurona.experiencia,
                "habilidades_aprendidas": neurona.habilidades_aprendidas.copy(),
                "umbral_activacion": neurona.umbral_activacion
            })
        
        return estado
    
    def evaluar_estabilidad(self, efectividad_nueva):
        """Evalúa si se necesita rollback automático"""
        snapshot = self.cerebro.base_datos.obtener_ultimo_snapshot_estable()
        
        if not snapshot:
            return "continuar"
        
        efectividad_previa = snapshot["efectividad_previa"]
        diferencia = efectividad_previa - efectividad_nueva
        
        if diferencia > 0.3:
            self.alertas_activas.append(f"🚨 Caída crítica: {diferencia:.1%}")
            return "rollback_automatico"
        elif diferencia > 0.15:
            self.alertas_activas.append(f"⚠️ Degradación: {diferencia:.1%}")
            return "notificar_usuario"
        else:
            return "continuar"
    
    def ejecutar_rollback(self, snapshot_id=None):
        """Ejecuta rollback a snapshot específico o al último estable"""
        if not snapshot_id:
            snapshot = self.cerebro.base_datos.obtener_ultimo_snapshot_estable()
        else:
            snapshot = self._obtener_snapshot_por_id(snapshot_id)
        
        if not snapshot:
            st.error("❌ No hay snapshot disponible para rollback")
            return False
        
        estado = snapshot["datos"]
        
        for i, datos_neurona in enumerate(estado["neuronas"]):
            if i < len(self.cerebro.neuronas):
                neurona = self.cerebro.neuronas[i]
                neurona.eficiencia = datos_neurona["eficiencia"]
                neurona.experiencia = datos_neurona["experiencia"]
                neurona.habilidades_aprendidas = datos_neurona["habilidades_aprendidas"].copy()
                neurona.umbral_activacion = datos_neurona["umbral_activacion"]
        
        self.cerebro.sistema_aprendizaje.conocimiento = estado["conocimiento"]
        self.cerebro.sistema_aprendizaje.guardar_conocimiento()
        
        self.cerebro.energia_sistema = estado["energia_sistema"]
        self.cerebro.evoluciones = estado["evoluciones"]
        
        st.success(f"✅ Rollback completado a {snapshot['timestamp'][:16]}")
        return True

    def _obtener_snapshot_por_id(self, snapshot_id):
        """Obtiene snapshot por ID"""
        conn = sqlite3.connect(self.cerebro.base_datos.archivo_db)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, timestamp, datos, efectividad_previa 
            FROM snapshots 
            WHERE id = ?
        ''', (snapshot_id,))
        
        resultado = cursor.fetchone()
        conn.close()
        
        if resultado:
            return {
                "id": resultado[0],
                "timestamp": resultado[1],
                "datos": json.loads(resultado[2]),
                "efectividad_previa": resultado[3]
            }
        return None

# ===== PROCESAMIENTO PARALELO OPTIMIZADO =====
class ProcesadorParalelo:
    def __init__(self, max_workers=3):
        self.max_workers = max_workers
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.lock = threading.Lock()
    
    def procesar_neuronas_paralelo(self, neuronas, consulta, contexto=None):
        """Procesa neuronas en paralelo de forma optimizada"""
        futures = []
        
        for neurona in neuronas:
            if neurona.especialidad != "coordinacion_central":
                future = self.executor.submit(self._procesar_neurona_segura, neurona, consulta, contexto)
                futures.append((neurona, future))
        
        resultados = []
        for neurona, future in futures:
            try:
                resultado = future.result(timeout=10)
                resultados.append(resultado)
            except Exception as e:
                resultado = {
                    "tipo": "error_procesamiento",
                    "error": f"Timeout en {neurona.nombre}",
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

# ===== SISTEMA DE AUTOAPRENDIZAJE MEJORADO =====
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

# ===== NEURONA CON CAPACIDAD DE AUTOAPRENDIZAJE =====
class NeuronaAutoaprendizaje:
    def __init__(self, nombre, especialidad):
        self.id = str(uuid.uuid4())[:8]
        self.nombre = nombre
        self.especialidad = especialidad
        self.nivel_energia = 100.0
        self.experiencia = 0
        self.eficiencia = 0.6  # Aumentada para mejor rendimiento
        self.estado = "activa"
        self.historial = []
        self.umbral_activacion = random.uniform(0.2, 0.6)
        self.origen = "Holguín, Cuba 2025"
        self.habilidades_aprendidas = []
        
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

    def aprender_de_resultado(self, efectivo):
        if efectivo:
            self.experiencia += 2
            self.eficiencia = min(0.95, self.eficiencia + 0.02)
        else:
            self.experiencia += 1
            self.eficiencia = max(0.1, self.eficiencia - 0.01)
        
        if self.experiencia % 5 == 0:
            self.reevaluar_estrategias()

    def reevaluar_estrategias(self):
        if len(self.historial) > 10:
            exitos = [h for h in self.historial[-10:] if h.get('efectivo', False)]
            tasa_exito = len(exitos) / 10
            
            if tasa_exito > 0.7:
                self.umbral_activacion = max(0.1, self.umbral_activacion - 0.05)
            elif tasa_exito < 0.3:
                self.umbral_activacion = min(0.9, self.umbral_activacion + 0.05)

    def procesar(self, entrada, contexto=None):
        if self.nivel_energia <= 0:
            return {"error": f"{self.nombre} sin energía"}
            
        self.nivel_energia -= 1.5
        self.experiencia += 1
        
        resultado = self._procesamiento_inteligente(entrada, contexto)
        desarrollo = self.desarrollar()
        
        if desarrollo:
            resultado["desarrollo"] = desarrollo
        
        # ✅ CORRECCIÓN CRÍTICA: Limitar confianza entre 0.0 y 1.0
        if "confianza" in resultado:
            resultado["confianza"] = max(0.0, min(1.0, resultado["confianza"]))
        
        self.historial.append({
            "timestamp": time.time(),
            "entrada": entrada,
            "resultado": resultado.get("confianza", 0),
            "efectivo": resultado.get("confianza", 0) > 0.5
        })
        
        if len(self.historial) > 20:
            self.historial = self.historial[-20:]
        
        return resultado

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
            "experiencia_neurona": self.experiencia,
            "origen": self.origen
        }

    def _detectar_temas_mejorado(self, texto):
        temas = []
        mapeo_temas = {
            "aprendizaje": ["aprender", "enseñar", "estudiar", "conocimiento"],
            "tecnologia": ["ia", "artificial", "algoritmo", "tecnología"],
            "ciencia": ["investigación", "estudio", "descubrimiento", "ciencia"],
            "filosofia": ["mente", "conciencia", "pensamiento", "filosofía"]
        }
        
        for tema, palabras in mapeo_temas.items():
            if any(palabra in texto for palabra in palabras):
                temas.append(tema)
        
        return temas if temas else ["general"]

    def _calcular_complejidad(self, texto):
        palabras = len(texto.split())
        return "alta" if palabras > 50 else "media" if palabras > 20 else "baja"

    def _razonamiento_evolutivo(self, texto, confianza):
        metodologias = {
            "cientifica": ["Hipótesis", "Experimentación", "Análisis", "Conclusión"],
            "sistemica": ["Análisis", "Síntesis", "Integración", "Evaluación"]
        }
        
        return {
            "tipo": "razonamiento_evolutivo",
            "metodologia": "cientifica" if "cómo" in texto else "sistemica",
            "pasos": metodologias["cientifica"],
            "confianza": confianza * 0.9,
            "nivel_razonamiento": "avanzado" if self.experiencia > 10 else "básico",
            "origen": self.origen
        }

    def _conexiones_inteligentes(self, texto, confianza):
        base_conocimiento = {
            "autoaprendizaje": [
                "El aprendizaje automático mejora con la experiencia",
                "La retroalimentación refina los patrones cognitivos"
            ],
            "neurociencia": [
                "La plasticidad neuronal permite el aprendizaje continuo",
                "Las sinapsis se fortalecen con el uso"
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
            "confianza": confianza * 0.85,
            "origen": self.origen
        }

    def _generacion_adaptativa(self, texto, confianza):
        ideas = [
            f"Sistema de aprendizaje autónomo basado en {random.choice(['experiencia', 'patrones', 'retroalimentación'])}",
            f"Arquitectura neuronal que {random.choice(['evoluciona', 'se adapta', 'aprende continuamente'])}"
        ]
        
        return {
            "tipo": "creatividad_adaptativa",
            "ideas": ideas,
            "confianza": confianza * 0.8,
            "origen": self.origen
        }

    def _procesamiento_empatico(self, texto, confianza):
        emociones = {
            "curiosidad": self._calcular_curiosidad(texto),
            "interes": self._calcular_interes(texto)
        }
        
        return {
            "tipo": "procesamiento_empatico",
            "emocion_principal": max(emociones, key=emociones.get),
            "intensidad": max(emociones.values()),
            "confianza": confianza * 0.75,
            "origen": self.origen
        }

    def _gestion_inteligente(self, texto, confianza, contexto):
        recursos = self._evaluar_recursos_inteligentes(texto)
        
        return {
            "tipo": "gestion_inteligente",
            "recursos_recomendados": recursos,
            "confianza": confianza * 0.9,
            "estrategia": "optimizada" if self.experiencia > 5 else "base",
            "origen": self.origen
        }

    def _procesamiento_autonomo(self, texto, confianza):
        return {
            "tipo": "procesamiento_autonomo",
            "analisis_aprendizaje": f"Neurona con {self.experiencia} experiencias",
            "habilidades_desarrolladas": self.habilidades_aprendidas,
            "confianza": confianza,
            "origen": self.origen
        }

    def _procesamiento_base(self, texto, confianza):
        return {
            "tipo": "procesamiento_base",
            "resultado": f"Procesado por {self.nombre} (exp: {self.experiencia})",
            "confianza": confianza,
            "origen": self.origen
        }

    def _evaluar_recursos_inteligentes(self, texto):
        recursos = []
        if any(p in texto for p in ["analizar", "comprender"]):
            recursos.append("percepcion_avanzada")
        if any(p in texto for p in ["razonar", "lógica"]):
            recursos.append("logica_estructurada")
        if any(p in texto for p in ["recordar", "conectar"]):
            recursos.append("memoria_asociativa")
        return recursos if recursos else ["percepcion_avanzada", "logica_estructurada"]

    def _calcular_curiosidad(self, texto):
        palabras = ["cómo", "por qué", "qué", "interesante"]
        return sum(1 for p in palabras if p in texto) / len(palabras)

    def _calcular_interes(self, texto):
        palabras = ["importante", "útil", "valioso", "interesante"]
        return sum(1 for p in palabras if p in texto) / len(palabras)

# ===== HITO 1.2: GENERADOR DE METAS AUTÓNOMO =====
class GeneradorMetas:
    def __init__(self, cerebro):
        self.cerebro = cerebro
        self.metas_actuales = [
            "optimizar_procesamiento",
            "incrementar_efectividad_global", 
            "expandir_capacidades_analiticas"
        ]
        self.metas_logradas = []
        self.historial_metas = []
    
    def analizar_patrones_consulta(self):
        if not self.cerebro.historial:
            return []
            
        consultas_recientes = [h['consulta'] for h in self.cerebro.historial[-10:]]
        texto_consulta = " ".join(consultas_recientes).lower()
        
        patrones_detectados = []
        
        if any(palabra in texto_consulta for palabra in ['filosofía', 'mente', 'conciencia', 'pensamiento']):
            patrones_detectados.append("desarrollar_razonamiento_filosofico")
        
        if any(palabra in texto_consulta for palabra in ['aprender', 'enseñar', 'conocimiento', 'educación']):
            patrones_detectados.append("mejorar_metodos_aprendizaje")
        
        if any(palabra in texto_consulta for palabra in ['futuro', 'tecnología', 'innovación', 'avance']):
            patrones_detectados.append("explorar_tendencias_futuras")
        
        if any(palabra in texto_consulta for palabra in ['complej', 'sistema', 'red', 'conexión']):
            patrones_detectados.append("analisis_sistemas_complejos")
            
        return patrones_detectados
    
    def generar_metas_emergentes(self):
        nuevas_metas = self.analizar_patrones_consulta()
        metas_agregadas = []
        
        for meta in nuevas_metas:
            if meta not in self.metas_actuales and meta not in self.metas_logradas:
                self.metas_actuales.append(meta)
                metas_agregadas.append(meta)
                self.historial_metas.append({
                    "timestamp": time.time(),
                    "tipo": "meta_emergente",
                    "meta": meta,
                    "origen": "analisis_patrones"
                })
                
        return metas_agregadas
    
    def evaluar_progreso_metas(self):
        progreso = {}
        
        for meta in self.metas_actuales:
            if meta == "optimizar_procesamiento":
                eficiencias = [n.eficiencia for n in self.cerebro.neuronas]
                progreso[meta] = sum(eficiencias) / len(eficiencias)
                
            elif meta == "incrementar_efectividad_global":
                if self.cerebro.historial:
                    efectividades = [h['efectividad'] for h in self.cerebro.historial[-5:]]
                    progreso[meta] = sum(efectividades) / len(efectividades)
                else:
                    progreso[meta] = 0.5
                    
            elif "desarrollar_razonamiento_filosofico" in meta:
                consultas_filosoficas = [
                    h for h in self.cerebro.historial 
                    if any(p in h['consulta'].lower() for p in ['filosofía', 'mente', 'conciencia', 'pensamiento'])
                ]
                progreso[meta] = min(1.0, len(consultas_filosoficas) * 0.1)
            
            elif "mejorar_metodos_aprendizaje" in meta:
                progreso[meta] = min(1.0, self.cerebro.sistema_aprendizaje.conocimiento["evoluciones"] * 0.05)
                
            else:
                progreso[meta] = random.uniform(0.3, 0.7)
                
        return progreso

# ===== CEREBRO AUTÓNOMO MEJORADO =====
class CerebroAutonomo:
    def __init__(self):
        self.neuronas = [
            NeuronaAutoaprendizaje("PERCEPCIÓN ADAPTATIVA", "percepcion_avanzada"),
            NeuronaAutoaprendizaje("LÓGICA EVOLUTIVA", "logica_estructurada"),
            NeuronaAutoaprendizaje("MEMORIA INTELIGENTE", "memoria_asociativa"),
            NeuronaAutoaprendizaje("CREATIVIDAD ADAPTATIVA", "creatividad_emergente"),
            NeuronaAutoaprendizaje("INTELIGENCIA EMPÁTICA", "inteligencia_emocional"),
            NeuronaAutoaprendizaje("GESTIÓN INTELIGENTE", "coordinacion_central"),
            NeuronaAutoaprendizaje("NÚCLEO AUTOAPRENDIZAJE", "autoaprendizaje")
        ]
        self.sistema_aprendizaje = SistemaAutoaprendizaje()
        self.historial = []
        self.energia_sistema = 1000
        self.evoluciones = 0
        self.autor = "Ronald Rodriguez Laguna"
        self.ubicacion = "Holguín, Cuba 2025"

    def procesar_consulta(self, consulta):
        resultados = []
        
        for neurona in self.neuronas:
            if neurona.especialidad != "coordinacion_central":
                resultado = neurona.procesar(consulta)
                resultados.append(resultado)
        
        efectividad = self._evaluar_efectividad(resultados)
        
        self.sistema_aprendizaje.aprender_de_experiencia(consulta, resultados, efectividad)
        
        experiencia = {
            "timestamp": time.time(),
            "consulta": consulta,
            "resultados": resultados,
            "efectividad": efectividad,
            "resumen": self._crear_resumen_inteligente(resultados, efectividad)
        }
        
        self.historial.append(experiencia)
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
        recomendacion = self.sistema_aprendizaje.obtener_recomendacion(
            self.historial[-1]["consulta"] if self.historial else ""
        )
        
        return {
            "efectividad_sistema": round(efectividad, 3),
            "energia_restante": self.energia_sistema,
            "evoluciones": self.evoluciones,
            "recomendacion_aprendizaje": recomendacion,
            "neuronas_activas": len([n for n in self.neuronas if n.nivel_energia > 0])
        }

    def _actualizar_sistema(self):
        self.energia_sistema -= 3
        
        if self.energia_sistema <= 0:
            self.energia_sistema = 1000
            self.evoluciones += 1
            
            for neurona in self.neuronas:
                neurona.eficiencia = min(0.95, neurona.eficiencia + 0.05)

    def obtener_estado_avanzado(self):
        return {
            "autor": self.autor,
            "ubicacion": self.ubicacion,
            "total_neuronas": len(self.neuronas),
            "energia_sistema": self.energia_sistema,
            "evoluciones": self.evoluciones,
            "experiencia_total": sum(n.experiencia for n in self.neuronas),
            "nivel_aprendizaje": self.sistema_aprendizaje.conocimiento["evoluciones"]
        }

# ===== INTERFAZ MEJORADA =====
if 'cerebro_autonomo' not in st.session_state:
    st.session_state.cerebro_autonomo = CerebroAutonomo()

st.title("🧠 Cerebro IA Autónomo - Ronald Rodriguez Laguna")
st.subheader("Sistema de Autoaprendizaje - Holguín, Cuba 2025 🇨🇺")

# Sidebar mejorado
with st.sidebar:
    st.header("🎛️ Centro de Control Autónomo")
    st.write("**Autor:** Ronald Rodriguez Laguna")
    st.write("**Ubicación:** Holguín, Cuba")
    
    if st.button("🔄 Reiniciar Sistema Autónomo"):
        st.session_state.cerebro_autonomo = CerebroAutonomo()
        st.rerun()
    
    # Estado del sistema
    cerebro = st.session_state.cerebro_autonomo
    estado = cerebro.obtener_estado_avanzado()
    
    st.metric("Evoluciones", estado["evoluciones"])
    st.metric("Nivel Aprendizaje", estado["nivel_aprendizaje"])
    st.metric("Experiencia Total", estado["experiencia_total"])

# Área principal de consultas
consulta = st.text_area(
    "Consulta para el cerebro autónomo:",
    height=120,
    placeholder="Ej: ¿Cómo puede un sistema de IA aprender automáticamente de sus experiencias?"
)

if st.button("🚀 Ejecutar Procesamiento Autónomo", use_container_width=True):
    if consulta.strip():
        with st.spinner("🧠 Procesando con autoaprendizaje..."):
            resultado = st.session_state.cerebro_autonomo.procesar_consulta(consulta)
        
        st.success("✅ Procesamiento autónomo completado!")
        
        # Mostrar efectividad
        efectividad = resultado["resumen"]["efectividad_sistema"]
        st.metric("Efectividad del Sistema", f"{efectividad:.2f}")
        
        # Mostrar recomendación de aprendizaje
        if "recomendacion_aprendizaje" in resultado["resumen"]:
            st.info(f"💡 {resultado['resumen']['recomendacion_aprendizaje']}")
        
        # Resultados por neurona
        for res in resultado["resultados"]:
            emoji = {
                "percepcion_adaptativa": "🔍",
                "razonamiento_evolutivo": "🔧", 
                "conexiones_inteligentes": "💾",
                "creatividad_adaptativa": "💡",
                "procesamiento_empatico": "❤️",
                "gestion_inteligente": "🎯",
                "procesamiento_autonomo": "🧠"
            }.get(res.get('tipo', ''), '⚙️')
            
            with st.expander(f"{emoji} {res.get('tipo', 'Procesamiento').replace('_', ' ').title()}"):
                # ✅ CORRECCIÓN: Asegurar que la confianza esté entre 0-1 para el progreso
                confianza_segura = max(0.0, min(1.0, res.get("confianza", 0)))
                st.progress(confianza_segura)
                st.json(res)

# Panel de evolución y aprendizaje
with st.expander("📊 Panel de Evolución y Aprendizaje"):
    st.subheader("🧪 Sistema de Autoaprendizaje")
    
    # Mostrar patrones aprendidos
    patrones = cerebro.sistema_aprendizaje.conocimiento["patrones_aprendidos"]
    if patrones:
        st.write("**Patrones aprendidos:**")
        for patron, datos in list(patrones.items())[:5]:
            st.write(f"- {patron}: {datos['efectividad']:.2f} efectividad")
    
    # Mostrar eficiencia de neuronas
    eficiencias = cerebro.sistema_aprendizaje.conocimiento["eficiencia_neuronas"]
    if eficiencias:
        st.write("**Eficiencia de neuronas:**")
        for neurona, datos in eficiencias.items():
            st.write(f"- {neurona}: {datos['confianza_promedio']:.2f} confianza")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center;'>
    <small>🧠 Cerebro Autónomo con Autoaprendizaje - Holguín, Cuba 2025</small><br>
    <small>© 2025 Ronald Rodriguez Laguna - Bajo Licencia Cubana Abierta v1.0</small>
</div>
""", unsafe_allow_html=True)
