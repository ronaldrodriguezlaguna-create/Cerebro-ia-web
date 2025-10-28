    """
🧠 CEREBRO ARTIFICIAL AUTOAPRENDIZAJE
Copyright (c) 2025 Ronald Rodriguez Laguna - Holguín, Cuba
Bajo Licencia Cubana Abierta v1.0
"""

import streamlit as st
import time
import uuid
import random
import json
import os
from datetime import datetime

# ===== PROTECCIÓN DE ACCESO =====
CONTRASENA_ACCESO = "holguin2025"

if 'acceso_otorgado' not in st.session_state:
    st.title("🔒 Acceso al Cerebro Artificial")
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

# ===== SISTEMA DE AUTOAPRENDIZAJE AVANZADO =====
class SistemaAutoaprendizaje:
    def __init__(self):
        self.archivo = "aprendizaje_cerebral.json"
        self.cargar_conocimiento()
    
    def cargar_conocimiento(self):
        try:
            with open(self.archivo, 'r') as f:
                self.conocimiento = json.load(f)
        except:
            self.conocimiento = {
                "patrones_aprendidos": {},
                "eficiencia_neuronas": {},
                "conexiones_efectivas": [],
                "errores_evitados": [],
                "evoluciones": 0
            }
    
    def guardar_conocimiento(self):
        try:
            with open(self.archivo, 'w') as f:
                json.dump(self.conocimiento, f, indent=2)
        except:
            pass
    
    def aprender_de_experiencia(self, consulta, resultados, efectividad):
        # Aprender patrones de consultas efectivas
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
        
        # Aprender de neuronas más efectivas
        for resultado in resultados:
            tipo_neurona = resultado.get("tipo", "")
            confianza = resultado.get("confianza", 0)
            
            if tipo_neurona not in self.conocimiento["eficiencia_neuronas"]:
                self.conocimiento["eficiencia_neuronas"][tipo_neurona] = {
                    "confianza_promedio": confianza,
                    "usos": 1,
                    "efectividad": efectividad
                }
            else:
                datos = self.conocimiento["eficiencia_neuronas"][tipo_neurona]
                datos["confianza_promedio"] = (datos["confianza_promedio"] + confianza) / 2
                datos["usos"] += 1
                datos["efectividad"] = (datos["efectividad"] + efectividad) / 2
        
        self.conocimiento["evoluciones"] += 1
        self.guardar_conocimiento()
    
    def obtener_recomendacion(self, consulta):
        palabras_clave = consulta.lower().split()[:3]
        patron = "_".join(palabras_clave)
        
        if patron in self.conocimiento["patrones_aprendidos"]:
            patron_data = self.conocimiento["patrones_aprendidos"][patron]
            if patron_data["efectividad"] > 0.7:
                return f"Patrón conocido: {patron} (efectividad: {patron_data['efectividad']:.2f})"
        
        # Recomendar neuronas más efectivas
        neuronas_efectivas = [
            neurona for neurona, datos in self.conocimiento["eficiencia_neuronas"].items()
            if datos["efectividad"] > 0.6
        ]
        
        if neuronas_efectivas:
            return f"Neuronas recomendadas: {', '.join(neuronas_efectivas[:2])}"
        
        return "Explorando nuevos patrones..."

# ===== NEURONA CON CAPACIDAD DE AUTOAPRENDIZAJE =====
class NeuronaAutoaprendizaje:
    def __init__(self, nombre, especialidad):
        self.id = str(uuid.uuid4())[:8]
        self.nombre = nombre
        self.especialidad = especialidad
        self.nivel_energia = 100.0
        self.experiencia = 0
        self.eficiencia = 0.3
        self.estado = "activa"
        self.historial = []
        self.umbral_activacion = random.uniform(0.2, 0.6)
        self.origen = "Holguín, Cuba 2025"
        self.habilidades_aprendidas = []
        
    def desarrollar(self):
        # Auto-mejora basada en experiencia
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
        """Aprende de cada interacción"""
        if efectivo:
            self.experiencia += 2
            self.eficiencia = min(0.95, self.eficiencia + 0.02)
        else:
            self.experiencia += 1
            self.eficiencia = max(0.1, self.eficiencia - 0.01)
        
        # Aprendizaje por refuerzo
        if self.experiencia % 5 == 0:
            self.reevaluar_estrategias()

    def reevaluar_estrategias(self):
        """Revisa y mejora sus estrategias de procesamiento"""
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
        
        # Registrar en historial para aprendizaje
        self.historial.append({
            "timestamp": time.time(),
            "entrada": entrada,
            "resultado": resultado.get("confianza", 0),
            "efectivo": resultado.get("confianza", 0) > 0.5
        })
        
        # Mantener historial manejable
        if len(self.historial) > 20:
            self.historial = self.historial[-20:]
        
        return resultado

    def _procesamiento_inteligente(self, entrada, contexto):
        # Procesamiento base que todas las neuronas tienen
        entrada = entrada.lower()
        
        # Aplicar aprendizaje acumulado
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
        # Análisis que mejora con la experiencia
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

    def _procesamiento_base(self, texto, confianza):
        return {
            "tipo": "procesamiento_base",
            "resultado": f"Procesado por {self.nombre} (exp: {self.experiencia})",
            "confianza": confianza,
            "origen": self.origen
        }

# ===== CEREBRO AUTÓNOMO CON AUTOAPRENDIZAJE =====
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
        # Procesamiento con aprendizaje integrado
        resultados = []
        
        for neurona in self.neuronas:
            if neurona.especialidad != "coordinacion_central":
                resultado = neurona.procesar(consulta)
                resultados.append(resultado)
        
        # Evaluar efectividad y aprender
        efectividad = self._evaluar_efectividad(resultados)
        
        # Aprender de la experiencia
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
        # Evaluar qué tan efectivo fue el procesamiento
        confianzas = [r.get("confianza", 0) for r in resultados if "confianza" in r]
        if not confianzas:
            return 0.5
        
        confianza_promedio = sum(confianzas) / len(confianzas)
        
        # Efectividad basada en confianza y completitud
        efectividad = min(1.0, confianza_promedio * 1.2)
        
        # Ajustar basado en experiencia del sistema
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
        self.energia_sistema -= 3  # Menor consumo por optimización
        
        if self.energia_sistema <= 0:
            self.energia_sistema = 1000
            self.evoluciones += 1
            
            # Aplicar mejoras evolutivas
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
                "logica_evolutiva": "🔧", 
                "memoria_inteligente": "💾",
                "creatividad_adaptativa": "💡",
                "inteligencia_empatica": "❤️",
                "gestion_inteligente": "🎯",
                "procesamiento_autonomo": "🧠"
            }.get(res.get('tipo', ''), '⚙️')
            
            with st.expander(f"{emoji} {res.get('tipo', 'Procesamiento').replace('_', ' ').title()}"):
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

