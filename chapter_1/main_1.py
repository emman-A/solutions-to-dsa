#REINFORCEMENT
#R_1.1
# def is_multiple(n, m):
#     return n % m == 0

# # Test the function
# is_multiple(5, 2)

#R_1.2
# def is_even(k):
#     return k & 1 == 0

# is_even(51)

#R_1.3
# def minmax(data):
#    mini = data[0]
#    maxi =data[0]
#    for i in range(1, len(data)):
#       if data[i] < mini:
#         mini = data[i]

#       elif data[i] > maxi:
#         maxi = data[i]

#    return mini, maxi


# data = [5,3, 10, 46]
# print(minmax(data))

#R_1.4
# def squared_values(n):
#     total = 0
#     while n > 0:
#         square = (n-1)**2
#         total =sum(square)
#         n -= 1
#     return total

# squared_values(5)
#OR
# def square_num():
#     return sum(i**2 for i in range(1, n))


#R_1.5
# def square_num():
#     return sum(i**2 for i in range(1, n))

#R_1.6
# def odd_square(n):
#   total = 0
#   for i in range(1, n):
#     if i % 2 != 0:
#       total += i**2
#   return total

# odd_square(4)

#R_1.7
# def odd_square(n):
#   return sum(i**2 for i in range(1, n) if i%2 != 0)

# odd_square(5)

#R_1.11
# my_list = []
# for i in range(9):
#   i = 2**i
#   my_list.append(i)
# print(my_list)

#        #OR
# [2**i for i in range(9)]

#R_1.12
# import random

# def choice(data):
#     element = random.choice(data)
#     return element
# data = range(1, 100)
# choice(data)


#CREATIVITY

# 1.13
# def reverse_list(data):
#   return data[::-1]

# data = [1, 2, 3, 4, 5]
# reverse_list(data)

#1.14
# def odd_product(data):
#   for i in range(len(data)):
#     for j in range(i+1, len(data)):
#       if (data[i] * data[j]) % 2 != 0:
#         return True
#   return False

# data = [2, 3, 4, 6]
# print(odd_product(data))

#1.15
# def is_distinct(n):
#   for i in range(len(n)):
#     for j in range(i+1, len(n)):
#       if n[i] == n[j]:
#         return False
#   return True
  
# n = [1, 2, 3, 4, 5, 2]
# print(is_distinct(n))

#1.18
# print([i*(i+1) for i in range(10)])

#1.19
# print([chr(i) for i in range(ord('a'), ord('z')+1)])

#1.20
# import random

# def shuffle(data):
#   for i in range(len(data)-1, 0, -1):
#     j = random.randint(0, i)
#     data[i], data[j] = data[j], data[i]

#1.22
# def dot_product(a, b):
#   product = []
#   if len(a) != len(b):
#     return None
#   else:
#     for i in range(len(a)):
#       product.append(a[i]*b[i])
#     return product
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(dot_product(a, b))

#1.24
# def count_vowels(data):
#     vowels = ('a', 'e', 'i', 'o', 'u')
#     count = 0
#     for j in data:
#       if j in vowels:
#           count += 1
#     return count
# data = "zoauaeel"
# count_vowels(data)   


