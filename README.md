# RGBlent Backend

## Demo Version

There is a demo version of this app available on the branch vc_demoday (same story with the backend repo). It is the result of me hacking together the last bits of my app just in time to present it. Code-wise it's not terrible but it's both below my personal standards and too big to commit all at once. Here's a summary of the changes between main (as of commit cc2486f) and the vc_demoday branch:

- `rgblent/urls.pyh`
  - from `rgblent_api.models`
    - imported PaletteView
    - imported color_blend
  - registered `PaletteView` with the router
  - added `color_blend` to urls
- `rgblent_api/fixtures/{users,tokens}.json`
  - added a user for Val *(that's me!)*
  - added a token for Val
- `rgblent_api/fixtures/{palettes,user_colors}.json`
  - Val has a copy of the default palette
  - Val has a copy of the default colors
- `rgblent_api/views`
  - `__init__.py`
    - exported `color_blend`
    - exported `PaletteView`
  - `color.py`
    - importing `colorblend` from utils *(the naming of this utility doesn't match `color_info` and I will address that)*
    - `id` is now a field in the `ColorSerializer`
    - added a `UserColorSerializer` with `color` (`ColorSerializer`) and `label` fields
    - added `favorite` POST detail action to the `ColorView` *(there seems to be a duplicate in `user.py`)* 
    - added `color_blend` POST view with `AllowAny` permissions
  - `palette.py`
    - import `get_user_model`
    - import `Color` model
    - import `rgb_hex__int_tuple`
    - added `id` field to `PaletteSerializer`
    - added `PaletteView` with list and create views
  - `user.py`
    - import `Color` model
    - import serialziers from `.color`
    - import `rgb_hex__int_tuple`
    - added `favaorite` POST action to `ProfileView` *(there seems to be a duplicate in `color.py`)*
- `utils/color.py`
  - added an `average` helper function
  - added a `colorblend` utility function (uses `average`)

Most of this just needs a once over and some docstrings. Renaming, deduplicating and light refactoring along the way as I commit it a chunk at a time. Until I have that time, I will probably just run `vc_demoday` for testing. If that makes it into `main` on the client repo I'll mention it there.
    
## Stack

- django
	- django-rest-framework
- python-colormath

## Setup Commands

- Run `init_database.sh` to ~~hear more about your car's extended warranty~~ initialize the database.
	- if loading the default colors fails migrations are reset
	- you can explicitly ask for migrations to be reset by passing the `migrations` argument
	- read the script for more details

- Handling new migrations
	1) add the filename(s) of the new migrations to `init_database.sh`
	2) add the (negated) filename to .gitignore
	3) don't forget to commit these changes as well as the migrations!

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
