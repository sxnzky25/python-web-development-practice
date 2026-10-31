print("==============================")
print("       LOGIN SYSTEM")
print("==============================")

username = "sean"
password = "12345"

user = input("Enter username: ")
passw = input("Enter password: ")

if user == username and passw == password:
    print("Login successful!")
else:
    print("Invalid username or password.")