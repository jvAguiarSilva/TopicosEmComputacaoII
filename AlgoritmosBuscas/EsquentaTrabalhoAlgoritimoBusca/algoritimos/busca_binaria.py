import csv
from mensure.mensure import memit_timeit_busca_binaria
from datetime import datetime

# Arquivo de Log
datetime_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
filename = f"busca_binaria_{datetime_now}.log"
fp = open(filename, "w+")


@memit_timeit_busca_binaria(stream=fp)
def busca_binaria_main(x, v, e, d):
    return busca_binaria(x, v, e, d)


def busca_binaria(x, v, e, d):
    meio = (e + d) // 2
    if v[meio] == x:
        return meio
    if e >= d:
        return -1
    elif v[meio] < x:
        return busca_binaria(x, v, meio + 1, d)
    else:
        return busca_binaria(x, v, e, meio - 1)


if __name__ == "__main__":
    # ORDENADOS:

    # 100
    vet_100 = []
    with open("../datasets/ordenados/100.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_100.append(int(cell))

    print(busca_binaria_main(70, vet_100, 0, len(vet_100) - 1))

    # 200
    vet_200 = []
    with open("../datasets/ordenados/200.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_200.append(int(cell))

    print(busca_binaria_main(70, vet_200, 0, len(vet_200) - 1))

    # 1000
    vet_1000 = []
    with open("../datasets/ordenados/1000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_1000.append(int(cell))

    print(busca_binaria_main(70, vet_1000, 0, len(vet_1000) - 1))

    # 2000
    vet_2000 = []
    with open("../datasets/ordenados/2000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_2000.append(int(cell))

    print(busca_binaria_main(70, vet_2000, 0, len(vet_2000) - 1))

    # 5000
    vet_5000 = []
    with open("../datasets/ordenados/5000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_5000.append(int(cell))

    print(busca_binaria_main(70, vet_5000, 0, len(vet_5000) - 1))

    # 10000
    vet_10000 = []
    with open("../datasets/ordenados/10000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_10000.append(int(cell))

    print(busca_binaria_main(70, vet_10000, 0, len(vet_10000) - 1))

    # 50000
    vet_50000 = []
    with open("../datasets/ordenados/50000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_50000.append(int(cell))

    print(busca_binaria_main(77, vet_50000, 0, len(vet_50000) - 1))

    # 100000
    vet_100000 = []
    with open("../datasets/ordenados/100000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_100000.append(int(cell))

    print(busca_binaria_main(70, vet_100000, 0, len(vet_100000) - 1))

    # 500000
    vet_500000 = []
    with open("../datasets/ordenados/500000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_500000.append(int(cell))

    print(busca_binaria_main(71, vet_500000, 0, len(vet_500000) - 1))

    # 1000000
    vet_1000000 = []
    with open("../datasets/ordenados/1000000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_1000000.append(int(cell))

    print(busca_binaria_main(70, vet_1000000, 0, len(vet_1000000) - 1))

    # 5000000
    vet_5000000 = []
    with open("../datasets/ordenados/5000000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_5000000.append(int(cell))

    print(busca_binaria_main(70, vet_5000000, 0, len(vet_5000000) - 1))

    # 10000000
    vet_10000000 = []
    with open("../datasets/ordenados/10000000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_10000000.append(int(cell))

    print(busca_binaria_main(71, vet_10000000, 0, len(vet_10000000) - 1))

    # 100000000
    vet_100000000 = []
    with open("../datasets/ordenados/100000000.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for cell in row:
                vet_100000000.append(int(cell))

    print(busca_binaria_main(70, vet_100000000, 0, len(vet_100000000) - 1))
