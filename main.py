import random


def montyHallProblem(N=100000, doorChange=True):
    '''
    Very simple Python program to verify the Monty Hall Problem. It prints the success percentage in input case.
    :param N: total attempts.
    :param doorChange: boolean that denotes if change the door or not after the first goat removal.
    :return: None
    '''
    # Bisogna scegliere una porta, indice di questo lista
    problem = ['goat', 'goat', 'car']
    victories = 0
    for n in range(N):

        random.shuffle(problem)

        # Indice della porta scelta
        chosen = random.randint(0, 2)

        # Si rimuove una capra
        doors_indices = [0, 1, 2]
        doors_indices.remove(chosen)

        for i in doors_indices:
            if problem[i] == 'goat':
                doors_indices.remove(i)
                break

        # Si cambia la porta oppure no
        if door_change:
            chosen = doors_indices[0]

        if problem[chosen] == 'car':
            victories += 1

    print('Victories: ' + str(victories) + '   Total attempts: ' + str(N) + '   Door change: ' + str(door_change)
          + '   Success rate: ' + str(victories/N) + '%')


if __name__ == '__main__':
    door_change = False
    N = 100000

    montyHallProblem(N, door_change)