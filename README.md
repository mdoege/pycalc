## PyCalc, a simple scientific calculator in PyGame

It works the same as the Python math module in interactive mode:

* This calculator uses binary, not decimal, so it has the usual rounding errors when comparing its results to a decimal calculator, e.g. for "0.1 + 0.2".
* The green buttons are for base conversion (hex/oct/bin) and entering numbers in other bases (0x, 0o, 0b).
* The trigonometric functions all expect rad of course.
* "fah" and "cel" are Fahrenheit/Celsius conversion.
* The imaginary unit j has a button. Note that not all Python math functions work with imaginary numbers, e.g. "exp" does not but "**2" does. Also "abs" is useful for imaginary numbers, e.g. "abs(3+4j)" = 5.
* SCI displays the result in scientific notation, pressing "=" switches back to normal display.
* The "e" button has multiple functions: As a variable, it is 2.718…; it is also used for entering numbers in scientific notation, e.g. 2e18; and it is the hex digit that equals 14.

![screenshot1](https://github.com/mdoege/pycalc/raw/master/pycalc.png "PyCalc screenshot")

### License

Public Domain / CC0

