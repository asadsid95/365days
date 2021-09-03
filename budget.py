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

        allowable_expense = {'Allowable food': 400, 'Allowable clothing': 150, 'Allowable Hobby':100}

        # Balances in categories ##

        # for i in allowable_expense.values():
        #     print(i)

        allow = allowable_expense.values()
        input = self.input.values()

        # for i,j in allowable_expense.items():
        #     print(i,j)

        # print(type(allowable_expense.values()))
        for i in range(len(input)):
            for j in allow:
               # print((input(i), '                  ', allow(j))) ### error: 'dict_values' object is not callable
                print(j - i) ## Learned about augmented assignment statement ; Modifies the actual object vs assigning to target



        # Transfers between categories ##



        # print('Total expense: ', type(allowable_expense.values()), type(self.input))

        return None


    # print('end of Budget class')

# print("break")

def main():

    default_value=100

    data = {'Food': 300, 'Clothing': 100, 'Hobby': default_value}

    user_input = Budget(data)

    user_input.exps_calc(10000)

if __name__ == "__main__":
    main()
