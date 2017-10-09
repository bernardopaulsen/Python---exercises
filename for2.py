compras = []
while True:
    produto = input("Produto: ")
    if produto == "fim":
        break
    compras.append(produto)
print("Lista de compras:")
for e in compras:
    print(e)
