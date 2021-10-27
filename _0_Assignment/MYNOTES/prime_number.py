def check_prime(value):
    if value == 4:
        return False
    if value <= 0:
        return False
    for i in range(2,value // 2):
        if value % i == 0:
            return False
    else:
        return True
if __name__ == "__main__":
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

    list_prime = []
    for i in range(start_num, end_num):
        if check_prime(i) is True:
            list_prime.append(i)

    if len(list_prime) > 0:
        print(f"the prime number between {start_num} and {end_num} are:")
        for i in list_prime:
            print(i, end=" ")
    else:
        print(f"there are no prime number between {start_num} and {end_num}")

