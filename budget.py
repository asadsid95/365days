# Budget app
'''
# Problem: Create a Budget class that can instantiate ~~~ objects based on different budget categories ~~~ like food, clothing, and entertainment. These objects should allow for depositing and withdrawing funds from each category, as well computing category balances and transferring balance amounts between categories

# IOW:

# Categories: Food, Clothing, Hobby, Subscriptions, PC equip, coffee
#
# Features: expenses,
#            deposit/withdraw funds from each category,
#              balances/transfer between categories

# Input: Dict {} of all expenses i.e. transactions history type data
# Output: expenses, deposit/wd funds from each catg., balances/transfer between categories

# Topics found during reading on Decorators (Credits: https://book.pythontips.com/en/latest/decorators.html ):
# - Nested function
# - function as argument for another func.
# - ANSWER TO LONG-TIME QUESTION: having () in front of functions executes them (i.e. returns whatever code's inside of them) BUT w/o them, function itself is assigned to the variables
'''

class Budget:
    # return 0

    # dict w/ input value
    def __init__(self, input):
        self.input = input     # dict w/ input values
        return None

    # Get total expense
    def exps_calc(self, expense):
        # print(expense)
        # print(self.input.values())

        total_expense = {'Allowable food': 400, 'Allowable clothing': 150, 'Allowable Hobby':100}

        for i,j in total_expense.items():
            print(i,j)

        # for i in self.input.values():
        #     total_expense -= i

        print('Total expense: ', total_expense)

        return None


    # print('end of Budget class')

# print("break")


def main():

    default_value=100


    data = {'Food': 300, 'Clothing': 100, 'Hobby': default_value}

    user_input = Budget(data)

    print(user_input.exps_calc(10000))


if __name__ == "__main__":
    main()
