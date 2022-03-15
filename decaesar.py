def encrypted(text, key):
    """Ceasarchifferskryptering
    
    Args: 
        text (_str_): Den text som ska krypteras.
        key (_int_): Hur många steg ska vi skifta?
    """

    encrypted = ""
    # loop through the message char by char
    for char in text:
        # check if it's an upper case letter
        if char.isupper():
            char_index = ord(char) - ord('A')

            #shift the current character by key positions
            char_shifted =  (char_index + key) % 26 + ord('A')
            char_new = chr(char_shifted)
            encrypted += char_new
        elif char.islower():
            char_index = ord(char) - ord('a')

            char_shifted = (char_index + key) % 26 + ord ('a')
            char_new = chr(char_shifted)
            encrypted += char_new

        elif char.isdigit():
            char_new = (int (char) + key) % 10
            encrypted += str(char_new)

        else:
            encrypted += char
    return encrypted

def main():
    message = input("What do you want to decrypt?")
    encrypted_message = encrypted(message, 1)
    print(f"Message: {message}")
    print(f"Encrypted message with 1 shift: {encrypted_message}")

if __name__ == "__main__":
    main()