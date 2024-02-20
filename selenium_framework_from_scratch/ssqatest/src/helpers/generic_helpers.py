
import random
import string
import logging as log


def generate_random_email_pwd(domain=None, email_prefix=None):
    if not domain:
        domain = 'gmail.com'
    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))

    email = email_prefix + '_' + random_string + '@' + domain
    log.info(f'Generated random email ---> {email}')

    random_pwd_length = 12
    random_pwd = ''.join(random.choices(string.ascii_letters, k=random_pwd_length))

    return email, random_pwd


def generate_random_chars():
    random_email_string_length = 5
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    return random_string


def generate_address():
    street_number = generate_random_number()
    address = 'CALLE' + street_number + '#' + street_number + '-' + street_number
    log.info(f'Generated random email ---> {address}')
    return address


def generate_random_number():
    random_number_len = 10
    number_generated = ''.join(str(random.randint(0, 10)) for _ in range(random_number_len))
    return number_generated
