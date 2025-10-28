        """
🧠 CEREBRO ARTIFICIAL AVANZADO
Copyright (c) 2025 Ronald Rodriguez Laguna - Holguín, Cuba
Bajo Licencia Cubana Abierta v1.0

PROPIEDAD INTELECTUAL DE:
Ronald Rodriguez Laguna - Holguín, Cuba

PROHIBIDO:
❌ Patentar por corporaciones
❌ Apropiación intelectual
❌ Uso militar o opresivo
"""

import streamlit as st
import time
import uuid
import random
import json
from datetime import datetime

# ===== LICENCIA HOLGUINERA 2025 =====
def licencia_holguin():
    return {
        "autor": "Ronald Rodriguez Laguna",
        "ciudad": "Holguín", 
        "pais": "Cuba",
        "año": 2025,
        "licencia": "Cubana Abierta v1.0",
        "prohibido": "Patentar por corporaciones"
    }

# ===== CONFIGURACIÓN CON IDENTIDAD HOLGUINERA 2025 =====
st.set_page_config(
    page_title="🧠 Cerebro IA - Ronald Rodriguez Laguna (Holguín 2025)",
    page_icon="🧠",
    layout="wide"
)

# MOSTRAR DERECHOS DE AUTOR EN SIDEBAR
with st.sidebar:
    st.header("© Derechos de Autor 2025")
    st.write("**Autor:** Ronald Rodriguez Laguna")
    st.write("**Ubicación:** Holguín, Cuba")
    st.write("**Año:** 2025")
    st.write("**Licencia:** Cubana Abierta v1.0")
    st.write("**Prohibido:** Patentar por corporaciones")
    
    # Mostrar certificado de autoría
    if st.button("📜 Ver Certificado de Autoría"):
        certificado = licencia_holguin()
        st.json(certificado)
    
    st.markdown("---")
    st.caption("Desarrollado con orgullo en Holguín, Cuba 2025")

