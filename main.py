# Geoffrey Clark's Lab 6 encoder python file

# Joshua Gallardo's decoder

def encoder(password):
    encoded_password = ""
    for digit in password:
        shifted_digit = str((int(digit) + 3) % 10)
        encoded_password += shifted_digit
    return encoded_password


def decoder(encoder):
    my_dict = {"0": 7, "1": 8, "2": 9, "3": 0, "4": 1, "5": 2, "6": 3, "7": 4, "8": 5, "9": 6}
    result = ""
    for digit in encoder:
        my_array = my_dict[digit]
        result = result + str(my_array)
    return (result)


def main():
    encoded_password = ""
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("\nPlease enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            # run decoder here
            print("The encoded password is " + encoded_password + ", and the original password is " + decoder(
                encoded_password) + ".")
        elif option == "3":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
