import cipher

class AtbashCipher(cipher.Cipher):
  """Represents an Atbash cipher - a substitution cipher where the encrypted message 
  is obtained by looking up each letter and finding the corresponding letter in a 
  reversed alphabet.
  Attributes:
    _alphabet (str): string of the alphabet
    _cipherbet (str): string of the cipherbet
  Functions:
    _encrypt_letter(self, letter) - encrypts a letter 
    _decrypt_letter(self, letter) - decrypts a letter
  """

  def __init__(self):
    super().__init__()
    self._cipherbet = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

  def _encrypt_letter(self, letter):
    location = self._alphabet.find(letter)
    return self._cipherbet[location]

  def _decrypt_letter(self, letter):
    location = self._cipherbet.find(letter)
    return self._alphabet[location]