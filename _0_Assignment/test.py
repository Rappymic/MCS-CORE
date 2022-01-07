x = -436423487589437589734895723423423

if x<0:
    b = -1
else:
    b = 1

temp_str = str(x)[::-1]
temp_str = temp_str.rstrip('-')

temp_str = int(temp_str)*b
if -2**31 < temp_str < 2**31 -1:
    pass
else:
    temp_str = 0

print(temp_str)