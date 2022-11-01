
# myfile = open("some_file.txt")
# txt = myfile.read()
# print(txt)
# myfile.close()

# from random import randrange


# print(randrange(10))

# # Python code to
# # demonstrate readlines()
  
# L = ["Geeks\n", "for\n", "Geeks\n"]
  
# # writing to file
# file1 = open('myfile.txt', 'w')
# file1.writelines(L)
# file1.close()
  
# # Using readlines()
# file1 = open('myfile.txt', 'r')
# Lines = file1.readlines()
  
# count = 0
# # Strips the newline character
# for line in Lines:
#     count += 1
#     print("Line{}: {}".format(count, line.strip()))

from pathlib import Path

for i in range(1,10):
    current_file = Path("questions/file" + str(i) + ".txt")

    if current_file.is_file():
        print("file" + str(i) + ".txt is exist")
    else:
        print("file" + str(i) + ".txt is not exist")
        continue

    


# txt = current_file.read()
# print(txt)

# current_file.close()