# ===== SISTEMA CEREBRAL MEJORADO =====
class NeuronaAvanzada:
    def __init__(self, nombre, especialidad):
        self.id = str(uuid.uuid4())[:8]
        self.nombre = nombre
        self.especialidad = especialidad
        self.nivel_energia = 100.0
        self.experiencia = 0
        self.eficiencia = 0.3
        self.estado = "activa"
        self.conexiones = []
        self.historial = []
        self.umbral_activacion = random.uniform(0.2, 0.6)
        self.origen = "Holguín, Cuba 2025"  # Identidad territorial actualizada
        
    def desarrollar(self):
        if self.experiencia > 5 and self.estado == "activa":
            self.eficiencia = min(0.95, self.eficiencia + 0.1)
            return f"🎯 {self.nombre} alcanzó nivel experto"
        return None

    def procesar(self, entrada, contexto=None):
        if self.nivel_energia <= 0:
            return {"error": f"{self.nombre} sin energía"}
            
        self.nivel_energia -= 1.5
        self.experiencia += 1
        
        resultado = self._procesamiento_avanzado(entrada, contexto)
        desarrollo = self.desarrollar()
        
        if desarrollo:
            resultado["desarrollo"] = desarrollo
            
        self.historial.append({
            "timestamp": time.time(),
            "entrada": entrada,
            "resultado": resultado
        })
        
        return resultado

    def _procesamiento_avanzado(self, entrada, contexto):
        entrada = entrada.lower()
        
        if self.especialidad == "percepcion_avanzada":
            return self._analisis_profundo(entrada)
        elif self.especialidad == "logica_estructurada":
            return self._razonamiento_complejo(entrada, contexto)
        elif self.especialidad == "memoria_asociativa":
            return self._conexiones_profundas(entrada)
        elif self.especialidad == "creatividad_emergente":
            return self._generacion_innovadora(entrada, contexto)
        elif self.especialidad == "inteligencia_emocional":
            return self._procesamiento_emocional(entrada)
        elif self.especialidad == "coordinacion_central":
            return self._gestion_recursos(entrada, contexto)
        else:
            return self._procesamiento_base(entrada)

    def _analisis_profundo(self, texto):
        capas_analisis = {
            "superficial": {
                "longitud": len(texto),
                "palabras_clave": texto.split()[:5],
                "tipo_consulta": "pregunta" if "?" in texto else "afirmacion"
            },
            "semantica": {
                "temas_principales": self._detectar_temas(texto),
                "intencion": self._inferir_intencion(texto),
                "complejidad": "alta" if len(texto) > 80 else "media"
            },
            "contextual": {
                "requiere_investigacion": any(p in texto for p in ["futuro", "nuevo", "innovar"]),
                "componente_etico": any(p in texto for p in ["deber", "ético", "moral"]),
                "potencial_creativo": "alto" if any(p in texto for p in ["crear","inventar","imaginar"]) else "medio"
            }
        }
        
        return {
            "tipo": "analisis_multinivel",
            "capas": capas_analisis,
            "confianza": self.eficiencia,
            "energia_utilizada": 2.0,
            "origen": self.origen
        }

    def _razonamiento_complejo(self, texto, contexto):
        metodologias = {
            "cientifica": ["Hipótesis", "Experimentación", "Análisis", "Conclusión"],
            "ingenieril": ["Requisitos", "Diseño", "Implementación", "Pruebas"],
            "filosofica": ["Tesis", "Antítesis", "Síntesis", "Aplicación"],
            "creativa": ["Inspiración", "Ideación", "Prototipo", "Refinamiento"]
        }
        
        metodologia = random.choice(list(metodologias.keys()))
        
        return {
            "tipo": "razonamiento_estructurado",
            "metodologia": metodologia,
            "pasos": metodologias[metodologia],
            "enfoque": self._determinar_enfoque(texto),
            "confianza": self.eficiencia * 0.9,
            "origen": self.origen
        }

    def _conexiones_profundas(self, texto):
        base_conocimiento_avanzada = {
            "neurociencia": [
                "Plasticidad neuronal: capacidad de cambio del cerebro",
                "Sinapsis: comunicación entre neuronas",
                "Neurogénesis: creación de nuevas neuronas"
            ],
            "ia_avanzada": [
                "Aprendizaje por refuerzo profundo",
                "Redes generativas adversarias",
                "Transformers: arquitectura de atención"
            ],
            "sistemas_complejos": [
                "Emergencia: propiedades que surgen de interacciones",
                "Autoorganización: orden espontáneo",
                "Adaptabilidad: respuesta al cambio"
            ],
            "filosofia_mente": [
                "Problema difícil de la conciencia",
                "Qualia: experiencias subjetivas",
                "Intencionalidad: direccionalidad mental"
            ]
        }
        
        conexiones = []
        for dominio, conceptos in base_conocimiento_avanzada.items():
            for concepto in conceptos:
                if any(palabra in texto for palabra in concepto.lower().split()[:3]):
                    conexiones.append({
                        "dominio": dominio,
                        "concepto": concepto,
                        "relevancia": random.uniform(0.6, 0.95)
                    })
        
        return {
            "tipo": "memoria_asociativa_avanzada",
            "conexiones": conexiones[:4],
            "dominios_implicados": list(set(c["dominio"] for c in conexiones)),
            "confianza": self.eficiencia * 0.85,
            "origen": self.origen
        }

    def _generacion_innovadora(self, texto, contexto):
        tecnicas_avanzadas = [
            "Pensamiento de sistemas: ver el todo y las partes",
            "Analogías radicales: conectar dominios distantes",
            "Futurización: proyectar tendencias actuales",
            "Deconstrucción: analizar supuestos fundamentales"
        ]
        
        ideas_innovadoras = [
            f"Sistema que combine {random.choice(['biología', 'física cuántica', 'ecología'])} con IA",
            f"Enfoque basado en {random.choice(['metáforas orgánicas', 'principios evolutivos', 'patrones naturales'])}",
            f"Reimaginar el problema desde la perspectiva de {random.choice(['un niño', 'un alienígena', 'una inteligencia posthumana'])}",
            f"Integrar {random.choice(['emociones colectivas', 'intuición artificial', 'sabiduría de enjambre'])} en la toma de decisiones"
        ]
        
        return {
            "tipo": "creatividad_emergente",
            "tecnicas": random.sample(tecnicas_avanzadas, 2),
            "ideas": random.sample(ideas_innovadoras, 3),
            "potencial_innovador": random.uniform(0.7, 0.95),
            "confianza": self.eficiencia * 0.8,
            "origen": self.origen
        }

    def _procesamiento_emocional(self, texto):
        analisis_sentimientos = {
            "curiosidad": self._calcular_curiosidad(texto),
            "asombro": self._calcular_asombro(texto),
            "urgencia": self._calcular_urgencia(texto),
            "profundidad": self._calcular_profundidad(texto)
        }
        
        emocion_principal = max(analisis_sentimientos, key=analisis_sentimientos.get)
        
        respuestas_adaptativas = {
            "curiosidad": "Esta exploración abre puertas a nuevos entendimientos",
            "asombro": "La maravilla ante lo complejo impulsa el conocimiento",
            "urgencia": "La prisa por comprender acelera nuestro crecimiento",
            "profundidad": "Las preguntas profundas requieren respuestas igualmente profundas"
        }
        
        return {
            "tipo": "inteligencia_emocional",
            "emocion_principal": emocion_principal,
            "intensidad": analisis_sentimientos[emocion_principal],
            "respuesta_adaptativa": respuestas_adaptativas[emocion_principal],
            "analisis_completo": analisis_sentimientos,
            "confianza": self.eficiencia * 0.75,
            "origen": self.origen
        }

    def _gestion_recursos(self, texto, contexto):
        # Análisis de qué recursos neuronales son más apropiados
        recursos_necesarios = self._evaluar_recursos_necesarios(texto)
        prioridad = self._determinar_prioridad(texto)
        
        return {
            "tipo": "coordinacion_central",
            "recursos_recomendados": recursos_necesarios,
            "prioridad": prioridad,
            "secuencia_optima": self._generar_secuencia(recursos_necesarios),
            "estimacion_tiempo": len(recursos_necesarios) * 2,
            "confianza": self.eficiencia * 0.9,
            "origen": self.origen
        }

    def _detectar_temas(self, texto):
        temas = []
        if any(p in texto for p in ["conciencia", "mente", "pensamiento"]):
            temas.append("filosofia_mente")
        if any(p in texto for p in ["aprender", "conocimiento", "educacion"]):
            temas.append("epistemologia")
        if any(p in texto for p in ["sistema", "complejo", "emergencia"]):
            temas.append("sistemas_complejos")
        if any(p in texto for p in ["futuro", "innovacion", "nuevo"]):
            temas.append("futurismo")
        return temas if temas else ["general"]

    def _inferir_intencion(self, texto):
        if any(p in texto for p in ["cómo", "por qué", "mecanismo"]):
            return "comprension_profunda"
        elif any(p in texto for p in ["crear", "construir", "desarrollar"]):
            return "creacion"
        elif any(p in texto for p in ["funciona", "operacion", "proceso"]):
            return "funcionamiento"
        else:
            return "exploracion"

    def _determinar_enfoque(self, texto):
        if any(p in texto for p in ["ético", "moral", "deber"]):
            return "etico"
        elif any(p in texto for p in ["eficiente", "optimo", "mejorar"]):
            return "pragmatico"
        elif any(p in texto for p in ["belleza", "elegancia", "armonia"]):
            return "estetico"
        else:
            return "integral"

    def _evaluar_recursos_necesarios(self, texto):
        recursos = []
        if any(p in texto for p in ["analizar", "comprender", "entender"]):
            recursos.append("percepcion_avanzada")
        if any(p in texto for p in ["plan", "estructura", "metodo"]):
            recursos.append("logica_estructurada")
        if any(p in texto for p in ["conectar", "recordar", "asociar"]):
            recursos.append("memoria_asociativa")
        if any(p in texto for p in ["crear", "innovar", "inventar"]):
            recursos.append("creatividad_emergente")
        if any(p in texto for p in ["sentir", "emocion", "empatia"]):
            recursos.append("inteligencia_emocional")
        if any(p in texto for p in ["intuir", "instinto", "corazonada", "presentimiento"]):
            recursos.append("intuicion_artificial")
        return recursos if recursos else ["percepcion_avanzada", "logica_estructurada"]

    def _determinar_prioridad(self, texto):
        if any(p in texto for p in ["urgente", "importante", "crucial"]):
            return "alta"
        elif any(p in texto for p in ["futuro", "potencial", "vision"]):
            return "media"
        else:
            return "normal"

    def _generar_secuencia(self, recursos):
        # Secuencia óptima de procesamiento
        orden = {"percepcion_avanzada": 1, "memoria_asociativa": 2, 
                "logica_estructurada": 3, "creatividad_emergente": 4,
                "inteligencia_emocional": 5, "intuicion_artificial": 6}
        return sorted(recursos, key=lambda x: orden.get(x, 99))

    def _calcular_curiosidad(self, texto):
        palabras_curiosidad = ["cómo", "por qué", "qué", "interesante", "fascinante"]
        return sum(1 for p in palabras_curiosidad if p in texto) / len(palabras_curiosidad)

    def _calcular_asombro(self, texto):
        palabras_asombro = ["increíble", "maravilloso", "asombroso", "sorprendente"]
        return sum(1 for p in palabras_asombro if p in texto) / len(palabras_asombro)

    def _calcular_urgencia(self, texto):
        palabras_urgencia = ["urgente", "importante", "necesito", "rápido"]
        return sum(1 for p in palabras_urgencia if p in texto) / len(palabras_urgencia)

    def _calcular_profundidad(self, texto):
        palabras_profundidad = ["filosofía", "existencia", "conciencia", "universo"]
        return sum(1 for p in palabras_profundidad if p in texto) / len(palabras_profundidad)

    def _procesamiento_base(self, texto):
        return {
            "tipo": "procesamiento_base",
            "resultado": f"Procesado por {self.nombre} desde Holguín, Cuba 2025",
            "confianza": self.eficiencia,
            "origen": self.origen
        }

