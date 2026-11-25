p = int(input("Enter amino acid value: "))

if 1 < p < 8:
    print("SMALL PEPTIDE")
elif 9 < p < 50:
    print("POLYPEPTIDE")
else:
    print("INVALID")
