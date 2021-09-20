#!/usr/bin/env python3
from utils.hash_password import hash_pbkdf2


def hash_user(user_dict):
    # TODO play with typing my parameters
    if user_dict["model"] != "auth.user":
        return
    user_dict["fields"]["password"] = hash_pbkdf2(
        user_dict["fields"]["password"])


if __name__ == "__main__":
    from django.conf import settings  # needed for hasing
    from sys import argv, stderr
    import json

    settings.configure()
    fixture_paths = argv[1:]

    if fixture_paths.__len__() < 1:
        stderr.write("Please provide a fixture file.\n")
        exit(1)

    for path in fixture_paths:
        with open(path, 'r') as fixture_file:
            fixture = json.load(fixture_file)
            if type(fixture) == type([]):
                for user in fixture:
                    hash_user(user)
            elif type(fixture) == type({}):
                hash_user(fixture)
        with open(path, 'w') as fixture_file:
            json.dump(fixture, fixture_file, indent=2)
