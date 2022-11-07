import random


# Hàm khởi tạo nhiễm sắc thể ngẫu nhiên
def randomChromosome(queenNum):
    return [random.randint(1, queenNum) for _ in range(queenNum)]


# Hàm tính độ tốt
def fitness(chromosome):
    horizontal_collisions = sum([chromosome.count(queen) - 1 for queen in chromosome]) / 2  # Đụng độ chiều ngang
    diagonal_collisions = 0  # Đụng độ chiều dọc

    n = len(chromosome)  # lấy độ dài của nst
    left_diagonal = [0] * 2*n  # chéo trái
    right_diagonal = [0] * 2*n  # chéo phải
    # => [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  if n=8
    for i in range(1, n):
        left_diagonal[i + chromosome[i]] += 1
        right_diagonal[len(chromosome) - i + chromosome[i]] += 1

    for i in range(1, 2*n):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i] - 1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i] - 1
        diagonal_collisions += counter
    return int(maxFitness - (horizontal_collisions + diagonal_collisions))


def probability(chromosome, fitness):
    return fitness(chromosome) / maxFitness


def randomPick(population, probabilities):
    populationWithProbability = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbability)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shoudn't get here"


def reproduce(x, y):
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]


def mutate(x):
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x


def printChromosome(chrom):
    print("Nhiem sac the = {}, Fitness = {}".format(str(chrom), fitness(chrom)))


def geneticQueen(population, fitness):
    mutationProbability = 0.03
    newPopulation = []
    probabilitis = [probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = randomPick(population, probabilitis)
        y = randomPick(population, probabilitis)
        child = reproduce(x, y)

        if random.random() < mutationProbability:
            child = mutate(child)
        printChromosome(child)
        newPopulation.append(child)
        if fitness(child) == maxFitness: break
    return newPopulation


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('TramNQ')

    # queenNum = int(input("Nhập số lượng quân hậu: "))   #Số lượng hậu
    queenNum = 8
    maxFitness = (queenNum * (queenNum - 1)) / 2  # 8*7/2 =28
    population = [randomChromosome(queenNum) for _ in range(500)]

    generation = 1
    while not maxFitness in [fitness(chrom) for chrom in population]:
        print("===The he {} ===".format(generation))
        population = geneticQueen(population, fitness)
        print("")
        print("MaxFitness = {}".format(max([fitness(n) for n in population])))
        generation += 1
    chrom_out = []
    print("Solved in Generation {}!".format(generation - 1))
    for chrom in population:
        if fitness(chrom) == maxFitness:
            print("")
            print("One of the solutions: ")
            chrom_out = chrom
            printChromosome(chrom)

    board = []

    for x in range(queenNum):
        board.append(["x"] * queenNum)

    for i in range(queenNum):
        board[queenNum - chrom_out[i]][i] = "Q"


    def print_board(board):
        for row in board:
            print(" ".join(row))


    print()
    print_board(board)
