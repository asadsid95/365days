#
# T - 1d ; practise for 15-min technical assessment


# Problem: Ccharacter frequency from a string
# I.M.O.W: string as input is checked for character (alphabet is constraining)


#  -----------------------
# Test cases: hello, google, company's name, XY12344
# Questions to ask: range and type of input, type for output; String -> dict

# Input: String i.e. 'hello' , 'google'
# Output: {h:1, o:1, l:2, e:1}; mention the data types + reason

# Approach: iterate over string's characters, check if its been counted before -- increase counter +1 || assign 1 to the charac


def char_freq(input):

    some_dict = {}

    for i in input:
        dict_freq = some_dict.keys()  # for each iteration, dict is updated

        if i in dict_freq:
            some_dict[i] += 1
        else:
            some_dict[i] = 1
    # print(some_dict)

    return some_dict


# Problem: Sort a list
# I.M.O.W: Re arrange elements in a list in desc order

# Input / Test cases: [12,3,4,2,3,33,2,4,67] <list>
# Output: [67,33,12,...] <list>

# Iterate over list and compare to a counter value,  if element > counter -- update counter & append elemnt to new list ||

#

def sort_list(input):

    # This could be used to sort string
    listified = list(input)
    # print(sorted(listified))

    # Built-in function used
    # print(sorted(input, reverse=True))

    counter = 0
    new_list = []
    for i in input:
        if i > counter:
            new_list.append(i)
            counter = i
        else:
            break

            # How to read a lower value element & have that sorted

    print(new_list)
    print(counter)
    return(new_list)


def main():
    char_freq('XYZ123444')
    char_freq('GOOOOOGLE')

    sort_list([4, 5, 4, 3, 1])
    sort_list('this is to be sorted')


if __name__ == "__main__":
    main()
