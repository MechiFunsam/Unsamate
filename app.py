# Unsamate
# Unsamate 
import streamlit as st  
import os  

# Configuración de la página  
st.set_page_config(page_title="Comunsam", layout="wide")  

# Título de la aplicación  
st.title("Repositorio de Comunicación, Unsam")  

# Crear el directorio 'uploads' si no existe  
if not os.path.exists("uploads"):  
    os.makedirs("uploads")  

# Subir archivos  
uploaded_file = st.file_uploader("Sumá tus archivos aquí", type=["pdf", "docx", "txt"])  

if uploaded_file is not None:  
    # Guardar el archivo en el directorio 'uploads'  
    save_path = os.path.join("uploads", uploaded_file.name)  
    with open(save_path, "wb") as f:  
        f.write(uploaded_file.getbuffer())  
    st.success(f"Archivo {uploaded_file.name} subido exitosamente")  

# Mostrar archivos subidos  
st.header("Apuntes Comunsam")  
files = os.listdir("uploads")  
if files:  
    for file in files:  
        st.write(file)  
        # Crear botón de descarga  
        with open(os.path.join("uploads", file), "rb") as f:  
            st.download_button(label="Descargar", data=f, file_name=file)  
else:  
    st.write("No hay archivos subidos aún.")
