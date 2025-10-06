import streamlit as st
import pandas as pd
import os

# Título de la aplicación
st.title('🎬 Videos de Partidos de Fútbol')

# --- Preparación de los datos de ejemplo ---
# Suponiendo que los videos están en una carpeta llamada 'videos'.
# La estructura de la carpeta sería:
#
# /videos
#   /match_id_1
#     video1.mp4
#     video2.mp4
#   /match_id_2
#     video3.mp4
#
# Para este ejemplo, simularemos un DataFrame con la información de los partidos.
# En una aplicación real, este DataFrame se cargaría desde una base de datos o archivo.

# Ruta base donde se encuentran los videos
VIDEO_PATH_BASE = 'static'

# Crear una lista de diccionarios para simular una base de datos de partidos
data = [
    {'match_id': 'match_id_1', 'equipo_local': 'Real Madrid', 'equipo_visitante': 'Barcelona', 'fecha': '2025-09-15'},
    {'match_id': 'match_id_2', 'equipo_local': 'Boca Juniors', 'equipo_visitante': 'River Plate', 'fecha': '2025-09-10'},
    {'match_id': 'match_id_3', 'equipo_local': 'Manchester Utd', 'equipo_visitante': 'Liverpool', 'fecha': '2025-09-05'},
    # Agrega más partidos aquí si lo deseas
]

df = pd.DataFrame(data)

# --- Controles para la navegación ---
# Seleccionar un partido por equipo local y visitante
st.sidebar.header('🔍 Selecciona un Partido')
partido_seleccionado = st.sidebar.selectbox(
    'Elige un partido:',
    df.apply(lambda row: f"{row['equipo_local']} vs {row['equipo_visitante']} ({row['fecha']})", axis=1)
)

# Obtener el match_id del partido seleccionado
match_id = df.loc[
    df.apply(lambda row: f"{row['equipo_local']} vs {row['equipo_visitante']} ({row['fecha']})", axis=1) == partido_seleccionado,
    'match_id'
].iloc[0]

# Título para los videos del partido seleccionado
st.header(f"Videos de {partido_seleccionado}")

# --- Carga y visualización de videos ---
# En una aplicación real, aquí es donde cargarías los nombres de archivo de video para el match_id seleccionado
# del sistema de archivos o de una base de datos.
# Para este ejemplo, simulamos la existencia de los archivos de video.
try:
    # Ruta de la carpeta específica del partido
    partido_path = os.path.join(VIDEO_PATH_BASE, match_id)
    
    # Obtener la lista de archivos de video en la carpeta
    if os.path.exists(partido_path):
        video_files = [f for f in os.listdir(partido_path) if f.endswith('.mp4')]
    else:
        video_files = []

    if not video_files:
        st.warning('⚠️ No se encontraron videos para este partido.')
    else:
        # Iterar sobre la lista de videos y mostrarlos
        for video_file in video_files:
            video_path = os.path.join(partido_path, video_file)
            st.markdown(f"**Video: {video_file}**")
            st.video(video_path)
            st.markdown("---") # Separador para cada video
            
except Exception as e:
    st.error(f'❌ Ocurrió un error al cargar los videos: {e}')