#file_object = open("filename", "mode")

# with open("","") as file:
#     content = file.read(any number)
#     print(content)

# with open("","") as file:
#     file.write()


# with open(r"C:\Users\mohit\Downloads\file1.txt","r") as file1:
#     content = file1.read()
#     print(content)


# with open(r"C:\Users\mohit\Downloads\file1.txt","r") as file1:
#       content = file1.readline()
#       print(content)

# with open(r"C:\Users\mohit\Downloads\file1.txt","r") as file1:
#       content = file1.readlines()
#       print(content)


# with open(r"C:\Users\mohit\Downloads\file1.txt","r") as file1:
#        for line in file1:
#               print(line.strip()) 



# count = 0

# with open(r"C:\Users\mohit\Downloads\file1.txt","r") as file1:
#        for line in file1:
#               if line.strip():
#                count += 1
       
# print(count)


# with open(r"C:\Users\mohit\Downloads\file1.txt","w") as file1:
#      file1.write("nikhi\n")
#      file1.write("b.tech")


# with open(r"C:\Users\mohit\Downloads\file1.txt","r") as file1:
#     content = file1.read()
#     print(content)

# with open(r"C:\Users\mohit\Downloads\file1.txt","a") as file1:
#      file1.write("karan , 23 , pune\n")



# with open(r"C:\Users\mohit\Downloads\file1.txt","r") as file1:
#      content = file1.read()
#      print(content)


with open(r"C:\Users\mohit\Downloads\file1.txt","r+") as file1: 
    lines = file1.readlines()
    lines[0] = lines[0].replace("Amit", "Amit Kumar")

    file1.seek(0)
    file1.writelines(lines)