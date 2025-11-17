def printOptions():
    print("Welcome to the message encoder!")

    options = """
    1: Tutorial
    2: Encode a message
    3: Decode a message
    4: See Examples
    5: Quit
    """
    print(options)

def tutorial():
    print("The message encoder is a simple xor encoder with two parts: The message and a 1 character key")
    print("The encoder then encodes every byte with the key, and shows the resulting encoded value")
    print("The decoder does the opposite: It decodes the string! (Given you have the key, of course)")

def encode():
    ct = input("Enter the sentence you want to encrypt")
    while True:
        key = input("Enter a 1 character key")
        if len(key) == 1:
            break
        print("I said 1 character!")
    

    
def grabInput():
    userInput = input()
    match userInput:
        case 1:
            tutorial()
        case 2:
            encode()
        case 3:
        case 4:
        case _:
            print("Invalid Input!")
