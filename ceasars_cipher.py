import string

def encode(letter):

    letter = letter.upper()

    position = ord(letter)-64 

    new_position = position%26

    new_letter = chr((new_position+3)+64)

    return (new_letter)

def decode(letter):

    letter = letter.upper()

    position = ord(letter)-64 

    new_position = position%26

    new_letter = chr((new_position-3)+64)

    return(new_letter)

def encoder(string):

    string_length = len(string)
    
    words = []
    encoded_sentence=[]

    words=string.split(" ")
    
    for i in range(0, len(words)):

        letters=[]
        letters = list(words[i])

        encoded_letters=[]

        for j in range(0, (len(letters))):

            new_letter = encode(letters[j])
            encoded_letters.append(new_letter)

        finished_word = "".join(encoded_letters)

        encoded_sentence.append(finished_word)

    final_encoded = " ".join(encoded_sentence)
    print(final_encoded)

    return final_encoded

def decoder(string):

    string_length = len(string)
    
    words = []
    encoded_sentence=[]

    words=string.split(" ")
    
    for i in range(0, len(words)):

        letters=[]
        letters = list(words[i])

        encoded_letters=[]

        for j in range(0, (len(letters))):

            new_letter = decode(letters[j])
            encoded_letters.append(new_letter)

        finished_word = "".join(encoded_letters)

        encoded_sentence.append(finished_word)

    final_encoded = " ".join(encoded_sentence)
    print(final_encoded)

    return final_encoded

def main_menu():
    while True:
        print("\n1. Encode\n2. Decode\n3. Exit\n")

        choice = input("what is youe option")

        match choice:
            case "1":
                text = input("Please enter the text to be encoded\n")
                print("\nEncoding\n")
                encoded_text = encoder(text)

                decode_now = int(input("\nDo you also want to decode the text, press 1 for yes\n"))

                if(decode_now==1):
                    decoder(encoded_text)

            case "2":
                text = input("Please enter the text to be encoded\n")
                print("\nDecoding\n")
                decoder(text)
            case "3":
                print("\nGoodBye\n")
                break;
            case _:
                print("\nINVALID\n")


main_menu()





"""
new_letter = encode(letter)
print(new_letter)
new_letter = decode(new_letter)
print(new_letter)
"""
