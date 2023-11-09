#This module is not intended to be imported to other programs.
assert __name__ == "__main__", \
    "This module is not intended to be imported."

#Tasks 2 - 5:
from random import randint

creator = "Sebastian Weckström"
number1, number2 = randint(0, 9), randint(0, 9)
operands = ("*", "+", "/", "-")
results = (
    number1 * number2,
    number1 + number2,
    number1 / number2 if number2 else "¯\_(ツ)_/¯",
    number1 - number2
)

print(f"Printer App \nThis app is made by {creator}.")

#print(number1)
print(f"The value of number1 is {number1}.")
print(f"The value of number2 is {number2}.")

for i in range(4):
    print(f"{number1} {operands[i]} {number2} = {results[i]}")



