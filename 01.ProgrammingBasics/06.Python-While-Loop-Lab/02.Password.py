username = input()
password = input()
try_password = input()

while try_password != password:
    try_password = input()
print(f'Welcome {username}!')
