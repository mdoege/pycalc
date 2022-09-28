## PyCalc, a collection of simple calculators in PyGame

Three scientific calculators (using binary internally):

    pycalc_light, pycalc_dark, pycalc_lcars

Four-function calculator (using decimal internally, based on Python's *decimal* module):

    pycalc_desk

The **decimal calculator** is useful to avoid the rounding errors of the binary calculators due to their decimal➜binary➜decimal conversions, which is better for e.g. financial calculations. It also has memory (M+ to add, MR to recall value, AC to clear) and the comma is used as a decimal separator in results.

The **scientific calculators** work the same as the Python math module in interactive mode:

* They use binary numbers internally, not decimal, so it has the usual rounding errors when comparing its results to a decimal calculator, e.g. "0.1 + 0.2" does not evaluate to exactly 0.3.
* The green buttons are for base conversion (hex/oct/bin) and entering numbers in other bases (0x, 0o, 0b).
* The trigonometric functions all input or output angles in rad of course, so use "rad" and "deg" to convert accordingly.
* "fah" and "cel" are Fahrenheit/Celsius conversion. E.g. "cel(100)" converts 100°F to Celsius. They also demonstrate how to add custom functions to the calculator.
* The imaginary unit j has a button. Note that not all Python math functions work with imaginary numbers, e.g. "exp" does not but "**2" does. Also "abs" is useful for imaginary numbers, e.g. "abs(3+4j)" = 5.
* SCI displays the result in scientific notation, pressing "=" switches back to normal display.
* The "e" button has multiple functions: As a variable, it is 2.718… (see table below); it is also used for entering numbers in scientific notation, e.g. 2e18; and it is the hex digit that equals 14.
* You can get asin, acos, and atan by first typing "a" from the hex block and then sin/cos/tan.

### Physical constants

The hex buttons (a to f) and "j" can also be used as these predefined variables (a, b) or constants:

| Button | Equals |
| ---    | ---    |
| a      | last computed answer |
| b      | next-to-last answer |
| c      | speed of light in m/s |
| d      | Avogadro constant, molecules per mole |
| e      | Euler's number 2.718… |
| f      | gravitational constant in m³/(kg s) |
| j      | astronomical unit (AU) in m |

### Screenshots

![screenshot1](pycalc.png "PyCalc screenshot (dark/light versions)")

![screenshot2](pycalc2.png "PyCalc screenshot (LCARS version)")

![screenshot3](pycalc3.png "PyCalc screenshot (decimal version)")

### License

Public Domain / CC0

### Typeface credits

* *Digital-7 Mono* by Sizenko Alexander
* *Antonio* by Vernon Adams
* *Fixedsys Excelsior 2.00* by Darien Valentine
* *OCRA* by Matthew Skala
