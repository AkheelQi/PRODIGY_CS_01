def encrypt(text, shift):
    # Initialize an empty string to store the encrypted text
    encrypted_text = ""
    # Iterate through each character in the input text
    for char in text:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Calculate the shift amount within the range of the alphabet (0-25)
            shift_amount = shift % 26
            # Calculate the new character by shifting the ASCII value
            new_char = ord(char) + shift_amount
            # If the character is lowercase
            if char.islower():
                # Wrap around if the new character goes past 'z'
                if new_char > ord('z'):
                    new_char -= 26
                # Append the new character to the encrypted text
                encrypted_text += chr(new_char)
            # If the character is uppercase
            elif char.isupper():
                # Wrap around if the new character goes past 'Z'
                if new_char > ord('Z'):
                    new_char -= 26
                # Append the new character to the encrypted text
                encrypted_text += chr(new_char)
        else:
            # If the character is not an alphabet letter, leave it unchanged
            encrypted_text += char
    # Return the encrypted text
    return encrypted_text


def decrypt(text, shift):
    # Initialize an empty string to store the decrypted text
    decrypted_text = ""
    # Iterate through each character in the input text
    for char in text:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Calculate the shift amount within the range of the alphabet (0-25)
            shift_amount = shift % 26
            # Calculate the new character by shifting the ASCII value
            new_char = ord(char) - shift_amount
            # If the character is lowercase
            if char.islower():
                # Wrap around if the new character goes before 'a'
                if new_char < ord('a'):
                    new_char += 26
                # Append the new character to the decrypted text
                decrypted_text += chr(new_char)
            # If the character is uppercase
            elif char.isupper():
                # Wrap around if the new character goes before 'A'
                if new_char < ord('A'):
                    new_char += 26
                # Append the new character to the decrypted text
                decrypted_text += chr(new_char)
        else:
            # If the character is not an alphabet letter, leave it unchanged
            decrypted_text += char
    # Return the decrypted text
    return decrypted_text


def main():
    while True:
        # Prompt the user to choose encryption or decryption
        operation = input("Would you like to (e)ncrypt or (d)ecrypt a message? (e/d): ").lower()
        # Validate the user input
        if operation not in ['e', 'd']:
            print("Invalid choice. Please choose 'e' for encrypt or 'd' for decrypt.")
            continue

        # Prompt the user to enter the message
        message = input("Enter your message: ")
        # Prompt the user to enter the shift value
        shift = int(input("Enter the shift value: "))

        # Perform encryption if the user chose 'e'
        if operation == 'e':
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        # Perform decryption if the user chose 'd'
        else:
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")

        # Ask if the user wants to perform another operation
        another = input("Would you like to perform another operation? (y/n): ").lower()
        # Exit the loop if the user chooses 'n'
        if another != 'y':
            break


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
