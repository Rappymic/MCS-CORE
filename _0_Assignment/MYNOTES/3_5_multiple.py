"""Write a function that returns the sum of multiples of 3 and 5 between 0 and
limit (parameter). For example, if limit is 20, it should return the sum of 3,
5, 6, 9, 10, 12, 15, 18, 20."""


def _3_5_multi_sum(end_limit):
    temp_list = []
    for i in range(1, end_limit + 1):
        if i % 3 == 0 or i % 5 == 0:
            temp_list.append(i)
    temp_var = 1
    for i in temp_list:
        temp_var *= i
    return temp_var


a = _3_5_multi_sum(20)
print(f"the sum of multiple of 3 or 5 upto 20 is:", a)

import prime_number

print(prime_number.check_prime(47))


def cube_num(num):
    return num ** 3


print("The cube of number 3 is", cube_num(3), "\n")


def print_table(num):
    multiple = 1
    while multiple < 11:
        print(f"{num} X {multiple} =".ljust(8), num * multiple)
        multiple += 1


print("The table of number 5 is")
print_table(5)


def fibb_series(nth_index):
    if nth_index == 1:
        return 1
    if nth_index == 2:
        return 2
    else:
        nth_no = fibb_series(nth_index - 2) + fibb_series(nth_index - 1)
        return nth_no


print("Fibbonachi Series".center(80, "-"))
for i in range(1, 20):
    if i == 19:
        print(fibb_series(i))
    else:
        print(fibb_series(i), end=" ")


def multiple_list(list_):
    multi = 1
    for i_ in list_:
        multi = multi * i_
    return multi


print("-".ljust(80, "-"))
print("The multiplication of list")
print(multiple_list([1, 2, 3, 4, 5, 6]))
print("Reverse of string".center(80, "-"))


def revers_string(str_):
    # temp_list = list(str)
    # temp_list = temp_list[::-1]
    # final_str = "".join(temp_list)
    final_str = str_[::-1]
    return final_str


def upper_lower(str_):
    u = 0
    for char in str_:
        if f"{char}".isupper():
            u += 1
    return u


string1 = "THis is a laptop"

print(revers_string(string1))

print("The upper case letter in the strings are ", upper_lower(string1))
print("The Lower case letter in the strings are ",
      len(string1) - upper_lower(string1))
