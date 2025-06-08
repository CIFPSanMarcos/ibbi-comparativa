# 🔋 Comparativa de Consumo Energético con Mensaje de Concienciación

Este proyecto es una aplicación web desarrollada con **Streamlit** que permite visualizar y comparar el consumo energético diario en distintas zonas de un centro educativo. Además, genera automáticamente un **mensaje de concienciación energética** utilizando la API de OpenAI.

---

## 🎯 Objetivos

- Visualizar el consumo energético diario por zonas del centro.
- Comparar los datos con el día anterior y mostrar las diferencias.
- Generar gráficas interactivas con **Plotly**.
- Crear un mensaje de concienciación personalizado según los datos, con ayuda de un modelo de lenguaje de OpenAI (GPT).

---

## 🛠️ Tecnologías utilizadas

- [Streamlit](https://streamlit.io/) – interfaz web interactiva
- [Pandas](https://pandas.pydata.org/) – análisis y transformación de datos
- [Plotly](https://plotly.com/python/) – visualización interactiva de datos
- [OpenAI API](https://platform.openai.com/) – generación de texto con IA

---

## 🚀 Cómo usar la app

1. **Instalación de dependencias**

   ```bash
   pip install -r requirements.txt
````

2. **Ejecutar la app**

   ```bash
   streamlit run app/app.py
   ```

3. **Interacción**

   * Selecciona una fecha concreta.
   * Explora los consumos por zonas y sus comparativas.
   * Haz clic en “Generar mensaje de concienciación” para obtener una recomendación automática.

---

## 📁 Estructura del proyecto

```
├── app/
│   └── app.py                      # Aplicación principal de Streamlit
├── data/
│   └── consumo_energia.csv     # Dataset de ejemplo con consumos energéticos
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Este archivo
```

---

## 📌 Ejemplo de mensaje generado

> *"El consumo energético de hoy ha disminuido un 8% respecto a ayer. ¡Excelente! Este tipo de acciones ayudan a reducir nuestra huella ecológica. Sigamos así."*

---

## 🔐 Notas importantes

* Para usar la API de OpenAI, necesitas tener una **clave de API válida** y almacenarla como variable de entorno:

  ```bash
  export OPENAI_API_KEY="tu_clave_aquí"
  ```

* El dataset de consumo debe tener el siguiente formato mínimo:
  `fecha, zona, consumo`
  (Opcionalmente: `potencia`, `voltaje`, `intensidad`, etc.)

---

## 📚 Licencia

Este proyecto se comparte con fines educativos bajo la licencia [MIT](https://opensource.org/licenses/MIT).
