# Name - Krisha Hemani
#      - Justin Ha
# Program - Practice
# Date - 03/14/2024
# Module 7 - Secret Decoder Ring
# Purpose - create a secret decoder ring that allows the user to encode and decode messages using different types of encryption.

import atbash
import caesar_cipher
import check_input


def main():
  """Main Function"""
  while True:
    message_type = check_input.get_int_range(
        "Secret Decoder Ring:\n1. Encrypt\n2. Decrypt \n", 1, 2)
    #Encypting a message
    if message_type == 1:
      cipher_type = check_input.get_int_range(
          "Enter encryption type:\n1. Atbash\n2. Caesar \n", 1, 2)
      message = input("Enter message: ")
      if cipher_type == 1:
        b = atbash.AtbashCipher()
        encrypted_message = b.encrypt_message(message)
      elif cipher_type == 2:
        c = caesar_cipher.CaesarCipher(
            check_input.get_int_range("Enter shift value: ", 0, 25))
        encrypted_message = c.encrypt_message(message)
      with open("message.txt", "w") as file:
        file.write(encrypted_message)
      print("Encrypted message saved to \"message.txt\".")
    #Decrypting a message
    elif message_type == 2:
      cipher_type = check_input.get_int_range(
          "Enter decryption type:\n1. Atbash\n2. Caesar \n", 1, 2)
      if cipher_type == 1:
        b = atbash.AtbashCipher()
        with open("message.txt", "r") as file:
          message = file.read()
        decrypted_message = b.decrypt_message(message)
      elif cipher_type == 2:
        c = caesar_cipher.CaesarCipher(
            check_input.get_int_range("Enter shift value: ", 0, 25))
        with open("message.txt", "r") as file:
          message = file.read()
        decrypted_message = c.decrypt_message(message)
      print("Reading encrypted message from \"message.txt\".")
      print("Decrypted message:", decrypted_message)
      break


main()