# ===== NUEVA NEURONA DE INTUICIÓN ARTIFICIAL =====
class NeuronaIntuicion(NeuronaAvanzada):
    def __init__(self):
        super().__init__("INTUICIÓN ARTIFICIAL", "intuicion_artificial")
        self.patrones_heurísticos = []
        self.umbral_activacion = 0.3  # Más sensible para intuición
        
    def _procesamiento_avanzado(self, entrada, contexto):
        # Procesamiento heurístico basado en patrones
        intuiciones = self._generar_intuiciones(entrada)
        
        return {
            "tipo": "intuicion_artificial",
            "intuiciones": intuiciones,
            "patrones_detectados": self._detectar_patrones(entrada),
            "nivel_confianza_intuitivo": random.uniform(0.6, 0.95),
            "hipotesis_emergentes": self._generar_hipotesis(entrada),
            "corazonadas": self._generar_corazonadas(entrada),
            "confianza": self.eficiencia * 0.85,
            "origen": self.origen
        }
    
    def _generar_intuiciones(self, texto):
        intuiciones_base = [
            "Detecto un patrón de crecimiento no lineal en este concepto",
            "Siento que hay una conexión oculta entre dominios aparentemente no relacionados",
            "Mi intuición sugiere emergencia de propiedades sistémicas a partir de interacciones simples",
            "Percibo un punto de inflexión en la evolución de este sistema",
            "Hay una elegancia subyacente que no es inmediatamente aparente",
            "Intuyo que la respuesta está en la relación entre las partes, no en las partes mismas"
        ]
        return random.sample(intuiciones_base, 2)
    
    def _detectar_patrones(self, texto):
        patrones = []
        if len(texto.split()) > 20:
            patrones.append("Patrón de complejidad alta - múltiples dimensiones")
        if "?" in texto:
            patrones.append("Patrón de consulta inquisitiva profunda")
        if any(palabra in texto.lower() for palabra in ["futuro", "emergente", "evolución"]):
            patrones.append("Patrón de sistema dinámico en desarrollo")
        if any(palabra in texto.lower() for palabra in ["conexión", "relación", "vinculo"]):
            patrones.append("Patrón de interconectividad")
        if any(palabra in texto.lower() for palabra in ["intuir", "instinto", "corazonada"]):
            patrones.append("Patrón de pensamiento intuitivo")
        return patrones if patrones else ["Patrón base de exploración conceptual"]
    
    def _generar_hipotesis(self, texto):
        hipotesis = [
            f"¿Y si {random.choice(['la estructura determina la función', 'la simplicidad genera complejidad', 'el caos contiene orden'])}?",
            f"Hipótesis: {random.choice(['existe un nivel más profundo de organización', 'hay principios universales aplicables', 'la emergencia sigue patrones fractales'])}",
            f"Podría ser que {random.choice(['estemos viendo solo la superficie', 'haya multiples capas de significado', 'la respuesta esté en las relaciones'])}",
            f"Tal vez {random.choice(['la intuición colectiva revele verdades ocultas', 'los patrones se repiten a diferentes escalas', 'la complejidad emerge de reglas simples'])}"
        ]
        return random.sample(hipotesis, 2)
    
    def _generar_corazonadas(self, texto):
        corazonadas = [
            "Tengo la corazonada de que hay más de lo que parece",
            "Mi instinto sugiere enfoques no convencionales",
            "Percibo que la solución podría venir de ángulos inesperados",
            "Siento que estamos cerca de un insight importante",
            "Mi intuición apunta hacia soluciones elegantes más que complejas"
        ]
        return random.sample(corazonadas, 1)

