from http.client import responses

import requests

class DadosUsuario:
    def __init__(self):
        self.url_petstore_user = 'https://petstore.swagger.io/v2/user'
        self.id = None
        self.username = None
        self.firstName = None
        self.lastName = None
        self.email = None
        self.password = None
        self.phone = None
        self.userStatus = None
        self.status_code = None


    def post_criar_novo_usuario(self):
        header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        data = self.gerar_dados_usuario()

        response = requests.post(self.url_petstore_user, headers=header, json=data)
        self.status_code = response.status_code
        return response



    def get_consulta_usuario(self, username):
        response = requests.get(f"{self.url_petstore_user}/{username}")
        return response



    def put_alterar_usuario(self, username, novos_dados):
        url = f"{self.url_petstore_user}/{username}"

        headers = {
            "Content-Type": "application/json"
        }
        response = requests.put(url, json=novos_dados, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Erro ao alterar o usuário {username}. Status: {response.status_code}, Detalhes: {response.text}")

        return response

    def get_deletar_usuario(self, username):
        response = requests.delete(f"{self.url_petstore_user}/{username}")
        return response



    def gerar_dados_usuario(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "userStatus": 1
        }