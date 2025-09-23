sequence="ATTAC"

print(len(sequence))
print(sequence.count("A"))
print(sequence.count("T"))
print(sequence.count("C"))
print(sequence.count("G"))


sequence2="ATtaC"
sequence2= sequence2.upper()
print(len(sequence2))
print(sequence2.count("A"))
print(sequence2.count("T"))
print(sequence2.count("C"))
print(sequence2.count("G"))


sequence3="ATUt*aC"
sequence3= sequence3.upper()

print(len(sequence3))
print(sequence3.count("A"))
print(sequence3.count("T"))
print(sequence3.count("C"))
print(sequence3.count("G"))

known = (sequence3.count("A")) +(sequence3.count("T"))+(sequence3.count("C"))+(sequence3.count("G"))
print(known)

unkown = (len(sequence3)) - known
print(unkown)

adenine = sequence3.count("A")
print("adenine = "+ str(adenine))

