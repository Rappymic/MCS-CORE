message = "This is a normal string"

def len_of_string(msg):
    return len(msg)

print(f"the length of '{message}' is".ljust(40, "-"), len_of_string(message))