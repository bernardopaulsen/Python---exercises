velocidade = int(input("Digite a velocidade de seu carro: "))

if velocidade <= 80:
    print("Sem multa!")

if velocidade > 80:
    multa = 5 * (velocidade - 80)
    print("Multa = R$%6.2f" % multa)
