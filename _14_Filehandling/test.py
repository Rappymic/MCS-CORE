import requests
import json

url = "https://www.gov.uk/bank-holidays.json"
file = requests.get(url)
content = file.content
json_parsed = json.loads(content)
list_country = []
for keys in json_parsed.keys():
    list_country.append(keys)
event_list = json_parsed[list_country[0]]['events']
year_list = []
for i in event_list:
    year_list.append(i['date'])
temp_year = [item[:4] for item in year_list]
string1 = str(temp_year)
years = set(temp_year)
years = list(years)
years.sort()
print(list_country[0])
for i in years:
    print(f"The holidays in {i} is {string1.count(i)}")
