import json

f = open('test.json')

data = json.load(f)



print(data[0]["LINK"])
# number is which json dictionary to look, link is our keyword and is CASE SENSITIVE

f.close()