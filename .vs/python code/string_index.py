mail = input("enter your email")

index = mail.index("@")
username = mail[:index]
domain = mail[index+1:]

print(f"your username is {username} and your domain is {domain}")
