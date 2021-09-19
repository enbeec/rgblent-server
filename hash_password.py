#!/usr/bin/env python3

if __name__ == "__main__":
    from utils.hash_password import hash_pbkdf2
    from django.conf import settings  # needed for hasing
    from sys import argv, stdout, stderr
    settings.configure()

    args = argv[1:]

    if args.__len__() < 2:
        stderr.write("please provide an input file")
        exit(1)

    passwords = args[1:]

    # prints a newline separated list of hashes given input args
    for i, plaintext in enumerate(args[:-1]):
        if i > 0:
            stdout.write("\n")
        stdout.write(
            hash_pbkdf2(plaintext.strip())
        )
