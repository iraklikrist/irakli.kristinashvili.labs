import numpy as np




# #1
# user_input = input("Enter a string: ")
# symbol_count = len(user_input)
# print("Number of symbols in the string:", symbol_count)
# #2
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# merged_string = string1 + string2
# print("Merged string:", merged_string)
# #3
# user_input = input("Enter a string: ")
# count_a = user_input.count('a')
# print("The symbol 'a' appears", count_a, "times in the string.")
# #4
# fruits = ["banana", "apple", "watermelon"]
# sorted_fruits = sorted(fruits)
# print("Fruits in ascending alphabetical order:")
# for fruit in sorted_fruits:
#     print(fruit)
# #5
# text = "სწავლის ძირი მწარე არის, კენწეროში გატკბილდების"
# first_20_characters = text[:20]
# print("First 20 characters:", first_20_characters)
# count_s_character = text.count("ს")
# print("Number of times 'ს' appears:", count_s_character)
# #9
# text = "Hello, this is an example of a string. Please, write this text and do some exercises."
# new_text = text.replace("is", "were")
# print("Modified text:")
# print(new_text)
# #10
# text = "Hello, this is an example of a string. Please, write this text and do some exercises."
# words = text.split()
# num_words = len(words)
# print("Number of words:", num_words)
# #11
# text = "Have a nice day"
# reversed_text = text[::-1]
# for symbol in reversed_text:
#     print(symbol)
# #12
# user_input = input("Enter a text value: ")
# at_symbol_position = user_input.find("@")
# if at_symbol_position == -1:
#     print("Enter Valid Email")
# elif user_input.count("@") > 1:
#     print("Enter Valid Email")
# else:
#     print("The '@' symbol is at position:", at_symbol_position)
# #13
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# email = f"{first_name.lower()}.{last_name.lower()}@edu.ge"
# print("Your email address is:", email)
# #14
# user_input = input("Enter a string: ")
# string_length = len(user_input)
# part_length = string_length // 3
# parts = np.array_split(user_input, 3)
# for i, part in enumerate(parts):
#     print(f"Part {i + 1}: {part}")
# #15
# vector1 = np.array([1, 2, 3])
# vector2 = np.array([4, 5, 6])
# vector3 = np.random.rand(3)
# vector4 = np.random.rand(3)
# result = vector1 + vector2
# result2 = vector3 + vector4
# print("Vector 1:", vector1)
# print("Vector 2:", vector2)
# print("Sum of vectors:", result)
# print("Vector 3:", vector3)
# print("Vector 4:", vector4)
# print("Sum of vectors:", result2)
# #16
# matrix1 = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])
#
# matrix2 = np.array([[9, 8, 7],
#                    [6, 5, 4],
#                    [3, 2, 1]])
#
# result3 = matrix1 + matrix2
# print("Matrix 1:")
# print(matrix1)
# print("\nMatrix 2:")
# print(matrix2)
# print("\nSum of matrices:")
# print(result)
# matrix3 = np.random.rand(3, 3)
# matrix4 = np.random.rand(3, 3)
# result4 = matrix3 + matrix4
# #17
# vector3 = np.random.rand(3)
# vector4 = np.random.rand(3)
# result = vector1 * vector2
# result2 = vector3 * vector4
# print("Vector 1:", vector1)
# print("Vector 2:", vector2)
# print("Multiplication of vectors:", result)
# print("Vector 3:", vector3)
# print("Vector 4:", vector4)
# print("Multiplication of vectors:", result2)
# #18
# result3 = matrix1 * matrix2
# print("Result3:")
# print(result3)
# print("\nMultiplication of matrices:")
# print(result3)
# matrix3 = np.random.rand(3, 3)
# matrix4 = np.random.rand(3, 3)
# result4 = matrix3 * matrix4
# print("Matrix 3:")
# print(matrix3)
# print("\nMatrix 4:")
# print(matrix4)
# print("\nResult4:")
# print(result4)
#19
# matrix = np.random.randint(0, 10, size=(3, 3))
# print(matrix)
#20

matrix = np.random.randint(0, 10, size=(3, 3))
print(matrix)
user_input = input("Enter a number to remove from the matrix: ")
number_to_remove = int(user_input)
if number_to_remove in matrix:
    matrix = np.where(matrix == number_to_remove, 0, matrix)
    print("New Matrix (number removed):")
    print(matrix)
else:
    print(f"The number {number_to_remove} is not in the matrix.")
#21
matrix = np.random.randint(0, 10, size=(3, 3))
print("Initial Matrix:")
print(matrix)
user_input = input("Enter a row number to delete (0, 1, or 2): ")
row_to_delete = int(user_input)
if 0 <= row_to_delete <= 2:
    matrix = np.delete(matrix, row_to_delete, axis=0)
    print("New Matrix (row removed):")
    print(matrix)
else:
    print("Invalid row number. Please enter 0, 1, or 2.")
#22
matrix = np.random.randint(0, 11, size=(3, 3))
print("Initial Matrix:")
print(matrix)
matrix[matrix == 0] = 1
print("Matrix with 0 replaced by 1:")
print(matrix)






