import requests
from functions import *
from tests.variables.config import *


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # user login
    def login(self):
        headers = {"Authorization": api_key}
        body_login = [
                    {
                    "username": self.username,
                    "password": self.password  
                    }
                ]
        login_response = requests.get(endpoint + "/user/login", headers=headers, json=body_login)
        status_code_login = login_response.status_code
        print(status_code_login)        
        return(status_code_login)