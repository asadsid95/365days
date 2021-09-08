# Budget app

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

        # allowable_expense = {'Allowable food': 499990, 'Allowable clothing': 150, 'Allowable Hobby':1545540}

        # allowable_categories = ['Allowable food', 'Allowable clothing','Allowable Hobby']
        # allowable_amounts= [8999, 999,1000]
        # allowable_expense = dict(zip(allowable_categories,allowable_amounts))

        # print(allowable_expense)



        # Balances in categories ##

        # allow = list(allowable_expense.values())
        # input = list(self.input.values())

        # First time using List Comph.
        # new_list = [allow[i] - input[i] for i in range(len(input))]
        # for i in range(len(input)):

        #     new_list.append(allow[i] - input[i])

        # allow = new_list
        # print('Remaining expense (list): ', allow)

        # Updating values in allowable_expense

        #Attempt # 2 ##




        # Attempt# 1: INCORRECT## tldr; changing values via .items() and using counter but that hasnt worked

        # k=0
        # for i,j in allowable_expense.items():
        #     j = allow[k]
        #     print(k)
        #     k += 1
        #     print(k)

        #     print(allowable_expense)


        # 2nd approach for balancing (set for another iteration):
        #   print(tuple(zip(allow, input)))


        # Transfers between categories ##

        # print('Total expense: ', type(allowable_expense.values()), type(self.input))

        return None

    # print('end of Budget class')

# print("break")

def main():

    default_value=103038

    data = {'Food': 100000, 'Clothing': 100, 'Hobby': default_value}

    user_input = Budget(data)

    user_input.exps_calc(10000)

if __name__ == "__main__":
    main()
