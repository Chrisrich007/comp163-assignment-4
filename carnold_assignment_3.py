student_name = "Christopher Arnold"       
current_gpa = 3.48                  
study_hours = 25                     
social_points = 49                  
stress_level = "20"           
print(f"Welcome, {student_name}! Starting stats:")
print(f"GPA: {current_gpa}, Study Hours: {study_hours}, Social Points: {social_points}, Stress Level: {stress_level}")

print("\nChoose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    study_hours += 5
    stress_level -= 10
elif choice == "B":
    study_hours += 10
    stress_level += 5
elif choice == "C":
    if current_gpa >= 3.5:
        study_hours += 20
        stress_level += 15
    else:
        stress_level += 25
        study_hours += 15
else:
    print("Invalid input! Defaulting to Standard Load.")
