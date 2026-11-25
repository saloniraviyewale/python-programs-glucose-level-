W= float (input(“Enter your weight”))
H= float (input (“Enter your height”))
BMI = W/(H**2)
Print (“Your BMI is”, BMI, “kg/m^2”)
if (BMI < 18.5):
	Print (“UNDERWEIGHT”)
Elif (18.5 < BMI < 24.9):
	Print (“HEALTHY WEIGHT”)
elif (25 < BMI < 29.9):
	Print (“OVERWEIGHT”)
elif (30 < BMI < 39.9):
	Print (“OBESE”)
elif (BMI >=40):
	Print (“SEVERE OBESE”)
else :
	Print (“INVALID”)


