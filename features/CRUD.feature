# language: pt
Funcionalidade: Validar CRUD de Usuários

  Cenario: 1 - Criar um novo usuário
    Dado que eu cadastro um novo usuário
    Então o usuário deve ser incluído com sucesso

  Cenario: 2 - Consultar um usuário existente
    Dado que eu realizo uma consulta pelo usuário
    Então os dados do usuário devem ser retornados corretamente

  Cenario: 3 - Atualizar os dados de um usuário
    Dado que eu altero as informações de um usuário existente
    Então as novas informações devem ser salvas corretamente

  Cenario: 4 - Deletar um usuário
    Dado que eu excluo um usuário do sistema
    Então o usuário não deve mais existir no sistema
