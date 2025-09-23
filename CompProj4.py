protein = "ALA PRO ILU CYS"
residues = protein.split()
print(protein)
print(residues)
      
for name in ["Andrew", "Tsanwani", "Marco",
"Sophie"]:
    print("Hello,",name)

for element in [1,2,3,4]:
    print(element)
print("end")

#example indents change the result on the code, if not indented not part of the loop

for element in [1,2,3,4]:
    print(element)
    print("end")

for element in [1,2,3,4,5]:
    print("Hello")
print("end")

#2 different way of writing same thing in number of times 

for element in range(5):
    print("Hello")
print("end")

for element in range(10): #does not give the 0-9 range???
    print("element")          
print("end")

step = int(input("Insert Step:")) #insert input on terminal
for element in range(0,step*10+1, step):
    print(element)
print("end")

for element in range(10):
    print("TACG")


