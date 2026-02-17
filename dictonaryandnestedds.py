# countries = {
#     "India" = "Delhi",
#     "Russia" = "Mosco",
#     "America" = "New York"
#     "Afganistan" = "Kabul"
#     "Bangladesh" = "Dhaka"
# }

# print("countries and their capital")
# for country, capital in countries.items():
#     print(country, ":", capital) 

# countries = {
#     "India": "Delhi",
#     "Russia": "Moscow",
#     "America": "New York",
#     "Afghanistan": "Kabul",
#     "Bangladesh": "Dhaka"
# }

# print("Countries and their capital:")
# for country, capital in countries.items():
#     print(country, ":", capital)


# countries = {
#     "India": "Delhi",
#     "Russia": "Moscow",
#     "America": "New York",
#     "Afghanistan": "Kabul",
#     "Bangladesh": "Dhaka"
# }

# capital_india = countries["India"]
# print(capital_india)


# countries = {
#     "India": "Delhi",
#     "Russia": "Moscow",
#     "America": "New York",
#     "Afghanistan": "Kabul",
#     "Bangladesh": "Dhaka"
# }

# countries["japan"] = "tokyo"
# print(countries)



# countries = {
#     "India": "Delhi",
#     "Russia": "Moscow",
#     "America": "New York",
#     "Afghanistan": "Kabul",
#     "Bangladesh": "Dhaka"
# }

# countries["America"] = "Washigton"
# print(countries)


# students = {
#     "rahul" : 86,
#     "rohit" : 98,
#     "paglus" : 87,
#     "dalal" : 83,
#     "cwn" : 99
# }
# print("student name:")
# for name in students.keys():
#     print(name)


# students = {
#     "rahul" : 86,
#     "rohit" : 98,
#     "paglus" : 87,
#     "dalal" : 83,
#     "cwn" : 99
# }
# print("student marks:")
# for marks in students.values():
#     print(marks)


# students = {
#     "rahul" : 86,
#     "rohit" : 98,
#     "paglus" : 87,
#     "dalal" : 83,
#     "cwn" : 99
# }
# print("student name:")
# for name in students.update():
#     print(name)


# countries = {
#     "India": "Delhi",
#     "Germany": "Berlin",
#     "Russia": "Moscow",
#     "America": "New York"
# }

# countries.pop("Germany")

# print(countries)

# countries = {
#     "India": "Delhi",
#     "Germany": "Berlin",
#     "Russia": "Moscow",
#     "America": "New York"
# }

# countries.clear()
# print(countries)


# sentence = input("enter a element")
# words = sentence.split()
# frequency = {}

# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1
# print(frequency)



# student = [
#     {"name":"Amit","age": 20},
#     {"name":"Neha","age": 21},
#     {"name":"Rahul", "age": 19}
# ]


# student = [
#     {"name":"Amit","age": 20},
#     {"name":"Neha","age": 21},
#     {"name":"Rahul", "age": 19}
# ]
# print(student[0]["name"])


# students = {
#     "names":["cwn","dalal","orry"],
#     "ages":[20,21,19]
# }


# students = {
#     "names":["cwn","dalal","orry"],
#     "ages":[20,21,19]
# }
# print(students[0]["names"])

# students = {
#     "names":["cwn","dalal","orry"],
#     "ages":[20,21,19]
# }

# students ["names"] = "Priya"
# students ["ages"] = "21"
# print(students)

# students = {
#     "names":["cwn","dalal","orry"],
#     "ages":[20,21,19]
# }
# students ["cwn"] = 23
# print(students)


# students = {
#     "name": ["Rahul", "Neha", "Amit"],
#     "age": [20, 21, 19]
# }
# students["name"].remove("Neha")
# students["age"].remove(21)
# print(students)

# students = {
#     "name": ["Rahul", "Neha", "Amit"],
#     "age": [20, 21, 19]
# }
# max_age = max(students["age"])
# print("Maximum age:", max_age)



# students = {
#     "name": ["Rahul", "Neha", "Amit"],
#     "age": [20, 21, 19]
# }

# for i in range(len(students["age"])):
#     if students["age"][i] > 20:
#         print(students["name"][i])




# students = {
#     "name": ["Rahul", "Neha", "Amit"],
#     "age": [20, 21, 19]
# }
# min_age = min(students["age"])
# index = students["age"].index(min_age)

# print("Youngest student:", students["name"][index], "-", min_age)



# list_of_dict = []

# for i in range(len(students["name"])):
#     student = {
#         "name": students["name"][i],
#         "age": students["age"][i]
#     }
#     list_of_dict.append(student)

# print(list_of_dict)
