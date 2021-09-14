#!/usr/bin/env bash

API_APP="rgblent_api"

retry_with_migrations() {
	# execute again with "migrations" argument
	./$0 migrations
	# and exit entirely with return code
	exit $?
}

manage() {
	python3 manage.py "$@"
}

load() {
	python3 manage.py loaddata "$@"
}

MIGRATIONS_DIR="${API_APP}/migrations"
PROTECTED_MIGRATIONS="__init__.py foo"

if [ "$1" == "migrations" ]; then
	find ${MIGRATIONS_DIR} -type f $(printf "! -name %s " ${PROTECTED_MIGRATIONS}) -exec rm {} +
	rm db.sqlite3
	manage makemigrations ${API_APP}
	manage migrate
else
	rm db.sqlite3
	manage migrate
fi

# if default colors won't load, try rebuilding migrations
load default_colors ||  retry_with_migrations
load users
load tokens
load palettes
