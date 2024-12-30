import sender_stand_request
import data

def get_kit_body(kit_name):
    current_body = data.kit_body.copy()
    current_body['name'] = kit_name
    return current_body

def get_new_user_autoken():
    new_user = sender_stand_request.post_new_user(data.user_body.copy())
    au_token_value = new_user.json()["authToken"]
    new_user_autoken = data.headers.copy()
    new_user_autoken["Authorization"] = f"Bearer {au_token_value}"
    return new_user_autoken

def positive_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_kit(kit_body, get_new_user_autoken())
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_name

def negative_assert_symbol(kit_name):
    # El cuerpo actualizado de la solicitud se guarda en la variable user_body
    kit_body = get_kit_body(kit_name)
    # El resultado se guarda en la variable response
    kit_response = sender_stand_request.post_new_kit(kit_body, get_new_user_autoken())
    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert kit_response.json()["code"] == 400

# Prueba 1. Kit creado con éxito. El parámetro name contiene 1 caracteres
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

#prueba 2. Kit creado con éxito. El parámetro name contiene 511 caracteres
def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Prueba 3. Error. El parámetro contiene un string vacío
def test_create_kit_empty_name_get_error_response():
    negative_assert_symbol("")

# Prueba 4. Error. El parámetro name contiene 512 caracteres
def test_create_kit_512_letters_in_name_get_error_response():
        negative_assert_symbol("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Prueba 5. El parámetro name contiene un string de caracteres especiales
def test_create_kit_special_caracaters_get_success_response():
    positive_assert("\"№%@\",")

# Prueba 6. El parámetro name contiene espacios
def test_create_kit_white_space_get_success_response():
    positive_assert(" A Aaa ")

# Prueba 7. El parámetro name contiene un string de dígitos
def test_create_kit_numbers_allowed_get_success_response():
    positive_assert("123")

# Prueba 8. Error. Falta el parametro name en la solicitud
def negative_assert_no_name_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    kit_body = data.kit_body.copy()
    # El parámetro "name" se elimina de la solicitud
    kit_body.pop("name")
    # Comprueba la respuesta
    negative_assert_symbol(kit_body)

# Prueba 9. Error. El tipo del parámetro name: número
def test_create_kit_number_type_get_error_response():
    negative_assert_symbol(123)
