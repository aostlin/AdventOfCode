import math

def parse_input(file_path):
    secrets = []
    with open(file_path, 'r') as file:
        for line in file:
            secrets.append(int(line.replace('\n', '')))
    return secrets


def task1(secrets):

    last_secret = []

    for secret_number in secrets:
        i = 0
        while i < 2000:
            secret_number = generate_secret_number(secret_number)
            i += 1
        last_secret.append(secret_number)

    return sum(last_secret)


def generate_secret_number(secret_number):
    secret_number = prune(mix(secret_number * 64, secret_number))
    secret_number = prune(mix(math.floor(secret_number / 32), secret_number))
    secret_number = prune(mix(secret_number * 2048, secret_number))
    return secret_number


def mix(a, b):
    return a ^ b


def prune(a):
    return a % 16777216


if __name__ == "__main__":

    secret_numbers = parse_input('./input.dat')

    print(task1(secret_numbers))