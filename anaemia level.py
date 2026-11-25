h = float(input("Enter the haemoglobin level: "))

if h < 8:
    print("SEVERE ANAEMIA")
elif h < 9.6:
    print("MODERATE ANAEMIA")
elif h < 12:
    print("MILD ANAEMIA")
elif 13 <= h <= 16:
    print("NORMAL")
else:
    print("CONSULT A DOCTOR") 
