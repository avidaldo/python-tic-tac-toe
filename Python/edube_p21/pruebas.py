
# for i, elem in enumerate(hat_list): print(i, elem)

# list1= [1,2,3,4,5,6,7,8,9,10]
# list2= [list1[i] for i in range(len(list1)) if i%2==0]
# # enumerate y recuperar solo keys
# list22 = [e for i,e in enumerate(list1) if i%2==0]
# list3= [e for e in list1 if e%2==0]

# list4= [(e) for e in list1 if e%2!=0]


# array1 = (1,2,3,"4asdasds",5,6,7,8,'9',10) #tupla

# print(array1)

# def print_pretty_list(list_object):
#     print("--------------------")
#     print("length: ", len(list_object))
#     print("index    --   value")
#     for i, elem in enumerate(list_object):
#         print(f"{i}  -- {elem} ")
#     print("--------------------")


# numbers = [111, 7, 2, 1]
# print(numbers)
# print_pretty_list(numbers)

# ###

# numbers.append(4)
# print_pretty_list(numbers)
# print(numbers)

# ###

# numbers.insert(0, 222)
# print_pretty_list(numbers)
# print(numbers)




# my_list =[]
# for i in range(5): my_list.append(i + 1)
# print(my_list)


# my_list =[]
# for i in range(5): my_list.insert(0, i + 1)
# print(my_list)


# print([i+1 for i in range(5)])
# print([i for i in reversed(range(5))])
# print([i for i in (list(range(5)).reverse())])

# print(list(range(5, 0, -1)))

# print("--------------------")
# my_list = [1,2,3,4,5,6,7,8,9,]
# print(my_list)
# print(len(my_list)//2)
# print(list(range(len(my_list)//2)))

# for i in range(len(my_list)//2):
#     print(my_list[i])
#     my_list[i], my_list[len(my_list)-1-i] = my_list[len(my_list)-i-1], my_list[i]
# print(my_list)

# print(my_list[::-1]) # 
# print(my_list[:5:-1]) # 

#print(list(reversed(my_list)))


# my_list = [1, None, True, 'I am a string', 256, "último"]
# # # print(my_list[3]) # outputs: I am a string
# # print(my_list[-1])
# # #print(my_list[6]) # outputs: IndexError: list index out of range

# print(list(range(2)))
# for i in range(-3,3,1): print(i, my_list[i])
# print("--------------------")
# for i in range(-5,3): print(i, my_list[i])


# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2)




# found = 5 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(found)

# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits = 0

# for number in bets:
#     if number in drawn:
#         hits += 1

# print(hits)



# print(len([bet for bet in bets if bet in drawn]))



# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# #
# # Write your code here.
# #
# print("The list with unique elements only:")

# my_list = list(set(my_list))
# print(my_list)


# my_list = [1,2,3]
# print(list(range(len(my_list))))
# for v in range(len(my_list)):
#     print(v, my_list[v])
#     my_list.insert(1, my_list[v])
#     print(my_list)
    
    
# print(list(range(1)))


# for i in range(1):
#     print('#')
# else:
#     print('#')


# https://learnpython.com/blog/null-in-python/



#-------------------------------------------------------------

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# a = float(input('Enter the first side\'s length: '))
# b = float(input('Enter the second side\'s length: '))
# c = float(input('Enter the third side\'s length: '))

# if is_a_triangle(a, b, c):
#     print('Yes, it can be a triangle.')
# else:
#     print('No, it can\'t be a triangle.')
    
    
    
# from functools import reduce
# print(reduce(lambda a, b: bool(a and b), [0, 0, 1, 0, 0]))

temperature = float(input('Enter current temperature:'))

if temperature > 0:
    print("Above zero")
elif temperature < 0:
    prin("Below zero")
else:
    print("Zero")

