import random
import string
a, b, c = string.digits, string.ascii_uppercase, string.ascii_lowercase
d = a + b + c
def get_random_password(n = 8) -> str:
    password_list = random.sample(d, n)
    password = ''.join(password_list)
    return password

print(get_random_password(10))
