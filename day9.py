# Working to practise for 15-min technical assessment

# Calculating length of string

def calc_str_len(input):

    counter = 0

    for i in input:
        counter += 1
    return counter


# print(calc_str_len('Hello this string\'s length is being counted without built-in function.'))


def calc_str_len_2(input):
    str_list = list(input)

    counter = 0
    for s in str_list:
        counter += 1
    return counter


print(calc_str_len_2('hello'))


# Reverse Integer (LC # 7 )
