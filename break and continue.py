students = ["Devang", "Daksh", "Sahaj", "Aryan", "Ayush"]

for student in students: # loop through each student in the list
    if student == "Aryan": 
        break; # stops the loop immediately if "Aryan" is found
    if student == "Daksh": 
        continue; # skips "Daksh" and go to the next student
    print(student) 
