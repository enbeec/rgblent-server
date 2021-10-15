# RGBlent Backend

## Setup Commands

- Run `init_database.sh` to ~~hear more about your car's extended warranty~~ initialize the database.
	- if loading the default colors fails migrations are reset
	- you can explicitly ask for migrations to be reset by passing the `migrations` argument
	- read the script for more details

- Handling new migrations
	1) add the filename(s) of the new migrations to `init_database.sh`
	2) add the (negated) filename to .gitignore
	3) don't forget to commit these changes as well as the migrations!

- Working with the docs
	1) Javascript dependencies: `npm install --global apidoc serve`
	2) Build the docs: `apidoc -i ./rgblent_api/views -f .py -o docs/`
	3) Serve the docs: `cd docs; serve`


## Tricks

### Easy color fixture data using Vim

Color fixtures expect an unsigned, 8-bit integer (0-255) despite many of us using hex bytes (00-FF) to remember red, green and blue values. To use familiar hex values, simply create your `red`, `green` and `blue` fields like this:

```json
	...
	"red": 0xff,
	"green": 0x12,
	"blue": 0x34,
	...
```

and then run the following command *(hit ":" from NORMAL mode and then type the following)*: 

```
%s|0x..|\=printf("%d", submatch(0))
```

**TODO:** check to see if this works in VS Code Vim

## Stack

Python:
- django
	- django-rest-framework
- python-colormath

JavaScript:
- apidoc
- serve 
