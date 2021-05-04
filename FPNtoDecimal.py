#Gather the FPN
FPN = input("Enter a FPN: ")

#Set variables used in equation
S = FPN[0]
Exp = FPN[1:9]
Frac = FPN[9:len(FPN)]

EXP = int(Exp, 2) - 127

#Set the binary section of the formula used in class to get the binary number
Binary = float('1.'+Frac)
binary = round(Binary*pow(10,EXP))

#Set up variables for the loop used in the formula
temp = str(binary)
N=0
L=len(temp)-1

#For loop used to calculate the decimal from the FPN, the first part creates the decimal from the binary
for k in range(0,len(temp)):
  if(temp[k]=='1'):
      N+=2**L
  L-=1
if(S=='1'):#If the first number in the FPN is 1 then the number will be negative
  print('-'+str(N))
else:
  print(N)
