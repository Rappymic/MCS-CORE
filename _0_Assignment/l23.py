def numSteps(s: str) -> int:
    a = int(s, 2)

    def check_prime(no):
        if no % 2 == 0:
            return True
        else:
            return False

    count = 0
    while a != 1:
        count += 1
        if check_prime(a) == True:
            a = a / 2
        else:
            a = a + 1
    return count

a = "1111011110000011100000110001011011110010111001010111110001"
print(int(a,2))
print(numSteps(a))