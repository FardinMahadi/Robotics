import json

with open('data.json', 'r') as file:
    data = json.load(file)

inp_text = input("Enter a word: ")
query = inp_text.lower()

for i in range(len(data[query])):
    print(f"{i+1}. {data[query][i]}")