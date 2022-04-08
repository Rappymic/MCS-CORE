import hashlib

string1 = 'this is python'

encode = string1.encode()

text = hashlib.sha512(encode)

print(text.hexdigest())