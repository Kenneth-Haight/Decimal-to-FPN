#Gather decimal number
Decimal = float(input("Enter a Decimal to convert to FPN: "))

#If the decimal contains a negative, the first bit will be 1, if not it will be 0
temp = bin(int(Decimal))
if '-' in temp:
  Binary = temp[3:len(temp)]
  S = 1

else:
  Binary = temp[2:len(temp)]
  S = 0

#Take the binary of the decimal and apply the formula used in class to turn it into a floating point number
Temp = float(Binary)*pow(10, -(len(Binary)-1))
Exp = len(Binary)-1
#Gather the exponent of the FPN using 127
E = 127 + Exp
E = bin(E)
E = E[2:len(E)]

#Gather the F portion of the FPN
F = str(Temp)[2:len(str(Temp))]

#Print all 3 portions of the FPN
print(S, E, F)
