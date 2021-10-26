def check_palindrome(value):
    """only give whole number as value"""
    try:
        value = int(value)
    except Exception:
        return False
    value = str(value)
    result = []
    for i, char in enumerate(value):
        if value[i] == value[-i - 1]:
            result.append(1)
        else:
            result.append(0)
    for i in result:
        if i != 1:
            return False
    else:
        return True


print(check_palindrome("12321"))
