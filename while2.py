x = 0

soma = 0

n = 0

p = int(input("Digite o valor da compra: "))

while p >= 0:
    
    if p > 0:
        
        soma = soma + p

        x = x + 1

        m = soma/x

        n = n + 1

        print("Soma: R$%6.2f; Compras: %3.0f; Média: R$%6.2f." % (soma, n, m))

        p = int(input("Digite o valor da compra: "))
    
    if p == 0:
        
        print("Não existe almoço grátis! Digite outro valor!")

        p = int(input("Digite o valor da compra: "))

