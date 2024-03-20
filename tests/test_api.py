#! /usr/bin/env python3
import requests 
from .variables.config import *
from Users.main_user import *


# check login user
def test_login_user():
    login_user = User("Catbuytrer", "passty123")
    login_user_status_code = login_user.login()
    print("User logged", login_user_status_code)
    assert login_user_status_code == 200
    
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
    headers = {
            "Authorization": api_key ,
            # "Content-Type": "image/jpeg",
            # "User-Agent": "Mozilla/5.0",
            "accept": "application/json" }
    # with open(file_path, "rb") as image_file:
    #     image_data = image_file.read()     
    files = {'file': ('cat.jpg', open('C:/QA/projects/cat_api/cat.jpg', 'rb'), 'multipart/form-data')}
    petId = 240787
    upload_pet_response = requests.post(endpoint + f"/pet/{petId}/uploadImage", headers = headers, files = files)
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
        body_login = [
                {"username": "Catbuytrer",
                 "password": "passty123"  
                }
            ]
        login_response = requests.get(endpoint + "/user/login", headers=headers, json=body_login)
        status_code_login = login_response.status_code
        print(status_code_login)
        print(login_response.json())
        
        if status_code_login == 200:

            username = body_login[0]["username"]
            user_body = {
                "id": 1046,
                "username": "NEW_CAT_USER",
                "firstName": "Marirtyna",
                "lastName": "Gutrym",
                "email": "gurtym@gmail.com",
                "password": "passty123",
                "phone": "4353453try454",
                "userStatus": 0       
                }
            update_user_name_response = requests.put(endpoint + f"/user/{username}", headers=headers, json=user_body)
            update_user_name_status_code = update_user_name_response.status_code
            print(update_user_name_status_code)
            print(update_user_name_response.json())
    else:
        print("user creation ERRor")
    
# get user
def test_get_user():
    get_user_response = requests.get(endpoint + "/user/NEW_CAT_USER")
    status_code_get_user = get_user_response.status_code
    print(status_code_get_user)
    print(get_user_response.json())