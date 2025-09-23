



def filter_acgt(input_string):  #empty string
    
    result = "" #Iterate through each character
    
    
    for char in input_string:
        
        if char in "ACGT": #If the character is A, C, G, T, add it to the result
            result += char
            
    return result

input_string = "AHSGSGGCTXYZZACAGTTCTA"
filtered_string = filter_acgt(input_string)
print(filtered_string)  # Output: "AGCTACGT"
