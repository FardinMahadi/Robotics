inp_str = input("Enter a string: ")
result = ""

for ch in inp_str:
    if ch.islower():
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)