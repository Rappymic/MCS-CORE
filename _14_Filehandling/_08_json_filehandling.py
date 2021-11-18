import json

with open(r'file1.json', 'r') as f:
    fread = json.load(f)  # converting to json to python dictionary
    print(fread['phoneNumbers'][0]['number'])
    print(fread)
f.close()

with open('file2.json', 'w') as f:
    di = {'name': 'shiva', 'age': 26, 'course': 'python', 'contact': ['shiva@gmail.com', 64613]}
    json.dump(di, f, indent=4)
f.close()



