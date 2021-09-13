#!/usr/bin/env bash

manage() {
	python3 manage.py "$@"
}

load() {
	python3 manage.py loaddata "$@"
}

API_APP="rgblent_api"

if [ "$1" == "migrations" ]; then
	rm -rf $API_APP/migrations
	rm db.sqlite3
	manage makemigrations
	manage migrate
else
	rm db.sqlite3
	manage migrate
fi

# add fixtures using load() => load foo bar baz
