# Budget app

# Categories: Food, Clothing, Hobby, Subscriptions, PC equip, coffee
#
# Features: expenses i.e. deposit/withdraw funds from each category,
#              balances/transfer between categories

class Budget:
    # return 0

    # dict w/ input value
    def __init__(self, input):
        self.input = input     # dict w/ input values
        return None

    def exps_calc(self, expense):
        # print(expense)
        # print(self.input.values())

        total_expense = 0

        for i in self.input.values():
            total_expense += i

        print(total_expense)

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
