from arithmetic_arranger import arithmetic_arranger

while True:

    problems = [item for item in input("Please insert up to five arithmetic problems separated by comma: ").split(",")]

    answers = input("Would you like the answers to the problems to be displayed? (Y/N): ")
    while answers not in ["Y", "N"]:
        answers = input("Please choose Y or N: ")

    try:
        print("\n")
        if answers == "Y":
            print(arithmetic_arranger(problems, True))
        else:
            print(arithmetic_arranger(problems))
        print("\n")

    except:
        print("Input Error!\n")

    again = input("Would you like to insert up to 5 problems more? (Y/N): ")
    while again not in ["Y", "N"]:
        again = input("Please choose Y or N: ")

    if again == "N":
        print("Bye!")
        break

