# ---- Working to practise for 15-min technical assessment

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

    # print(calc_str_len_2('hello'))


# Show character frequency in string

# Input: 'Some string'
# Output: S = 2, o = 1, ...
# Approach: Iterate over the string; if alphabet has been read before, add 1 OR ELSE create a key/value pair with 1 as value for that alphabet/key

def char_freq(input):
    some_dict = {}
    for i in input:
        key = some_dict.keys()
        if i in key:
            some_dict[i] += 1
        else:
            some_dict[i] = 1
    return some_dict


print(char_freq('goooogle'))

# Reverse Integer (LC # 7 )
