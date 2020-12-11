def random_string(str_len):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(str_len))