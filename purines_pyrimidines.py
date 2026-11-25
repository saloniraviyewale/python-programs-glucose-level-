dna = input("Enter the DNA sequence: ").upper()

purines = dna.count("A") + dna.count("G")
pyrimidines = dna.count("T") + dna.count("C")

print("Total number of purines in the given DNA sequence is", purines)
print("Total number of pyrimidines in the given DNA sequence is", pyrimidines)
