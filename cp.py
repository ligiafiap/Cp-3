temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

maior_risco = 0
sala_risco =  0

for i in range(len(temperaturas)):

    soma = 0
    registro_critico = 0

    for temperatura in temperaturas[i]:
        soma += temperatura

        if temperatura > 32:
            registro_critico += 1

    print("Sala", i + 1)
    print(soma/4)
    print(registro_critico)
    print()

    if registro_critico > maior_risco:
        maior_risco = registro_critico
        sala_risco = i + 1
print("Sala com maior risco: Sala", sala_risco)







