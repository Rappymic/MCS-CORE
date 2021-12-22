from itertools import permutations
n = 5
input = ("( " * n) + (") " * n)
in_list = [f for f in input.split(" ") if f]
possible_combinations = list(permutations(in_list, n*2))
valid_list = []
print(in_list)
def ret_valid(el):
    num_open = num_close = 0
    for val in el:
        if val == "(":
            num_open += 1
        else:
            num_close += 1
        if num_close > num_open:
            return False
    return True

for el in possible_combinations:
    if ret_valid(el):
        if "".join(el) not in valid_list:
            valid_list.append("".join(el))
print(", ".join(valid_list))