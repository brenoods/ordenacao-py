import operator

with open("arq.txt") as dados:
    arquivos = dados.readlines()

    ordenado = []
    for linha in arquivos:
        linhaSplit = linha.split()
        ordenado.append(linhaSplit)

    for i in range(0, len(ordenado)):
        ordenado[i][1] = int(ordenado[i][1])

    print(sorted(ordenado, key=operator.itemgetter(1, 0))[-1])
