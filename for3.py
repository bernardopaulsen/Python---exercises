l = []
soma = 0
quadrados = 0
n = 0
som = 0
while True:
    a = int(input("Digite um número: "))
    if a == 0:
        break
    l.append(a)
    n = n + 1
    
for e in l:
    soma = soma + e
    quadrados = quadrados + e**2
    som = som + (e - (soma/n))**2
som = som/n



print("Soma = %d" % soma)
print("Média = %f" % (soma/n))
print("Soma dos quadrados = %d" % quadrados)
print("Variância = %f" % som)
print("Desvio padrão = %f" % (som**(1/2)))
