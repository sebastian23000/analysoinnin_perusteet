def exercise1():
    #1:
    furniture = ["table", "chair", "shelf"]

    #2.
    print(furniture)

    #3:
    print(furniture[:2])

    #4:
    if "sofa" in furniture:
        print(furniture[furniture.index("sofa")])

def exercise2():
    from random import randint

    thrown_dice_numbers = [randint(1, 6) for i in range(5)]

    print(thrown_dice_numbers)

    for func in (sum, max):
        print(func(thrown_dice_numbers))



def exercise3():
    from random import randint

    numbers = []
    for i in range(5):
        number = randint(1, 20 - i)
        #If number already exists in numbers,
        #then try 1 bigger number and repeat.
        while number in numbers:
            number += 1
            if number > 20:
                number = 1
        numbers.append(number)
    print(numbers)
    
if __name__ == "__main__":
    exercise3()
