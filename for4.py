l = []
x = 0
n = 0
somx = 0
somy = 0
somc = 0
# insetir os dados
while True:
    x = x + 1
    a = float(input("Digite X%d: " % x))
    if a == 0:
        break
    b = float(input("Digite Y%d: " % x))
    l.append([a, b])
    n = n + 1
print(l)
# começar repetição
for e in l:
    #soma dos X
    somx = somx + e[0]
    #soma dos Y
    somy = somy + e[1]
# media de x
medx = somx/n
# media de Y
medy = somy/n
for e in l:
    somc = somc + (e[0] - medx)*(e[1] - medy)
cov = somc/n

print(somx)
print(somy)
print(medx)
print(medy)
print(cov)
