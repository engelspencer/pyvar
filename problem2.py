import math

print("Please enter three float values.")

a=input("Value 1: ")
a=float(a)
b=input("Value 2: ")
b=float(b)
c=input("Value 3: ")
c=float(c)

bNeg = b - (2 * b)
bSq = b * b
fourac = 4 * a * c
twoa = 2 * a

quadFormPos = (bNeg + math.sqrt(bSq - fourac))/twoa
quadFormNeg = (bNeg - math.sqrt(bSq - fourac))/twoa

print(quadFormPos)
print(quadFormNeg)
