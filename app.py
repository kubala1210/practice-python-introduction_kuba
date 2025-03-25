
# Pobieram liczbę od uzytkownika
number = int(input("Enter your number: "))

"""
Sprawdzam warunek, czy podana liczba jest wieksza niz 10
Jeśli jest to gratuluje uzytkownikowi
"""

if number in range(10):
    print('Bravo!')
else:
    print("You didn't make it :(")

temp_1 = 5
temp_2 = 5.6
zdanie = 'Pięć przecinek sześć'
result_1 = temp_2 > temp_1

temp_types = f'{temp_1} is integer and {temp_2} is float'

list = [1, 2, 3]
tuple = (1, 2, 3)
dict = {"name": "Kuba", "age": 28}
set = {1, 1, 2, 2, 3, 3}

print(set)

name = 'Kuba'
weeks = 2
goal = "nauka python"

name_and_goal = "Mam na imię {}, od {} tygodni uczę się programowania. Moim celem jest {}".format(
    name, weeks, goal)

print(name_and_goal)

name_and_goal = f"Mam na imię {name}, od {weeks} tygodni uczę się programowania. Moim celem jest {goal}"

print(name_and_goal)
