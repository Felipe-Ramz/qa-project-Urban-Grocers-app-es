import sender_stand_request
import data

def get_new_user_token():
    response = sender_stand_request.post_new_user()
    response_json = response.json()
    return response_json["authToken"]

def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201

def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_create_kit_with_1_symbol_name():
    kit_body = data.get_kit_body('a')
    positive_assert(kit_body)

def test_create_kit_with_511_symbol_name():
    kit_body = data.get_kit_body('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')
    positive_assert(kit_body)

def test_create_kit_with_0_symbol_name():
    kit_body = data.get_kit_body('')
    negative_assert_code_400(kit_body)

def test_create_kit_with_512_symbol_name():
    kit_body = data.get_kit_body('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')
    negative_assert_code_400(kit_body)

def test_create_kit_with_character_symbol_name():
    kit_body = data.get_kit_body('"№%@",')
    positive_assert(kit_body)

def test_create_kit_with_space_symbol_name():
    kit_body = data.get_kit_body(' A Aaa ')
    positive_assert(kit_body)

def test_create_kit_with_number_symbol_name():
    kit_body = data.get_kit_body('123')
    positive_assert(kit_body)

def test_create_kit_with_missing_symbol_name():
    kit_body = data.get_kit_body("name")
    kit_body.pop("name")
    negative_assert_code_400(kit_body)

def test_create_kit_with_incorrect_symbol_name():
    kit_body = data.get_kit_body(123)
    negative_assert_code_400(kit_body)