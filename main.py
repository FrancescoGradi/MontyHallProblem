import random


def montyHallProblem(numDoors=3, N=100000, doorChange=True):
    '''
    Very simple Python program to verify the Monty Hall Problem. It prints the success percentage in input case.
    :param N: total attempts.
    :param doorChange: boolean that denotes if change the door or not after the first goat removal.
    :return: None
    '''
    # Bisogna scegliere una porta, indice di questo lista
    problem = ['goat' for i in range(numDoors - 1)]
    problem.append('car')
    victories = 0
    for n in range(N):

        random.shuffle(problem)

        # Indice della porta scelta
        chosen = random.randint(0, numDoors - 1)

        # Si rimuove la scelta dalle possibili
        doors_indices = list(range(numDoors))
        doors_indices.remove(chosen)

        # Vengono aperte tutte le porte tranne una e quella scelta
        # Per semplicità si eliminano tutte le capre: se c'è la macchina, rimarrà solo quella, altrimenti vengono
        # eliminati tutti gli indici. Tenendo traccia dell'ultimo indice eliminato, possiamo reintrodurre una capra
        # qualora sia necessario.
        idxs = []
        for i in doors_indices:
            if problem[i] == 'goat':
                idxs.append(i)
                last_index = i
        for idx in idxs:
            doors_indices.remove(idx)

        # Se la prima scelta è stata la macchina, la lista degli indici è vuota (per semplicità si eliminano tutte le
        # scelte corrispondenti a "goat"), ma avendo tenuto traccia degli indici eliminati posso correggere senza
        # sforzo.
        if len(doors_indices) == 0:
            doors_indices.append(last_index)

        # Si cambia la porta oppure no
        if doorChange:
            chosen = doors_indices[0]

        if problem[chosen] == 'car':
            victories += 1

    print('Victories: ' + str(victories) + '   Total attempts: ' + str(N) + '   Door change: ' + str(doorChange)
          + '   Number of doors: ' + str(numDoors) + '   Success rate: ' + str((victories/N) * 100) + '%')


if __name__ == '__main__':
    door_change = False
    N = 10000
    num_doors = 10
    montyHallProblem(num_doors, N, door_change)

    door_change = True

    montyHallProblem(num_doors, N, door_change)