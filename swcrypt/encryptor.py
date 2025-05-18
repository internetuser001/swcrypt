from random import *
import json

bla = int(input("1: key generation — 2: stable key use: "))

if bla == 1:
    key = {i: randint(0, 10**20) for i in range(2, 127)}
    json_key = json.dumps({str(k): v for k, v in key.items()})
    print("This is the key (save it!):")
    print(json_key)

elif bla == 2:
    key_input = input("Enter the key (JSON format): ")
    temp_key = json.loads(key_input)
    key = {int(k): v for k, v in temp_key.items()}

else:
    raise ValueError("Invalid choice.")

# --- Encryptor ---
def encryptor(sequence):
    sequence = str(sequence)
    final = ""
    for p in sequence:
        final += str(key[ord(p)]) + "/"
    return final

salah = input("Enter the sequence: ")
print("Encrypted:")
print(encryptor(salah))

        
    
    
    
    
    