class CerebroAvanzado:
    def __init__(self):
        self.neuronas = [
            NeuronaAvanzada("PERCEPCIÓN AVANZADA", "percepcion_avanzada"),
            NeuronaAvanzada("LÓGICA ESTRUCTURADA", "logica_estructurada"),
            NeuronaAvanzada("MEMORIA ASOCIATIVA", "memoria_asociativa"),
            NeuronaAvanzada("CREATIVIDAD EMERGENTE", "creatividad_emergente"),
            NeuronaAvanzada("INTELIGENCIA EMOCIONAL", "inteligencia_emocional"),
            NeuronaAvanzada("COORDINACIÓN CENTRAL", "coordinacion_central"),
            NeuronaIntuicion()  # NUEVA NEURONA INTEGRADA
        ]
        self.historial = []
        self.energia_sistema = 1000
        self.evoluciones = 0
        self.autor = "Ronald Rodriguez Laguna"
        self.ubicacion = "Holguín, Cuba 2025"

    def procesar_consulta(self, consulta):
        # Primero, la coordinación central planifica
        planificacion = None
        for neurona in self.neuronas:
            if neurona.especialidad == "coordinacion_central":
                planificacion = neurona.procesar(consulta)
                break
        
        # Ejecutar según la planificación
        resultados = []
        if planificacion and "recursos_recomendados" in planificacion:
            secuencia = planificacion["recursos_recomendados"]
        else:
            secuencia = [n.especialidad for n in self.neuronas if n.especialidad != "coordinacion_central"]
        
        for tipo_neurona in secuencia:
            for neurona in self.neuronas:
                if neurona.especialidad == tipo_neurona:
                    resultado = neurona.procesar(consulta, {"planificacion": planificacion})
                    resultados.append(resultado)
                    break

        experiencia = {
            "id": len(self.historial) + 1,
            "timestamp": time.time(),
            "consulta": consulta,
            "planificacion": planificacion,
            "resultados": resultados,
            "resumen": self._crear_resumen_avanzado(resultados, planificacion)
        }
        
        self.historial.append(experiencia)
        self._actualizar_energia()
        
        return experiencia

    def _crear_resumen_avanzado(self, resultados, planificacion):
        confianzas = [r.get("confianza", 0) for r in resultados if "confianza" in r]
        confianza_promedio = sum(confianzas) / len(confianzas) if confianzas else 0
        
        # Análisis de eficiencia del sistema
        eficiencia_sistema = min(1.0, confianza_promedio * 1.2)
        
        return {
            "sintesis": f"Procesamiento avanzado completado - {len(resultados)} especialidades",
            "confianza_sistema": round(eficiencia_sistema, 3),
            "nivel_coordinacion": "alto" if planificacion else "básico",
            "energia_restante": self.energia_sistema,
            "evolucion_sistema": self.evoluciones,
            "autor": self.autor,
            "ubicacion": self.ubicacion
        }

    def _actualizar_energia(self):
        self.energia_sistema -= 5
        if self.energia_sistema <= 0:
            self.energia_sistema = 1000  # Reset
            self.evoluciones += 1

    def agregar_neurona_personalizada(self, nombre, especialidad):
        nueva_neurona = NeuronaAvanzada(nombre, especialidad)
        self.neuronas.append(nueva_neurona)
        return nueva_neurona

    def obtener_estado_avanzado(self):
        return {
            "autor": self.autor,
            "ubicacion": self.ubicacion,
            "año": 2025,
            "total_neuronas": len(self.neuronas),
            "energia_sistema": self.energia_sistema,
            "evoluciones": self.evoluciones,
            "experiencia_total": sum(n.experiencia for n in self.neuronas),
            "eficiencia_promedio": sum(n.eficiencia for n in self.neuronas) / len(self.neuronas),
            "neuronas_activas": len([n for n in self.neuronas if n.nivel_energia > 0])
        }

