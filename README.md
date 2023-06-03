# Calculator
A **PEDMSA+LTR+IO** calculator with a simple pygame GUI.
----
#### BIG RED ALERT: This is the 'completed' version but it is subject to change. If there are any issues please create an issue in the section, in the case that you know what may be happening, please provide suggestions to improve the code and correct the issue. Thank you :)
#### Alert: If you want to, you may use the calculator without the given font but it may mess up the visuals (change all occurrences of 'digital-7.ttf' to None).

### Some Notes For The Tool:
- Brackets are included and work so long as all are matched properly, there must be an expression inside the bracket otherwise there will be an error.
- The calculator follows a PEDMSA+LTR+IO processing rule meaning that division is checked before subtraction and subtraction is checked before addition, it still goes left-to-right and inside-out so no need to worry about that.
- Using exponents: to do a power of a power you must specify whether it is (x^y)^x or x^(y^z) as LTR is used; if you wish to do a square root please convert the number to a fractional exponent.
- Turns long numbers (greater than 11 characters in length, including the dot for decimals) into scientific notation.
- Second page with more operators.
- // and % operators for cooler division (when using special divisions please make sure to use brackets as 20/5//4/2 reads as (20/5)//(4/2) as the regular division has a higher priority).
- Trigonometry functions and logarithim with base e, the base for the function cannot be changed.
- A +/- button to change the value from positive to negative and vica-versa.
- Fraction solution option (shows the values as a fraction if there is a '/' symbol in the equation).
