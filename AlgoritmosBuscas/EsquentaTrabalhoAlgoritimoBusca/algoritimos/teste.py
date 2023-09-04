def encontrar_posicao_numero(vet, numeroProcurado):
    posicao = -1

    for i in range(len(vet)):
        for j in range(len(vet)):
            for l in range(len(vet)):
                if (
                    vet[i] == numeroProcurado
                    and vet[j] == numeroProcurado
                    and vet[l] == numeroProcurado
                ):
                    posicao = i

    return posicao


vet = [2, 4, 5, 6, 2, 4, 9, 4, 5, 6]
numeroProcurado = 6
posicao = encontrar_posicao_numero(vet, numeroProcurado)

if posicao != -1:
    print("Posicao: ", posicao)
