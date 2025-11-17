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
    ct = input("Enter the sentence you want to encrypt:\n")
    while True:
        key = input("Enter a 1 character key:\n")
        if len(key) == 1:
            break
        print("I said 1 character!")
    enc = list(ct)
    for i in range(len(enc)):
        enc[i] = chr(ord(enc[i]) ^ ord(key))
    print(f"Encoded message: {b''.join([s.encode() for s in enc])}")
    
def decode():
    enc = input("Enter the encoded values exactly as formatted before, minus the b'' part! \n")
    ba = bytearray(enc.encode("utf-8").decode("unicode_escape").encode("latin-1"))
    key = input("Enter your 1 character key.\n")
    for i in range(len(ba)):
        ba[i] ^= ord(key)
    print(bytes(ba))

def showExamples():
    print("Encode: hello, key = 'a' -> b'\\t\\x04\\r\\r\\x0e'")
    print("Decode: \\t\\x04\\r\\r\\x0e, key = 'a' -> b'hello'\n")

    print("Encode: tillyctf is the best event ever to be hosted, key = 8 -> b'LQTTA[L^\\x18QK\\x18LP]\\x18Z]KL\\x18]N]VL\\x18]N]J\\x18LW\\x18Z]\\x18PWKL]\\\\'")
    print('Decode LQTTA[L^\\x18QK\\x18LP]\\x18Z]KL\\x18]N]VL\\x18]N]J\\x18LW\\x18Z]\\x18PWKL]\\\\, key = 8 -> b\'tillyctf is the best event ever to be hosted\'')

def grabInput():
    userInput = input()
    match userInput:
        case '1':
            tutorial()
        case '2':
            encode()
        case '3':
            decode()
        case '4':
            showExamples()
        case _:
            print("Invalid Input!")


while True:
    printOptions()
    grabInput()
    