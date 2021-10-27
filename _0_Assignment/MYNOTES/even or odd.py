"""Print even and odd no. between given No."""

def check_even(num):
    if num % 2 == 0 and num > 0:
        return True
    else:
        return False

while True:
    try:
        start_num = int(input("Enter starting range: "))
        end_num = int(input("Enter ending range: "))
        if start_num+1 < end_num:
            break
        else:
            print("Invalid Range!")
    except Exception as E:
        print("Enter a valid number!")
list_even = []
list_odd = []
for number in range(start_num, end_num):
    if check_even(number) is True:
        list_even.append(number)
    else:
        if number > 0:
            list_odd.append(number)

print(f"the even numbers b/w {start_num} and {end_num}".center(80, "-"))
print(f"the following {len(list_even)} number are even:")
for i, value in enumerate(list_even):
    print(f"{value}", end=" ")
print("\n")
print(f"the odd numbers b/w {start_num} and {end_num}".center(80, "-"))
print(f"the following {len(list_odd)} number are odd:")
for value in list_odd:
    print(value, end=" ")

