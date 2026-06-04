password = input("Enter the password :")

upper = 0
lower = 0
digit = 0
special = 0

for i in password:
    if i.isupper():
        upper = 1
        
        break
else:
    print("Does not contain capital letter")

for i in password:
    if i.islower():
        lower = 1
     
        break
else:
    print("Does not have small letter")

for i in password:
    if i.isdigit():
        digit = 1
        
        break
else:
    print("Does not have a digit")

if len(password) >= 8:
    print("")
else:
    print("Does not have 8 characters")

for i in password:
    if i == '!' or i == '"' or i == '#' or i == '$' or i == '%' or i == '&' or i == "'" or i == '(' or i == ')' or i == '*' or i == '+' or i == ',' or i == '-' or i == '.' or i == '/' or i == ':' or i == ';' or i == '<' or i == '=' or i == '>' or i == '?' or i == '@' or i == '[' or i == '\\' or i == ']' or i == '^' or i == '_' or i == '`' or i == '{' or i == '|' or i == '}' or i == '~':
        special = 1
        break
else:
    print("Does not contain special character")

if upper and lower and digit and special and len(password) >= 8:
    print("**********************")
    print("Strong Password")
    print("**********************")
else:
    print("Weak Password")
