import json
key_input = input("Enter the key (JSON format): ")
temp_key = json.loads(key_input)
key = {int(k): v for k, v in temp_key.items()}
def decryptor(encrypted_sequence):
    # Split the encrypted string by '/'
    encrypted_values = encrypted_sequence.strip("/").split("/")

    # Reverse the key dictionary: value -> ASCII code
    reverse_key = {v: k for k, v in key.items()}
    decrypted_chars = []

    for val in encrypted_values:
        try:
            num = int(val)
        except ValueError:
            raise ValueError(f"Invalid number format: {val}")

        ascii_code = reverse_key.get(num)
        if ascii_code is None:
            raise ValueError(f"Encrypted value {val} not found in key!")
        decrypted_chars.append(chr(ascii_code))

    return "".join(decrypted_chars)


salah=str(input("enter the encrypted sequence:"))
print("decrypted sucessfully!")
print("sequence:",decryptor(salah))
