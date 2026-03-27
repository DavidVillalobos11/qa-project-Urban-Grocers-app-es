from sender_stand_request import post_new_user, post_new_client_kit


def get_auth_token():
    response = post_new_user()
    return response.json()["authToken"]


# 1
def test_kit_name_1_char():
    token = get_auth_token()
    kit_body = {"name": "a"}

    response = post_new_client_kit(kit_body, token)

    assert response.status_code == 201
    assert response.json()["name"] == "a"


# 2
def test_kit_name_511_chars():
    token = get_auth_token()
    kit_body = {"name": "a" * 511}

    response = post_new_client_kit(kit_body, token)

    assert response.status_code == 201


# 3
def test_kit_name_empty():
    token = get_auth_token()
    kit_body = {"name": ""}

    response = post_new_client_kit(kit_body, token)

    assert response.status_code == 400


# 4
def test_kit_name_512_chars():
    token = get_auth_token()
    kit_body = {"name": "a" * 512}

    response = post_new_client_kit(kit_body, token)

    assert response.status_code == 400


# 5
def test_kit_special_chars():
    token = get_auth_token()
    kit_body = {"name": "№%@,"}

    response = post_new_client_kit(kit_body, token)

    assert response.status_code == 201


# 6
def test_kit_spaces():
    token = get_auth_token()
    kit_body = {"name": " A Aaa "}

    response = post_new_client_kit(kit_body, token)

    assert response.status_code == 201


# 7
def test_kit_numbers():
    token = get_auth_token()
    kit_body = {"name": "123"}

    response = post_new_client_kit(kit_body, token)

    assert response.status_code == 201


# 8
def test_kit_no_name():
    token = get_auth_token()
    kit_body = {}

    response = post_new_client_kit(kit_body, token)

    assert response.status_code == 400


# 9
def test_kit_wrong_type():
    token = get_auth_token()
    kit_body = {"name": 123}

    response = post_new_client_kit(kit_body, token)

    assert response.status_code == 400
