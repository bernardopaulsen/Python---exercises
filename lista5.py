l = []
print("Escreva o nome de um cliente para adiciona-lo à fila.")
print("Escreva A para atender um cliente.")
while True:
    print("Existem %d clientes na fila." % len(l))
    o = input("Escreva nome ou A:")
    if o == "A":
          if len(l) > 0:
              atendido = l.pop(0)
              print("Cliente %s atendido." % atendido)
          else:
              print("Fila vazia.")
    else:
          l.append(o)
          print("Cliente %s adicionado à fila" % o)
          
