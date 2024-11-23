from libc.stdlib cimport rand, srand
from libc.time cimport time
from typing import List

# Inicializa la semilla para la generación de números aleatorios
cdef public void initialize_random():
    srand(time(NULL))

# La función para obtener un movimiento de la máquina basado en la lista de movimientos disponibles
cdef public int machine_move(List[int] board, int size):
    cdef list available_moves = []
    cdef int i

    # Llenar la lista de movimientos disponibles
    for i in range(size):
        if board[i] == 0:
            available_moves.append(i)

    # Si no hay movimientos disponibles (todas las posiciones están ocupadas), retornar -1
    if not available_moves:
        return -1

    # Elegir un índice aleatorio de los movimientos disponibles
    cdef int random_index = available_moves[rand() % len(available_moves)]

    return random_index
