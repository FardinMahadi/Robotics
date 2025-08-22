import difflib
import json

with open('data.json', 'r') as file:
    data = json.load(file)

inp_text = input("Enter a word: ")
query = inp_text.lower()

matched = difflib.get_close_matches(query, data.keys(), n=5, cutoff=0.6)

if not matched:
    print("No matches found.")
elif len(matched) == 1:
    key = matched[0]
    print(f"Results for '{key}':")
    for i, value in enumerate(data[key], 1):
        print(f"{i}. {value}")
else:
    print("\nWhich word did you mean?")
    print("ID Word/s\n")
    for idx, key in enumerate(matched, 1):
        print(f"{idx}. {key}")
    try:
        print("\nType 0 if word not here.")
        selected = int(input("Type ID: "))
        if selected == 0:
            print("You entered a word that is not in the dictionary.")
        elif 1 <= selected <= len(matched):
            chosen_key = matched[selected - 1]
            print(f"\nResults for '{chosen_key}':")
            for i, value in enumerate(data[chosen_key], 1):
                print(f"{i}. {value}")
        else:
            print("Invalid ID. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")