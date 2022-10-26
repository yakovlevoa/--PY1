from random import sample


def get_random_password(q=8) -> str:
    l = 'qwertyuiopasdfghjklzxcvbnm'
    letters = [l for l in l]
    LETTERS = [l.upper() for l in l]
    digits = [str(d) for d in range(10)]
    alphabet = letters + LETTERS + digits
    password = ''.join(sample(alphabet, q))
    return password


print(get_random_password())
