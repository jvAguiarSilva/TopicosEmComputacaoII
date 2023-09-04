import csv
from mensure.mensure import memit_timeit
from datetime import datetime

# Arquivo de Log
datetime_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
filename = f"busca_cubica_{datetime_now}.log"
fp = open(filename, "w+")


@memit_timeit(stream=fp)
def busca_cubica(numeroProcurado, vet):
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


if __name__ == "__main__":
    # ORDENADOS:

    # 100
    vet_100 = []
    with open("../datasets/ordenados/100.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_100.append(int(cell))

    print(busca_cubica(70, vet_100))

    # 200
    vet_200 = []
    with open("../datasets/ordenados/200.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_200.append(int(cell))

    print(busca_cubica(70, vet_200))

    # 1000
    vet_1000 = []
    with open("../datasets/ordenados/1000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_1000.append(int(cell))

    print(busca_cubica(70, vet_1000))
