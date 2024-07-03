#advanced random password generator using python
import random
from string import punctuation, ascii_letters, digits

symbols = punctuation + ascii_letters + digits

secured_random = random.SystemRandom()

password = " ".join(secured_random.choice(symbols) for i in range(1, 10))
print(password)