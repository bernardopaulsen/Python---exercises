l = []
x = 0
n = 0
somx = 0
somy = 0
somvx = 0
somvy = 0
somc = 0

# Dados
while True:
    x = x + 1
    a = float(input("Digite X%d: " % x))
    if a == 0:
        break
    b = float(input("Digite Y%d: " % x))
    l.append([a, b])
    n = n + 1
print(l)


# Somas e médias
for e in l:
  
    somx = somx + e[0]
    somy = somy + e[1]

medx = somx/n
medy = somy/n


# Variância e desvio padrão
for e in l:
    
    somvx = somvx + (e[0] - medx)**2
    somvy = somvy + (e[1] - medy)**2

varx = somvx/n
vary = somvy/n
desx = varx**(1/2)
desy = vary**(1/2)


# Covariância e correlação
for e in l:
    somc = somc + (e[0] - medx)*(e[1] - medy)
cov = somc/n
cor = cov/(desx*desy)


# Escrever tudo

print()
print("Somas")
print("Soma de X: %f" % somx)
print("Soma de Y: %f" % somy)
print()
print("Médias")
print("Média de X: %f" % medx)
print("Média de Y: %f" % medy)
print()
print("Variâncias")
print("Variância de X: %f" % varx)
print("Variância de Y: %f" % vary)
print()
print("Desvios padrão")
print("Desvio padrão de X: %f" % desx)
print("Desvio padrão de Y: %f" % desy)
print()
print("Covariância e correlação")
print("Covariância: %f" % cov)
print("Correlação: %f" % cor)
