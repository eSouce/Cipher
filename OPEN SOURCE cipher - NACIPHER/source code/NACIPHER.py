def shift_letter(letter, shift):
    if letter.isalpha():
        return chr((ord(letter.upper()) - 65 + shift) % 26 + 65)
    return letter

def encode(message):
    result = ''
    position = 1
    for char in message:
        if char.isalpha():
            result += shift_letter(char, position)
            position += 1
    return result

def decode(message):
    result = ''
    position = 1
    for char in message:
        if char.isalpha():
            result += shift_letter(char, -position)
            position += 1
    return result

def main():
    print("=== Welcome to NACIPHER ===")
    while True:
        print("\n1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            msg = input("Enter message to encode: ")
            print("Encoded:", encode(msg))
        elif choice == '2':
            msg = input("Enter message to decode: ")
            print("Decoded:", decode(msg))
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
