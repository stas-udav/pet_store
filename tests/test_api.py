#! /usr/bin/env python3
import requests 
from  variables.config import *

# Create user
def test_create_user():
    body = {
            "id": 0,
            "username": "Udav",
            "firstName": "Stan",
            "lastName": "G",
            "email": "stan@gmail.com",
            "password": "stan",
            "phone": "3029479257",
            "userStatus": 0
            }
    create_user_response = requests.post(endpoint + "/user", body)
    status_code = create_user_response.status_code
    create_user_response_data = create_user_response.json()
    print(status_code)
    # print(create_user_response_data)
    assert status_code == 200


# upload pet image + pet Id
def test_upload_pet_image():
    headers = {"Authorization": api_key}
    # with open(file_path, "rb") as image_file:
    #     image_data = image_file.read()     
    files = {'image': (open(file_path, 'rb'))}  
    petId = 240787
    upload_pet_response = requests.post(endpoint + f"/pet/{petId}/uploadImage", headers = headers, files = files, )
    status_code = upload_pet_response.status_code
    # upload_pet_response_data = upload_pet_response.json()
    print(status_code)
    print(upload_pet_response.text)
    assert status_code == 200

# add new pet to the store
def test_add_new_pet():
    body = {
                    "id": 240787,
            "category": {
                "id": 453,
                "name": "Catyacin"
            },
            "name": "Cherry",
            "photoUrls": [
                ""
            ],
            "tags": [
                {
                "id": 34,
                "name": "Shkryab"
                }
            ],
            "status": "available"
                }
    headers = {"Authorization": api_key}
    add_new_pet_response = requests.post(endpoint + "/pet", headers=headers, json=body)
    status_code = add_new_pet_response.status_code
    add_new_pet_response_data = add_new_pet_response.json()
    print(add_new_pet_response_data)
    print(status_code)
    print(add_new_pet_response)
    assert status_code == 200, "Adding pet ERROR"
    return add_new_pet_response

# find pet by ID
def test_find_pet_id():
    pass

# create list of users
def test_create_list_users():
    headers = {"Authorization": api_key}
    body = [
            {
            "id": 1046,
            "username": "Catbuytrer",
            "firstName": "Marirtyna",
            "lastName": "Gutrym",
            "email": "gurtym@gmail.com",
            "password": "passty123",
            "phone": "4353453try454",
            "userStatus": 0       
            },
            {
            "id": 1044,
            "username": "dog-buyer",
            "firstName": "Sam",
            "lastName": "Deer",
            "email": "sam@gmail.com",
            "password": "pass34",
            "phone": "4353453454",
            "userStatus": 0       
            }
            ]
    create_users_response = requests.post(endpoint + "/user/createWithArray", headers=headers, json=body)
    status_code_create_users = create_users_response.status_code
    print(status_code_create_users)
    print(create_users_response)
    print(create_users_response.json())
    assert status_code_create_users == 200
    if status_code_create_users == 200:
        dog_buyer_user = body[1]
        user_name = dog_buyer_user["username"]
        print(user_name)
        username = user_name
        user_name_update_body = [
                                {"id": 1044,
                                "username": "DOG_LOVER",
                                "firstName": "Sam",
                                "lastName": "Deer",
                                "email": "sam@gmail.com",
                                "password": "pass34",
                                "phone": "4353453454",
                                "userStatus": 0       
                                }
                                ]

        update_user_name_response = requests.put(endpoint + f"/user/{username}", headers=headers, json=user_name_update_body)
        status_code_user_name_update = update_user_name_response.status_code
        print(status_code_user_name_update)
        print(username)
        assert status_code_user_name_update == 200, "ERROR user name update"
    else:
        print("ERROR user name update")

# get user
def test_get_user():
    get_user_response = requests.get(endpoint + "/user/dog-buyer")
    status_code_get_user = get_user_response.status_code
    print(status_code_get_user)
    print(get_user_response.json())