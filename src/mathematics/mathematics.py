'''
author: Rodrigo Dal Ri
email: rodrigodalri1995@gmail.com
'''
import math

r = 2

circumference = 2 * math.pi * r
print(f"Circumference of a Circle = 2 * {math.pi:.4} * {r} = {circumference:.4}")

area = math.pi * r * r
print(f"Area of a Circle = {math.pi:.4} * {r} * {r} = {area:.4}")

circumference2 = math.tau * r
print(f"Circumference of a Circle = {math.tau:.4} * {r} = {circumference2:.4}")

euler = math.e
print(f"Eulers number = {euler:.4}")

infPos = math.inf
print(f"Positive Infinity = {infPos}")

infNeg = -math.inf
print(f"Negative Infinity = {infNeg}")

notanumber = math.nan
print(f"NaN = {notanumber}")

fat = math.factorial(7)
print(f"7! = {fat}")

print(f"Ceil of 4.23 = {math.ceil(4.23)}")
print(f"Ceil of -11.453 = {math.ceil(-11.453)}")

print(f"Floor of 5.532 = {math.floor(5.532)}")
print(f"Floor of -6.432 = {math.floor(-6.432)}")

print(f"Truncate of 12.32 = {math.trunc(12.32)}")
print(f"Truncate of -43.24 = {math.trunc(-43.24)}")

print(f"6 is close 7? (error=1.0) = {math.isclose(6, 7, abs_tol=1.0)}")
print(f"6 is close 7? (error=0.2) = {math.isclose(6, 7, abs_tol=0.2)}")

print(f"2^5 = {math.pow(2, 5)}")
print(f"5^2.4 = {math.pow(5, 2.4)}")

print(f"e^21 = {math.exp(21)}")

print(f"loge(4) = {math.log(4)}")
print(f"log10(10) = {math.log(10, 10)}")

print(f"greatest common divisor 25 and 15 = {math.gcd(25,15)}")

print(f"square of 25 = {math.sqrt(25)}")
print(f"180 degrees = {math.radians(180)} radians")
print(f"pi radians = {math.degrees(math.pi)} degrees")