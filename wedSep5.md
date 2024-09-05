

Resolver bug de algoritmo de media da nota
-

nome = "Estacio"

vnome = []

for indice,letra in enumerate(nome):

    vnome.append(letra)

print(vnome[len(nome)])


-> `len()`, retorna o comprimento de um objeto. 
- O comprimento de um objeto é o número de itens contidos nele. A função `len()` pode ser usada com muitos tipos de dados diferentes, como listas, tuplas, dicionários, strings, conjuntos, entre outros.

-> O método `append()` é um recurso em Python que permite adicionar um elemento ao final de uma lista existente. Essa função é extremamente útil quando você precisa expandir uma lista com mais itens dinamicamente, sem precisar criar uma nova lista a cada vez.

=> `IndexError: list index out of range`;