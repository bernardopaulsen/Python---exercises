l = [5, 9, 13, 15, 8, 7, 10]
for x, e in enumerate(l):
    print("[%d] %d" % (x, e))
maximo = 0
for e in l:
    if e > maximo:
        maximo = e
print("Maximo = %d" % maximo)
