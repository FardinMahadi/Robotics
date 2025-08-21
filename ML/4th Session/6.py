num = input("Enter a number: ")
str_len = len(num)

for i in range(0, str_len // 2):
    if num[i] != num[str_len - i - 1]:
        print(f"{num} is not a palindrome ❌")
        exit()

print(f"{num} is a palindrome ✅")
