nome = "Estacio"
vnome = []
for indice,letra in enumerate(nome):
    vnome.append(letra)
try:
    print(" - ", vnome[len(nome)])
except:
    print("falha no programa -> ")

print("vnome -> ", vnome)

print("letra -> ", letra)
print("indice -> ", indice)