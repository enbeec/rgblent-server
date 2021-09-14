#!/usr/bin/env bash

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

API_APP="rgblent_api"

if [ "$1" == "migrations" ]; then
	# ONCE I FREEZE THE MODELS, THIS WILL CHANGE
	# TODO: a list of excluded migrations
	rm ${API_APP}/migrations/*.py
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
