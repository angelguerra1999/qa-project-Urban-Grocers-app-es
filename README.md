Angel Guerra, Sprint 7, Grupo 17

Urban Grocers Kit Creation Tests

Este proyecto se centra en la automatización de pruebas para la API de Urban.Grocers, una plataforma que permite la creación de kits de alimentos personalizados. Las pruebas se realizaron para asegurar la correcta funcionalidad de los endpoints relacionados con la creación y gestión de kits de alimentos. Las pruebas aseguran que el campo "name" en la solicitud de creación de un kit cumpla con los requisitos especificados.

Objetivos del Proyecto

Verificar la correcta creación de kits de alimentos.
Asegurar la integridad de los datos enviados y recibidos.
Validar las respuestas de la API para diferentes escenarios de prueba.

Tecnologías Utilizadas: Pycharm, Python, Pytest, Git, GitHub

Archivos

 `configuration.py`: Contiene las configuraciones de URL y rutas.
 
 `data.py`: Contiene los datos necesarios para las solicitudes.
 
 `sender_stand_request.py`: Contiene las funciones para enviar solicitudes a la API.
 
 `create_kit_name_kit_test.py`: Contiene las pruebas automatizadas.
 
 `README.md`: Este archivo con una descripción del proyecto.
 
 `.gitignore`: Lista de archivos y carpetas que Git debería ignorar.

Pruebas automatizadas en archivo create_kit_name_test.py

Prueba 1. Kit creado con éxito. El parámetro name contiene 1 caracteres
def test_create_kit_1_letter_in_name_get_success_response()

Prueba 2. Kit creado con éxito. El parámetro name contiene 511 caracteres
def test_create_kit_511_letters_in_name_get_success_response()

Prueba 3. Error. El parámetro contiene un string vacío
def test_create_kit_empty_name_get_error_response()

Prueba 4. Error. El parámetro name contiene 512 caracteres
def test_create_kit_512_letters_in_name_get_error_response()

Prueba 5. El parámetro name contiene un string de caracteres especiales
def test_create_kit_special_caracaters_get_success_response()

Prueba 6. El parámetro name contiene espacios
def test_create_kit_white_space_get_success_response()

Prueba 7. El parámetro name contiene un string de dígitos
def test_create_kit_numbers_allowed_get_success_response()

Prueba 8. Error. Falta el parametro name en la solicitud
def negative_assert_no_name_error_response()

Prueba 9. Error. El tipo del parámetro name: número
def test_create_kit_number_type_get_error_response

## Ejecución de Pruebas

Clona el repositorio en tu computadora: https://github.com/angelguerra1999/qa-project-Urban-Grocers-app-es.git

Navegar al directorio del proyecto: cd urban-grocers-api-testing

Instalar las dependencias: pip install, request 

Ejecutar las pruebas: pytest

