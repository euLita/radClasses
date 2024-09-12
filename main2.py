import os
print("Removendo diretorio")
try:
    os.mkdir("meu_diretorio")
    print("Diretorio removido com sucesso")
except Exception as error:
    print(error)