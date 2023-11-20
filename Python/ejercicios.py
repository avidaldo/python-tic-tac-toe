
def tipo_impositivo(renta):
    return (None if renta<0 else
            '5%' if renta < 10000 else
            '15%' if renta < 20000 else
            '20%' if renta < 35000 else
            '30%' if renta < 60000 else
            '45%')

print(f"Tu tipo impositivo es {tipo_impositivo(int(input('¿Cuál es tu renta anual? ')))}")











def print_count_down(num):
    print(*range(num, -1, -1), sep=', ')

print_count_down(int(input('Introduce un número entero positivo: ')))


CARACTER = '#'
# longitud = int(input('Introduce la longitud del diente de sierra (2<=n<=10): '))
# dientes = int(input('Introduce el número de dientes de la figura (1<=n<=10): '))
longitud = 5
dientes = 2

for i in range(dientes):
    for j in range(1, longitud + 1):
        print(CARACTER * j)
    for j in range(longitud-1, 0, -1):
        print(CARACTER * j)
        
        
        
        
        

def escalar_product(vector1, vector2, ndigits=2):
    if len(vector1) != len(vector2):
        raise ValueError('Los vectores deben tener la misma dimensión')
    return round(sum([vector1[i]*vector2[i] for i in range(len(vector1))]), ndigits)
#   return sum(i*j for i, j in zip(vector1, vector2))

# TEST_VECTOR_11 = [1.2, 3.5, -2.1, 6.6]
# TEST_VECTOR_12 = [3.3, -0.9, 1.8, 7.5]
# TEST_VECTOR_21 = [2.3, 1.5]
# TEST_VECTOR_22 = [2.0, -2.0]
# TEST_VECTOR_22b = [2, -2]

# print(escalar_product(TEST_VECTOR_11, TEST_VECTOR_12))
# print(escalar_product(TEST_VECTOR_21, TEST_VECTOR_22))
# print(escalar_product(TEST_VECTOR_21, TEST_VECTOR_22b))
# print(f'El producto escalar vale {escalar_product(TEST_VECTOR_21, TEST_VECTOR_22b):.2f}')

dimension = int(input('Introduce la dimensión de los vectores: '))
print('Introduce los valores del primer vector: ')
vector1 = [float(input(f"Dato {i}: ")) for i in range(dimension)]
print('Introduce los valores del segundo vector: ')
vector2 = [float(input(f"Dato {i}: ")) for i in range(dimension)]
print(f'El producto escalar vale {escalar_product(vector1, vector2):.2f}')




def input_numbers(num_elements):
    print('Introduce los números: ')
    nums = set()
    for i in range(num_elements):
        while True:
            new = input(f"Dato {i+1}: ")  
            if new not in nums: break
            print('Error, elemento repetido. ')
        nums.add(new)
    return nums

num_elements_1 = int(input('Introduce el número de elementos de la lista 1 (>0): '))
nums_1 = input_numbers(num_elements_1)
# nums_1 = {int(input(f"Dato {i+1}: ")) for i in range(num_elements_1)} # Sin comprobar repetidos
num_elements_2 = int(input('Introduce el número de elementos de la lista 2 (>0): '))
nums_2 = input_numbers(num_elements_2)

# nums_1 = {1, 2, 3, 4, 5}
# nums_2 = {3, 4, 5, 6, 7}

print('La intersección de las listas es: ', end='')
print(*(nums_1 & nums_2))