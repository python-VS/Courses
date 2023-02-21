import string
import random


lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
big_string = lower_case + upper_case + digits + symbols
run_pass = random.sample(big_string, 10)
password = ''.join(run_pass)

print(password)
