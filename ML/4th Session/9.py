def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

inp_text = input("Enter your life password: ")
shift_val = int(input("Enter a number to shift your code: "))

encrypted_code = encrypt(inp_text, shift_val)
decrypted_code = decrypt(encrypted_code, shift_val)

print(f"Encrypted code: {encrypted_code}")
print(f"Decrypted code: {decrypted_code}")