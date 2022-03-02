str1 = '00009400.000168.00034.00043/24'

def ret_ip_address(s : str):
    l1 = s.split('.')
    l2 = l1[-1].split('/')
    del l1[-1]
    l1 = l1 + l2
    print(l1)
    l2 = []
    for i in l1:
        l2.append(i.lstrip('0'))
    return (f'{l2[0]}.{l2[1]}.{l2[2]}.{l2[3]} Mask = {l2[4]}')


print(ret_ip_address(str1))