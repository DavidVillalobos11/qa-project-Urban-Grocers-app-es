# Urban Grocers API Testing

Este proyecto contiene pruebas automatizadas para la creación de kits en la API de Urban Grocers.

## 🔧 Requisitos
- Python 3.x
- requests
- pytest

## ▶️ Instalación

Instalar dependencias:
pip install requests pytest

## 🚀 Ejecución de pruebas

Ejecutar:
pytest create_kit_name_kit_test.py

## ⚠️ Nota
Antes de ejecutar las pruebas, asegúrate de:
- Iniciar el servidor en TripleTen
- Actualizar la variable BASE_URL en configuration.py

## 📌 Descripción

Se realizan pruebas sobre el campo "name" al crear un kit, validando:
- Longitud mínima y máxima
- Tipos de datos
- Caracteres especiales
