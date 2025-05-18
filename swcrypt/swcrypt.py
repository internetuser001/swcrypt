import subprocess
import sys

# Print the banner at start
print("""
                                             __   
  ________  _  __ ___________ ___.__._______/  |_ 
 /  ___/\ \/ \/ // ___\_  __ <   |  |\____ \   __\\
 \___ \  \     /\  \___|  | \/\___  ||  |_> >  |  
/____  >  \/\_/  \___  >__|   / ____||   __/|__|  
     \/              \/       \/     |__|         
                                                             
                --- credit:@internetuser001 ---                       
""")

print("Choose an option:")
print("1 — Encryption")
print("2 — Decryption")

choice = input("Enter 1 or 2: ").strip()

if choice == "1":
    subprocess.run([sys.executable, "encryptor.py"])
elif choice == "2":
    subprocess.run([sys.executable, "decryptor.py"])
else:
    print("Invalid choice.")
