import cipher

class CaesarCipher(cipher.Cipher):
  """Represents a Caesar Cipher - a substitution cipher where the encrypted message 
  is shifted by a certain number of letters.
  Attributes:
    _alphabet (str): string of the alphabet
    _shift (int): number of letters to shift
  Functions:
    _encrypt_letter(self, letter) - encrypts a letter by shifting it by the shift value
    _decrypt_letter(self, letter) - decrypts a letter by shifting it back by the shift value"""

  def __init__(self, shift):
    """Initializes the alphabet attribute."""
    super().__init__()
    if not (0 <= shift <= 25):
      raise ValueError("Value must be between 0 and 25.")
    else:
      self._shift = shift
    

  def _encrypt_letter(self, letter):
    """Encrypts a letter."""
    location = self._alphabet.find(letter)
    location = (location + self._shift) % 26
    return self._alphabet[location]

  def _decrypt_letter(self, letter):
    """Decrypts a letter."""
    location = self._alphabet.find(letter)
    location = (location - self._shift) % 26
    return self._alphabet[location]