import requests
import data
import configuration


def post_new_user():
    return requests.post(
        configuration.BASE_URL + configuration.CREATE_USER_PATH,
        json=data.user_body,
        headers=data.headers
    )


def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.post(
        configuration.BASE_URL + configuration.CREATE_KIT_PATH,
        json=kit_body,
        headers=headers
    )
