student_name = "Christopher Arnold"
current_gpa = 3.48
study_hours = 25
social_points = 49
stress_level = 20  

print(f"Welcome, {student_name}! Starting stats:")
print(f"GPA: {current_gpa}, Study Hours: {study_hours}, Social Points: {social_points}, Stress Level: {stress_level}")

print("\nChoose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice (A/B/C): ").strip().upper()

if choice == "A":
    study_hours += 5
    stress_level -= 10
    print("You chose Light load: more free time to recuperate.")
elif choice == "B":
    study_hours += 10
    stress_level += 5
    print("You chose Standard load: steady and balanced.")
elif choice == "C":
    if current_gpa >= 3.5:
        study_hours += 20
        stress_level += 15
        print("You took a Heavy load and your strong GPA helped you manage it.")
    else:
        study_hours += 15
        stress_level += 25
        print("You took a Heavy load — it's challenging and stressful given your GPA.")
else:
    print("Invalid input! Defaulting to Standard Load.")
    study_hours += 10
    stress_level += 5

study_options = ["Programming", "Math", "English", "History"]

print("\nWhat subject do you want to focus on?")
print(", ".join(study_options))

subject = input("Enter your choice: ").strip().title()

if subject not in study_options:
    print("Invalid subject! No changes made.")
else:

    if subject == "Programming":
        if current_gpa < 3.0 and study_hours > 20:
            current_gpa += 0.25  
            study_hours += 8
            print("Intense Programming focus: big GPA boost due to dedicated hours.")
        elif current_gpa >= 3.0 or social_points > 60:
            current_gpa += 0.12   
            study_hours += 5
            print("Programming practice improved your skills and marginally raised your GPA.")
        else:
            current_gpa += 0.05
            study_hours += 3
            print("Basic Programming study: small gains expected.")

    elif subject == "Math":
        if study_hours >= 30 and not (stress_level > 60):
            current_gpa += 0.2
            study_hours += 6
            print("Focused Math sessions paid off: your GPA increased noticeably.")
        elif study_hours >= 20 and stress_level <= 80:
            current_gpa += 0.1
            study_hours += 4
            print("Solid Math studying gave you a modest GPA boost.")
        else:
            study_hours += 2
            print("Math study was interrupted; small progress made.")

    elif subject == "English":
        if stress_level > 40 and social_points < 60:
            social_points += 15
            stress_level -= 12
            print("Group discussions in English lowered stress and boosted social points.")
        elif social_points >= 60 or stress_level <= 30:
            social_points += 8
            stress_level -= 5
            print("English improvement increased your social standing and eased pressure.")
        else:
            social_points += 5
            print("English practice gave a small social boost.")

    elif subject == "History":
        if not (study_hours < 15) and social_points > 40:
            current_gpa += 0.08
            social_points += 10
            stress_level -= 7
            print("History study with friends improved GPA and social life.")
        else:
            social_points += 6
            stress_level -= 2
            print("History study gave some social and stress benefits.")

print("\nFinal stats after your study choice:")
print(f"GPA: {round(current_gpa, 2)}, Study Hours: {study_hours}, Social Points: {social_points}, Stress Level: {stress_level}")
