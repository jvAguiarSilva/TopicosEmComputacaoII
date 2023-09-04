import csv
from mensure.mensure import memit_timeit
from datetime import datetime

# Arquivo de Log
datetime_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
filename = f"busca_quadratica_{datetime_now}.log"
fp = open(filename, "w+")


@memit_timeit(stream=fp)
def busca_quadratica(x, v):
    contador = 0
    posicao = -1
    entrou = False

    for i in range(len(v)):
        for j in range(i, len(v)):
            if v[i] == x:
                if not entrou:
                    posicao = i
                    if v[j] == x:
                        contador += 1
    if contador > 0:
        entrou = True

    if entrou:
        return posicao, contador
    else:
        return -1, 0


if __name__ == "__main__":
    # ORDENADOS:

    # 100
    vet_100 = []
    with open("../datasets/ordenados/100.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_100.append(int(cell))

    print(busca_quadratica(70, vet_100))

    # 200
    vet_200 = []
    with open("../datasets/ordenados/200.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_200.append(int(cell))

    print(busca_quadratica(70, vet_200))

    # 1000
    vet_1000 = []
    with open("../datasets/ordenados/1000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_1000.append(int(cell))

    print(busca_quadratica(70, vet_1000))

    # 2000
    vet_2000 = []
    with open("../datasets/ordenados/2000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_2000.append(int(cell))

    print(busca_quadratica(70, vet_2000))

    # 5000
    vet_5000 = []
    with open("../datasets/ordenados/5000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_5000.append(int(cell))

    print(busca_quadratica(70, vet_5000))

    # 10000
    vet_10000 = []
    with open("../datasets/ordenados/10000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_10000.append(int(cell))

    print(busca_quadratica(70, vet_10000))

    # 50000
    vet_50000 = []
    with open("../datasets/ordenados/50000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_50000.append(int(cell))

    print(busca_quadratica(77, vet_50000))

    # 100000
    vet_100000 = []
    with open("../datasets/ordenados/100000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_100000.append(int(cell))

    print(busca_quadratica(70, vet_100000))

    # # 500000
    # vet_500000 = []
    # with open("../datasets/ordenados/500000.csv", "r") as file:
    #     csv_reader = csv.reader(file)
    #     for row in csv_reader:
    #         for cell in row:
    #             vet_500000.append(int(cell))

    # print(busca_quadratica(71, vet_500000))

    # # 1000000
    # vet_1000000 = []
    # with open("../datasets/ordenados/1000000.csv", "r") as file:
    #     csv_reader = csv.reader(file)
    #     for row in csv_reader:
    #         for cell in row:
    #             vet_1000000.append(int(cell))

    # print(busca_quadratica(70, vet_1000000))

    # # 5000000
    # vet_5000000 = []
    # with open("../datasets/ordenados/5000000.csv", "r") as file:
    #     csv_reader = csv.reader(file)
    #     for row in csv_reader:
    #         for cell in row:
    #             vet_5000000.append(int(cell))

    # print(busca_quadratica(70, vet_5000000))

    # # 10000000
    # vet_10000000 = []
    # with open("../datasets/ordenados/10000000.csv", "r") as file:
    #     csv_reader = csv.reader(file)
    #     for row in csv_reader:
    #         for cell in row:
    #             vet_10000000.append(int(cell))

    # print(busca_quadratica(71, vet_10000000))

    # # 100000000
    # vet_100000000 = []
    # with open("../datasets/ordenados/100000000.csv", "r") as file:
    #     csv_reader = csv.reader(file)
    #     for row in csv_reader:
    #         for cell in row:
    #             vet_100000000.append(int(cell))

    # print(busca_quadratica(70, vet_100000000))
