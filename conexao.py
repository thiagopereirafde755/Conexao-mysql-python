import mysql.connector

conexao = mysql.connector.connect(
    host=" ",
    user=" ",
    password=" ",
    database=" ",
    port=
)
if conexao.is_connected():
    print("Conexão ao banco de dados realizada com sucesso!")
    conexao.close()  
else:
    print("Erro ao conectar ao banco de dados.")
