import abc

class Cipher(abc.ABC):
  """Represents an abstract class for ciphers.
  Attributes: 
    _alphabet (str): string of the alphabet"""
  
  def __init__(self):
    """Initializes the alphabet attribute."""
    self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
  def encrypt_message(self, message):
    """Converts the message to upper case letters, then encrypts the message."""
    message = message.upper()
    encrypted = ""
    for letter in message:
      if letter in self._alphabet:
        encrypted += self._encrypt_letter(letter)
      else:
        encrypted += letter
    return encrypted
    
  def decrypt_message(self, message):
    """Converts the message to upper case letters, then decrypts the message."""
    message = message.upper()
    decrypted = ""
    for letter in message:
      if letter in self._alphabet:
        decrypted += self._decrypt_letter(letter)
      else:
        decrypted += letter
    return decrypted

  """abstract methods for encrypt and decrypt"""
  @abc.abstractmethod
  def _encrypt_letter(self, letter):
    pass

  @abc.abstractmethod
  def _decrypt_letter(self, letter):
    pass