# Geoffrey Clark's Lab 6 encoder python file

# import Joshua Gallardo's decoder

def encode(password):
    encoded_password = ""
    for digit in password:
        shifted_digit = str((int(digit) + 3) % 10)
        encoded_password += shifted_digit
    return encoded_password


def main():
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("\nPlease enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif option == "2":
            pass
            # run decoder here

        elif option == "3":
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
