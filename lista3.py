l = []
x = 0
while True:
    n = input("Digite uma palavra (0 para sair): ")
    if n == "0":
        break
    l.append(n)
while x < len(l):
    print(l[x])
    x = x + 1
