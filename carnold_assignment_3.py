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

study_options = ["Programming", "Math", "English", "History"]

print("\nWhat subject do you want to focus on?")
print(study_options)

subject = input("Enter your choice: ")

if subject in study_options:
    if subject == "Programming" or subject == "Math":
        current_gpa += 0.1
        study_hours += 5
    elif subject == "English" or subject == "History":
        social_points += 5
        stress_level -= 5
else:
    print("Invalid subject! No changes made.")
