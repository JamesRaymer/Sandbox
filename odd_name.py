""" James """

name = input("Name: ")

while not name:
    name = input("Name: ")

print(name[::2])