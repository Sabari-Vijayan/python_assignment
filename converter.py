import string

print("Welcome to number type converter")
print("Here you can convert betwixt the given number bases\n")

choice = 0

def selection():

    choice = int(input("Choose from?\n1. Decimal\n2. Binary\n3. Octal\n4. Hexa-Decimal\n5. Exit\n\n"))

    match choice:
        case 1: 
            print("You chose Decimal number base\n")
            return 1 
        case 2:
            print("You chose binay number base\n")
            return 2 
        case 3:
            print("You chose Octal number base\n")
            return 3 
        case 4:
            print("You chose Hexa-Decimal number base\n")
            return 4
        case 5:
            print("You chose to exit\n")
            exit()
        case _:
            print("Default has been set to Decimal number base\n")
            return 1 

print("Chosse the base of the number you are going to convert\n")
first_number = int(selection())
print("Choose the base you want to convert into\n")
second_number = int(selection())

user_number = int(input("What is your number"))

def repeated_divmod(no, divisor):
    
    if no==0:
        return []

    quotient, remainder = divmod(no, divisor)
    return repeated_divmod(quotient, divisor) + [remainder]

def repeated_divmod_hex(no, divisor):
    
    if no==0:
        return []

    quotient, remainder = divmod(no, divisor)

    if(remainder > 9):
        match remainder:
            case 10:
                return repeated_divmod_hex(quotient, divisor) + "A"
            case 11:
                return repeated_divmod_hex(quotient, divisor) + "B"
            case 12: 
                return repeated_divmod_hex(quotient, dividor) + "C"
            case 13:
                return repeated_divmod_hex(quotient, divisor) + "D"
            case 14:
                return repeated_divmod_hex(quotient, divisor) + "E"
            case 15:
                return repeated_divmod_hex(quotient, divisor) + "F"

    return repeated_divmod_hex(quotient, divisor) + [remainder]


def DtoB(no):
    return "".join(map(str, repeated_divmod(no, 2)))

def DtoO(no):
    return "".join(map(str, repeated_divmod(no, 8)))

def DtoHex(no):
    return "".join(map(str, repeated_divmod_hex(no, 16)))

def convert(user, output, no):

    match (user, output):
  
        case(1,2):
            print("\nConverting from Decimal to Binary\n")
            print(DtoB(no))

        case(1,3):
            print("\nConverting from Decimal to Octal\n")
            print(DtoO(no))

        case(1,4):
            print("\nConverting from Decimal to Hexa-Decimal\n")
            print(DtoHex(no))

        case _:
            print("\nError\n")
            exit()

convert(first_number, second_number, user_number)






