import csv
from mensure.mensure import memit_timeit
from datetime import datetime

# Arquivo de Log
datetime_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
filename = f"busca_ternaria_{datetime_now}.log"
fp = open(filename, "w+")


@memit_timeit(stream=fp)
def busca_ternaria(x, vet):
    n = len(vet)
    inicio = 0
    fim = n - 1

    while inicio <= fim:
        meio_esquerdo = inicio + (fim - inicio) // 3
        meio_direito = fim - (fim - inicio) // 3

        if vet[meio_esquerdo] == x:
            return meio_esquerdo
        elif vet[meio_direito] == x:
            return meio_direito
        elif vet[meio_esquerdo] > x:
            fim = meio_esquerdo - 1
        elif vet[meio_direito] < x:
            inicio = meio_direito + 1
        else:
            inicio = meio_esquerdo + 1
            fim = meio_direito - 1

    return -1


if __name__ == "__main__":
    # ORDENADOS:

    # 100
    vet_100 = []
    with open("../datasets/ordenados/100.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_100.append(int(cell))

    print(busca_ternaria(70, vet_100))

    # 200
    vet_200 = []
    with open("../datasets/ordenados/200.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_200.append(int(cell))

    print(busca_ternaria(70, vet_200))

    # 1000
    vet_1000 = []
    with open("../datasets/ordenados/1000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_1000.append(int(cell))

    print(busca_ternaria(70, vet_1000))

    # 2000
    vet_2000 = []
    with open("../datasets/ordenados/2000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_2000.append(int(cell))

    print(busca_ternaria(70, vet_2000))

    # 5000
    vet_5000 = []
    with open("../datasets/ordenados/5000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_5000.append(int(cell))

    print(busca_ternaria(70, vet_5000))

    # 10000
    vet_10000 = []
    with open("../datasets/ordenados/10000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_10000.append(int(cell))

    print(busca_ternaria(70, vet_10000))

    # 50000
    vet_50000 = []
    with open("../datasets/ordenados/50000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_50000.append(int(cell))

    print(busca_ternaria(77, vet_50000))

    # 100000
    vet_100000 = []
    with open("../datasets/ordenados/100000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_100000.append(int(cell))

    print(busca_ternaria(70, vet_100000))

    # 500000
    vet_500000 = []
    with open("../datasets/ordenados/500000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_500000.append(int(cell))

    print(busca_ternaria(71, vet_500000))

    # 1000000
    vet_1000000 = []
    with open("../datasets/ordenados/1000000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_1000000.append(int(cell))

    print(busca_ternaria(70, vet_1000000))

    # 5000000
    vet_5000000 = []
    with open("../datasets/ordenados/5000000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_5000000.append(int(cell))

    print(busca_ternaria(70, vet_5000000))

    # 10000000
    vet_10000000 = []
    with open("../datasets/ordenados/10000000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_10000000.append(int(cell))

        print(busca_ternaria(71, vet_10000000))

    # 100000000
    vet_100000000 = []
    with open("../datasets/ordenados/100000000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_100000000.append(int(cell))
    print(busca_ternaria(70, vet_100000000))