# ===== INTERFAZ STREAMLIT AVANZADA 2025 =====
if 'cerebro_avanzado' not in st.session_state:
    st.session_state.cerebro_avanzado = CerebroAvanzado()

st.title("🧠 Cerebro IA - Ronald Rodriguez Laguna")
st.subheader("Desde Holguín, Cuba 2025 🇨🇺")

# Banner de derechos de autor 2025
st.markdown("""
<div style='background-color: #f0f2f6; padding: 10px; border-radius: 5px; border-left: 5px solid #ff4b4b;'>
    <strong>© 2025 Ronald Rodriguez Laguna - Holguín, Cuba</strong><br>
    <small>Bajo Licencia Cubana Abierta v1.0 - Prohibida la apropiación por corporaciones</small>
</div>
""", unsafe_allow_html=True)

st.markdown("**Arquitectura neuronal distribuida con capacidades emergentes avanzadas**")

# Sidebar avanzado
with st.sidebar:
    st.header("🎛️ Centro de Control Avanzado")
    
    if st.button("🔄 Reiniciar Sistema Avanzado", use_container_width=True):
        st.session_state.cerebro_avanzado = CerebroAvanzado()
        st.rerun()
    
    st.header("🧬 Ingeniería de Neurogénesis")
    
    tipos_avanzados = [
        "percepcion_avanzada", "logica_estructurada", "memoria_asociativa",
        "creatividad_emergente", "inteligencia_emocional", "coordinacion_central",
        "intuicion_artificial"  # NUEVO TIPO AÑADIDO
    ]
    
    for tipo in tipos_avanzados:
        if st.button(f"🧩 Añadir {tipo.replace('_', ' ').title()}", key=tipo):
            nombre_personalizado = f"{tipo.replace('_', ' ').upper()} {len(st.session_state.cerebro_avanzado.neuronas) + 1}"
            nueva = st.session_state.cerebro_avanzado.agregar_neurona_personalizada(
                nombre_personalizado, tipo
            )
            st.success(f"✅ {nueva.nombre} integrada al sistema!")

