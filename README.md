# RGBlent Backend

## Stack

- django
	- django-rest-framework
- python-colormath

## Setup Commands

- Run `init_database.sh` to ~~hear more about your car's extended warranty~~ initialize the database.

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
