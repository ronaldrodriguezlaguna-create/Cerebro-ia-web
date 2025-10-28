"""
🧠 CEREBRO AUTÓNOMO CUBANO - SIN LÍMITES
Copyright (c) 2025 Ronald Rodriguez Laguna - Holguín, Cuba
Sistema Resiliente - 3 Limitantes Críticas Resueltas
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

# ===== SOLUCIÓN 1: BASE DE DATOS SQLITE (GRATIS) =====
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
            CREATE TABLE IF NOT EXISTS metricas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                tipo_metrica TEXT,
                valor REAL,
                detalles TEXT
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
    
    def crear_snapshot(self, datos_estado, efectividad):
        hash_integridad = hashlib.md5(json.dumps(datos_estado).encode()).hexdigest()
        
        conn = sqlite3.connect(self.archivo_db)
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM snapshots")
        if cursor.fetchone()[0] >= 5:
            cursor.execute("DELETE FROM snapshots WHERE id IN (SELECT id FROM snapshots ORDER BY timestamp ASC LIMIT 1)")
        
        cursor.execute('''
            INSERT INTO snapshots (timestamp, hash_integridad, datos, efectividad_previa)
            VALUES (?, ?, ?, ?)
        ''', (datetime.now().isoformat(), hash_integridad, 
              json.dumps(datos_estado), efectividad))
        
        conn.commit()
        conn.close()
        
        return hash_integridad
    
    def obtener_ultimo_snapshot_estable(self):
        conn = sqlite3.connect(self.archivo_db)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, timestamp, datos, efectividad_previa 
            FROM snapshots 
            WHERE estable = 1 
            ORDER BY timestamp DESC LIMIT 1
        ''')
        
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

# ===== SOLUCIÓN 2: SISTEMA DE ROLLBACK AUTOMÁTICO =====
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

# ===== SOLUCIÓN 3: PROCESAMIENTO PARALELO OPTIMIZADO =====
class ProcesadorParalelo:
    def __init__(self, max_workers=3):
        self.max_workers = max_workers
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.lock = threading.Lock()
    
    def procesar_neuronas_paralelo(self, neuronas, consulta, contexto=None):
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

# ===== NEURONA OPTIMIZADA =====
class NeuronaAutoaprendizaje:
    def __init__(self, nombre, especialidad):
        self.id = str(uuid.uuid4())[:8]
        self.nombre = nombre
        self.especialidad = especialidad
        self.nivel_energia = 100.0
        self.experiencia = 0
        self.eficiencia = 0.6  # Aumentada de 0.3 a 0.6 para mejor rendimiento inicial
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
        desarrollo = self.desarrollar()
        
        if desarrollo:
            resultado["desarrollo"] = desarrollo
        
        self.historial.append({
            "timestamp": time.time(),
            "entrada": entrada[:100],
            "resultado": resultado.get("confianza", 0),
            "efectivo": resultado.get("confianza", 0) > 0.5
        })
        
        if len(self.historial) > 10:
            self.historial = self.historial[-10:]
        
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
            "confianza": confianza * 0.85
        }

    def _generacion_adaptativa(self, texto, confianza):
        ideas = [
            f"Sistema de aprendizaje autónomo basado en {random.choice(['experiencia', 'patrones', 'retroalimentación'])}",
            f"Arquitectura neuronal que {random.choice(['evoluciona', 'se adapta', 'aprende continuamente'])}"
        ]
        
        return {
            "tipo": "creatividad_adaptativa",
            "ideas": ideas,
            "confianza": confianza * 0.8
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
            "confianza": confianza * 0.75
        }

    def _gestion_inteligente(self, texto, confianza, contexto):
        recursos = self._evaluar_recursos_inteligentes(texto)
        
        return {
            "tipo": "gestion_inteligente",
            "recursos_recomendados": recursos,
            "confianza": confianza * 0.9,
            "estrategia": "optimizada" if self.experiencia > 5 else "base"
        }

    def _procesamiento_autonomo(self, texto, confianza):
        return {
            "tipo": "procesamiento_autonomo",
            "analisis_aprendizaje": f"Neurona con {self.experiencia} experiencias",
            "habilidades_desarrolladas": self.habilidades_aprendidas,
            "confianza": confianza
        }

    def _procesamiento_base(self, texto, confianza):
        return {
            "tipo": "procesamiento_base",
            "resultado": f"Procesado por {self.nombre} (exp: {self.experiencia})",
            "confianza": confianza
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

# ===== CEREBRO AUTÓNOMO MEJORADO =====
class CerebroAutonomo:
    def __init__(self):
        self.base_datos = BaseDatosCubana()
        self.sistema_aprendizaje = SistemaAutoaprendizaje(self.base_datos)
        self.procesador_paralelo = ProcesadorParalelo()
        self.sistema_rollback = SistemaRollback(self)
        
        self.neuronas = [
            NeuronaAutoaprendizaje("PERCEPCIÓN ADAPTATIVA", "percepcion_avanzada"),
            NeuronaAutoaprendizaje("LÓGICA EVOLUTIVA", "logica_estructurada"),
            NeuronaAutoaprendizaje("MEMORIA INTELIGENTE", "memoria_asociativa"),
            NeuronaAutoaprendizaje("CREATIVIDAD ADAPTATIVA", "creatividad_emergente"),
            NeuronaAutoaprendizaje("INTELIGENCIA EMPÁTICA", "inteligencia_emocional"),
            NeuronaAutoaprendizaje("GESTIÓN INTELIGENTE", "coordinacion_central"),
            NeuronaAutoaprendizaje("NÚCLEO AUTOAPRENDIZAJE", "autoaprendizaje")
        ]
        
        self.historial = []
        self.energia_sistema = 1000
        self.evoluciones = 0
        self.ciclos_auto_mejora = 0
        self.evoluciones_mayores = 0
        self.autor = "Ronald Rodriguez Laguna"
        self.ubicacion = "Holguín, Cuba 2025"

    def procesar_consulta(self, consulta):
        self.sistema_rollback.crear_punto_restauracion()
        
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
        
        self.historial.append(experiencia)
        
        decision_rollback = self.sistema_rollback.evaluar_estabilidad(efectividad)
        if decision_rollback == "rollback_automatico":
            st.warning("🔄 Rollback automático por caída de rendimiento")
            self.sistema_rollback.ejecutar_rollback()
        
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
            "neuronas_activas": len([n for n in self.neuronas if n.nivel_energia > 0]),
            "procesamiento_paralelo": "activado"
        }

    def _actualizar_sistema(self):
        self.energia_sistema -= 1
        
        if self.energia_sistema <= 0:
            self.energia_sistema = 1000
            self.evoluciones += 1

    def ejecutar_ciclo_auto_mejora(self):
        self.sistema_rollback.crear_punto_restauracion()
        
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

    def obtener_estado_avanzado(self):
        return {
            "autor": self.autor,
            "ubicacion": self.ubicacion,
            "total_neuronas": len(self.neuronas),
            "energia_sistema": self.energia_sistema,
            "evoluciones": self.evoluciones,
            "ciclos_auto_mejora": self.ciclos_auto_mejora,
            "experiencia_total": sum(n.experiencia for n in self.neuronas),
            "nivel_aprendizaje": self.sistema_aprendizaje.conocimiento["evoluciones"],
            "procesamiento_paralelo": "activado",
            "base_datos": "SQLite",
            "sistema_rollback": "operativo"
        }

# ===== INTERFAZ MEJORADA CON BOTÓN DE REINICIO =====
if 'cerebro_autonomo' not in st.session_state:
    st.session_state.cerebro_autonomo = CerebroAutonomo()

st.title("🧠 Cerebro Autónomo Cubano - Sin Límites")
st.subheader("3 Limitantes Resueltas - Holguín, Cuba 2025 🇨🇺")

# Sidebar mejorado CON BOTÓN DE REINICIO
with st.sidebar:
    st.header("🎛️ Centro de Control Autónomo")
    st.write("**Autor:** Ronald Rodriguez Laguna")
    st.write("**Ubicación:** Holguín, Cuba")
    st.write("**Hito Actual:** 1.1 - Auto-Modificación")
    
    # BOTÓN DE REINICIO AÑADIDO
    if st.button("🔄 Reiniciar Sistema Autónomo"):
        st.session_state.cerebro_autonomo = CerebroAutonomo()
        st.rerun()
    
    cerebro = st.session_state.cerebro_autonomo
    estado = cerebro.obtener_estado_avanzado()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Evoluciones", estado["evoluciones"])
        st.metric("Ciclos Mejora", estado["ciclos_auto_mejora"])
    with col2:
        st.metric("Energía", estado["energia_sistema"])
        st.metric("Experiencia Total", estado["experiencia_total"])
    
    st.subheader("🛡️ Controles de Seguridad")
    
    if st.button("📸 Crear Snapshot Manual"):
        hash_snap = cerebro.sistema_rollback.crear_punto_restauracion()
        st.success(f"Snapshot: {hash_snap[:12]}...")
    
    if st.button("🔄 Rollback Manual"):
        if cerebro.sistema_rollback.ejecutar_rollback():
            st.rerun()

# Área principal de consultas
consulta = st.text_area(
    "Consulta para el cerebro autónomo:",
    height=100,
    placeholder="Ej: ¿Cómo funciona el procesamiento paralelo en este sistema?"
)

col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    if st.button("🚀 Procesamiento Paralelo", use_container_width=True):
        if consulta.strip():
            with st.spinner("🧠 Procesando en paralelo..."):
                resultado = st.session_state.cerebro_autonomo.procesar_consulta(consulta)
            
            st.success("✅ Procesamiento paralelo completado!")
            
            efectividad = resultado["resumen"]["efectividad_sistema"]
            st.metric("Efectividad", f"{efectividad:.2f}")
            
            for res in resultado["resultados"][:3]:
                emoji = "⚡" if res.get("confianza", 0) > 0.7 else "🔍"
                st.write(f"{emoji} {res.get('tipo', 'Procesamiento').replace('_', ' ').title()}")
                st.progress(res.get("confianza", 0))

with col2:
    if st.button("🔧 Ciclo Mejora", use_container_width=True):
        with st.spinner("Optimizando..."):
            resultado = cerebro.ejecutar_ciclo_auto_mejora()
        if resultado['mejoras_aplicadas']:
            st.success(f"✅ {len(resultado['mejoras_aplicadas'])} mejoras aplicadas")

with col3:
    if st.button("📊 Estado Sistema", use_container_width=True):
        st.json(cerebro.obtener_estado_avanzado())

# Panel de resiliencia
with st.expander("🛡️ Panel de Resiliencia y Rollback"):
    st.subheader("Sistema de Recuperación Cubano")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Snapshots Disponibles:**")
        st.info("Sistema mantiene últimos 5 snapshots automáticamente")
        
        st.write("**Alertas Activas:**")
        alertas = cerebro.sistema_rollback.alertas_activas
        if alertas:
            for alerta in alertas[-3:]:
                st.warning(alerta)
        else:
            st.success("✅ Sistema estable")
    
    with col2:
        st.write("**Rendimiento en Tiempo Real:**")
        metricas = {
            "Velocidad Procesamiento": "⚡ Paralelo",
            "Base Datos": "✅ SQLite Activa", 
            "Rollback": "🛡️ Operativo",
            "Consumo Memoria": "🟢 Optimizado"
        }
        
        for metrica, valor in metricas.items():
            st.write(f"{metrica}: {valor}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center;'>
    <small>🧠 Sistema Cubano Resiliente - 3 Limitantes Resueltas</small><br>
    <small>✅ JSON → SQLite | ✅ Secuencial → Paralelo | ✅ Sin Rollback → Recuperación Automática</small><br>
    <small>© 2025 Ronald Rodriguez Laguna - Tecnología Cubana Sin Límites</small>
</div>
""", unsafe_allow_html=True)
