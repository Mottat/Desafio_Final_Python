from behave import *
from features.impl.impl import DadosUsuario


@given(u'que eu cadastro um novo usuário')
def step_impl(context):
    context.api = DadosUsuario()

    context.api.id = 1
    context.api.username = 'Motta'
    context.api.firstName = 'Thiago'
    context.api.lastName = 'Motta'
    context.api.email = 'motta@gmail.com'
    context.api.password = '123456'
    context.api.phone = '987654321'

    response = context.api.post_criar_novo_usuario()

    if response.status_code != 200:
        raise Exception(f"Erro ao criar o usuário: {response.status_code}, {response.text}")
    else:
        print(f"Usuário criado com sucesso: {response.json()}")
        context.username = context.api.username


@then(u'o usuário deve ser incluído com sucesso')
def step_impl(context):
    if not hasattr(context, 'username'):
        raise Exception("O username não foi armazenado no contexto! Não foi possível validar a criação do usuário.")

    username = context.username
    response = context.api.get_consulta_usuario(username)

    if response.status_code != 200:
        raise Exception(f"Erro ao consultar o usuário. Status: {response.status_code}, {response.text}")

    user_data = response.json()
    assert user_data['username'] == username, f"Esperado {username}, mas encontrado {user_data['username']}!"
    print(f"Usuário {username} incluído com sucesso: {user_data}")


@given(u'que eu realizo uma consulta pelo usuário')
def step_impl(context):
    context.api = DadosUsuario()
    username = "Motta"

    response = context.api.get_consulta_usuario(username)

    if response.status_code != 200:
        raise Exception(f"Erro ao validar o usuário. Status: {response.status_code}, {response.text}")


@then(u'os dados do usuário devem ser retornados corretamente')
def step_impl(context):
    username = "Motta"

    response = context.api.get_consulta_usuario(username)

    if response.status_code != 200:
        raise Exception(f"Erro ao consultar o usuário. Status: {response.status_code}, {response.text}")

    user_data = response.json()

    assert user_data['username'] == username, f"Esperado {username}, mas encontrado {user_data['username']}!"
    assert user_data['firstName'] == 'Thiago', f"Esperado 'Thiago', mas encontrado {user_data['firstName']}!"
    assert user_data['lastName'] == 'Motta', f"Esperado 'Motta', mas encontrado {user_data['lastName']}!"
    assert user_data['email'] == 'motta@gmail.com', f"Esperado 'motta@gmail.com', mas encontrado {user_data['email']}!"
    assert user_data['phone'] == '987654321', f"Esperado '987654321', mas encontrado {user_data['phone']}!"

    print(f"Os dados do usuário {username} foram retornados corretamente: {user_data}")


@given(u'que eu altero as informações de um usuário existente')
def step_impl(context):
    context.api = DadosUsuario()
    username = "Motta"

    novos_dados = {
        "id": 1,
        "username": username,
        "firstName": "Thiago2",
        "lastName": "Motta2",
        "email": "motta2@gmail.com",
        "phone": "987654321",
        "password": "123456",
        "userStatus": 1
    }

    response = context.api.put_alterar_usuario(username, novos_dados)

    if response.status_code not in [200, 204]:
        print(f"Erro ao alterar o usuário. Status: {response.status_code}, Detalhes: {response.text}")
        return

    print(f"Usuário {username} alterado com sucesso.")

    response_verificacao = context.api.get_consulta_usuario(username)

    if response_verificacao.status_code == 200:
        user_data = response_verificacao.json()
        print(f"Dados após alteração: {user_data}")
        context.user_data = user_data
    else:
        print(f"Erro ao verificar alteração. Status: {response_verificacao.status_code}, Detalhes: {response_verificacao.text}")
        context.user_data = None


@then(u'as novas informações devem ser salvas corretamente')
def step_impl(context):
    if not hasattr(context, 'user_data') or context.user_data is None:
        raise Exception("Os dados do usuário não foram recuperados após a alteração.")

    assert context.user_data['firstName'] == "Thiago2", f"Erro: Nome esperado 'Thiago2', mas recebido {context.user_data['firstName']}"
    assert context.user_data['lastName'] == "Motta2", f"Erro: Sobrenome esperado 'Motta2', mas recebido {context.user_data['lastName']}"
    assert context.user_data['email'] == "motta2@gmail.com", f"Erro: Email esperado 'motta2@gmail.com', mas recebido {context.user_data['email']}"
    assert context.user_data['phone'] == "987654321", f"Erro: Telefone esperado '987654321', mas recebido {context.user_data['phone']}"

    print(f"As novas informações foram salvas corretamente: {context.user_data}")


@given(u'que eu excluo um usuário do sistema')
def step_impl(context):
    context.api = DadosUsuario()
    username = "Motta"

    response = context.api.get_deletar_usuario(username)

    if response.status_code != 200:
        raise Exception(f"Erro ao validar o usuário. Status: {response.status_code}, {response.text}")


@then(u'o usuário não deve mais existir no sistema')
def step_impl(context):
    username = "Motta"

    response = context.api.get_consulta_usuario(username)

    if response.status_code == 404:
        print(f"O usuário {username} não existe mais no sistema.")
    else:
        raise Exception(f"O usuário {username} ainda existe no sistema. Status: {response.status_code}, {response.text}")
