import streamlit as st
import time
import os
import requests

DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def get_token():
    tb_url = st.secrets["TB_API_URL"]
    tb_user = st.secrets["TB_USER"]
    tb_pass = st.secrets["TB_PASS"]

    # 1. Autenticación: obtener JWT token
    auth_url = f"{tb_url}/api/auth/login"
    auth_payload = {
        "username": tb_user,
        "password": tb_pass
    }

    auth_response = requests.post(auth_url, json=auth_payload)
    if auth_response.status_code != 200:
        print("❌ Error al autenticar:", auth_response.text)
        exit()

    jwt_token = auth_response.json().get("token")
    print("🔐 Token obtenido correctamente")

    # Guardar token en archivo
    token_file = os.path.join(DIR_PATH, "../tmp", "token.txt")
    with open(token_file, "w") as f:
        f.write(jwt_token)
        print(f"💾 Token guardado en {token_file}")

if __name__ == "__main__":
    # Ejecutar la función para obtener el token
    get_token()
    print("✅ Proceso completado")
    time.sleep(5)  # Esperar 2 segundos antes de cerrar
