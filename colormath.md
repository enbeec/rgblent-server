# My Notes on `python-colormath`

## Clamped RGB Values

Some colorspaces (like CIE spaces) are larger than RGB spaces. When converting from CIE to RGB, use `clamped_rgb_{r,g,b}` properties to avoid invalid values.

## Conversion

Some color conversions go through RGB space. By default `colormath` goes through sRGB space when converting and I have no plans to deviate from that yet.

## Color Information Handling

The frontend and backend communicate in RGB-as-a-hex-string in all cases **except:**
	
	- `/colors/info` which takes a hex string but returns other colorspace info

