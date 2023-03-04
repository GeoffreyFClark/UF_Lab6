#  Geoffrey Clark's Decoder for Lab 6

def decoder(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        unshifted_digit = str((int(digit)-3) % 10)
        decoded_password += unshifted_digit
    return decoded_password

