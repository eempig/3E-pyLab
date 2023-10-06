# Prompt the user to enter the number of students
num_students = int(input("Enter the number of students: "))
student_data = []

# Collect data for each student
for i in range(num_students):
    name = input(f"Enter the name of student {i + 1}: ")
    scores = []

    # Collect three scores per student
    for j in range(3):
        score = float(input(f"Enter score {j + 1} for {name}: "))
        scores.append(score)

    # Store the student's name and scores as a tuple and append it to student_data
    student_data.append((name, scores))

# Define the threshold for exceptional students
threshold = 90
exceptional_students = []

# Grading Criteria and Rules
grades = []

for avg_score in [sum(scores) / len(scores) for _, scores in student_data]:
    if 99 <= avg_score <= 100:
        grades.append('1.00 (Excellent)')
    elif 96 <= avg_score < 99:
        grades.append('1.25 (Excellent)')
    elif 93 <= avg_score < 96:
        grades.append('1.50 (Very Good)')
    elif 90 <= avg_score < 93:
        grades.append('1.25 (Very Good)')
    elif 87 <= avg_score < 90:
        grades.append('2.00 (Good)')
    elif 84 <= avg_score < 87:
        grades.append('2.25 (Good)')
    elif 81 <= avg_score < 84:
        grades.append('2.50 (Satisfactory)')
    elif 78 <= avg_score < 81:
        grades.append('2.75 (Satisfactory)')
    elif 75 <= avg_score < 78:
        grades.append('3.00 (Passed)')
    elif 51 <= avg_score < 75:
        grades.append('INC (Incomplete)')
    elif 0 <= avg_score < 51:
        grades.append('5.00 (Failed)')
    else:
        grades.append('Invalid Score')

# Calculate individual average scores and identify exceptional students
for name, scores in student_data:
    avg_score = sum(scores) / len(scores)

    # Check if the student's average score is above or equal to the threshold
    if avg_score >= threshold:
        exceptional_students.append(name)

# Display the results
print("\nResults:")
for (name, scores), grade in zip(student_data, grades):
    avg_score = sum(scores) / len(scores)

    # Print student name, scores, average score (rounded to 2 decimal places), and grade
    print(f"Student: {name}")
    print(f"Scores: {', '.join(map(str, scores))}")
    print(f"Average Score: {avg_score:.2f}")  # Format avg_score to two decimal places
    print(f"Grade: {grade}\n")

# Print the names of exceptional students
print("Exceptional Students:")
for name in exceptional_students:
    print(name)
