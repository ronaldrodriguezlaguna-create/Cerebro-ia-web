import streamlit as st
import time
import uuid
import random

# Configuración de la página
st.set_page_config(
    page_title="🧠 Cerebro IA",
    page_icon="🧠",
    layout="wide"
)

# Sistema cerebral simple pero funcional
class Neurona:
    def __init__(self, nombre, tipo):
        self.id = str(uuid.uuid4())[:6]
        self.nombre = nombre
        self.tipo = tipo
        self.experiencia = 0
        self.eficiencia = 0.3
    
    def procesar(self, texto):
        self.experiencia += 1
        self.eficiencia = min(0.9, self.eficiencia + 0.02)
        
        if self.tipo == "percepcion":
            return self._analizar_contexto(texto)
        elif self.tipo == "logica":
            return self._aplicar_logica(texto)
        elif self.tipo == "memoria":
            return self._buscar_conexiones(texto)
        else:
            return {"resultado": f"Procesado por {self.nombre}", "confianza": self.eficiencia}
    
    def _analizar_contexto(self, texto):
        texto = texto.lower()
        if "conciencia" in texto:
            tema = "filosofia"
        elif "aprender" in texto or "educacion" in texto:
            tema = "educacion"
        elif "sistema" in texto or "algoritmo" in texto:
            tema = "tecnologia"
        else:
            tema = "general"
            
        return {
            "tipo": "percepcion",
            "tema": tema,
            "confianza": self.eficiencia,
            "analisis": f"Texto de {len(texto)} caracteres analizado"
        }
    
    def _aplicar_logica(self, texto):
        pasos = ["Análisis", "Planificación", "Ejecución", "Evaluación"]
        return {
            "tipo": "logica", 
            "pasos": pasos,
            "confianza": self.eficiencia,
            "complejidad": "alta" if len(texto) > 50 else "media"
        }
    
    def _buscar_conexiones(self, texto):
        conexiones = [
            "Aprendizaje autónomo",
            "Sistemas adaptativos",
            "Redes neuronales", 
            "Inteligencia emergente"
        ]
        return {
            "tipo": "memoria",
            "conexiones": conexiones,
            "confianza": self.eficiencia
        }

class Cerebro:
    def __init__(self):
        self.neuronas = [
            Neurona("PERCEPCIÓN", "percepcion"),
            Neurona("LÓGICA", "logica"), 
            Neurona("MEMORIA", "memoria")
        ]
        self.historial = []
    
    def procesar_consulta(self, consulta):
        resultados = []
        for neurona in self.neuronas:
            resultado = neurona.procesar(consulta)
            resultados.append(resultado)
        
        experiencia = {
            "id": len(self.historial) + 1,
            "consulta": consulta,
            "resultados": resultados,
            "timestamp": time.time()
        }
        self.historial.append(experiencia)
        return experiencia
    
    def agregar_neurona(self, tipo, nombre):
        nueva = Neurona(nombre, tipo)
        self.neuronas.append(nueva)
        return nueva

# INTERFAZ STREAMLIT
if 'cerebro' not in st.session_state:
    st.session_state.cerebro = Cerebro()

st.title("🧠 Cerebro IA - Conciencia Artificial")
st.markdown("Sistema neuronal con capacidades emergentes")

# Sidebar
with st.sidebar:
    st.header("🎛️ Controles")
    
    if st.button("🔄 Reiniciar Sistema"):
        st.session_state.cerebro = Cerebro()
        st.success("Sistema reiniciado!")
    
    st.header("🌟 Nueva Neurona")
    tipo = st.selectbox("Tipo:", ["percepcion", "logica", "memoria", "creatividad"])
    nombre = st.text_input("Nombre:", value=tipo.upper())
    
    if st.button("➕ Crear Neurona"):
        nueva = st.session_state.cerebro.agregar_neurona(tipo, nombre)
        st.success(f"✅ {nueva.nombre} creada!")

# Área principal
col1, col2 = st.columns([2, 1])

with col1:
    st.header("🎯 Consulta al Sistema")
    consulta = st.text_area("Escribe tu pregunta:", height=100)
    
    if st.button("🚀 Procesar") and consulta:
        with st.spinner("Procesando..."):
            resultado = st.session_state.cerebro.procesar_consulta(consulta)
        
        st.success("✅ Consulta procesada!")
        st.subheader("📊 Resultados")
        
        for res in resultado["resultados"]:
            with st.expander(f"{res['tipo'].upper()} (Confianza: {res['confianza']:.2f})"):
                if res["tipo"] == "percepcion":
                    st.write(f"**Tema:** {res['tema']}")
                elif res["tipo"] == "logica":
                    st.write("**Pasos:**")
                    for paso in res["pasos"]:
                        st.write(f"- {paso}")
                elif res["tipo"] == "memoria":
                    st.write("**Conexiones:**")
                    for conexion in res["conexiones"]:
                        st.write(f"- {conexion}")

with col2:
    st.header("📈 Estado")
    cerebro = st.session_state.cerebro
    
    st.metric("Neuronas", len(cerebro.neuronas))
    st.metric("Experiencia", sum(n.experiencia for n in cerebro.neuronas))
    st.metric("Consultas", len(cerebro.historial))
    
    st.header("🧩 Neuronas")
    for neurona in cerebro.neuronas:
        st.write(f"• {neurona.nombre} ({neurona.eficiencia:.0%})")

# Footer
st.markdown("---")
st.caption("Desarrollado con Streamlit - 100% Gratuito")
