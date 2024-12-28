# Urban Grocers Kit Creation Tests

Este proyecto contiene pruebas automatizadas para la creación de kits en la aplicación Urban Grocers. Las pruebas aseguran que el campo "name" en la solicitud de creación de un kit cumpla con los requisitos especificados.

## Archivos

- `configuration.py`: Contiene las configuraciones de URL y rutas.
- `data.py`: Contiene los datos necesarios para las solicitudes.
- `sender_stand_request.py`: Contiene las funciones para enviar solicitudes a la API.
- `create_kit_name_kit_test.py`: Contiene las pruebas automatizadas.
- `README.md`: Este archivo con una descripción del proyecto.
- `.gitignore`: Lista de archivos y carpetas que Git debería ignorar.

## Ejecución de Pruebas

1. Clona el repositorio en tu computadora.
2. Instala las dependencias necesarias.
3. Ejecuta las pruebas utilizando el siguiente comando:
   ```sh
   pytest create_kit_name_kit_test.py
