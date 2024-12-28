import sender_stand_request
import data

def get_kit_body(name):
    kit_body = {"name": name}
    return kit_body

def positive_assert(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

def get_new_user_token():
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    return user_response.json()["authToken"]

def test_create_kit_with_1_letter_name():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("a")
    positive_assert(kit_body, auth_token)

def test_create_kit_with_511_letter_name():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body, auth_token)

def test_create_kit_with_empty_name():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body, auth_token)

def test_create_kit_with_512_letter_name():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body, auth_token)

def test_create_kit_with_special_characters():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("№%@")
    positive_assert(kit_body, auth_token)

def test_create_kit_with_spaces():
    auth_token = get_new_user_token()
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body, auth_token)

def test_create_kit_with_numbers():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("123")
    positive_assert(kit_body, auth_token)

def test_create_kit_without_name():
    auth_token = get_new_user_token()
    kit_body = {}
    negative_assert_code_400(kit_body, auth_token)

def test_create_kit_with_number_name():
    auth_token = get_new_user_token()
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body, auth_token)

if __name__ == "__main__":
    test_create_kit_with_1_letter_name()
    test_create_kit_with_511_letter_name()
    test_create_kit_with_empty_name()
    test_create_kit_with_512_letter_name()
    test_create_kit_with_special_characters()
    test_create_kit_with_spaces()
    test_create_kit_with_numbers()
    test_create_kit_without_name()
    test_create_kit_with_number_name()
