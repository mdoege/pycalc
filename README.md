## PyCalc, a simple scientific calculator in PyGame

It works the same as the Python math module in interactive mode:

* This calculator uses binary, not decimal, so it has the usual rounding errors when comparing its results to a decimal calculator, e.g. for "0.1 + 0.2".
* The green buttons are for base conversion (hex/oct/bin) and entering numbers in other bases (0x, 0o, 0b).
* The trigonometric functions all input or output angles in rad of course, so use "rad" and "deg" to convert accordingly.
* "fah" and "cel" are Fahrenheit/Celsius conversion.
* The imaginary unit j has a button. Note that not all Python math functions work with imaginary numbers, e.g. "exp" does not but "**2" does. Also "abs" is useful for imaginary numbers, e.g. "abs(3+4j)" = 5.
* SCI displays the result in scientific notation, pressing "=" switches back to normal display.
* The "e" button has multiple functions: As a variable, it is 2.718… (see table below); it is also used for entering numbers in scientific notation, e.g. 2e18; and it is the hex digit that equals 14.
* You can get asin, acos, and atan by first typing "a" from the hex block and then sin/cos/tan.

The hex buttons (a to f) and "j" can also be used as these predefined variables (a, b) or constants:

| Button | Equals |
| ---    | ---    |
| a      | last computed answer |
| b      | next to last answer |
| c      | speed of light in m/s |
| d      | Avogadro constant, molecules per mole |
| e      | Euler's number 2.718… |
| f      | gravitational constant in m³/(kg s) |
| j      | astronomical unit (AU) in m |

![screenshot1](https://github.com/mdoege/pycalc/raw/master/pycalc.png "PyCalc screenshot")

### License

Public Domain / CC0

