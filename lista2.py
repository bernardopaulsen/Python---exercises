l = [0,0,0,0,0,0,0,0,0,0]
x = 0
print("Digite números de 1 a 10.")
while x < 10:
    l[x] = int(input("Número %d: " % ( x+ 1)))
    if l[x] > 10:
        print("Digite números de 1 a 10.")
    else:
        x = x + 1
while True:
    x = int(input("Digite o número a ser impresso: "))
    if x <= 10:
        print(l[x-1])
    else:
        print("Digite um número de 0 a 10!")
        
