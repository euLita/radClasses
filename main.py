import os
print("Criando diretorio")
try:
    os.mkdir("meu_diretorio")
    print("Diretorio criado com sucesso")
except Exception as error:
    print(error)
    print("Falha desconhecida")
except FileNotFoundError as error:
    print(error)
    print("Falha ao renomear o arquivo")