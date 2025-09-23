restrictionsites = ["GAATTC", "GGATCC", "AAGCTT"] #CREATES RESTRICTION SITES
for site in restrictionsites:
    print(f"{site} is a restriction site") #PRINTS EACH RESTRICTION SITE SAYING "IS A RESTRICTION SITE"

dnasequence = input("Insert a DNA sequence: ").strip() #TO FIND A SEQUENCE INSIDE GIVEN SEQUENCES
for site in restrictionsites:
    is_present = site in dnasequence
    print(f"{site} is in the sequence: {is_present}")