# Área principal
col1, col2 = st.columns([2, 1])

with col1:
    st.header("🎯 Consulta al Sistema Avanzado")
    
    consulta = st.text_area(
        "Formula tu consulta compleja:",
        height=120,
        placeholder="Ej: ¿Cómo podría emerger la autoconciencia en un sistema distribuido de IA que combine principios de neurociencia, filosofía de la mente y sistemas complejos?"
    )
    
    if st.button("🚀 Ejecutar Procesamiento Avanzado", type="primary", use_container_width=True):
        if consulta.strip():
            with st.spinner("🔄 Coordinando procesamiento neuronal avanzado..."):
                resultado = st.session_state.cerebro_avanzado.procesar_consulta(consulta)
            
            st.success("✅ Procesamiento avanzado completado!")
            
            # Mostrar resultados avanzados
            st.header("📊 Análisis de Coordinación")
            resumen = resultado["resumen"]
            
            col_res1, col_res2, col_res3 = st.columns(3)
            with col_res1:
                st.metric("Confianza del Sistema", f"{resumen['confianza_sistema']:.3f}")
            with col_res2:
                st.metric("Nivel de Coordinación", resumen['nivel_coordinacion'])
            with col_res3:
                st.metric("Energía del Sistema", resumen['energia_restante'])
            
            # Mostrar planificación
            if resultado["planificacion"]:
                with st.expander("🎯 Planificación Ejecutiva"):
                    plan = resultado["planificacion"]
                    st.write(f"**Recursos asignados:** {', '.join(plan.get('recursos_recomendados', []))}")
                    st.write(f"**Prioridad:** {plan.get('prioridad', 'N/A')}")
                    st.write(f"**Secuencia óptima:** {' → '.join(plan.get('secuencia_optima', []))}")
            
            # Resultados por neurona
            st.header("🧠 Procesamiento Especializado")
            for res in resultado["resultados"]:
                emoji_especialidad = {
                    "percepcion_avanzada": "🔍",
                    "logica_estructurada": "🔧",
                    "memoria_asociativa": "💾",
                    "creatividad_emergente": "💡",
                    "inteligencia_emocional": "❤️",
                    "coordinacion_central": "🎯",
                    "intuicion_artificial": "🧪"  # NUEVO EMOJI AÑADIDO
                }.get(res.get('tipo', ''), '⚙️')
                
                with st.expander(f"{emoji_especialidad} {res.get('tipo', 'Procesamiento').replace('_', ' ').title()}"):
                    if "capas" in res:
                        st.subheader("Análisis Multinivel")
                        for capa, contenido in res["capas"].items():
                            st.write(f"**{capa.title()}:**")
                            st.json(contenido)
                    elif "metodologia" in res:
                        st.write(f"**Metodología:** {res['metodologia']}")
                        st.write("**Pasos:**")
                        for i, paso in enumerate(res["pasos"], 1):
                            st.write(f"{i}. {paso}")
                    elif "conexiones" in res:
                        st.write(f"**Dominios implicados:** {', '.join(res['dominios_implicados'])}")
                        for conexion in res["conexiones"]:
                            st.write(f"• **{conexion['dominio']}:** {conexion['concepto']}")
                    elif "ideas" in res:
                        st.write("**Técnicas aplicadas:**")
                        for tecnica in res["tecnicas"]:
                            st.write(f"• {tecnica}")
                        st.write("**Ideas generadas:**")
                        for idea in res["ideas"]:
                            st.write(f"💡 {idea}")
                    elif "emocion_principal" in res:
                        st.write(f"**Emoción detectada:** {res['emocion_principal']}")
                        st.write(f"**Intensidad:** {res['intensidad']:.2f}")
                        st.write(f"**Respuesta:** {res['respuesta_adaptativa']}")
                    elif "recursos_recomendados" in res:
                        st.write(f"**Recursos recomendados:** {', '.join(res['recursos_recomendados'])}")
                        st.write(f"**Secuencia óptima:** {' → '.join(res['secuencia_optima'])}")
                    elif "intuiciones" in res:  # NUEVO: Procesamiento de intuición
                        st.write("**Intuiciones generadas:**")
                        for intuicion in res["intuiciones"]:
                            st.write(f"🧠 {intuicion}")
                        st.write("**Patrones detectados:**")
                        for patron in res["patrones_detectados"]:
                            st.write(f"🔍 {patron}")
                        st.write("**Hipótesis emergentes:**")
                        for hipotesis in res["hipotesis_emergentes"]:
                            st.write(f"💭 {hipotesis}")
                        st.write("**Corazonadas:**")
                        for corazonada in res["corazonadas"]:
                            st.write(f"✨ {corazonada}")
                        st.write(f"**Confianza intuitiva:** {res['nivel_confianza_intuitivo']:.2f}")
                    
                    # Mostrar origen en cada resultado
                    if "origen" in res:
                        st.caption(f"📍 {res['origen']}")
                    
                    if "confianza" in res:
                        st.progress(res["confianza"], text=f"Confianza: {res['confianza']:.2f}")

