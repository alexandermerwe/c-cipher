try:
    import pyperclip # pyperclip copies text to the clipboard.
except:
    pass # If pyperclip isn't installed, do nothing.

# Introduction and explanation of program to user:
print('Caesar Cipher is a program that encrypts/decrypts a message from the user.')
print('A key is used to shift up each letter\'s position in the alphabet ')
print('by a number provided (from 0 to 25).')
print('The shifted sequence will be the now encrypted message, ready for decryption')
print()

# All possible symbols that can be encrypted/decrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Let the user decide if they want to encrypt/decrypt:
while True: # Keep asking until the user enters e or d.
    response = input('Would you like to (e)ncrypt or (d)ecrypt?: ').lower() # The response will be forced lowercase
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter (e)ncrypt or (d)ecrypt.')

# Let the user enter the key to use:
while True: # Keep asking until the user enters a valid key.
    maxKey = len(SYMBOLS) - 1 # The maximum number that can be inputted
    key = input('Enter a key (from 0 to {}) to use: '.format(maxKey))
    if not key.isdecimal():
        continue
    
    if 0 <= int(key) <= maxKey:
        key = int(key)
        break

# Let the user enter the message to encrypt/decrypt:
message = input('Enter the message to {}: '.format(mode))

# Caesar Cipher only works on uppercase letters since [SYMBOLS] is all uppercase:
message = message.upper()

# Stores the encrypted/decrypted form of the message:
translated = '' # Leave empty for use later

# Encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
        # Get the encrypted/decrypted number for this symbol.
        num = SYMBOLS.find(symbol) # Get the number of the symbol in [SYMBOLS].
        if mode == 'encrypt':
            num = num + key # We add our key for encrypting
        elif mode == 'decrypt':
            num = num - key # We subtract our key for decrypting

        # Handle the wrap-around if [num] >= len(SYMBOLS) or if [num] < 0.
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # Add encrypted/decrypted number's symbol to translated:
        translated = translated + SYMBOLS[num]
    else:
        # Just add symbol without encrypting/decrypting:
        translated = translated + symbol # In the case of punctuation etc.

# Display the encrypted/decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard'.format(mode))
except:
    pass # Do nothing if pyperclip wasn't installed