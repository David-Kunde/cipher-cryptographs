def encode():
    message = str(input('enter a message here to encode to SED: '))
    for i in list(message):
        encoded_character = [(chr((ord(i) << 8))) for i in list(message)]
    print('ENCODED: ', ''.join(encoded_character))


def decode():
    message = str(input('enter an SED encoded message here to decode: '))
    for i in list(message):
        decoded_character = [(chr((ord(i) >> 8))) for i in list(message)]
    print('DECODED: ', ''.join(decoded_character))


if __name__ == '__main__':
    # encode()
    decode()
    
#YOU MUST BE OBIDIENT TO SAVE THE COUNTRY!