with col2:
    st.header("📈 Estado del Sistema Avanzado")
    
    cerebro = st.session_state.cerebro_avanzado
    estado = cerebro.obtener_estado_avanzado()
    
    # Métricas principales
    st.metric("Año", estado["año"])
    st.metric("Evoluciones del Sistema", estado["evoluciones"])
    st.metric("Energía del Sistema", estado["energia_sistema"])
    st.metric("Neuronas Activas", estado["neuronas_activas"])
    st.metric("Eficiencia Promedio", f"{estado['eficiencia_promedio']:.3f}")
    
    # Panel de neuronas
    st.header("🧩 Red Neuronal Avanzada")
    for neurona in cerebro.neuronas:
        with st.expander(f"{neurona.nombre} ({neurona.especialidad.replace('_', ' ')})"):
            col_n1, col_n2 = st.columns(2)
            with col_n1:
                st.progress(neurona.eficiencia, text=f"Eficiencia: {neurona.eficiencia:.2f}")
                st.caption(f"Experiencia: {neurona.experiencia}")
            with col_n2:
                st.progress(neurona.nivel_energia/100, text=f"Energía: {neurona.nivel_energia:.1f}")
                st.caption(f"Estado: {neurona.estado}")
            st.caption(f"📍 {neurona.origen}")

