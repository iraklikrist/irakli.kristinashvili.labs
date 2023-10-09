# #2
# numbers = list(range(1, 101))
# with open("data1.txt", "w") as file:
#     for number in numbers:
#         file.write(str(number) + "\n")
#
# print("Numbers have been saved to data1.txt")
# #4
# import os
# folder_name = "myfiles2"
# os.makedirs(folder_name, exist_ok=True)
#
# for i in range(1, 31):
#     filename = f"program{i}.txt"
#     file_path = os.path.join(folder_name, filename)
#     with open(file_path, "w") as file:
#         file.write(f"This is program {i}.")
#
# print("Folder 'myfiles2' and 30 files have been created.")
# #10
# my_dict = {0: 10, 1: 20}
# my_dict[2] = 30
# my_dict[3] = 40
# print("Updated Dictionary:")
# print(my_dict)
# del my_dict[1]
# print("Dictionary after deleting an element:")
# print(my_dict)
#12
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key_to_check = 3
if key_to_check in d:
    print(f"Key {key_to_check} exists in the dictionary.")
else:
    print(f"Key {key_to_check} does not exist in the dictionary.")
#15
my_list = [0, 1, 2, 3, 4]
my_list.append(5)
my_list.append(6)
my_list.append(7)
print("Updated List after adding elements:")
print(my_list)
del my_list[2]
del my_list[4]
print("Final Elements:")
for item in my_list:
    print(item)

