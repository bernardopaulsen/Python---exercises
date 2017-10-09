notas = [0,0,0,0,0]
soma = 0
x = 0
while x < 5:
    notas[x] = int(input("Nota %.0f: " % (x + 1)))
    if notas[x] > 10:
        print("Digite um número de 0 a 10!")
        notas[x] = int(input("Nota %.0f: " % (x + 1)))
    soma = soma + notas[x]
    x = x + 1
x = 0
print("Notas:")
print(notas)
while x < 5:
    if notas[x] >= 6:
        y = "Aprovado!"
    else:
        y = "Reprovado!"
    print("Nota %d: %s" % ((x+1), y))
    x = x + 1
print("Média:")
print("%.1f" % (soma/5))
