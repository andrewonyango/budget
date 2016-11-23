import budget

while True:
    try:
        print()  # print a newline
        grants = input("Enter a list of grant requests separated by spaces: ")
        grants = [int(g) for g in grants.split()]
        available_budget = int(input("Enter the available budget: "))

        b = budget.Budget()
        print("The budget cap is",
            b.awardBudgetCutProblem(grants, available_budget))
        break
    except ValueError as error:
        print(error)
    except:
        print("An unknown error occured. Check your inputs.")
