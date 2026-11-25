bpc = int(input("Enter the bases per coil: "))

if bpc == 11:
    print("DNA sequence is of type A")
elif bpc == 10:
    print("DNA sequence is of type B")
elif bpc == 12:
    print("DNA sequence is of type Z")
else:
    print("INVALID")
