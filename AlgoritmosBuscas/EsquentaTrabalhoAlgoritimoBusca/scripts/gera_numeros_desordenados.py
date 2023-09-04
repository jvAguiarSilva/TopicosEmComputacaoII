import random
import math
import csv


def gerar_vetor_nao_ordenado(tamanho):
    vetor = [random.randint(0, tamanho) for _ in range(tamanho)]
    return vetor


def vetor_para_matriz(vetor):
    tamanho = len(vetor)
    num_linhas = math.ceil(tamanho / 10)
    matriz = [vetor[i : i + 10] for i in range(0, tamanho, 10)]
    # Preencher as linhas incompletas com zeros
    if len(matriz[-1]) < 10:
        matriz[-1] += [0] * (10 - len(matriz[-1]))
    return matriz


def salvar_matriz_csv(matriz, nome_arquivo):
    with open(nome_arquivo, "w", newline="") as arquivo:
        writer = csv.writer(arquivo)
        for linha in matriz:
            writer.writerow(linha)


n = int(input("Digite o tamanho do vetor (n): "))
vetor_gerado = gerar_vetor_nao_ordenado(n)
matriz_gerada = vetor_para_matriz(vetor_gerado)

nome_arquivo = input(
    "Digite o nome do arquivo CSV para salvar a matriz (sem a extensão): "
)
nome_arquivo_com_extensao = nome_arquivo + ".csv"
salvar_matriz_csv(matriz_gerada, nome_arquivo_com_extensao)
print(f"A matriz foi salva no arquivo '{nome_arquivo_com_extensao}'.")
