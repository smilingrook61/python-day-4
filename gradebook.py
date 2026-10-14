grades = {
    "Jeff" : "D",
    "Alvin" : "F",
    "Jorbius" : "A++++++++++"
}

name = input("What is your name?")
if (grades.get(name)):
    print(grades.get(name))

else:
    print("Student Not Found")

