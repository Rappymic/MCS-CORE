from time import time


def check_2power(num: int):
    if num == 2 or num == 1:
        return True 
    if int(str(num)[-1])%2 !=0:
        return False
    check_no = 2
    while check_no < num:
        check_no *=2
        if check_no == num:
            return True
    return False


start_time = time()
print(check_2power(1))
final_time = time() -start_time
print(final_time)