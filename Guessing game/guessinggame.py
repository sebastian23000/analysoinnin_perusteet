if __name__=="__main__":
    from random import choice

    names = [
        "Ada", "Bjarne", "Dennis", "Dutch",
        "Guido", "Julia", "Linus", "Tim"
    ]
    name = choice(names)

    count_guesses = 0

    while True:
        print("Please, guess my name. " \
            + "(Case-sensitivity doesn't count here.)")
        put = input(": ")
        count_guesses += 1

        if put.lower() == name.lower():
            print(f"You guessed it right!")
            break

        else:
            print(f"The name is not {put}.")
            print("Do you want to continue (y/n)?")
            put = input(": ")
            if put.lower() == "n":
                print("Alright, let's quit.")
                break

            elif put.lower() == "y":
                print("Let's continue!")

                if count_guesses == 1:
                    print("Hint: The name consists " \
                        + f"of {len(name)} characters.")
                elif count_guesses % 3 == 0 \
                 and count_guesses <= 3*len(name):
                    print(
                        "Hint: The first " \
                     + f"{count_guesses//3} letters " \
                     +  "of the name are " \
                     + f"{name[:count_guesses//3]}"
                    )

            else:
                print("I don't know what you tried " \
                    + "to say, but let's continue!")

    print(f"The name was {name}.")
    print(f"You guessed {count_guesses} times.")

            
