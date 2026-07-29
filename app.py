import streamlit as st

# Configuración estética de la app de simulación
st.set_page_config(page_title="Mi Simulador CEAM 2027", page_icon="🩺", layout="centered")

st.title("🩺 Mi Simulador Interactivo CEAM 2027")
st.subheader("Entrenamiento de Percentil Alto para la Residencia en Bolivia")
st.markdown("---")

# BASE DE DATOS MODULAR DE PREGUNTAS (Aquí es donde irás sumando tus temas)
preguntas_db = [
    {
        "id": 1,
        "pregunta": "¿Qué porcentaje de recién nacidos a término y prematuros se ven afectados por la ictericia durante la primera semana de vida?",
        "opciones": [
            "A) 10% a término y 20% prematuros",
            "B) 30% a término y 50% prematuros",
            "C) 60% a término y 80% prematuros",
            "D) 80% a término y 90% prematuros",
            "E) Solo ocurre en el 5% de los nacimientos"
        ],
        "correcta": 2, # Corresponde al índice de la opción C (0=A, 1=B, 2=C...)
        "justificacion": "La ictericia afecta al 60% de los recién nacidos a término y al 80% de los prematuros durante su primera semana debido a la inmadurez hepática fisiológica."
    },
    {
        "id": 2,
        "pregunta": "¿Qué porcentaje de tiempo de exposición al ácido (pH <4) en una pH-metría de 24 horas confirma un reflujo patológico definitivo según el Consenso de Lyon?",
        "opciones": [
            "A) > 1% del tiempo total",
            "B) > 2% del tiempo total",
            "C) > 4% del tiempo total",
            "D) > 6% del tiempo total",
            "E) > 12% del tiempo total"
        ],
        "correcta": 3, # Corresponde al índice de la opción D (3)
        "justificacion": "El Consenso de Lyon unificó los criterios de ERGE, dictaminando que un Tiempo de Exposición al Ácido (TEA) superior al 6% en 24 horas confirma de forma concluyente un reflujo patológico."
    }
]

# Inicializar memoria interna del examen
if 'evaluadas' not in st.session_state:
    st.session_state.evaluadas = {}

puntos = 0

# Renderizado dinámico e interactivo de las preguntas en la web
for q in preguntas_db:
    st.markdown(f"##### **Pregunta {q['id']}:** {q['pregunta']}")
    
    # Botones interactivos para cliquear directamente en la pantalla
    seleccion = st.radio("Marca tu opción:", q['opciones'], index=None, key=f"p_{q['id']}")
    
    if seleccion:
        indice = q['opciones'].index(seleccion)
        st.session_state.evaluadas[q['id']] = indice
        
        # Validación con colores en tiempo real (Luz verde / Luz roja)
        if indice == q['correcta']:
            st.success("✅ **¡CORRECTO!**")
            puntos += 1
        else:
            st.error(f"❌ **INCORRECTO.** La respuesta correcta era: {q['opciones'][q['correcta']]}")
            
        # Desplegable interactivo para la justificación de CEAM
        with st.expander("🔍 Ver Justificación Técnica Avanzada"):
            st.info(q['justificacion'])
    st.markdown("---")

# Marcador y barra de progreso al responder todo
if len(st.session_state.evaluadas) == len(preguntas_db):
    st.balloons()
    st.metric(label="Calificación de Simulación", value=f"{puntos} / {len(preguntas_db)}")
    rendimiento = (puntos / len(preguntas_db)) * 100
    st.info(f"Tu puntuación actual te posiciona en el **Percentil {rendimiento:.1f}%** de la convocatoria.")
