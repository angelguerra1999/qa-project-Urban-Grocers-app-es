import configuration
import requests
import data

def post_new_user(user_body):
    url = configuration.URL_SERVICE + configuration.CREATE_USER_PATH
    headers = data.headers
    response = requests.post(url, json=user_body, headers=headers)
    return response

def post_new_client_kit(kit_body, auth_token):
    url = configuration.URL_SERVICE + configuration.CREATE_KIT_PATH
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(url, json=kit_body, headers=headers)
    return response