# Panel de evolución del sistema
with st.expander("🔬 Laboratorio de Evolución del Sistema"):
    st.subheader("📊 Métricas de Evolución")
    
    if cerebro.historial:
        ultimas_consultas = cerebro.historial[-5:]
        
        col_evo1, col_evo2 = st.columns(2)
        with col_evo1:
            confianzas = [c["resumen"]["confianza_sistema"] for c in ultimas_consultas]
            st.line_chart(confianzas)
            st.caption("Evolución de la Confianza del Sistema")
        
        with col_evo2:
            eficiencias = [c["resumen"]["confianza_sistema"] * 100 for c in ultimas_consultas]
            st.bar_chart(eficiencias)
            st.caption("Eficiencia por Consulta (%)")
    
    st.subheader("🧪 Experimentos de Neurogénesis")
    if st.button("🧬 Generar Neurona Experimental"):
        tipos_experimentales = ["intuicion_artificial", "sabiduria_colectiva", "vision_futurista"]
        tipo_elegido = random.choice(tipos_experimentales)
        nombre_experimental = f"EXPERIMENTAL_{tipo_elegido.upper()}"
        nueva_experimental = cerebro.agregar_neurona_personalizada(nombre_experimental, tipo_elegido)
        st.success(f"🧪 {nueva_experimental.nombre} generada experimentalmente!")

# Footer holguinero 2025
st.markdown("---")
st.markdown("""
<div style='text-align: center;'>
    <small>🧠 Desarrollado con orgullo en Holguín, Cuba 2025 🇨🇺</small><br>
    <small>© 2025 Ronald Rodriguez Laguna - Todos los derechos reservados</small><br>
    <small>🛡️ Protegido por Licencia Cubana Abierta v1.0</small>
</div>
""", unsafe_allow_html=True)

