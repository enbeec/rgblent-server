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
	# ONCE I DEPLOY THIS I WILL NOT HANDLE THINGS THIS CRUDELY
	rm -rf ${API_APP}/migrations
	rm db.sqlite3
	manage makemigrations ${API_APP}
	manage migrate
else
	rm db.sqlite3
	manage migrate
	# if default colors won't load, try rebuilding migrations
	load default_colors ||  retry_with_migrations
fi

# add fixtures using load() => load foo bar baz

load users
load tokens
