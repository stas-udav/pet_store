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
    upload_pet_response = requests.post(endpoint + "/pet/240787/uploadImage]", headers = headers, files = files, )
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