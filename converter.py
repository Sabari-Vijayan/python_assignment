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

user_number = (input("What is your number"))

def repeated_divmod(no, divisor):
    
    no = int(no)

    if no==0:
        return []

    quotient, remainder = divmod(no, divisor)
    return repeated_divmod(quotient, divisor) + [remainder]

def repeated_divmod_hex(no, divisor):
    
    no = int(no)

    if no==0:
        return []

    quotient, remainder = divmod(no, divisor)

    if(remainder > 9):
        match remainder:
            case 10:
                return repeated_divmod_hex(quotient, divisor) + ["A"]
            case 11:
                return repeated_divmod_hex(quotient, divisor) + ["B"]
            case 12: 
                return repeated_divmod_hex(quotient, divisor) + ["C"]
            case 13:
                return repeated_divmod_hex(quotient, divisor) + ["D"]
            case 14:
                return repeated_divmod_hex(quotient, divisor) + ["E"]
            case 15:
                return repeated_divmod_hex(quotient, divisor) + ["F"]

    return repeated_divmod_hex(quotient, divisor) + [remainder]


def DtoB(no):
    return "".join(map(str, repeated_divmod(no, 2)))

def DtoO(no):
    return "".join(map(str, repeated_divmod(no, 8)))

def DtoHex(no):
    return "".join(map(str, repeated_divmod_hex(no, 16)))

def AnyToDecimal(no, base):
    # Ensure it's a string for slicing
    no = str(no).upper()
    
    if not no:
        return 0

    # For Hex, we need to convert letters back to numbers
    hex_digits = "0123456789ABCDEF"
    digit_value = hex_digits.index(no[0]) 

    power = len(no) - 1
    
    # Logic: (digit * base^power) + recursive call for rest of string
    return (digit_value * (base ** power)) + AnyToDecimal(no[1:], base)

def BinarytoOandHex(no, groupbits):
    if not no:
        return "0"

    # 1. Ensure 'no' is the string we work with
    binary_str = str(no)

    # 2. Padding: This MUST happen before the loop
    remainder = len(binary_str) % groupbits
    if remainder > 0:
        binary_str = "0" * (groupbits - remainder) + binary_str

    result = ""
    hex_digits = "0123456789ABCDEF"

    # 3. Slice the PADDED string
    for i in range(0, len(binary_str), groupbits):
        group = binary_str[i : i + groupbits]
        
        # Convert group to a decimal value
        val = AnyToDecimal(group, 2)

        # 4. Map the value to the correct Hex/Octal character
        # (This handles 10 -> 'A', 11 -> 'B', etc.)
        result += hex_digits[val]

    return result

def OtoBandHex(no, base):

    decimal_value = AnyToDecimal(no, base)
    return DtoB(decimal_value)

def OtoHex(no):
    decimal = AnyToDecimal(no, 8)
    return DtoHex(decimal)

def HextoO(no):
    decimal = AnyToDecimal(no, 2)
    return DtoO (decimal)

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

        case(2,1):
            print("\nConverting from Binary to Decimal\n")
            print(AnyToDecimal((str(no)), 2))

        case(2,3):
            print("\nConverting from Binary to Octal\n")
            print(BinarytoOandHex(no, 3))

        case(2,4):
            print("\nConverting from Binary to Hexa-Decimal\n")
            print(BinarytoOandHex(no, 4))

        case(3,1):
            print("\nConverting from Octal to Decimal\n")
            print(AnyToDecimal((str(no)), 8))

        case(3,2):
            print("\nConverting from Octal to Binary\n")
            print(OtoBandHex((str(no)), 8))

        case(3,4):
            print("\nConverting from Octal to Hexa-Decimal\n")
            print(OtoHex((str(no))))

        case(4,1):
            print("\nConverting from Hexa-Decimal to Decimal\n")
            print(AnyToDecimal((str(no)), 16))

        case(4,2):
            print("\nConverting from Hexa-Decimal to Binary\n")
            print(OtoBandHex((str(no)), 16))

        case(4,3):
            print("\nConverting from Hexa-Decimal to Octal\n")
            print(HextoO(no))

        case _:
            print("\nError\n")
            exit()

convert(first_number, second_number, user_number)






