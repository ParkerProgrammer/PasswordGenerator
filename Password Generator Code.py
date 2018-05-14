# Impots librarys
import string
import random

#Creates empty lisst
password = [ ]

#Generates random letter
ranLet = random.choice(string.ascii_letters)

#Creates a random number
ranNum = (random.randint(7,14))

# Generates password
def generatePassword():
    for i in range(0, ranNum):
        code = random.choice(string.ascii_uppercase + string.digits + string.ascii_letters)
        password.append(code)
        charRemove(password)
        # Tests that there is upper case and lower case characters & digits
        rules = [lambda password: any(x.isupper() for x in password),
        lambda password: any(x.islower() for x in password),
        lambda password: any(x.isdigit() for x in password),
        ]
    if all(rule(password) for rule in rules):
        print("PASS: Password contains upper case and lower case characters & digits")
        return password
    else:
        del password[:]
        generatePassword()

# Removes duplicate characters
def charRemove(password):
    p = 1
    for i in range (len(password)-1):
        if password[i] == password[p].lower() or password[i] == password[p].upper() or password[i] == password[p]:
            password.remove(password[p])
            password.append(ranLet)
            # Extra failsafe
            if password[i] == password[p].lower() or password[i] == password[p].upper() or password[i] == password[p]:
                password.remove(password[p])
                password.append(ranLet)
        p+=1
        if p > (len(password)):
            return password

# Validates Password
def validatePassword(password):
    length = len(password)
    password.isalnum()
    # Tests that password is correct length
    if length >=7 <= 14:
        print("PASS: Password is in correct length")
    else:
        print("FAIL: Password is not in correct length")
    # Tests that password only contain alphanumeric characters 
    if password.isalnum() == True:
        print("PASS: Password only contains alphanumeric characters")
    else:
        print("FAIL: Password does not only contain alphanumeric characters")
    # Tests there are no duplicates
    p = 1
    for i in range (len(password)-1):
        if password[i] == password[p].lower() or password[i] == password[p].upper() or password[i] == password[p]:
            print(password[i])
            print(password[p])
            print("FAIL: Duplicates found")
        p+=1
        if p > (len(password)):
            print("PASS: No duplicates found")
            return password
        else:
            print("PASS: No duplicates found")
            return password

# Generates password 
generatePassword()

#Turns password into string
password = ''.join(password)

# Makes sure password is secure and then displays it
print(validatePassword(password))


